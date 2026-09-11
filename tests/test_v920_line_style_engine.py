from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LineStyleEngineV920Tests(unittest.TestCase):
    def test_line_style_engine_is_rendering_only(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        for token in [
            "不拥有独立 Figure Authority",
            "不改变任何已有准入",
            "journal_competition_hybrid",
            "competition_clean",
            "decision_highlight",
            "dense_scientific",
            "technical_monochrome",
            "Line Role Classification",
            "Visual Mapping for Lines",
            "Marker Policy",
            "Smoothing / Interpolation Policy",
            "Uncertainty / Band Policy",
            "Final-size Line QA",
        ]:
            self.assertIn(token, text)

    def test_multi_competition_synthesis_is_reference_not_imitation(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        for token in ["高教社杯", "MCM / ICM", "华中杯", "APMCM", "MathorCup", "深圳杯"]:
            self.assertIn(token, text)
        self.assertIn("可迁移原则", text)
        self.assertIn("不得复制、描摹、换色复刻", text)
        self.assertIn("不得为了“像某个比赛”改变当前 Core conclusion", text)

    def test_line_channels_have_distinct_semantic_jobs(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        for token in [
            "Color      = 对象 / 指标 / 稳定类别语义",
            "LineStyle  = 场景 / 状态 / 观测-vs模型 / 基准-vs结果",
            "LineWidth  = 重要程度 / 视觉权重",
            "Marker     = 真实离散采样点 / 关键事件 / 推荐点 / 临界点",
            "Band       = 真实区间 / 不确定性 / 阶段背景",
        ]:
            self.assertIn(token, text)

    def test_line_widths_are_soft_starting_ranges_not_hard_limits(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        self.assertIn("起点区间而非固定规则", text)
        self.assertIn("不设置跨所有 Figure 的硬阈值", text)
        self.assertIn("1.7–2.1 pt", text)
        self.assertIn("1.1–1.5 pt", text)
        self.assertIn("0.8–1.1 pt", text)

    def test_smoothing_cannot_fabricate_shape(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        self.assertIn("禁止为了圆润使用 spline / Bezier", text)
        self.assertIn("制造不存在的新峰谷、拐点或阈值交点", text)
        self.assertIn("原始采样点或原始趋势必须仍可验证", text)

    def test_existing_figure_contract_constraints_are_preserved(self):
        contract = (ROOT / "templates/figure/result_figure_contract.md").read_text(encoding="utf-8")
        for token in [
            "Line style profile",
            "Line role map",
            "Line visual semantics",
            "Marker policy",
            "Smoothing / interpolation policy",
            "Uncertainty band / boundary policy",
            "Line final-size QA",
            "MAIN_TEXT / APPENDIX / TABLE_ONLY / MERGE / DROP",
            "不设置每问必须或最多多少张图的固定数量限制",
            "不得借后端切换改变 Figure Evidence、accepted workbook、数据范围、统计口径、Visual Mapping、图数量、合图/拆图或 Main-text Admission",
        ]:
            self.assertIn(token, contract)

    def test_authority_level_still_owns_original_limits(self):
        module = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in [
            "单一通用 Authority",
            "不设置每问必须或最多多少张图的固定数量限制",
            "不得复制、描摹、换色复刻",
            "MAIN_TEXT",
            "APPENDIX",
            "TABLE_ONLY",
            "MERGE",
            "DROP",
            "禁止 rainbow / jet / HSV 无序彩虹",
            "红—绿不得承担唯一关键信息区分",
        ]:
            self.assertIn(token, module)

    def test_no_new_external_runtime_dependency(self):
        text = (ROOT / "templates/figure/line_style_engine.md").read_text(encoding="utf-8")
        self.assertIn("不增加 gramm、SciencePlots、外部 colormap、export_fig", text)
        self.assertIn("任何其他第三方运行依赖", text)


if __name__ == "__main__":
    unittest.main()
