# Literature-Guided Figure Selection：文献引导选图参考

本文件只负责**外部论文与资料的视觉参考流程**，不拥有 Figure Evidence 决策权。最终图型、Evidence Structure、Figure level、Composite Encoding、Layout、Enhancement 与 Portfolio 判定仍统一服从 `modules/04_figure_evidence.md`。

## 何时使用

当准备为某个 Core conclusion 选择正式结果图、预处理证据图、敏感性/鲁棒性图、优化图、空间图、预测诊断图或机制相关数值图时，在 Scientific Figure Synthesis 前先判断是否需要外部文献视觉参考。

若题目和证据结构非常常见、当前仓库索引已经足以直接确定图型，可以快速跳过；若存在以下任一情况，则优先检索相关论文和权威资料：

- 不确定同类科学结论通常采用什么图型表达；
- 多种候选视觉结构都合理，难以判断哪一种最符合科研表达习惯；
- 涉及预测诊断、空间场、Pareto、多参数响应、网络、调度、稳定/失效区、复杂分布或多面板组织；
- 需要判断是否应加入置信区间、原始点、阈值线、参考线、局部放大、边际分布、残差、可行域或其他证据层；
- 当前方案明显退化为大量 plain bar / plain line / plain scatter，需要寻找更符合该领域证据结构的表达方式。

## 检索目标

检索的目标不是寻找“最好看的图”，而是回答：**同类研究通常如何把同类证据变成可验证的 Figure？**

重点观察：

1. 图型和坐标结构：line、scatter、box/violin、heatmap、contour、Pareto、map、network、Gantt、ECDF、calibration、residual 等；
2. 变量映射：横轴、纵轴、颜色、marker、线型、分面分别承担什么语义；
3. 证据层：是否同时保留原始样本、误差/区间、阈值、基准、可行边界、推荐点、关键事件；
4. 多面板逻辑：不同 panel 是否共同回答一个 Primary question，以及是 global-detail、before-after、main-diagnostic 还是 parameter-response；
5. 信息层级：哪些对象高亮，哪些作为背景或上下文降权；
6. caption 责任：图注通常补充哪些统计口径、单位、样本量、时间范围或判定标准；
7. 领域惯例：该问题类型是否存在较稳定、评审熟悉的科研可视化形式。

## 检索来源

优先顺序一般为：

- 同领域同行评审论文与综述；
- 相关领域的高质量开放论文、预印本或会议论文；
- 官方技术报告、标准、机构报告；
- 与赛题高度相近的优秀数学建模论文，仅作为竞赛表达参考。

不得把营销文章、图表模板网站、无方法说明的图片合集或纯设计案例作为主要科学依据。

## 检索方法

围绕“问题领域 + Evidence Structure + 科学图型/诊断任务”组合关键词检索，而不是只搜题目名称。

例如：

- `energy scheduling resource utilization Gantt paper`
- `multi objective optimization Pareto front recommendation figure`
- `crop yield spatial heterogeneity map uncertainty paper`
- `prediction observed predicted residual calibration figure`
- `parameter sensitivity heatmap contour stability region`

检索数量不设固定上限或下限。以**视觉模式基本饱和**为停止标准：继续查看新论文已很少出现新的合理证据结构时即可停止。

## 文献视觉摘要

每个候选 Figure 只需保留紧凑摘要，不复制论文图片：

| 字段 | 记录内容 |
|---|---|
| Search intent | 本次为了判断什么视觉问题而检索 |
| Reference set | 关键论文/报告的题名、作者/机构、年份、链接或 DOI |
| Recurrent visual pattern | 多篇资料反复出现的科学视觉结构 |
| Useful evidence layers | 原始点、区间、阈值、基准、边界、残差、局部放大等 |
| Domain convention | 该领域常见但非强制的表达惯例 |
| Transferable idea | 可迁移到当前问题的结构性做法 |
| Rejected imitation | 明确哪些配色、布局、图形细节或视觉风格不应照搬 |

## 选择规则

文献只能提供 **Candidate visual structures**，不能替代当前证据判断。

最终仍按以下逻辑决定：

`Core conclusion → Evidence level → Primary question → Available evidence dimensions → Literature visual reference → Scientific Figure Synthesis → Basic-form Challenge → Composite Encoding → Rendering Profile → Layout / Enhancement`

若文献常用图型与当前 accepted workbook 的 Evidence Structure 不一致，以当前真实数据和 Core conclusion 为准；不得为了“像论文”强行采用某图型。

若不同文献采用不同图型，应比较它们各自保留的证据维度，不用“出现次数最多”机械投票。

## 禁止事项

- 不得直接复制、描摹或轻微修改论文中的现成 Figure；
- 不得把论文配色、panel 排版、图标和装饰元素当成模板机械复刻；
- 不得因为顶刊用了 3D、雷达、Sankey、复杂网络或多面板，就认为当前问题也必须使用；
- 不得用文献中的数值、阈值、误差范围替代本题工作簿事实；
- 不得从截图反推原始数据；
- 不得为了图型多样性而选择领域中不常用、但视觉上更花哨的表达。

## 与图表去重的关系

文献检索不是增加图数量的理由。若参考文献提出多个视觉结构，但它们在当前论文中证明的是同一结论、使用同一数据且展示同一结构，应优先选择信息效率最高的一种，或在同一 Figure 内进行合理 Composite Encoding。

不设置“每问必须/最多几张图”的固定数量规则。图的数量由证据需要自然决定，判断重点始终是：**这张图相对已有图新增了什么可验证信息？**
