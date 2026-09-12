# 结果图型选择索引

本文件只是候选视觉结构索引；通用 Figure 决策权统一属于 `modules/04_figure_evidence.md`。图型由 Core conclusion、Evidence Structure、accepted workbook 和信息展示效率共同决定，不按软件默认、外部图库示例、图型新奇度或固定禁用清单选择。

## 使用顺序

```text
Core conclusion
→ Evidence level
→ Evidence structure
→ Literature visual reference（必要时）
→ Visual Mapping
→ Candidate visual structures
→ Basic-form Challenge
→ Low-information Visualization Penalty
→ Composite / Layout
→ Rendering / Enhancement
→ Palette / Competition Visual Quality
→ Main-text Admission
```

其中 Visual Mapping 参考 `templates/figure/visual_mapping_contract.md`，CUMCM 最终视觉成熟度参考 `templates/figure/cumcm_visual_quality_gate.md`。本 Skill 采用“吸收理念、不增加外部运行依赖”的方案，不要求安装 gramm、SciencePlots、RainCloudPlots、UltraPlot、Crameri/cmap、export_fig 等包。

## 可选视觉参考

本地资产仅在图型或多面板布局需要视觉对照时按 `assets/figure_assets.yaml` 加载；外部论文视觉参考按 `templates/figure/literature_figure_reference.md` 执行。二者都不能提供本题数值事实、固定 palette 或最终结论。

## Figure-type Preference：优先高信息、可直接读懂的视觉结构

正文核心 Figure 的默认候选顺序应偏向能够直接承载趋势、比较、边界、推荐、区间和原始样本的结构：

**优先候选**：
- line / multi-line + interval / event / threshold；
- scatter / observed-vs-predicted / fit + CI；
- sorted dot / interval dot / lollipop；
- bar + error / benchmark（仅当绝对量比较确实最直接）；
- contour / isoline + direct labels / boundary；
- box/violin + raw samples；
- Pareto + feasible state + recommendation；
- overview + detail / inset / small multiples；
- 其他能把 Core conclusion 直接转成可比较几何位置、长度、趋势或边界的复合结构。

**低优先候选**：普通 matrix heatmap、gridmap、方格色块图、仅靠颜色深浅表达大小的矩阵图。它们不能因为“整齐”“容易生成”“看起来像科研图”自动进入候选前列。

这里的低优先不等于全面禁用：真实空间场、物理场、遥感栅格、相关矩阵、混淆矩阵、明确二维参数交互面等**二维结构本身就是科学对象**的情况仍可使用色场/矩阵表达，但必须通过下面的 Heatmap / Gridmap Exception Gate。

## Heatmap / Gridmap Ultra-low Priority Gate

普通 heatmap / gridmap / matrix color-block Figure 默认优先级设为 **ultra-low**。只有以下条件大体同时成立时，才允许进入正文候选：

1. 二维矩阵/网格结构本身就是当前 Core conclusion 的重要证据，而不是把一维比较硬铺成二维方格；
2. X/Y 两个维度都有真实、可解释的科学语义；
3. 颜色编码确实揭示 cluster、interaction、regime、boundary、anomaly、spatial field 或其他二维结构；
4. line / dot / bar / small multiples / contour-only / table 等更直接的替代结构会明显损失关键信息；
5. 关键模式在论文最终尺寸下仍可读，必要时有 contour/direct label、边界、推荐点或其他明确辅助，而不是只能“大概看颜色深浅”；
6. 通过 Main-text Admission，且能够写出明确的 `Unique information contribution`。

以下情况默认降级为 `APPENDIX / TABLE_ONLY / MERGE / DROP`，或改用更高信息结构：

- 时间序列或参数序列本可用 line/interval 清楚表达，却被铺成一排/多排色块；
- 少量类别比较本可用 sorted dot / interval dot / bar 更直接，却用方格深浅替代；
- 热力图只有颜色梯度，没有可解释二维模式、边界或交互；
- 图占版面很大，但正文只能得到“颜色更深/更浅”这种弱结论；
- colorbar 往返搜索成本高，读者无法快速读出关键数值；
- 为了“稳妥”“科研感”或避免设计更强的 Figure 而默认选择热力图。

