# 结果图 Figure Contract

| 字段 | 内容 |
|---|---|
| Figure ID | 图 X |
| Core conclusion | 一句话核心结论 |
| Evidence level | L1 / L2 / L3 / L4 |
| Primary question | 该 Figure 唯一一级阅读任务 |
| Figure role | 趋势 / 分布 / 诊断 / 敏感性 / 鲁棒性 / Pareto / 空间 / 网络 / 构成 / 多维画像 |
| Available evidence dimensions | 当前 accepted 工作簿实际具备的时间、空间、样本、状态、约束、不确定性、多目标等维度 |
| Evidence structure | 简单比较 / 分布 / 时间演化 / 空间 / 机制 / 边界 / 参数响应 / 不确定性 / 多目标 / 稳定区 / 网络 / 调度 / 诊断 / 全局—局部 |
| Literature search intent | 本图在选型前需要通过论文/权威资料解决的视觉问题；若无需外部检索，说明原因 |
| Literature visual references | 关键论文/报告及其反复出现的视觉结构、证据层和领域惯例；详细参考 `templates/figure/literature_figure_reference.md` |
| Transferable visual ideas | 可迁移到当前问题的结构性做法，如 raw points、CI、threshold、feasible boundary、zoom、marginal、residual、panel relation；不得复制现成 Figure |
| Figure level | F1 / F2 / F3；F1 核心图需通过 Basic-form Challenge |
| Candidate visual structures | 至少两个合理候选；可来自当前 Evidence Structure 与文献视觉参考，不要求为了多样性凑图型 |
| Selected visual structure | 最终采用的科学视觉结构 |
| Literature divergence rationale | 若最终图型不同于文献常见做法，说明为何当前数据结构/Core conclusion 更适合另一结构；若一致，说明采用的是结构原则而非图形照搬 |
| Basic-form challenge | 若最终为 plain bar/line/scatter/box/histogram，说明为何更丰富结构不存在或无信息增益；否则写通过升级 |
| Composite encoding | none 或 box+scatter / violin+scatter / line+interval / scatter+fit+CI / heatmap+contour / trajectory+boundary 等 |
| Scientific Rendering Profile | Distribution / Regression-Prediction / Dynamic / Parameter Surface / Spatial / Optimization-Pareto / High-density Scatter / custom |
| Palette profile | `competition_high_contrast / journal_balanced / monochrome_print / custom`；只选择与当前证据密度和论文场景匹配的 profile，具体规则服从 Module 04 Publication Rendering Grammar |
| Color semantics | 记录主对象、对照、基准、风险/失效、推荐方案、CI/区间、背景或参考元素各自承担的颜色语义；同一对象和同一方向性语义全文保持一致 |
| Aesthetic balance check | 检查白底、主次层级、视觉焦点、饱和度与明度层级、辅助元素降权，以及颜色复杂度是否与证据复杂度匹配；不得让所有对象同时高饱和争夺注意力 |
| Color accessibility / print fallback | 关键区分不得只依赖难以辨识的颜色；必要时追加 marker / line style / hatch 等冗余编码，使灰度打印和常见色觉差异下仍可判断核心结论 |
| Scientific value rationale | 相较替代方案如何增加可验证信息、揭示模型结构或降低评委搜索成本 |
| Unique information contribution | 相对当前论文已有图表，本 Figure 新增了什么可验证信息；若不能明确说明，优先合并或删除 |
| Main-text admission test | 删除这张图后，是否会让一个重要结论明显更难被相信、理解、比较或验证？若不会，则默认不直接进入正文 |
| Main-text admission decision | `MAIN_TEXT / APPENDIX / TABLE_ONLY / MERGE / DROP` |
| Main-text admission rationale | 说明其对正文论证链的不可替代贡献；若只是重复已有数值、视觉换皮、装饰性展示或弱信息图，应说明为何移附录、转表、合并或删除 |
| DOCX/LaTeX caption | 正式图号与图名；必要时补充样本、统计口径、时间范围和误差 |
| In-figure title | 正式论文图固定为 `none`；不设置整体 `title` / `sgtitle`，多面板按需只保留 a/b/c/d 等 panel label |
| Enhancement | 可选：none / Local Zoom / Small Multiples / Focus Highlighting / Semantic Background / Composite Diagnostic / Conditional 3D；可合理组合 |
| Enhancement rationale | 为什么基础布局不足，以及增强后增加了什么可验证信息或降低了什么视觉搜索成本 |
| Global/detail strategy | none / inset / detached zoom / overview+detail / split figures；说明全局—局部关系 |
| Rejected alternatives | 记录 1--2 个关键备选及否决原因，避免因为模板默认或“论文常见”而机械选图 |
| Source workbook | `问题X求解/问题X求解结果.xlsx` 或 `问题X求解/问题X结果深化分析.xlsx` |
| Worksheet | 中文工作表名 |
| Required columns | 绘图必需真实字段、记录键、单位和排序字段 |
| Expected positions | 可选列号，仅作结构漂移警告 |
| MATLAB script | `问题X求解/qX_plot.m` |
| Panel map | a/b/c/d 或其他 axes 的证据职责；无多面板时写单图职责 |
| Statistics/error | 误差线、区间、样本量和统计口径 |
| Export files | 求解阶段留空；论文阶段人工确认后可登记项目级 `figures/qx_*.pdf`、`.png` 或 `.svg` |
| Framework registry | `模型论文框架.md` 中的对应图表登记 |
| Paper location | 正文章节；仅 `MAIN_TEXT` 必须给出正文位置，其他决策记录附录/表格/合并去向 |
| Reviewer risk | 可能质疑点与处理 |

