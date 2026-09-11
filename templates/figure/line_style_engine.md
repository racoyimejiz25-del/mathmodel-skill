# Line Style Engine：竞赛—期刊融合线条渲染

本模板只实现 `modules/04_figure_evidence.md` 中既有的 Publication Rendering Grammar、Visual Mapping、Palette / Aesthetic 与 Final-size QA 要求，**不拥有独立 Figure Authority，不改变任何已有准入、证据、数据事实源、图数量、文献参考或禁止事项**。

它解决的问题只有一个：**一张已经被允许存在、且其证据结构已经确定的 Figure，折线、直线、参考线、阈值线、拟合线和不确定性边界怎样画得更成熟、更清楚、更像高水平竞赛/科研论文。**

## 1. 综合策略：多来源吸收，不模仿任何比赛

采用“综合自适应型”思路，但不同来源只承担不同的渲染启发：

- 高教社杯 / CUMCM：作为中文数学建模论文的竞赛完成度与最终插入尺寸基线之一；
- MCM / ICM Outstanding 类论文：吸收线条层级、`color + linestyle + semantic background + threshold/event line` 等科学复合编码思想；
- 华中杯：吸收“评委第一眼能抓住重点”的焦点突出意识；
- APMCM：吸收跨 Figure 字体、线宽、图例、panel、留白和配色角色的一致性；
- MathorCup：吸收多方案、多场景、高信息密度时的降权、分组和可读性组织；
- 深圳杯等研究型建模竞赛：吸收技术论文式克制、严谨和不过度装饰的视觉语法。

以上都只是**可迁移原则**。不得复制、描摹、换色复刻任何具体论文的 Figure、palette、panel 排版、线型组合或视觉皮肤；不得为了“像某个比赛”改变当前 Core conclusion、Evidence Structure、accepted workbook 或 Main-text Admission 结论。

## 2. 默认策略：Journal Competition Hybrid

默认 line-style profile 为 `journal_competition_hybrid`：

> 高教社杯的竞赛可读性 + MCM/ICM 的线条层级 + 华中杯的重点突出 + 期刊绘图的克制感。

它不是固定皮肤，而是默认层级规则：

- 主结果清楚但不过粗；
- 对比结果比主结果略低视觉权重；
- 基准、参考、网格、背景轨迹进一步降权；
- 颜色、虚实、粗细、marker 分别承担不同语义，不让颜色独自承担全部区分；
- 同一对象、状态、方向性语义跨 panel / 跨 Figure 稳定；
- 最终以论文真实插入尺寸复核，而不是在 MATLAB/Python 大窗口里判断。

## 3. 可选 Line Style Profiles

### `competition_clean`

适合普通时序、趋势、方案比较、敏感性辅助图。特点：白底、主线清楚、对比线克制、参考线弱、marker 少、网格弱或关闭。

### `journal_competition_hybrid`（默认）

适合大多数正式正文结果图。特点：线宽、实虚、饱和度和 marker 分工明确；既保留竞赛快速阅读，也避免 Excel/MATLAB 默认软件感。

### `decision_highlight`

适合最优方案、推荐策略、关键路径、临界点和策略切换。只允许少量核心对象进入最高视觉权重；其他方案必须主动降权，避免所有曲线同时高亮。

### `dense_scientific`

适合多算法、多场景、多轨迹、参数扫描和 ensemble。少量 focus lines 保持可见，大量 context lines 使用更细、更浅或更透明的表达；若仍难读，优先 small multiples / 合理拆图，而不是继续堆颜色。

### `technical_monochrome`

适合技术验证、理论对照、收敛/误差、打印友好场景。主要依赖灰阶、line style、marker、line weight，不让颜色成为唯一语义。

Profile 只决定渲染起点，不改变 Figure Evidence level、Figure level、Main-text Admission 或 Layout / Split decision。

## 4. Line Role Classification：先分角色，再定样式

每条线先声明角色：

