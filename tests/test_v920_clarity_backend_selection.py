from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class ClarityBackendSelectionV920Tests(unittest.TestCase):
    def test_module_workflow_contains_backend_clarity_and_aesthetic_gates(self):
        text = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in [
            "Rendering Backend Selection",
            "Clarity & Visibility Review",
            "Aesthetic Review",
            "Main-text Admission",
            "Final-size / Export QA",
            "Portfolio Gate",
            "q{x}_plot.py",
            "q{x}_plot.m",
            "data_process_plot.py",
            "data_process.m",
        ]:
            self.assertIn(token, text)
        self.assertIn("不强制任一后端", text)
        self.assertIn("不设置每问必须或最多多少张图的固定数量限制", text)

    def test_clarity_review_requires_labels_contrast_and_final_size_visibility(self):
        text = (ROOT / "templates/figure/clarity_visibility_review.md").read_text(encoding="utf-8")
        for token in [
            "Direct Label / Contour Label Gate",
            "Foreground–Background Contrast Gate",
            "Final-size Visibility",
            "Semantic Clarity Check",
            "Clarity Repair Order",
            "Backend Escalation",
            "Aesthetic Review",
            "contour labels",
            "深蓝",
        ]:
            self.assertIn(token, text)
        self.assertIn("黑色不是默认正确答案", text)
        self.assertIn("清楚 + 克制 + 协调 + 有焦点", text)
        self.assertIn("Clarity & Visibility FAIL", text)

    def test_backend_gate_is_adaptive_not_matlab_or_python_forced(self):
        text = (ROOT / "templates/figure/rendering_backend_selection.md").read_text(encoding="utf-8")
        for token in [
            "不强制 MATLAB，也不强制 Python",
            "Python / MATLAB",
            "Final-size readability",
            "Export fidelity",
            "Paper-level consistency",
            "qX_plot.py",
            "qX_plot.m",
            "data_process_plot.py",
            "data_process.m",
        ]:
            self.assertIn(token, text)
        self.assertIn("后端是渲染手段，不是证据来源", text)
        self.assertIn("不要求每张 Figure 都同时写 Python 和 MATLAB 两份生产代码", text)
        self.assertIn("不得因为换后端而修改 accepted 数据", text)
        self.assertIn("不增加 SciencePlots", text)

    def test_result_contract_records_backend_and_clarity_without_changing_admission(self):
        text = (ROOT / "templates/figure/result_figure_contract.md").read_text(encoding="utf-8")
        for token in [
            "Rendering backend candidates",
            "Selected rendering backend",
            "Backend selection rationale",
            "Backend comparison mode",
            "Direct label / contour label decision",
            "Foreground–background contrast",
            "Semantic clarity check",
            "Clarity & visibility review",
            "Clarity repair action",
            "Aesthetic review",
            "Figure script",
            "MAIN_TEXT / APPENDIX / TABLE_ONLY / MERGE / DROP",
        ]:
            self.assertIn(token, text)
        self.assertIn("不得借后端切换改变 Figure Evidence", text)
        self.assertIn("清晰性 FAIL 不能被“整体挺好看”覆盖", text)

    def test_output_contract_uses_exactly_one_backend_selected_figure_script(self):
        contract = yaml.safe_load((ROOT / "core/output_contract.yaml").read_text(encoding="utf-8"))
        self.assertEqual(contract["version"], "9.2.0")
        figure_contract = contract["matlab_figure_contract"]
        self.assertEqual(figure_contract["backend_policy"], "adaptive_python_or_matlab_no_forced_default")
        self.assertTrue(figure_contract["rendering_backend_selection_required"])
        self.assertTrue(figure_contract["clarity_visibility_review_required"])
        self.assertTrue(figure_contract["aesthetic_review_required"])
        self.assertFalse(figure_contract["external_plotting_dependency_required"])
        self.assertEqual(contract["per_question"]["exact_default_file_count"], 5)
        self.assertEqual(contract["global_preprocessing"]["exact_default_file_count"], 3)
        self.assertIn("q{阿拉伯序号}_plot.py", contract["per_question"]["figure_script_candidates"])
        self.assertIn("q{阿拉伯序号}_plot.m", contract["per_question"]["figure_script_candidates"])
        self.assertIn("data_process_plot.py", contract["global_preprocessing"]["figure_script_candidates"])
        self.assertIn("data_process.m", contract["global_preprocessing"]["figure_script_candidates"])
        self.assertIn("figure_scripts", contract["project_sync"]["stage_requirements"]["figures"])
        conditional = contract["project_sync"]["conditional_stage_requirements"]["preprocessing_decision_project_level"]
        self.assertIn("preprocessing_figure_script", conditional["figures"])

    def test_runtime_discovery_accepts_python_or_matlab_plot_script(self):
        snapshot = (ROOT / "scripts/project_snapshot.py").read_text(encoding="utf-8")
        sync = (ROOT / "scripts/sync_project.py").read_text(encoding="utf-8")
        for token in ["q{number}_plot", 'f"{stem}.py"', 'f"{stem}.m"', "figure_backend", "figure_script"]:
            self.assertIn(token, snapshot)
        self.assertIn("正式Figure pipeline默认只保留一个生产后端", snapshot)
        for token in ["data_process_plot.py", "data_process.m", "preprocessing_figure_script", "qX_plot.py或qX_plot.m"]:
            self.assertIn(token, sync)
        self.assertNotIn("提交ZIP缺少MATLAB脚本", sync)

    def test_existing_truth_and_aesthetic_limits_remain(self):
        module = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in [
            "不得复制、描摹、换色复刻",
            "禁止 rainbow / jet / HSV 无序彩虹",
            "红—绿不得承担唯一关键信息区分",
            "MAIN_TEXT",
            "APPENDIX",
            "TABLE_ONLY",
            "MERGE",
            "DROP",
            "不得为了美观用 spline / Bezier",
            "accepted workbook",
        ]:
            self.assertIn(token, module)

    def test_entry_skill_exposes_backend_and_clarity_capabilities(self):
        root_skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        packaged = (ROOT / "skills/mathmodel-skill/SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(root_skill, packaged)
        for token in [
            "adaptive Python/MATLAB Rendering Backend Selection",
            "Clarity & Visibility",
            "Figure 后端选择",
            "Figure 清晰度审查",
            "不强制任一后端",
        ]:
            self.assertIn(token, root_skill)


if __name__ == "__main__":
    unittest.main()
