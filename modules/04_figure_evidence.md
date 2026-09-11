# Module 04：结果图、预处理图证据与机理图精修

本模块是当前 Figure Evidence 的单一通用 Authority。`packs/artifact/figure.md`、`templates/figure/*.md` 与各类绘图模板只能引用或实现这里的规则，不得建立第二套绘图决策权威。

本模块采用 **方案 4：只吸收成熟科研作图方法的设计理念，不把 gramm、SciencePlots、RainCloudPlots、UltraPlot、Crameri/cmap、export_fig 等外部包变成运行依赖**。数据驱动 Figure 的正式渲染后端在 Python / MATLAB 中按当前 Figure 实际需要选择；外部项目只提供图形语法、证据叠加、布局、科学配色和出版 QA 的设计启发，不形成软件强制。

## 顶层 Figure Workflow

进入本模块时先读取 current `模型论文框架.md` 中的当前有效口径、相关小问结果摘要、待办缺口和既有图表映射，用于确定“哪些结论需要图证据”；随后再从真实工作簿读取具体数值和底层序列。不得仅凭聊天记忆或框架摘要数字反推图数据。

顶层顺序固定为：

```text
核心结论
→ 证据层级
→ 证据结构
→ 文献视觉参考（必要时）
→ Visual Mapping
→ 候选视觉结构
→ Basic-form Challenge
→ 合图 / 拆图
→ Rendering Backend Selection
→ Scientific Rendering Profile
→ 科研增强
→ 配色与视觉层级
→ Line Style Engine
→ Clarity & Visibility Review
→ Aesthetic Review
→ Main-text Admission
→ Final-size / Export QA
→ Portfolio Gate 与正文证据闭环
```

`Primary question`、`Available evidence dimensions`、工作簿字段检查、图例策略、画布策略等继续作为内部执行检查，不从工作流中删除。

## 正确顺序

1. 继承已经锁定的 `preprocessing_decision`；若为 `project_level`，确认 `数据预处理结果.xlsx` 已 accepted 且预处理质量门通过；
2. Python 完成完整主求解并通过主结果质量门；03A 应已经保存本次主计算真实产生且具有解释/绘图/验证价值的状态、过程与结构证据；
3. Python 基于题目风险完成实际需要的结果深化分析，并验收 `问题X求解/` 中两个标准工作簿；03B 应保存参数、场景、阈值、算法、结构、异质性等分析的细粒度底层证据；
4. 只有上述数值阶段完成后才进入 Figure Evidence；先明确每张图读取原始数据、统一预处理工作簿或两个标准结果工作簿中的哪一种事实源；
5. 若为 `project_level`，项目级预处理证据图脚本由 Rendering Backend Selection Gate 在 `数据预处理/data_process_plot.py` 与 `数据预处理/data_process.m` 中二选一；两者都只能把已验收预处理工作簿中的底层证据转成图，不得重新执行预处理；
6. 为每个候选 Figure 写 Core conclusion、Evidence level、Primary question、Available evidence dimensions；
7. 识别 Evidence Structure；若同领域视觉惯例、复杂证据或候选图型不确定，执行 **Literature-Guided Figure Reference Gate**；
8. 执行 **Visual Mapping Gate**，先明确 `x / y / color / size / shape / facet / annotation / uncertainty` 各自是否承担真实证据语义；
9. 执行 **Scientific Figure Synthesis Gate**，比较合理候选视觉结构；不得先问“bar 还是 line”；
10. 若候选核心图退化为 plain bar / plain line / plain scatter / plain box / plain histogram，执行 **Basic-form Challenge**；
11. 执行 **Composite Encoding Preference** 与 Figure Layout Gate，先决定互补证据应合图还是拆图，再进入渲染；
12. 执行 **Rendering Backend Selection Gate**，按当前图型、直接标注、前景—背景对比、字体、layout、透明对象、最终尺寸和导出表现，在 Python / MATLAB 中选择综合质量更好的正式生产后端；不强制任一后端；
13. 选定后端后进入对应 **Scientific Rendering Profile**；
14. 基础布局确定后执行 Figure Enhancement Gate；只有在增加可验证信息、降低视觉搜索成本或强化关键证据时增加 Local Zoom、Small Multiples、Focus Highlighting、Semantic Background、Composite Diagnostic 或 Conditional 3D；
15. 执行 Publication Rendering Grammar、Line Style Engine 与 **Competition Visual Quality Gate**，完成语义配色、画布、字体、图例、留白、线宽和视觉层级；
16. 执行 **Clarity & Visibility Review**；检查关键线/等值线/边界/标签是否表述清楚且肉眼可见，必要时增加 contour/direct labels、调整前景—背景对比、线宽、线型或重新进入 Backend Selection；
17. 执行 **Aesthetic Review**；在清晰、数据诚实和语义一致前提下检查整体协调、成熟度、留白、视觉焦点和是否存在默认软件感；
18. 执行 **Main-text Admission Gate**，决定 `MAIN_TEXT / APPENDIX / TABLE_ONLY / MERGE / DROP`；图已画完、图很清楚或图很漂亮都不等于可以入正文；
19. 生成正式绘图代码前实际读取工作簿，锁定工作簿名、工作表名、真实表头、单位和数据类型；
20. 拟定 DOCX/LaTeX 正式 caption；正式论文图不设置整体 `title` / `sgtitle`，多面板按需只保留 a/b/c/d 等 panel label；
21. 各问正式生产脚本在同一 `问题X求解/` 中按后端二选一：`q{x}_plot.py` 或 `q{x}_plot.m`；默认不同时保留两份正式生产脚本。项目级预处理图脚本同理二选一；
22. 在论文预计插图宽度下执行 Final-size Readability / Export QA，再执行 **Figure Portfolio Scientific Quality Gate**；
23. 检查核心结论是否有图或表证据并同步 `模型论文框架.md`；默认只保留交互图窗或本地预览供人工检查，除非用户明确要求正式导出。