## Low-information Visualization Penalty

任何候选 Figure 若“形式完整但信息密度低”，都必须降权。重点审查：

- 是否只能展示大小高低，却不能展示趋势、差异、边界、阈值、推荐或不确定性；
- 是否需要读者在大量颜色/方格中自行寻找结论；
- 是否占用较大版面却只能支撑一句很弱的描述；
- 是否因为保守地选择软件默认图型而牺牲了更直观、更美观的高信息结构；
- 是否存在更直接的 position / length / line / point / contour / small-multiple 编码。

若是，则优先重新设计，而不是仅通过换 palette、加边框、加网格把低信息图“美化”。

## Evidence Structure → Scientific Visual Structure

| Evidence Structure | 优先科学视觉结构 | 常见基础退化 | 需要检查的底层证据 |
|---|---|---|---|
| 简单离散比较 | interval dot / sorted dot / bar+error+benchmark | plain bar / color-block grid | 对象、指标、误差/区间、基准 |
| 分布 | box+raw、violin+raw+median、raincloud-like、ECDF+quantile | 均值柱状、plain box | 逐样本、组别、样本量、分位数 |
| 时间演化 | line+interval+event、state trajectory、overview+detail | plain line / time×metric heatmap | 时间、状态、区间、事件、阶段 |
| 空间结构 | field+path+boundary、critical node / flow；真实栅格场可用 field+contour | 区域均值柱状 / 无语义方格 | 坐标、网格/节点值、路径、边界 |
| 机制关系 | trajectory+critical state、phase/response relation | 指标柱状 | 机制变量、状态量、临界点 |
| 约束/可行域 | feasible region+boundary+recommended point | 可行/不可行计数柱状 | 约束、容差、变量、可行状态 |
| 参数响应 | 单参数优先 curve+stable/risk band；双参数优先 contour/response relation，只有通过 Heatmap Exception 才叠加色场 | 多组柱状 / 默认 heatmap | 参数网格、响应、阈值、状态 |
| 不确定性 | interval+raw、ECDF、quantile band | 均值±单数字 | 重复/场景结果、分位数、失败标记 |
| 多目标权衡 | Pareto+feasible state+knee+recommendation+zoom | 各目标分开柱状 | 全候选、各目标、推荐点 |
| 稳定/失效 | response+semantic background+threshold | “变化不大”折线 / 风险色块矩阵 | 扫描点、状态、阈值、失效标记 |
| 网络/流 | network+weighted flow+focus | 节点分数柱状 | 节点、边、权重、路径/流量 |
| 调度/资源 | Gantt+resource utilization+conflict context | 完工时间柱状 | 作业、资源、起止、占用/冲突 |
| 预测/诊断 | observed-vs-predicted+CI+residual/marginal | 模型指标柱状 | 逐样本真实/预测/残差/区间 |
| 全局—局部 | overview + inset/detached detail | 单图截轴 | 全局序列、ROI、临界/局部状态 |

## Visual Mapping 快速检查

在选最终图型前至少问：

- `X / Y` 是否对应最直接的比较或关系？
- `Color` 是否真的承担类别、方向、状态、风险或焦点语义？若颜色只是把本可用位置/长度表达的一维数值铺成方格，应优先不用 heatmap；
- `Size` 是否能准确表达第三个量，还是只是制造气泡视觉？
- `Shape / line style / hatch` 是否用于有意义的类别或 print-safe 冗余编码？
- `Facet / Panel` 是否表示阶段、场景、区域、算法、前后或全局—局部强关系？
- `Annotation` 是否只保留阈值、推荐点、事件、极值、边界等不可替代信息？
- `Uncertainty` 是否存在真实 CI、prediction interval、quantile 或样本离散性？

无真实语义的通道应删除，不为了“丰富”强行增加 color + size + shape + 3D + facet。

## Composite Encoding 快速索引

当多个编码共享同一证据空间并共同回答一个 Primary question 时，可优先组合：

