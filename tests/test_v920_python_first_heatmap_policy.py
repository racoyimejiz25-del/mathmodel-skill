from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PythonFirstHeatmapPolicyV920Tests(unittest.TestCase):
    def test_authority_is_python_first_without_becoming_python_only(self):
        text = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in [
            "Python-first",
            "默认优先用 Python",
            "只有 MATLAB",
            "如果两者视觉质量实质相当，**选择 Python**",
            "accepted workbook",
            "Main-text Admission",
        ]:
            self.assertIn(token, text)
        self.assertIn("MATLAB 有明确优势时例外", text)

    def test_heatmap_and_gridmap_are_ultra_low_priority(self):
        module = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        chart = (ROOT / "templates/figure/chart_selection.md").read_text(encoding="utf-8")
        for text in (module, chart):
            self.assertIn("Heatmap / Gridmap Ultra-low Priority Gate", text)
            self.assertIn("ultra-low", text)
            self.assertIn("Low-information Visualization Penalty", text)
        self.assertIn("不得因为“稳妥、整齐、容易生成、像科研图”而默认选热力图或方格图", module)
        self.assertIn("过度保守选图的警告信号", chart)

    def test_heatmap_is_not_banned_when_2d_structure_is_real(self):
        module = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        chart = (ROOT / "templates/figure/chart_selection.md").read_text(encoding="utf-8")
        for token in ["真实遥感栅格", "物理场", "空间场", "混淆矩阵", "相关矩阵", "二维参数交互面"]:
            self.assertIn(token, module)
        self.assertIn("低优先不等于全面禁用", chart)

    def test_chart_selection_prefers_direct_high_information_encodings(self):
        text = (ROOT / "templates/figure/chart_selection.md").read_text(encoding="utf-8")
        for token in [
            "line / multi-line",
            "scatter",
            "sorted dot",
            "interval dot",
            "contour / isoline",
            "small multiples",
            "overview + detail",
        ]:
            self.assertIn(token, text)

    def test_backend_template_defaults_to_python_and_keeps_matlab_exception(self):
        text = (ROOT / "templates/figure/rendering_backend_selection.md").read_text(encoding="utf-8")
        for token in [
            "Python-first",
            "默认先用 Python",
            "MATLAB 例外准入",
            "如果 Python 与 MATLAB 最终质量实质相当，**选择 Python**",
            "问题X求解/qX_plot.py",
            "数据预处理/data_process_plot.py",
        ]:
            self.assertIn(token, text)
        self.assertIn("不得把 Python-first 解释为“一律 Python”", text)

    def test_figure_contract_records_low_information_and_heatmap_exception(self):
        text = (ROOT / "templates/figure/result_figure_contract.md").read_text(encoding="utf-8")
        for token in [
            "Low-information visualization review",
            "Heatmap / gridmap priority",
            "ULTRA_LOW",
            "Heatmap / gridmap exception rationale",
            "Selected rendering backend",
            "默认 `Python`",
            "Figure script",
        ]:
            self.assertIn(token, text)

    def test_existing_limits_are_preserved(self):
        module = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in [
            "不设置每问必须或最多多少张图的固定数量限制",
            "不得复制、描摹、换色复刻",
            "MAIN_TEXT",
            "APPENDIX",
            "TABLE_ONLY",
            "MERGE",
            "DROP",
            "禁止 rainbow / jet / HSV 无序彩虹",
            "红—绿不得承担唯一关键信息区分",
            "不得为了美观用 spline / Bezier 制造新峰谷和拐点",
        ]:
            self.assertIn(token, module)


if __name__ == "__main__":
    unittest.main()
