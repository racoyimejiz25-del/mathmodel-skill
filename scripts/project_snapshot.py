#!/usr/bin/env python3
"""Project artifact discovery and per-question snapshots extracted mechanically from sync_project."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

import artifact_fingerprint as ARTIFACT_FINGERPRINT

SKILL_ROOT = Path(__file__).resolve().parent.parent


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


WORKBOOK_VALIDATION = _load_module(
    "hsk_project_snapshot_workbook_validation",
    SKILL_ROOT / "templates/code" / "hsk_pipeline" / "workbook_validation.py",
)

sha256_file = ARTIFACT_FINGERPRINT.sha256_file
combined_hash = ARTIFACT_FINGERPRINT.combined_hash
framework_section_hash = ARTIFACT_FINGERPRINT.framework_section_hash

QUESTION_RE = re.compile(r"问题([一二三四五六七八九十百]+)")

MATLAB_TITLE_RE = re.compile(r"\b(?:title|sgtitle)\s*\(", re.IGNORECASE)
PYTHON_TITLE_RE = re.compile(
    r"(?:\bplt\s*\.\s*(?:title|suptitle)|\b(?:fig|figure)\s*\.\s*suptitle|\.\s*set_title)\s*\(",
    re.IGNORECASE,
)

MATLAB_EXPORT_RE = re.compile(
    r"(?:exportgraphics|print)\s*\([^\n]*?[\"']([^\"']+\.(?:png|pdf|svg|tif|tiff|jpg|jpeg))[\"']",
    re.IGNORECASE,
)
PYTHON_EXPORT_RE = re.compile(
    r"(?:savefig)\s*\([^\n]*?[\"']([^\"']+\.(?:png|pdf|svg|tif|tiff|jpg|jpeg))[\"']",
    re.IGNORECASE,
)

WORKBOOK_REF_RE = re.compile(r"[\"']([^\"']+\.xlsx)[\"']", re.IGNORECASE)

FIGURE_SUFFIXES = {".png", ".pdf", ".svg", ".tif", ".tiff", ".jpg", ".jpeg"}

DATA_SUFFIXES = {".csv", ".xlsx", ".xls", ".json", ".yaml", ".yml", ".txt"}

SOLVED_STATUSES = {"solved", "analyzed", "validated", "written", "completed"}

ANALYZED_STATUSES = {"analyzed", "validated", "written", "completed"}

VALID_PREPROCESSING_DECISIONS = {"not_needed", "question_local", "project_level"}


def question_key(chinese_name: str) -> str:
    order = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    suffix = chinese_name.removeprefix("问题")
    return f"Q{order.index(suffix) + 1}" if suffix in order else chinese_name


def chinese_question_name(key: str) -> str:
    order = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    match = re.fullmatch(r"Q(\d+)", key)
    if match and 1 <= int(match.group(1)) <= len(order):
        return f"问题{order[int(match.group(1)) - 1]}"
    return key


def question_number(chinese_name: str) -> int | None:
    match = re.fullmatch(r"Q(\d+)", question_key(chinese_name))
    return int(match.group(1)) if match else None


def preprocessing_decision(state: Mapping[str, Any]) -> str | None:
    value = str(((state.get("preprocessing") or {}).get("decision", ""))).strip()
    return value if value in VALID_PREPROCESSING_DECISIONS else None


def data_source_files(
    root: Path, state: Mapping[str, Any]
) -> tuple[list[Path], str, list[str], list[str]]:
    issues: list[str] = []
    warnings: list[str] = []
    entries = ((state.get("data") or {}).get("sources") or []) if state else []
    files: list[Path] = []
    if entries:
        for entry in entries:
            relative = str((entry or {}).get("path", "")).strip()
            if not relative:
                issues.append("data.sources 存在空路径")
                continue
            path = (root / relative).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                issues.append(f"data.sources 路径越出项目根目录: {relative}")
                continue
            if path.is_file():
                files.append(path)
            elif path.is_dir():
                files.extend(item for item in path.rglob("*") if item.is_file())
            else:
                issues.append(f"data.sources 文件不存在: {relative}")
        return files, "declared_sources", issues, warnings
    for path in root.iterdir() if root.is_dir() else []:
        if path.is_file() and not path.name.startswith("."):
            if path.name not in {"模型论文框架.md", "sync_report.yaml"} and path.suffix.lower() in DATA_SUFFIXES:
                files.append(path)
    warnings.append("项目状态未声明data.sources；data hash使用受限根目录数据文件回退扫描")
    return files, "fallback_scan", issues, warnings


def active_data_hash(
    root: Path,
    state: Mapping[str, Any],
    raw_files: Iterable[Path],
    raw_mode: str,
) -> tuple[str | None, str, list[str]]:
    """Select raw or accepted unified workbook as the downstream data hash fact source."""
    decision = preprocessing_decision(state)
    warnings: list[str] = []
    raw_hash = combined_hash(raw_files, root)
    if decision != "project_level":
        return raw_hash, raw_mode, warnings
    preprocessing = state.get("preprocessing") or {}
    workbook_rel = str(preprocessing.get("workbook") or "数据预处理/数据预处理结果.xlsx")
    workbook = (root / workbook_rel).resolve()
    if (
        preprocessing.get("status") == "accepted"
        and preprocessing.get("quality_status") == "passed"
        and workbook.is_file()
    ):
        return sha256_file(workbook), "preprocessing_workbook", warnings
    warnings.append("preprocessing_decision=project_level但统一预处理工作簿尚未accepted；当前data hash仍使用原始数据，仅可用于预处理阶段")
    return raw_hash, "raw_project_level_pending", warnings


def _classification(entry: Mapping[str, Any]):
    classification = entry.get("classification") or {}
    objective = classification.get("objective")
    structures = tuple(classification.get("structures", []) or [])
    old = entry.get("problem_types") or {}
    labels = [old.get("primary"), *(old.get("secondary", []) or [])]
    problem_types = tuple(dict.fromkeys(str(item) for item in labels if item))
    capabilities = entry.get("capabilities")
    return objective, structures, problem_types, capabilities if isinstance(capabilities, Mapping) else None


def _question_dir(root: Path, chinese_name: str) -> Path:
    current = root / f"{chinese_name}求解"
    if current.is_dir():
        return current
    return root / "结果数据表" / chinese_name


def _question_names(root: Path, state: Mapping[str, Any]) -> list[str]:
    names = {chinese_question_name(str(key)) for key in (state.get("subproblems") or {})}
    names.update(
        path.name.removesuffix("求解")
        for path in root.glob("问题*求解")
        if path.is_dir() and QUESTION_RE.fullmatch(path.name.removesuffix("求解"))
    )
    result_root = root / "结果数据表"
    if result_root.is_dir():
        names.update(
            path.name for path in result_root.iterdir()
            if path.is_dir() and QUESTION_RE.fullmatch(path.name)
        )
    return sorted(names, key=lambda value: question_number(value) or 999)


def _stage_code_paths(root: Path, chinese_name: str) -> tuple[Path | None, Path | None, bool]:
    current_dir = root / f"{chinese_name}求解"
    primary = current_dir / f"{chinese_name}求解.py"
    analysis = current_dir / f"{chinese_name}结果深化分析.py"
    if primary.is_file() or analysis.is_file():
        legacy_single = primary.is_file() and not analysis.is_file()
        return primary if primary.is_file() else None, analysis if analysis.is_file() else None, legacy_single
    legacy_primary = root / f"{chinese_name}求解.py"
    legacy_analysis = root / f"{chinese_name}结果深化分析.py"
    return (
        legacy_primary if legacy_primary.is_file() else None,
        legacy_analysis if legacy_analysis.is_file() else None,
        legacy_primary.is_file() and not legacy_analysis.is_file(),
    )


def _python_files(root: Path, chinese_name: str) -> list[Path]:
    primary, analysis, _ = _stage_code_paths(root, chinese_name)
    return [path for path in (primary, analysis) if path is not None]


def _analysis_path(result_dir: Path, chinese_name: str) -> tuple[Path, bool]:
    current = result_dir / f"{chinese_name}结果深化分析.xlsx"
    if current.is_file():
        return current, False
    legacy = result_dir / f"{chinese_name}敏感性与鲁棒性结果.xlsx"
    return (legacy, True) if legacy.is_file() else (current, False)


def _figure_files(result_dir: Path) -> list[Path]:
    directories = [result_dir, result_dir / "图表"]
    return sorted(
        {path for directory in directories if directory.is_dir() for path in directory.iterdir()
         if path.is_file() and path.suffix.lower() in FIGURE_SUFFIXES},
        key=lambda item: item.as_posix(),
    )


def _validate_workbook(path: Path, kind: str, schema: Mapping[str, Any], entry: Mapping[str, Any]) -> list[str]:
    objective, structures, problem_types, capabilities = _classification(entry)
    try:
        WORKBOOK_VALIDATION.validate_workbook_file(
            path, kind, schema=schema, problem_types=problem_types,
            capabilities=capabilities, objective=objective, structures=structures,
            require_quality_passed=True,
        )
    except Exception as exc:  # noqa: BLE001
        return [f"{path.name}: {exc}"]
    return []


def _has_sheets(path: Path, names: set[str]) -> bool:
    if not path.is_file():
        return False
    try:
        return names.issubset(WORKBOOK_VALIDATION.read_workbook_tables(path))
    except Exception:  # noqa: BLE001
        return False


def _matlab_executable_text(text: str) -> str:
    """Remove MATLAB comments while preserving percent signs inside quoted strings."""
    cleaned: list[str] = []
    for source in text.splitlines():
        line = source
        in_single = False
        in_double = False
        index = 0
        while index < len(line):
            char = line[index]
            if char == '"' and not in_single:
                if in_double and index + 1 < len(line) and line[index + 1] == '"':
                    index += 2
                    continue
                in_double = not in_double
            elif char == "'" and not in_double:
                if in_single:
                    if index + 1 < len(line) and line[index + 1] == "'":
                        index += 2
                        continue
                    in_single = False
                else:
                    previous = line[index - 1] if index else ""
                    if not previous or not (previous.isalnum() or previous in "_)]}."):
                        in_single = True
            elif char == "%" and not in_single and not in_double:
                line = line[:index]
                break
            index += 1
        cleaned.append(line)
    return "\n".join(cleaned)


def _parse_matlab(script: Path) -> tuple[bool, list[str], list[str]]:
    if not script.is_file():
        return False, [], []
    text = script.read_text(encoding="utf-8", errors="ignore")
    code_text = _matlab_executable_text(text)
    return (
        bool(MATLAB_TITLE_RE.search(code_text)),
        WORKBOOK_REF_RE.findall(code_text),
        MATLAB_EXPORT_RE.findall(code_text),
    )


def _parse_python_figure(script: Path) -> tuple[bool, list[str], list[str]]:
    if not script.is_file():
        return False, [], []
    text = script.read_text(encoding="utf-8", errors="ignore")
    return (
        bool(PYTHON_TITLE_RE.search(text)),
        WORKBOOK_REF_RE.findall(text),
        PYTHON_EXPORT_RE.findall(text),
    )


def _figure_script_candidates(result_dir: Path, number: int | None) -> list[Path]:
    stem = f"q{number}_plot" if number else "q_plot"
    return [result_dir / f"{stem}.py", result_dir / f"{stem}.m"]


def _select_figure_script(
    result_dir: Path,
    number: int | None,
    entry: Mapping[str, Any],
) -> tuple[Path | None, list[Path]]:
    candidates = [path for path in _figure_script_candidates(result_dir, number) if path.is_file()]
    if not candidates:
        return None, []
    declared = str(entry.get("matlab_script") or "").strip()
    if declared:
        declared_name = Path(declared).name
        for candidate in candidates:
            if candidate.name == declared_name:
                return candidate, candidates
    return candidates[0], candidates


def _parse_figure_script(script: Path | None) -> tuple[str | None, bool, list[str], list[str]]:
    if script is None:
        return None, False, [], []
    if script.suffix.lower() == ".py":
        has_title, workbooks, exports = _parse_python_figure(script)
        return "Python", has_title, workbooks, exports
    if script.suffix.lower() == ".m":
        has_title, workbooks, exports = _parse_matlab(script)
        return "MATLAB", has_title, workbooks, exports
    return None, False, [], []


def _snapshot_question(
    root: Path,
    chinese_name: str,
    entry: Mapping[str, Any],
    schema: Mapping[str, Any],
    data_hash: str | None,
    delivery_scope: str | None,
) -> dict[str, Any]:
    key = question_key(chinese_name)
    result_dir = _question_dir(root, chinese_name)
    solution = result_dir / f"{chinese_name}求解结果.xlsx"
    analysis_workbook, legacy_analysis_workbook = _analysis_path(result_dir, chinese_name)
    primary_code, analysis_code, legacy_single_code = _stage_code_paths(root, chinese_name)
    number = question_number(chinese_name)
    figure_script, figure_candidates = _select_figure_script(result_dir, number, entry)
    figures = _figure_files(result_dir)
    status = str(entry.get("status", "pending"))
    require_solution = status in SOLVED_STATUSES
    require_analysis = status in ANALYZED_STATUSES
    require_analysis_code = status in ANALYZED_STATUSES and bool(entry.get("analysis_code_sha256"))
    if delivery_scope in {"results", "figures", "docx"}:
        require_solution = True
        require_analysis = True
        require_analysis_code = True

    issues: list[str] = []
    warnings: list[str] = []
    if delivery_scope == "code" and primary_code is None:
        issues.append("代码交付缺少标准主求解Python脚本")
    if require_solution and not solution.is_file():
        issues.append("缺少标准求解结果工作簿")
    if require_analysis and not analysis_workbook.is_file():
        issues.append("缺少标准结果深化分析工作簿")
    if require_analysis_code and analysis_code is None:
        if delivery_scope is None and legacy_single_code and not entry.get("analysis_code_sha256"):
            warnings.append("检测到v6.6.x单脚本项目；只读兼容，重新深化分析时应迁移为独立结果深化分析脚本")
        else:
            issues.append("缺少标准结果深化分析Python脚本")
    if solution.is_file():
        issues.extend(_validate_workbook(solution, "solution", schema, entry))
    if analysis_workbook.is_file():
        issues.extend(_validate_workbook(analysis_workbook, "result_analysis", schema, entry))
        if legacy_analysis_workbook:
            warnings.append("使用旧敏感性与鲁棒性工作簿名；新交付应迁移为结果深化分析工作簿")

    quality_exists = _has_sheets(solution, {"主结果质量门"})
    analysis_report_exists = _has_sheets(analysis_workbook, {"分析设计", "结论稳定性汇总"})
    if require_solution and not quality_exists:
        issues.append("主求解工作簿缺少主结果质量门报告")
    if require_analysis and not analysis_report_exists:
        issues.append("结果深化分析工作簿缺少分析设计或结论稳定性汇总")

    figure_backend, figure_has_title, workbook_refs, exports = _parse_figure_script(figure_script)
    if len(figure_candidates) > 1:
        message = "检测到qX_plot.py与qX_plot.m同时存在；正式Figure pipeline默认只保留一个生产后端"
        if delivery_scope == "figures":
            issues.append(message)
        else:
            warnings.append(message)
    if delivery_scope == "figures":
        if figure_script is None:
            issues.append("图表交付缺少正式Figure脚本；应按Backend Selection选择qX_plot.py或qX_plot.m")
        else:
            if figure_has_title:
                issues.append("正式论文图不得设置整体title/sgtitle/suptitle；正式图名由LaTeX/DOCX caption承担")
            standard = {
                f"{chinese_name}求解结果.xlsx",
                f"{chinese_name}结果深化分析.xlsx",
                f"{chinese_name}敏感性与鲁棒性结果.xlsx",
            }
            if not {Path(item).name for item in workbook_refs}.intersection(standard):
                issues.append("Figure脚本未发现标准工作簿引用")
            for item in exports:
                export_path = (figure_script.parent / item).resolve()
                if not export_path.is_file():
                    shown = export_path.relative_to(root).as_posix() if export_path.is_relative_to(root) else export_path.as_posix()
                    issues.append(f"Figure脚本声明导出的图不存在: {shown}")

    framework = root / "模型论文框架.md"
    hashes = {
        "data": data_hash,
        "primary_code": sha256_file(primary_code) if primary_code else None,
        "analysis_code": sha256_file(analysis_code) if analysis_code else None,
        "solution_workbook": sha256_file(solution) if solution.is_file() else None,
        "result_analysis_workbook": sha256_file(analysis_workbook) if analysis_workbook.is_file() else None,
        # Compatibility key name retained until the next project-state schema migration.
        # Its value is the selected Figure production script hash, regardless of .py/.m backend.
        "matlab_script": sha256_file(figure_script) if figure_script else None,
        "figure_bundle": combined_hash(figures, root),
        "framework": framework_section_hash(framework, str(entry.get("framework_section", ""))),
    }
    hashes = {name: value for name, value in hashes.items() if value}
    figure_relative = figure_script.relative_to(root).as_posix() if figure_script else None
    return {
        "key": key,
        "chinese_name": chinese_name,
        "status": status,
        "primary_code": primary_code.relative_to(root).as_posix() if primary_code else None,
        "result_analysis_code": analysis_code.relative_to(root).as_posix() if analysis_code else None,
        "primary_code_sha256": sha256_file(primary_code) if primary_code else None,
        "analysis_code_sha256": sha256_file(analysis_code) if analysis_code else None,
        "legacy_single_code": legacy_single_code,
        "solution_workbook": solution.relative_to(root).as_posix() if solution.is_file() else None,
        "result_analysis_workbook": analysis_workbook.relative_to(root).as_posix() if analysis_workbook.is_file() else None,
        "legacy_analysis_workbook": legacy_analysis_workbook,
        "result_quality_report": quality_exists,
        "result_analysis_report": analysis_report_exists,
        "figure_script": figure_relative,
        "figure_backend": figure_backend,
        # Compatibility alias: project_state still names this carrier `matlab_script`.
        "matlab_script": figure_relative,
        "matlab_has_title": figure_has_title,
        "figure_has_title": figure_has_title,
        "workbook_references": workbook_refs,
        "declared_exports": exports,
        "figures": [path.relative_to(root).as_posix() for path in figures],
        "individual_figure_hashes": {
            path.relative_to(root).as_posix(): sha256_file(path) for path in figures
        },
        "artifact_hashes": hashes,
        "issues": issues,
        "warnings": warnings,
    }