- `FOCUS`：主结果、推荐方案、关键预测、主要机制线；
- `COMPARISON`：其他方案、场景、算法、对照组；
- `CONTEXT`：历史背景、ensemble 背景轨迹、非重点路径；
- `REFERENCE`：零线、均值线、1:1 line、基准线；
- `THRESHOLD_BOUNDARY`：风险阈值、可行边界、目标线、事件线；
- `FIT_MODEL`：拟合线、预测线、理论曲线；
- `UNCERTAINTY_BOUNDARY`：CI / prediction interval / quantile envelope 的边界。

不得所有线默认同粗、同饱和、同线型。

## 5. Visual Mapping for Lines

优先按以下语义分工：

```text
Color      = 对象 / 指标 / 稳定类别语义
LineStyle  = 场景 / 状态 / 观测-vs模型 / 基准-vs结果
LineWidth  = 重要程度 / 视觉权重
Marker     = 真实离散采样点 / 关键事件 / 推荐点 / 临界点
Band       = 真实区间 / 不确定性 / 阶段背景
Annotation = 少量不可替代的极值、交点、阈值、策略切换
```

如果一个通道没有真实语义，就不要启用。颜色、虚实、粗细、marker 不应重复表达同一信息，除非是为了灰度打印或色觉可访问性的必要冗余编码。

## 6. 线宽层级：使用相对层级，不设死值

线宽采用相对层级，不设置跨所有 Figure 的硬阈值。可把以下数值作为常见正文尺寸下的**起点区间而非固定规则**：

- `FOCUS`：约 1.7–2.1 pt；
- `COMPARISON`：约 1.1–1.5 pt；
- `CONTEXT / REFERENCE`：约 0.8–1.1 pt；
- 真正承担核心结论的 `THRESHOLD_BOUNDARY` 可略高于普通 reference，但原则上不应压过主数据线。

实际值必须根据 Figure 尺寸、DPI/vector export、曲线密度、颜色对比和论文插入宽度调整。若缩小后层级消失，重新布局或调整相对权重，不机械把全部线一起加粗。

## 7. LineStyle Policy：虚实必须有语义

- 实线优先承担主结果、主要观测或主要方案；
- 虚线可承担模型/拟合、次场景、基准或对照；
- 点划线优先承担阈值、目标、事件或特殊状态；
- 点线只在低权重参考或额外场景确有必要时使用；
- 不得为了“丰富”给每条线随机分配 dash pattern；
- 多 panel 中同一语义必须保持同一线型。

当 `Color = 指标/对象` 时，可以优先令 `LineStyle = 场景/状态`，避免同一张图同时需要大量颜色。

## 8. Marker Policy：marker 是证据，不是装饰

- 密集连续时序默认不显示每个点 marker；
- 离散实验、参数扫描、年份/场景等真实离散点可使用小 marker；
- 推荐点、极值、交点、阈值触发点、策略切换点可单独加强 marker；
- 点数很多时允许稀疏显示 marker，但折线本身仍必须连接全部真实数据点；
- 不得为了“好看”给每条线分配大而不同的 marker；
- marker 不得遮住误差棒、关键交点或邻近曲线。

## 9. Smoothing / Interpolation Policy：美观不能制造数据

- 离散实验点、年份、独立场景、参数扫描、算法迭代记录默认保持真实折线或真实采样结构；
- **禁止为了圆润使用 spline / Bezier / 高阶插值制造不存在的新峰谷、拐点或阈值交点**；
- 只有模型本身定义连续函数、物理过程确为连续曲线，或已合法完成平滑/拟合且该处理属于 accepted 事实源时，才允许画平滑线；
- 若同时展示拟合和平滑结果，原始采样点或原始趋势必须仍可验证，不得用光滑线掩盖不利数据。

## 10. Uncertainty / Band Policy

当上下界的主要职责是表达不确定性时，优先使用：

> 主趋势线 + 低视觉权重 band

而不是让 `center / upper / lower` 三根线拥有相同视觉权重。

