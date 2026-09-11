# CUMCM / 高教社杯 Figure Visual Quality Gate

本模板实现 `modules/04_figure_evidence.md` 的 Competition Visual Quality Gate，不拥有独立 Figure Authority，也不要求安装任何外部作图库。

## 外部视觉基准

全国大学生数学建模竞赛官网的“历年竞赛结果”将“历年论文展示”指向教育部中国大学生在线数学建模论文展示页面。CUMCM 正式论文 Figure 在联网条件允许时，可查阅近几年组委会公开展示论文，学习其整体图文成熟度、版面秩序、图表与正文融合方式以及常见视觉惯例。

稳定入口：

- 全国大学生数学建模竞赛官网历年竞赛结果：`https://www.mcm.edu.cn/html_cn/block/018500ec1a6bd8c7e9997133def2b590.html`
- 中国大学生在线历年数学建模论文展示：`https://dxs.moe.gov.cn/zx/hd/sxjm/sxjmlw/qkt_sxjm_lw_lwzs.shtml`

这只是**视觉质量参考**。不得复制、描摹、换色复刻展示论文 Figure，也不得从展示图逆推任何数值。

## 最低成熟度目标

最终 Figure 至少应避免明显低于近年公开展示优秀论文的视觉完成度。重点检查：

| 维度 | PASS 要求 | 常见 FAIL |
|---|---|---|
| 信息主次 | 第一眼能识别核心对象、主要比较或临界区域 | 所有元素同权重、同饱和度 |
| 配色协调 | 色彩克制且有语义，同类对象全文一致 | 默认随机色序、彩虹色、过度鲜艳 |
| 字体与字号 | 按论文实际插入尺寸仍能读清坐标、单位、legend | MATLAB 窗口里清楚，插 Word 后变小 |
| 轴与网格 | 轴线清楚但不厚重；网格必要才启用且弱化 | 粗黑边框、密集深网格 |
| 留白与画布 | plot area、legend、colorbar、annotation 有稳定空间 | 文字挤压、裁切、大片无意义空白 |
| 图例策略 | 不遮挡证据，跨 panel 语义统一 | legend 压在关键数据上、每 panel 重复大图例 |
| 证据完整性 | 阈值、CI、边界、推荐点、样本分布存在时得到表达 | 为了好看把关键证据删成几根柱/线 |
| 图题关系 | caption 承担论文图名，图内只保留读图需要的标签 | 图内重复大标题、subtitle 堆叠 |
| 风格一致性 | 同篇论文颜色、字体、线宽、marker 语法基本稳定 | 每张图像来自不同模板 |
| 适度美感 | 干净、平衡、有焦点，视觉密度与科学信息匹配 | 霓虹、阴影、发光、装饰性 3D、花哨背景 |

## Benchmark Procedure

联网且当前任务是 CUMCM 正式 Figure 时：

1. 先按当前 Evidence Structure / Figure role 确定需要参考的同类图，而不是随机浏览“最好看的图”；
2. 查看近年公开展示论文中同类证据常见的版面、配色层级、标注密度、panel 关系和 caption 使用；
3. 当视觉模式已经趋于稳定即可停止，不设置固定篇数；
4. 只提取可迁移原则，不复制具体图形皮肤；
5. 回到当前 accepted workbook 和 Figure Contract 完成独立设计。

若无法联网，不阻塞绘图；直接按 Module 04 的稳定审美规则执行。

## Final-size 审美复核

所有准备进入正文的 Figure 都必须在预计插入宽度下复核，而不是只在 MATLAB / Python 大图窗里判断：

- 文字是否仍清楚；
- 主次是否仍明显；
- 颜色在缩小后是否仍可区分；
- legend / colorbar 是否挤压数据区；
- marker、线型和误差带是否仍可辨；
- a/b/c/d panel label 是否统一；
- 图与 caption 连续阅读时是否自然。

若缩小后美感和证据层级明显下降，优先重新布局、拆图、减少冗余标注或调整视觉权重，不要简单继续缩小字体。

## 与正文准入的边界

**好看不能让一张低价值图进入正文。** Competition Visual Quality Gate 只评估“值得存在的 Figure 是否画得成熟”；是否值得进入正文仍由 Main-text Admission Gate 决定。