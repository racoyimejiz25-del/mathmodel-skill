# Visual Mapping Contract

本模板实现 `modules/04_figure_evidence.md` 的 Visual Mapping Gate，不拥有独立 Figure 决策权。

## 目的

在决定 bar / line / scatter / heatmap / composite Figure 之前，先说明每个视觉通道到底承载什么科学证据。思想可借鉴 Grammar of Graphics / gramm，但本 Skill **不要求安装任何外部作图库**；MATLAB / Python 原生实现即可。

| 通道 | 当前映射 | 是否必要 | 证据职责 / 删除理由 |
|---|---|---|---|
| X |  | yes / no | 有序、连续、时间或类别变量 |
| Y |  | yes / no | 响应、状态、目标或比较指标 |
| Color |  | yes / no | 类别、方向、状态、风险或焦点语义；无真实语义则不用 |
| Size |  | yes / no | 第三个可比较量；若读者难以精确比较则改用 panel / label |
| Shape |  | yes / no | 类别/状态冗余编码，尤其用于色觉与黑白打印安全 |
| Facet / Panel |  | yes / no | 阶段、场景、区域、算法、前后对比等强关系 |
| Line style / Hatch |  | yes / no | 与颜色互补的 print-safe 次级语义 |
| Annotation |  | yes / no | 阈值、推荐点、极值、事件、边界、交点等不可替代信息 |
| Uncertainty |  | yes / no | CI、prediction interval、quantile、sample spread、失败场景 |

## Mapping 审查

- 每一个启用的视觉通道都必须能追溯到当前 Core conclusion、Evidence Structure 或 accepted workbook 中的真实证据。
- 不为了“信息量大”强行启用 color + size + shape + 3D + facet；通道越多，越需要证明它们不可替代。
- 同一对象、状态、方向性语义在同一 Figure、跨 panel 和跨正文 Figure 中保持一致。
- Color 不是默认首选编码；能用位置、长度、排序、线型或 facet 更准确表达时，不必用颜色承担全部语义。
- 颜色无法独立承担关键结论时，加入 marker / line style / hatch / direct label 等冗余编码。
- 若多个通道只是重复同一信息且没有降低搜索成本，应删除冗余通道。

## 与候选图型的关系

Visual Mapping 先于最终图型。完成 Mapping 后再进入：

`Candidate visual structures → Basic-form Challenge → Composite Encoding → Layout → Rendering / Enhancement`。

如果某个候选图型需要不存在或无意义的视觉通道才能成立，应否决该候选，而不是为图型迁就数据。