本 Skill **不设置每问必须或最多多少张图的固定数量限制**。数量由证据需要自然决定；只限制重复、低价值、无独立信息贡献和“为了作图而作图”的 Figure。

## A 类：机理与推导图

优先表达公式来源、约束来源、临界状态和策略机制。图内只放对象、变量、方向、边界、距离、角度、流向和临界状态，完整推导留在正文。禁止用通用“输入—模型—输出”流程图替代题目专属机理图。

正式机理/推导图采用 **monochrome-first（黑白线稿优先）** 视觉语法：默认白底、黑色或深灰轮廓/箭头/文字，次级结构仅用灰度、线宽、虚实、形状和留白降权。只有黑白线型与形状仍不足以区分且确有论证收益时，才允许加入少量强调色，并必须保证转灰度或黑白打印后仍能辨识。

对象表达优先使用与题意实体一致的规则几何图元；几何精度要求高时可交给 Python / MATLAB / TikZ / GeoGebra。禁止用渐变、阴影、拟物 3D、高饱和色块或无来源图标制造“立体感”。视觉层级优先顺序为 `shape / geometry → line style / line width → grayscale → optional accent color`。

### Mechanism Diagram Backend Selection Gate

| 证据结构 | 首选后端 | 准入理由 |
|---|---|---|
| 题目对象关系、机制作用链、反馈、状态切换、约束来源，且赛中需要快速修改对象/箭头/文字 | draw.io | 离散关系适合可编辑矢量图元 |
| 工作簿驱动的主结果、分布、误差、敏感性、空间场、Pareto 或网络权重 | Python / MATLAB | 先按 Rendering Backend Selection Gate 比较当前 Figure 的清晰度、审美、最终尺寸和导出表现 |
| 精确二维几何、连续函数、切线、坐标变换或按比例边界 | Python / MATLAB / TikZ / GeoGebra | 需要解析或坐标精度；数据驱动部分仍受事实源约束 |
| 简短公式依赖且必须与 LaTeX 字体一致 | TikZ | 直接服从论文公式环境 |
| 临时讨论草图 | PPT / 手绘 | 只能作为草案，入文前转为正式后端 |

draw.io 仅适用于**非数据驱动、题目专属且能绑定模型/公式/约束/判定条件**的机理图。只有通用研究阶段、算法名称或“输入—处理—输出”盒子的图不得作为核心机理图。

### Editable draw.io 生产链

```text
current Framework + Mechanism Contract
→ backend selected
→ mechanism_drawio_spec v1
→ deterministic uncompressed .drawio
→ structure_checked
→ preview_rendered
→ visual_reviewed
→ approved_for_paper
→ formal PDF/SVG/PNG + Framework登记
```

执行要求：先恢复题目对象、符号、公式、约束、判断条件和 Core conclusion；具体数值仍只能来自 accepted workbook。静态校验只能检查结构、几何和安全，不能替代语义真实性与审美复核。未查看最新渲染预览时不得进入 `approved_for_paper`。