Figure Contract 默认登记在 `模型论文框架.md`，不生成独立 `figure_evidence` 文件。`Literature search intent / Literature visual references / Transferable visual ideas` 只记录选图依据，不把外部论文变成数值事实源；`Candidate visual structures / Basic-form challenge / Scientific value rationale` 只记录科研表达决策，不变成样式参数表；`Palette profile / Color semantics / Aesthetic balance check / Color accessibility` 只负责落实 Module 04 已有 Publication Rendering Grammar，不建立第二套配色 Authority；Enhancement 只记录决策与理由，**不记录 inset 坐标、透明度等 MATLAB 实现参数**。

合同的核心问题是：这张图为什么比一个普通柱状/折线/散点更能解释当前模型；若基础图已经是最直接答案，则说明其信息结构为何确实简单，而不是为了“高级”强行复杂化。文献中常见的图型只能作为候选，最终仍以当前 Core conclusion、真实 Evidence Structure 和 accepted workbook 为准。

## 科研配色控制：语义优先、审美受控

配色采用**半约束策略**，不把整篇论文锁死为一套固定蓝红 HEX 色值，也不允许每张图随意换色。颜色首先承担科学语义，其次才承担美感。总体目标是：白底、清楚、统一、主次分明、适度有吸引力，但不能以装饰性牺牲可读性和数据诚实。

- 对连续且单向递增的数值，优先使用感知上有序的 sequential colormap；颜色明度/饱和度变化必须与数值顺序一致。
- 只有存在真实中心点或参考值（如 0、目标值、基准值、正负偏差）时才使用 diverging colormap，并把中心准确放在该科学参考值上。
- 对无序类别使用 restrained qualitative palette；类别较多时优先结合 marker、line style、small multiples 或 focus highlighting，而不是无限增加高饱和颜色。
- 普通正文 Figure 优先形成“主色角色 + 强调角色 + 中性灰辅助”的视觉层级；这是一种审美倾向而非固定颜色数量上限。只有真实证据结构要求更多类别时才扩展颜色角色。
- 推荐方案、关键路径、阈值附近对象或主比较对象可以提高视觉权重；CI、原始背景点、参考线、非重点方案、辅助网格和语义背景应适度降权。
- 全文同一对象、同一状态和同一方向性语义保持稳定颜色映射，避免同一个“风险/基准/推荐方案”在不同 Figure 中反复换色。
- 禁止 `rainbow/jet`、无序彩虹、所有对象同时高饱和，以及单纯为了“高级感”增加渐变、霓虹、发光或大面积装饰色块。
- 红—绿不得作为唯一的关键信息区分；必要时用线型、marker、hatch、边框或文字标签提供冗余编码。
- 文献视觉参考可以帮助判断颜色层级和领域惯例，但不得照抄论文的完整 palette；仍需根据本题对象语义重新映射。

**美感不是独立的正文准入理由。**若一种配色“更好看”但破坏了数值顺序、类别区分、风险方向、阈值语义、黑白打印可读性或全文语义一致性，则否决该配色。配色优化只能发生在“数据真实 → 证据清楚 → 语义一致”的基础上。

在真正进入正文前必须执行 Main-text Admission Test。**“图已经画出来”“图看起来高级”“论文里别人也画过”“可以让论文更丰富”均不是正文准入理由。**正文 Figure 应直接承担一个重要结论的证明、比较、机制解释、边界识别、诊断或可信度支撑。若删除后正文核心判断基本不受影响，则优先 `APPENDIX / TABLE_ONLY / MERGE / DROP`，而不是为了作图而作图。

以下情况通常不应单独进入正文：与已有 Figure/Table 证明同一事实且没有新增结构；只把表格数值换成视觉形式；只展示“有变化”但没有阈值、比较、机制或决策含义；纯装饰性 3D、雷达、网络或复杂多面板；无法在正文附近明确写出“由图可得”的实质性结论。反之，即使图型简单，只要它是某个重要结论最直接、不可替代的证据，也可以进入正文。

本 Skill **不设置每问必须或最多多少张图的固定数量限制**。图数量由证据需要自然决定，但每张新增 Figure 都应能说明其相对已有图表的独立信息贡献，并通过正文准入判断。