- `box + raw scatter`；
- `violin / raincloud-like + raw + median/quartile`；
- `line + CI / prediction interval`；
- `scatter + fit/identity + CI`；
- `scatter + marginal histogram/KDE`；
- `bar + errorbar + benchmark`；
- `contour + feasible boundary + current/recommended point`；
- `heatmap + contour / feasible boundary` **仅在 Heatmap / Gridmap Ultra-low Priority Gate 通过后**；
- `Pareto + recommendation + Local Zoom`；
- `trajectory + field + boundary`；
- `observed-vs-predicted + interval + residual/marginal`。

组合的目标是保留真实样本、统计结构、阈值/边界和模型关系，不是增加装饰数量。双 Y 轴、柱线组合只有联合语义和量纲关系清楚时才允许。

## Scientific Rendering Profile 快速索引

| Profile | 核心元素 | 典型用途 |
|---|---|---|
| Distribution | raw + box/violin/ECDF + median/quantile | 分组、重复试验、鲁棒性 |
| Regression / Prediction | scatter + identity/fit + interval + residual/marginal | 预测、拟合、分类概率诊断 |
| Dynamic | trajectory + interval + event/threshold + zoom | 时序、状态演化、控制 |
| Parameter Response / Surface | 单参数 curve/band；双参数 contour+boundary+point，必要时才加低权重色场 | 参数敏感性、双因素响应 |
| Spatial | field/path/flow/node/boundary；真实空间场可使用连续色场 | 选址、路径、覆盖、空间残差 |
| Optimization / Pareto | candidates + Pareto + feasible state + knee/recommendation | 优化与方案选择 |
| High-density Scatter | alpha / binned / hexbin / 2D density | 大样本仿真、候选解云 |

## Publication-ready 候选结构

- **Multi-Metric Comparison Strip**：多指标比较同一对象且量纲/合理范围不同；
- **Ordered Ablation Ladder**：只用于真实嵌套递进模型；
- **Composition / Decomposition**：stack 必须可加和，分母明确；
- **Evidence Matrix**：对象×指标、场景×方法、阶段×状态等规则矩阵；只有矩阵结构本身有信息价值时使用，不把它默认实现为彩色方格；
- **Milestone-aware Trend**：事件/阶段必须有题面或 accepted evidence 来源；
- **Normalized Multi-Criteria Radar**：只用于少量对象、方向统一、归一化清楚的无量纲指标；
- **Density / State-Space Evidence**：density 辅助揭示结构，不覆盖原始样本；
- **Comparative Performance Matrix**：原始值与相对改善语义分离，列独立 normalization 不伪装跨列可比。

## Figure Enhancement 快速索引

| 当前问题 | 优先增强 |
|---|---|
| 全局尺度压缩关键差异/阈值 | Local Zoom / overview+detail |
| 多线遮挡、legend 搜索成本高 | Small Multiples |
| 对象多但核心只依赖少量对象 | Focus Highlighting |
| 存在真实稳定/风险/可行/阶段区 | Semantic Background |
| 中心关系、边际分布、残差共同决定可信度 | Composite Diagnostic |
| 第三维真实且 2D 明显损失结构 | Conditional 3D |

Enhancement 默认 `none`；没有信息增益就不增强。

## 图型退化与正文准入

正文核心 Figure 连续出现 plain bar / line / scatter 时，不机械换皮，而是回 accepted workbook 检查是否存在状态、时间、空间、分布、阈值、不确定性、多目标、候选解或逐样本证据。

同时，若正文候选集中出现大量 heatmap / 方格色块图，应视为**过度保守选图的警告信号**：逐张执行 Heatmap / Gridmap Ultra-low Priority Gate，并优先尝试 line / dot / contour / small multiples / composite 等更直接、更美观且信息密度更高的表达。

最终仍执行 Module 04 的 Main-text Admission：删除这张图后，若重要结论并不会明显更难被相信、理解、比较或验证，则优先 `APPENDIX / TABLE_ONLY / MERGE / DROP`。

本索引**不限制每问 Figure 数量**，也不要求固定图型多样性。只要求每张新增 Figure 有独立信息贡献，并达到相应科研与竞赛视觉质量。