纯视觉修改不递增模型 `semantic_revision`；新增/删除对象、改变关系方向、公式、约束、阈值、判定条件或反馈属于语义修改，必须回到 current Framework 与模型 Authority 裁决。

具体字段和 CLI 参考 `templates/figure/mechanism_drawio_spec.yaml` 与 `templates/figure/mechanism_drawio_patterns.md`；它们只实现本节，不拥有独立 Figure 决策权。

## B 类：项目级预处理证据图

当 `preprocessing_decision=project_level` 时，必须生成独立的预处理**绘图**脚本，但不强制 MATLAB。正式生产脚本由 Rendering Backend Selection Gate 在以下两种形式中二选一：

- `数据预处理/data_process_plot.py`
- `数据预处理/data_process.m`

二者都只读取 `数据预处理/数据预处理结果.xlsx`。绘图脚本不允许重新清洗、插值、滤波、重采样、预测填补、训练模型或重新确定参数；Python 被选作绘图后端也不能借“已有 Python 环境”把预处理或统计重新塞回 Figure 阶段。

至少有一张图直接回答：为什么需要处理、处理是否解决已审计问题、恢复误差是否可接受、滤波是否保留信息、重采样/对齐是否满足模型输入、异常处理是否有清晰边界等问题之一。优先考虑处理前后时序/轨迹/空间场、缺失与恢复、分布 + 原始点、真实值—恢复值 + 误差、频谱、重采样覆盖、阈值边界等证据。

## C 类：各问结果图合同

每张结果图至少记录：Core conclusion、Evidence level、Primary question、Figure role、Available evidence dimensions、Evidence structure、Literature visual reference、Visual mapping、Figure level、Candidate visual structures、Selected visual structure、Basic-form challenge、Composite encoding、Layout / Split decision、Rendering backend、Backend rationale、Scientific Rendering Profile、Palette profile、Color semantics、Line style profile、Clarity & visibility review、Aesthetic review、Competition visual benchmark、Unique information contribution、Main-text admission decision、In-figure title=`none`、论文 caption、Panel map、Enhancement、Source workbook、Worksheet、Required headers、Figure script、Statistics/error、Reviewer risk、Paper location 和 Caption duty。详细字段由 `templates/figure/result_figure_contract.md` 实现。

结果证据优先来自本问标准工作簿：主结果证据来自 `问题X求解结果.xlsx`；参数、场景、算法、结构、阈值、异质性和稳定范围证据来自 `问题X结果深化分析.xlsx`。**无论 Python 还是 MATLAB，绘图脚本都不得重新求解、重新做敏感性/统计分析或从摘要数字反推绘图序列。**

## Figure Evidence 层级

```text
L1 主结果证据       → 直接回答本问主要数值/结构结论
L2 机制或异质性证据 → 解释结论为何发生、发生在哪里、对谁成立
L3 稳健性证据       → 敏感性、阈值、场景、多算法、结构稳定范围
L4 数值合法性证据   → 收敛、频带、残差、可行性、预处理有效性等方法后盾
```

同一 Figure 可以包含多个 panel，但默认应属于同一 Evidence level 并共同回答一个 Primary question。跨层级合图只有在同屏比较确实不可替代时才允许。

## Literature-Guided Figure Reference Gate：查论文是为了选图，不是复制图

当图型选择不确定、证据结构复杂、领域存在稳定可视化惯例，或普通基础图明显不足时，先查同领域论文、综述、会议论文、官方技术报告与高质量竞赛展示论文，回答：**“同类研究通常如何把同类证据变成可验证的 Figure？”**

重点观察：图型/坐标结构、变量映射、raw points / CI / threshold / benchmark / feasible boundary / recommendation 等证据层、多 panel 关系、全局—局部组织、caption 职责与领域惯例。详细记录参考 `templates/figure/literature_figure_reference.md`。

规则：

- 文献只提供候选视觉结构，不提供本题数值事实；
- 不复制、描摹、换色复刻或从截图逆推数据；
- 不按出现频率投票选图；当前 Core conclusion + Evidence Structure + accepted workbook 永远优先；
- 不设置固定检索篇数；当视觉模式已趋于稳定即可停止；
- “文献里常见”不能单独成为新增 Figure 或正文准入理由。

## Visual Mapping Gate：先声明证据映射，再选择图型

吸收 Grammar-of-Graphics / gramm 的思想，但**不引入其软件依赖**。候选 Figure 在选图前先声明：