只有上下界本身具有独立物理、可行性或安全边界意义时，才把上下界作为正式边界线强调。Band 的透明度、颜色和边界不能遮蔽主数据或误导范围宽度。

## 11. Reference / Threshold / Grid Hierarchy

视觉权重一般满足：

```text
FOCUS data
> important COMPARISON / meaningful THRESHOLD
> ordinary COMPARISON
> REFERENCE
> GRID / decorative context
```

- 普通 grid 默认关闭；确实提高读数效率时才使用浅、稀、置于数据后方的网格；
- 零线、1:1 line、均值线、基准线使用中性细线；
- 阈值/事件线只有真正承担结论时才提高视觉权重；
- 不得出现粗黑边框 + 粗网格 + 粗数据线同时竞争注意力。

## 12. Multi-line / Dense Figure Policy

当线很多时，不以“再加颜色”作为第一解决方案：

1. 先确认是否真的需要所有线同时存在；
2. 保留少量 `FOCUS`，其余转为 `COMPARISON / CONTEXT`；
3. 可使用浅化、细化、适度透明、同色族或 shared legend；
4. 语义允许时使用 `Color = object`、`LineStyle = scenario` 的二维编码；
5. 若视觉搜索成本仍高，优先 small multiples / focus highlighting / 合理拆图；
6. 不得隐藏对结论不利的真实轨迹。

## 13. Annotation Density Policy

默认不对每个折线点标数值。优先只标：

- 关键极值；
- 重要交点；
- 阈值首次触发；
- 推荐方案；
- 策略切换；
- 必须在图中即时读取的关键数字。

大量精确数值交给 Table / caption / 正文，不用 annotation 把折线图变成数据标签墙。

## 14. Paper-level Consistency

整篇论文至少保持以下线条语法稳定：

- 同一对象的主色角色；
- 同一“推荐/最优/风险/基准”语义；
- observation / model / benchmark / threshold 的实虚习惯；
- 典型主线、对比线、reference 的相对线宽层级；
- marker 的含义；
- panel / legend / grid 的使用方式。

不同 Figure 可以根据 Evidence Structure 切换 profile，但不应让每张图看起来来自不同模板。

## 15. Final-size Line QA

正文 Figure 在预计插入宽度下至少检查：

- 主线是否仍明显但不过粗；
- 次要线是否仍可辨但不抢焦点；
- dash pattern 缩小后是否还能区分；
- marker 是否变成视觉噪声；
- reference / grid 是否过重；
- band 是否吞没主线；
- 多线在灰度打印或常见色觉差异下是否仍能完成核心比较；
- 最细线在目标导出格式中是否丢失；
- 关键阈值、交点、推荐点是否仍清楚。

若 FAIL，优先调整相对线宽、线型、布局、label 或拆分，而不是盲目增加所有颜色与线宽。

## 16. 与现有限制的边界

本模板明确不改变以下已有规则：

- 不设置每问必须或最多多少张 Figure；
- 不因为风格漂亮而新增 Figure；
- 不改变 Main-text Admission 的 `MAIN_TEXT / APPENDIX / TABLE_ONLY / MERGE / DROP`；
- 不改变“删除这张图后，重要结论是否更难被相信、理解、比较或验证”的正文准入测试；
- 不改变 accepted workbook / 真实字段 / 数值事实源要求；
- 不允许 MATLAB/Python 绘图脚本重新求解、重新统计或反推底层数据；
- 不改变 Literature-Guided Figure Reference 的“参考结构而不复制”原则；
- 不改变 semi-constrained scientific palette、禁止 rainbow/jet、红绿不得作为唯一关键信息区分等配色规则；
- 不改变 Basic-form Challenge、Composite Encoding、Layout、Enhancement、Final-size / Export QA 和 Portfolio Gate；
- 不增加 gramm、SciencePlots、外部 colormap、export_fig 或任何其他第三方运行依赖。

**线条美感只能提高已经成立的证据表达质量，不能创造证据，也不能改变一张图是否应该存在。**