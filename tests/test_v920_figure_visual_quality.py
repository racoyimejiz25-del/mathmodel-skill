from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class FigureVisualQualityV920Tests(unittest.TestCase):
    def test_release_carriers_are_v920(self):
        bootstrap = yaml.safe_load((ROOT / "core/bootstrap.yaml").read_text(encoding="utf-8"))
        plugin = yaml.safe_load((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(bootstrap["skill_version"], "9.2.0")
        self.assertEqual(plugin["version"], "9.2.0")

    def test_module_04_owns_complete_figure_workflow(self):
        text = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        required = [
            "Literature-Guided Figure Reference Gate",
            "Visual Mapping Gate",
            "Basic-form Challenge",
            "Composite Encoding Preference",
            "Figure Layout Gate",
            "Figure Enhancement Gate",
            "Competition Visual Quality Gate",
            "Main-text Admission Gate",
            "Redundancy / Unique Contribution Check",
            "Final-size Readability / Export QA",
            "Figure Portfolio Scientific Quality Gate",
        ]
        for token in required:
            self.assertIn(token, text)
        self.assertIn("不设置每问必须或最多多少张图的固定数量限制", text)
        self.assertIn("只吸收成熟科研作图方法的设计理念", text)
        self.assertIn("不把 gramm、SciencePlots、RainCloudPlots、UltraPlot", text)
        self.assertIn("不得复制、描摹、换色复刻", text)
        self.assertIn("删除这张图后", text)
        self.assertIn("MAIN_TEXT", text)
        self.assertIn("APPENDIX", text)
        self.assertIn("TABLE_ONLY", text)
        self.assertIn("MERGE", text)
        self.assertIn("DROP", text)

    def test_figure_contract_preserves_user_checks_and_aesthetics(self):
        text = (ROOT / "templates/figure/result_figure_contract.md").read_text(encoding="utf-8")
        for token in [
            "Evidence level",
            "Evidence structure",
            "Literature visual references",
            "Visual mapping",
            "Mapping redundancy check",
            "Basic-form challenge",
            "Composite encoding",
            "Layout / Split decision",
            "Enhancement",
            "Palette profile",
            "Color semantics",
            "Aesthetic balance check",
            "Competition visual benchmark",
            "Final-size readability",
            "Unique information contribution",
            "Main-text admission decision",
        ]:
            self.assertIn(token, text)
        self.assertIn("不设置每问必须或最多多少张图的固定数量限制", text)
        self.assertIn("美感必须达到成熟竞赛论文水平", text)
        self.assertIn("质量标尺，不是唯一选图/设计参考源", text)
        self.assertIn("不意味着只参照或模仿高教社杯", text)

    def test_visual_mapping_is_dependency_free(self):
        text = (ROOT / "templates/figure/visual_mapping_contract.md").read_text(encoding="utf-8")
        for token in ["X", "Y", "Color", "Size", "Shape", "Facet", "Annotation", "Uncertainty"]:
            self.assertIn(token, text)
        self.assertIn("不要求安装任何外部作图库", text)
        self.assertIn("无真实语义", text)

    def test_cumcm_quality_gate_is_level_benchmark_not_sole_reference(self):
        text = (ROOT / "templates/figure/cumcm_visual_quality_gate.md").read_text(encoding="utf-8")
        self.assertIn("mcm.edu.cn", text)
        self.assertIn("dxs.moe.gov.cn", text)
        self.assertIn("高教社杯是质量标尺，不是唯一参考源", text)
        self.assertIn("整体视觉完成度、清晰度、版面成熟度和论文融合度至少应达到相近档次", text)
        self.assertIn("实际选图与视觉设计仍采用多源参考", text)
        self.assertIn("只看高教社杯论文选图", text)
        self.assertIn("不得复制、描摹、换色复刻", text)
        self.assertIn("Final-size", text)
        self.assertIn("好看不能让一张低价值图进入正文", text)

    def test_literature_reference_remains_multi_source_and_domain_first(self):
        text = (ROOT / "templates/figure/literature_figure_reference.md").read_text(encoding="utf-8")
        self.assertIn("质量水平锚点之一", text)
        self.assertIn("不是唯一的选图资料源", text)
        self.assertIn("同领域同行评审论文与综述", text)
        self.assertIn("官方技术报告、标准、机构报告", text)
        self.assertIn("不要把“与高教社杯优秀论文水平相近”误解为“只查高教社杯论文”", text)
        self.assertIn("质量标尺和选图资料源是两件事", text)

    def test_palette_rules_are_semantic_not_decorative(self):
        text = (ROOT / "modules/04_figure_evidence.md").read_text(encoding="utf-8")
        for token in ["sequential", "centered diverging", "restrained qualitative", "cyclic", "rainbow", "jet"]:
            self.assertIn(token, text)
        self.assertIn("红—绿不得承担唯一关键信息区分", text)
        self.assertIn("主色角色 + 强调角色 + 中性灰辅助", text)


if __name__ == "__main__":
    unittest.main()