```text
X          = 哪个有序/连续/类别变量
Y          = 哪个响应/指标/状态量
Color      = 是否承担真实类别、方向、状态或焦点语义
Size       = 是否真的对应第三个可比较量
Shape      = 是否用于类别/状态冗余编码
Facet      = 是否表示阶段、场景、区域、算法或其他可比较分组
Annotation = 阈值、推荐点、极值、事件、边界等哪类不可替代信息
Uncertainty= CI / prediction interval / quantile / sample spread 等真实不确定性
```

任何通道若没有真实语义就留空。不得为了“丰富”强行把无意义变量塞进颜色、尺寸、3D、marker 或 panel。Visual Mapping 的目标是防止软件默认图型反客为主，并让同一对象跨 panel / 跨 Figure 保持稳定视觉语义。

## Scientific Figure Synthesis Gate：从证据结构设计 Figure

正式绘图前识别 Evidence Structure：简单离散比较、分布、时间演化、空间结构、机制、约束/可行域、参数响应/交互、不确定性、多目标、稳定/风险/失效区域、网络流、调度、诊断、全局—局部等。

每个候选核心图至少比较两种合理视觉结构，选择依据是：能否揭示模型结构、是否保留真实数据粒度、是否提高可验证信息密度、是否降低评委搜索成本、是否更直接支撑当前 Core conclusion。高级不是复杂；直接二维图能闭合结论时，不得为了“高级感”强行 3D 或堆编码。

## Basic-form Challenge：基础图只在信息结构确实简单时保留

plain bar / line / scatter / boxplot / histogram 允许使用，但若准备进入正文核心 Figure，必须先检查 accepted 数据是否还包含时间/空间结构、原始样本、不确定性、约束/边界、机制变量、参数交互、多目标、全局—局部、阈值或策略切换。存在这些结构且能提高可验证信息密度时，优先升级表达。

- **F1 基础表达**：真正的一维简单事实、辅助图和附录；
- **F2 增强科研表达**：box+raw、violin+raw、line+interval、scatter+fit/identity+CI、heatmap+contour、ECDF+quantile、Gantt+utilization、Pareto+recommendation 等；
- **F3 核心科学综合图**：空间场+轨迹+边界+临界状态、Pareto+可行状态+推荐+局部放大、response surface+contour+稳定/失效区等。

F2/F3 的“高级”来自证据结构，不来自装饰数量。

## Composite Encoding Preference：同一证据空间优先融合互补编码

当多个编码共享同一证据空间并共同回答一个 Primary question 时，优先融合。例如：箱线+原始散点、小提琴+原始点+中位数、折线+CI、散点+拟合/1:1线+CI、散点+边际分布、柱状+误差棒+基准、热力图+等高线/阈值边界、Pareto+推荐点+Local Zoom、轨迹+空间场+边界、真实—预测+区间+残差。

双 Y 轴、柱线组合等只有联合语义与量纲关系清楚时才允许，禁止为了“显得高级”强行叠加。

## Figure Layout Gate：先证据关系，后版式

不存在固定默认版式。单图能闭合 Primary question 时优先单图；两个证据单元强配对使用 1×2 / 2×1；三个 panel 必须形成不可拆序列才使用 1×3；2×2 只有四个 panel 服务同一 Core conclusion、结构对称且拆开会明显损失直接比较时保留。超过 4 panel 只在 small multiples / 地图阵列 / 参数矩阵 / 时序快照等“多 panel 本身就是比较结构”时例外。

这里的 panel 复杂度建议**不是每问 Figure 数量上限**。当两个 Figure 分别承担不可替代的 L1/L2/L3 证据时可以同时存在。

## Rendering Backend Selection Gate：Python / MATLAB 谁更适合当前 Figure

数据驱动 Figure 不设置固定 MATLAB 或 Python 默认。后端选择只发生在 Figure 的证据结构和视觉结构已经确定之后，详细执行参考 `templates/figure/rendering_backend_selection.md`。

至少比较：

- 当前图型与 Evidence Structure 的实现自然度；
- contour/direct label、线条/背景对比、marker、band、annotation 的可控性；
- 中文/公式/单位 typography；
- shared legend、colorbar、inset、small multiples、复杂 panel 的 layout；
- scientific colormap、透明对象和高密度数据的表现；
- 论文实际插入宽度下的可读性；
- PDF/SVG/EPS/PNG 导出后的字体、裁切、透明度和最细线；
- 当前项目的可复现环境与整篇 Figure 风格一致性。

