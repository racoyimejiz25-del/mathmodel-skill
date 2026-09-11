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
→ Composite / Layout
→ Rendering / Enhancement
→ Palette / Competition Visual Quality
→ Main-text Admission
```

其中 Visual Mapping 参考 `templates/figure/visual_mapping_contract.md`，CUMCM 最终视觉成熟度参考 `templates/figure/cumcm_visual_quality_gate.md`。本 Skill 采用“吸收理念、不增加外部运行依赖”的方案，不要求安装 gramm、SciencePlots、RainCloudPlots、UltraPlot、Crameri/cmap、export_fig 等包。

## 可选视觉参考

本地资产仅在图型或多面板布局需要视觉对照时按 `assets/figure_assets.yaml` 加载；外部论文视觉参考按 `templates/figure/literature_figure_reference.md` 执行。二者都不能提供本题数值事实、固定 palette 或最终结论。

## Evidence Structure → Scientific Visual Structure

| Evidence Structure | 优先科学视觉结构 | 常见基础退化 | 需要检查的底层证据 |
|---|---|---|---|
| 简单离散比较 | interval dot / sorted dot / bar+error+benchmark | plain bar | 对象、指标、误差/区间、基准 |
| 分布 | box+raw、violin+raw+median、raincloud-like、ECDF+quantile | 均值柱状、plain box | 逐样本、组别、样本量、分位数 |
| 时间演化 | line+interval+event、state trajectory、overview+detail | plain line | 时间、状态、区间、事件、阶段 |
| 空间结构 | field+path+boundary、critical node / flow | 区域均值柱状 | 坐标、网格/节点值、路径、边界 |
| 机制关系 | trajectory+critical state、phase/response relation | 指标柱状 | 机制变量、状态量、临界点 |
| 约束/可行域 | feasible region+boundary+recommended point | 可行/不可行计数柱状 | 约束、容差、变量、可行状态 |
| 参数响应 | curve+stable/risk band、heatmap+contour+operating point | 多组柱状 | 参数网格、响应、阈值、状态 |
| 不确定性 | interval+raw、ECDF、quantile band | 均值±单数字 | 重复/场景结果、分位数、失败标记 |
| 多目标权衡 | Pareto+feasible state+knee+recommendation+zoom | 各目标分开柱状 | 全候选、各目标、推荐点 |
| 稳定/失效 | response+semantic background+threshold | “变化不大”折线 | 扫描点、状态、阈值、失效标记 |
| 网络/流 | network+weighted flow+focus | 节点分数柱状 | 节点、边、权重、路径/流量 |
| 调度/资源 | Gantt+resource utilization+conflict context | 完工时间柱状 | 作业、资源、起止、占用/冲突 |
| 预测/诊断 | observed-vs-predicted+CI+residual/marginal | 模型指标柱状 | 逐样本真实/预测/残差/区间 |
| 全局—局部 | overview + inset/detached detail | 单图截轴 | 全局序列、ROI、临界/局部状态 |

## Visual Mapping 快速检查

在选最终图型前至少问：

- `X / Y` 是否对应最直接的比较或关系？
- `Color` 是否真的承担类别、方向、状态、风险或焦点语义？
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
- `heatmap + contour / feasible boundary`；
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
| Parameter Surface | heatmap + contour + point + feasible boundary | 参数敏感性、双因素响应 |
| Spatial | field + path/flow + node + boundary + colorbar | 选址、路径、覆盖、空间残差 |
| Optimization / Pareto | candidates + Pareto + feasible state + knee/recommendation | 优化与方案选择 |
| High-density Scatter | alpha / binned / hexbin / 2D density | 大样本仿真、候选解云 |

## Publication-ready 候选结构

- **Multi-Metric Comparison Strip**：多指标比较同一对象且量纲/合理范围不同；
- **Ordered Ablation Ladder**：只用于真实嵌套递进模型；
- **Composition / Decomposition**：stack 必须可加和，分母明确；
- **Evidence Matrix**：对象×指标、场景×方法、阶段×状态等规则矩阵；
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

最终仍执行 Module 04 的 Main-text Admission：删除这张图后，若重要结论并不会明显更难被相信、理解、比较或验证，则优先 `APPENDIX / TABLE_ONLY / MERGE / DROP`。

本索引**不限制每问 Figure 数量**，也不要求固定图型多样性。只要求每张新增 Figure 有独立信息贡献，并达到相应科研与竞赛视觉质量。