**不要求每张图都写 Python 和 MATLAB 两份代码。**只有 F3/MAIN_TEXT 核心图且后端优劣不明确、当前后端经过合理修正仍不能通过 Clarity/Aesthetic Review，或用户明确要求时，才做同数据、同 Visual Mapping、同最终尺寸的低成本小样比较；最终默认只保留一个正式生产后端。

如果两者视觉质量实质相当，优先当前项目更稳定、更少新增依赖且更容易维持全文一致性的后端；这只是 tie-breaker，不构成固定软件偏好。

## Scientific Rendering Profiles

- **Distribution**：raw samples 优先可见；box/violin + scatter、ECDF + quantile 或 histogram/density + raw context；
- **Regression / Prediction**：observed-vs-predicted、identity/合法 fit、CI/prediction interval、residual/marginal；
- **Dynamic**：trajectory/state + uncertainty + event/threshold + critical point，必要时 Global–Detail；
- **Parameter Surface**：heatmap + contour + current/recommended point + feasible boundary；第三维确有意义才用 3D；
- **Spatial**：field + path/flow + critical nodes + boundary + colorbar；
- **Optimization / Pareto**：candidates + Pareto + feasible state + recommendation + knee/threshold + global/detail；
- **High-density Scatter**：alpha scatter、binned/hexbin、2D histogram/density contour，避免不可读点云。

Profile 描述证据如何渲染，不绑定 Python 或 MATLAB。

## Figure Enhancement Gate：焦点—上下文信息增强

Enhancement 默认 `none`。只有增强后能增加可验证信息、降低视觉搜索成本或强化关键证据才启用：

- **Local Zoom**：临界点、交点、Pareto 膝点、残差尾部、局部关键窗；主图保留全局上下文；
- **Small Multiples**：多线遮挡、legend 搜索成本高；跨 panel 幅度比较时保持统一尺度；
- **Focus Highlighting**：核心对象高权重，上下文灰化/浅化，不得隐藏不利对象；
- **Semantic Background**：只用于真实稳定/风险/可行/阶段区间；
- **Composite Diagnostic**：中心关系 + 边际/残差共同回答同一 Primary question；
- **Conditional 3D**：只有第三维真实且 2D 会损失关键结构时准入。

对离散实验点、独立场景点、参数扫描点或迭代记录，**不得为了美观用 spline / Bezier 制造新峰谷和拐点**。

## Publication Rendering Grammar：成熟论文图实现层

前述 Gate 决定“表达什么”；Publication Rendering Grammar 只决定怎样稳定渲染成成熟论文图，不得反向创造证据。

### Palette Profile Selection

采用**半约束、语义优先**配色，不把整篇论文锁死为固定 HEX。

- `competition_high_contrast`：保留为兼容 profile 名，但含义调整为“竞赛论文中清晰、克制、焦点明确的高对比”，不是所有对象都高饱和；适合少量关键对象与评委快速阅读；
- `journal_balanced`：适合多方法、多 panel、多指标和密集 benchmark，优先中等饱和、稳定明度差和中性灰辅助；
- `monochrome_print`：灰阶、marker、linestyle、hatch 与 line weight 为主，颜色不得成为唯一语义。

可保留以下颜色作为兼容 fallback，而不是强制默认 palette：亮蓝 `#1478FF`、鲜红 `#F04444`、亮绿 `#16B364`、亮橙 `#F79009`、亮紫 `#7A5AF8`、深灰 `#252B37`、浅灰 `#E9EAEB`。真实项目应根据语义角色、对象数量、图型密度和最终输出介质决定是否降饱和或换用更平衡的科学色。

连续单向量使用感知上有序的 sequential colormap；只有存在真实中心值（0、基准、目标、正负偏差）才使用 centered diverging colormap；无序类别使用 restrained qualitative palette；周期变量才考虑 cyclic colormap。禁止 rainbow / jet / HSV 无序彩虹。红—绿不得承担唯一关键信息区分，必要时追加 marker / line style / hatch。

普通正文 Figure 优先形成“主色角色 + 强调角色 + 中性灰辅助”的层级。这是审美倾向，不是固定颜色数量上限。全文同一对象、状态和方向性语义必须保持稳定映射。

### Line Style Engine

折线、直线、参考线、阈值线、拟合线和不确定性边界按 `templates/figure/line_style_engine.md` 执行。默认 `journal_competition_hybrid` 只是渲染起点，不改变证据与正文准入。优先按 `Color=对象/指标`、`LineStyle=场景/状态`、`LineWidth=重要程度`、`Marker=真实离散/关键点`、`Band=真实区间/阶段` 分工。

线条美感必须服从 Clarity & Visibility Review：若黑色等值线陷入深色背景、浅色线消失在浅背景或缩小后 dash/marker 无法辨识，允许调整颜色、明度、线宽、线型和必要标签；不得为了“保持默认黑线”牺牲可见性，也不得为了清楚换成刺眼且破坏全文风格的颜色。

### Publication Frame / Typography

数据驱动 Figure 默认白底；普通二维 Cartesian 图优先 open-axis publication frame，上/右边框弱化或隐藏、刻度朝外、无边框 legend、默认 `grid off`。heatmap / matrix、3D / polar 或完整 frame 明显提高判读时可例外。

字号使用层级而不是所有文字同大；中文字体使用稳定 fallback。不得用极小字体换取更多 panel，也不得用粗轴、粗网格和大标题抢夺数据注意力。

### Adaptive Canvas / Panel Geometry

Figure 尺寸由 panel 数量、label 长度、legend 复杂度、metric 数量和阅读方向驱动。长类别优先增加画布/边距或改横向编码，不把字号压到不可读；panel spacing 紧凑但不得裁剪 tick、legend、annotation、colorbar。

### Legend Strategy

条目少可 in-axis / outside；多 panel 共用语义采用 shared legend；条目很多且会挤压数据区可用 Dedicated Legend Tile；每 panel 单主曲线时可以 direct label。目标是降低搜索成本，不制造装饰性 panel。

### Axis Range / Baseline Honesty

bar / stacked bar 承担绝对量比较时默认零基线；若零基线压缩差异，优先 interval dot、dumbbell、Global+Detail 或表格，不悄悄截断柱形。line/scatter/dot 可局部缩放但刻度必须透明。normalization / bandwidth 必须可解释。

## Clarity & Visibility Review：先保证看得清、说得明白

详细规则由 `templates/figure/clarity_visibility_review.md` 实现。该 Review 独立于一般审美检查，重点防止“图不难看，但信息读不清”。

必须检查：

1. **Direct label / contour label**：关键等值线、边界线、阈值线、推荐点、交点和阶段分界是否需要直接标注；等值线承担定量解释且读者需要频繁来回看 colorbar 时，应优先考虑稀疏、克制的 contour labels；
2. **Foreground–background contrast**：关键线条与实际背景是否有足够明度/色相对比；黑线在深蓝等暗背景上看不清时，必须允许改成协调的浅灰白、冷灰或其他高对比颜色，而不是死守黑色；
3. **Final-size visibility**：缩到论文真实插图宽度后，最细线、dash、marker、contour label、colorbar tick 和 annotation 是否仍清楚；
4. **Semantic clarity**：读者是否明确知道线、颜色、band、区域分别代表什么，而不是依赖猜测；
5. **Occlusion / clutter**：标签、legend、colorbar、annotation 是否遮挡关键证据；
6. **Aesthetic-preserving repair**：清晰度修正必须保持整体 palette、留白、主次和论文一致性，不得用荧光、高噪声颜色粗暴解决。

如果核心视觉元素在当前设计下无法被清楚辨认，则 Figure 不得视为通过最终图像质量审查。当前后端经过一次合理修正仍 FAIL 时，可以返回 Rendering Backend Selection Gate 比较另一后端。

## Aesthetic Review：清楚之后再审美

Aesthetic Review 不负责决定 Figure 是否科学上值得存在，只检查“值得存在且已清楚的 Figure 是否达到成熟论文的视觉完成度”。至少检查：

- 白底/合理浅底、整体平衡与留白；
- 核心焦点是否明确，次要元素是否合理降权；
- 色彩是否协调、克制并符合科学语义；
- 线宽、marker、字体、axis、legend、colorbar、panel label 是否形成稳定层级；
- 是否存在 MATLAB/Python 默认主题感、随机色序、粗网格、拥挤边框、默认大 marker 或无目的装饰；
- 同篇论文不同后端生成的 Figure 是否仍像同一套视觉系统；
- 清晰度修正后是否变得刺眼、杂乱或破坏全文一致性。

Aesthetic Review 不能覆盖 Clarity FAIL，也不能让低价值 Figure 进入正文。

## Competition Visual Quality Gate：至少达到近年高教社杯展示论文的成熟度

全国大学生数学建模竞赛官网的“历年竞赛结果”把历年论文展示指向教育部中国大学生在线；因此 CUMCM / 高教社杯项目的正式 Figure 以**近几年组委会公开展示论文的整体视觉成熟度**作为最低外部基准之一。参考入口见 `templates/figure/cumcm_visual_quality_gate.md`。

这里的“相近”不是复制某篇论文，而是要求最终 Figure 在论文实际插入尺寸下至少做到：

1. **一眼有主次**：核心对象、基准、辅助对象和背景层级清楚，不出现全图同饱和度；
2. **版面干净**：白底或合理浅底、留白稳定、轴线/网格不过重、legend 不压住数据；
3. **字体可读**：插入 Word/LaTeX 后按预计宽度查看，坐标、单位、图例、panel label 仍可读；
4. **颜色协调**：颜色数量与证据复杂度匹配，同类对象跨图一致，连续/发散/分类色图选择符合数据语义；
5. **结构完整**：关键阈值、误差、边界、推荐点、样本分布等存在时不被“漂亮但简化”的基础图吞掉；
6. **图文融合**：图题由 caption 承担，图内不堆论文标题式大字；图能在正文附近形成明确“由图可得”的论证；
7. **无明显默认软件感**：避免未经整理的 MATLAB/Python 默认色序、默认粗网格、拥挤 legend、随机字号、过多边框和裁切；
8. **不过度设计**：不靠渐变、霓虹、阴影、发光、装饰性 3D、花哨背景制造“高级感”。

当联网且任务属于 CUMCM 正式论文 Figure 时，可查阅近期官方展示论文的视觉惯例直到模式基本饱和；若无法联网，不阻塞作图，改用本 Gate 的稳定规则。外部展示论文只作为**视觉质量参考**，绝不成为本题数值事实源。

## Main-text Admission Gate：不要为了作图而作图

每张候选 Figure 在真正进入正文前必须回答：

> **删除这张图后，是否会让一个重要结论明显更难被相信、理解、比较或验证？**

若不会，默认不直接进入正文。统一决策：

```text
MAIN_TEXT  → 对重要结论有直接、不可替代的证明/比较/机制/边界/诊断价值
APPENDIX   → 有复核价值，但不是正文核心
TABLE_ONLY → 精确数值比视觉模式更重要，表格更高效
MERGE      → 与已有图互补但单独信息贡献不足，合并更清楚
DROP       → 重复、换皮、装饰性或无实质信息增益
```

“图已经画出来”“看起来高级”“别人论文也画过”“让论文更丰富”“颜色很好看”“Python画得更漂亮”“MATLAB画得更像竞赛图”均不是准入理由。即使图型简单，只要它是重要结论最直接、不可替代的证据，也可以进入正文。

### Redundancy / Unique Contribution Check

重点检查三类冗余：

- **Data overlap**：是否几乎使用同一批数据；
- **Claim overlap**：是否证明同一个结论；
- **Structure overlap**：是否只是 bar→radar、line→area 等视觉换皮。

每张新增 Figure 必须能写出 `Unique information contribution`。同数据 + 同结论 + 同结构且只有皮肤变化的 Figure 优先 `MERGE / TABLE_ONLY / DROP`。

## Final-size Readability / Export QA

图在 Python/MATLAB 大窗口里好看不等于进论文后好看。正式入文前必须按预计插图宽度检查：文字、marker、线型、误差区间、颜色差异、legend、colorbar、panel label、contour label 和关键边界是否仍清楚；缩小后若信息层级崩塌，应先重新布局而不是继续缩字体。

用户明确要求正式导出时优先 vector-first（PDF/SVG/EPS，视当前后端与环境支持）；PNG 以约 300 DPI 为起点，极密集图确有需要可提高。检查字体、裁切、透明对象、colorbar、legend、白底和灰度/色觉可读性。方案 4 不要求安装 `export_fig`、SciencePlots 等外部包；使用当前环境可复现的原生/既有科学绘图能力即可。

如果两个后端在大窗口中都不错，但只有一个在最终插入尺寸或正式导出格式中稳定通过 Clarity + Aesthetic + Export QA，则选通过者作为生产后端。

## 视觉注意力预算

- 一张 Figure 原则上只有 1 个一级 Core conclusion / Primary question；
- 同一视觉层级中真正竞争注意力的主要对象通常控制在少量范围；对象多时优先分组、small multiples、focus highlighting 或合理拆图；
- 主要视觉编码通常不宜过多；Composite Diagnostic 可以有多个 axes，但共享同一 Primary question；
- 信息密度可以高，但读者不应在不同 panel 反复学习新的颜色、线型和指标语法。

## 实表读取规则

正式绘图脚本必须：使用已核对的真实工作簿名、工作表名和表头；读取第一行原始表头并做空白归一化；每个要求字段精确相等匹配并断言唯一；工作簿变化后重新读取并更新 Figure Contract；检查文件、工作表、非空、主键、非法值和排序。禁止模糊匹配、别名猜测和自动回退。

MATLAB 示例：

```matlab
headers = strtrim(string(raw(1, :)));
xMatches = find(headers == xHeader);
assert(numel(xMatches) == 1, "字段缺失或重复: %s", xHeader);
xColumn = xMatches(1);
```

Python 也必须执行同等严格的**精确表头唯一匹配**，不得因为 pandas 方便而改成 contains、模糊列名、静默别名或自动 fallback。

## 图题、配色与风格

正式论文图不设置整体 `title` / `sgtitle` / `suptitle`。DOCX/LaTeX caption 承担图号、图名与必要统计口径；多面板按需只保留 a/b/c/d。默认白底、清楚细轴、中文坐标轴和单位；网格若启用应浅、稀并置于数据后方。

配色动态规则：主结果/推荐方案/关键曲线可以使用较高视觉权重；背景、参考线、CI、次要对象和上下文降权；同一对象和语义全文一致；连续场使用语义匹配的 sequential，正负偏差/相对基准使用 centered diverging；高对比不等于全图鲜艳。

对 contour / surface 类 Figure，不得机械使用统一黑色等值线。线色必须通过 Foreground–Background Contrast Gate；必要时可在深色区域使用协调的浅色线，并给关键等值线添加稀疏数值标签，只要不破坏科学色义和整体美感。

## Figure Portfolio Scientific Quality Gate

进入 DOCX/LaTeX 前，对正文核心 Figure 集合做论文级复审：

1. 是否出现大量基础图型，且底层其实存在时间、空间、分布、边界、机制、不确定性或多目标结构；
2. 是否有 Data / Claim / Structure overlap 导致重复；
3. 是否跳过 Literature Reference、Visual Mapping、Basic-form Challenge、合图/拆图、Rendering Backend Selection、Clarity & Visibility Review、Aesthetic Review 或 Main-text Admission；
4. 是否存在“每张单图都好看，但整篇颜色、字号、线宽、legend 和 panel 语法互相打架”；
5. 是否在最终插入尺寸下仍清楚；
6. CUMCM 正式稿是否达到 Competition Visual Quality Gate 的最低成熟度；
7. 是否有核心机制、空间、动态、阈值或不确定性结论只有文字/表格而缺直接证据；
8. 是否为了凑图型多样性强行雷达、桑基、3D 或装饰性复杂图；
9. Python 与 MATLAB 混用时是否仍保持统一字体、色义、线宽层级、legend、panel、留白和导出质量；
10. 是否存在某张图“美观但关键线看不清”或“看得清但颜色刺眼、标签过密”的 Clarity/Aesthetic 冲突未解决。

不得设置“每问最多 N 张”“必须有 N 种图型”等机械指标。

## Missing Scientific Evidence Check

不按章节字数或图文比例机械补图，而按核心结论检查：核心机制是否无图；空间结构是否只有汇总数；动态过程是否被压成最终值；关键阈值/边界是否无直接视觉证据；重要分布/不确定性是否只报均值；主结果是否只有表格而明显存在更有效的科研图表达。只有存在真实证据源时才补图，不编造数据。

## 分析图准入

结果深化分析不是每种方法都要画图。只有分析方法与风险来源匹配、图能展示稳定范围/阈值/算法一致性/结构差异/异质性、底层数据完整写入分析工作簿且图能支撑正文核心判断时才入图。统一扰动曲线、无解释算法柱状图和只展示“结果变化不大”的装饰图删除。

## 入文闭环

预处理图后正文必须解释原始问题、处理机制、关键参数、验证误差或信息保留情况，以及处理后数据为何可以进入后续模型；结果图后解释趋势、关键数值、机制、稳定范围或失效边界。所有进入正文的 Figure 必须能在附近正文中明确承担论证责任；无法写出实质性“由图可得”的图应回到 Main-text Admission Gate 重新裁决。