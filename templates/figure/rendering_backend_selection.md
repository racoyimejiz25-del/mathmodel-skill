# Rendering Backend Selection Gate：Python-first，MATLAB 按需例外

本模板只实现 `modules/04_figure_evidence.md` 的 Rendering Backend Selection Gate，**不拥有独立 Figure Authority**。它只回答：在 Figure 的 Core conclusion、Evidence Structure、Visual Mapping、候选视觉结构和事实源已经确定后，使用哪个后端能把该 Figure 渲染得更清楚、成熟、美观且可复现。

## 1. 核心原则：Python 优先，不强制 MATLAB

数据驱动 Figure 的正式渲染后端采用 **Python-first**：默认先用 Python 作为生产后端；只有出现明确的图型、环境、导出或最终版面理由时，才切换到 MATLAB。

Python-first 是**生产偏好，不是证据规则**。它不能改变任何已有 Figure 限制：

- Core conclusion、Evidence level、Evidence Structure、Visual Mapping、Main-text Admission 均不改变；
- 具体数值仍来自 accepted workbook / 当前允许的数据事实源；
- 绘图脚本不得重新求解、重新做敏感性/统计分析、重新预处理或从摘要数字反推底层序列；
- 不得为了换后端而改变模型、参数、阈值、样本、时间窗、排序、插值或统计口径；
- 不增加 SciencePlots、gramm、第三方 colormap、export_fig 等仅为“风格”服务的新强制运行依赖。

默认优先 Python 的理由是：在当前 Skill 的目标中，Python 对精细 typography、直接标注、线条主次、透明 band、inset、small multiples、复杂 panel、科学配色和逐图审美修正通常提供更灵活的 Figure-level 控制。**这不是“Python 天生更高级”，而是把默认生产路径从软件历史习惯改成更利于高质量视觉迭代的路径。**

## 2. MATLAB 例外准入

只有至少一项成立时，才将正式生产后端从 Python 切换为 MATLAB，并在 Figure Contract 中写明 rationale：

- 当前工程已有稳定 MATLAB 图形链，Python 复现会明显增加环境风险或时间成本；
- 某类工程数值场、规则网格或专用对象在 MATLAB 中经过最终尺寸审查后**明显更清楚、更稳定或更美观**；
- Python 版本经过一次合理的 Clarity / Aesthetic 修正后仍无法解决字体、导出、布局、性能或交互检查问题；
- 用户明确指定 MATLAB；
- 同数据低成本小样比较表明 MATLAB 在最终论文尺寸下综合质量更高。

不得仅因为“以前一直用 MATLAB”“MATLAB 画场图方便”“现成代码是 `.m`”就自动触发例外。

## 3. 后端选择维度

正式选择前按当前 Figure 逐项判断：

| 维度 | 需要判断的问题 |
|---|---|
| Evidence Structure 适配 | 当前图是 distribution、dense scatter、network、Pareto、dynamic、contour、multi-panel 还是普通 Cartesian？Python 是否能自然保留证据结构；若不能，MATLAB 是否有明确优势？ |
| 线条与直接标注 | 等值线数值、阈值、关键点、direct label、dash、marker、band 是否容易做到清楚且不过度拥挤？ |
| 前景—背景对比 | 深浅背景、连续色场、等值线和边界线的颜色/明度能否稳定控制？ |
| Layout / Panel | shared legend、colorbar、small multiples、inset、global-detail、复杂 panel spacing 是否容易达到最终版面要求？ |
| Typography | 中文、数学符号、单位、上下标、字体 fallback 在论文实际插入尺寸下是否稳定？ |
| Scientific color | sequential / centered diverging / restrained qualitative / cyclic 语义能否可靠实现且不过饱和？ |
| Transparency / uncertainty | CI band、背景轨迹、semantic region、alpha 对象导出后是否可靠？ |
| Final-size readability | 缩到 Word/LaTeX 真实插图宽度后，线、字、marker、dash、contour label、legend 是否仍清楚？ |
| Export fidelity | PDF/SVG/EPS/PNG 的字体、裁切、透明度、色彩和最细线是否稳定？ |
| Paper-level consistency | 与论文已有 Figure 的字体、色义、线条语法、panel 和留白是否更容易保持一致？ |
| Reproducibility / environment | 当前环境已有依赖、字体和工具链是否可靠；是否需要为了美观额外安装包？ |

所谓“更美观”必须同时包含**清晰、层级、协调、留白、字体、线条、配色和最终尺寸表现**，不能只比较大窗口截图的视觉冲击。

## 4. 默认决策逻辑

```text
Figure structure 已确定
→ 默认 Python 原生科学绘图实现
→ Clarity & Visibility Review
→ Aesthetic Review
→ Final-size / Export QA
→ 若通过：Python 保持为正式生产后端
→ 若未通过：先做一次合理的 Python 视觉修正
→ 仍未通过且 MATLAB 有明确优势：进入 MATLAB 例外准入
```

如果 Python 与 MATLAB 最终质量实质相当，**选择 Python**，以维持统一的 Python-first Figure pipeline。只有 MATLAB 存在可说明的实际优势才切换。

如果 Python 在视觉上稍好，但会引入不可复现字体、额外强制依赖、事实源漂移或导出不稳定，则仍不得仅凭“更漂亮”选它；Python-first 不覆盖可复现性和数据事实源约束。

## 5. 何时需要双后端小样比较

**不要求每张 Figure 都同时写 Python 和 MATLAB 两份生产代码。**只有以下情况之一成立时，才建议做低成本小样比较：

- F3 / MAIN_TEXT 核心 Figure，Python 与 MATLAB 都可能有明显优势；
- contour / dense multi-panel /复杂 direct labeling 等视觉结果明显受后端布局能力影响；
- Python 经过一次合理修正后仍无法通过 Clarity & Visibility Review 或 Aesthetic Review；
- 用户明确要求比较两个后端的成图质量。

比较时必须使用同一 accepted 数据、同一 Visual Mapping、同一 caption duty 和相近最终插入尺寸；不得通过改变数据范围、色义或信息层来让某一后端“赢”。

比较完成后只保留**一个正式生产后端**。另一份若只是试验小样，不进入默认交付目录和正式证据链。

## 6. 后端倾向

- **Python 默认优先**：折线/多折线、散点/拟合、分布、误差带、排序点图、Pareto、small multiples、inset、复杂 annotation、复合诊断、需要精细版式和视觉层级的 Figure；
- **MATLAB 例外候选**：规则网格工程数值场、已有成熟 MATLAB 工程接口、或经实际 Final-size QA 证明 MATLAB 明显更稳定的图；
- contour / surface **不能仅按图型自动切 MATLAB**；Python 先尝试，等值线标签、背景对比、colorbar、字体和最终插图效果必须通过审查；
- 同一论文允许少量 Figure 使用 MATLAB 例外后端，但 Paper-level Consistency Gate 必须保证它们看起来属于同一篇论文。

## 7. 正式脚本命名

数据驱动结果图默认正式生产脚本：

- `问题X求解/qX_plot.py`

只有通过 MATLAB 例外准入时才使用：

- `问题X求解/qX_plot.m`

同一问默认只保留一个正式生产脚本；另一个后端的小样不得伪装成第二个正式 Figure pipeline。

若 `preprocessing_decision=project_level`，项目级预处理证据图默认：

- `数据预处理/data_process_plot.py`

只有 MATLAB 例外成立时才改用：

- `数据预处理/data_process.m`

无论后端，两者都只能读取 `数据预处理结果.xlsx` 中已验收的底层证据，不得重新清洗、插值、滤波、重采样、预测填补、训练模型或重新确定参数。

## 8. 与其他 Gate 的关系

- `Literature-Guided Figure Reference` 决定可借鉴的证据表达原则，不决定软件；
- `Visual Mapping` 决定变量如何映射到视觉通道，不决定软件；
- `Chart Selection` 必须先通过图型价值审查，Python-first **不能成为滥用 heatmap/gridmap 的理由**；
- `Line Style Engine` 决定线条语义和层级，不绑定软件；
- `Clarity & Visibility Review` 可以要求调整颜色、线宽、标签、对比或重新进入后端选择；
- `Aesthetic Review` 检查整体成熟度与协调性；
- `Main-text Admission` 决定 Figure 是否值得进入正文，不能由后端或美感改变；
- `Final-size / Export QA` 是最终裁决依据之一，大窗口截图不能替代。

## 9. 禁止事项

- 禁止固定写成“工作簿驱动结果图一律 MATLAB”；
- 禁止把 Python-first 解释为“一律 Python”，MATLAB 有明确质量优势时允许例外；
- 禁止因为换后端而修改 accepted 数据、统计量或模型结论；
- 禁止为了比较后端额外制造两套不同 Visual Mapping；
- 禁止把“软件更高级”当成 Figure 准入理由；
- 禁止仅凭默认主题、默认 colormap 或默认线宽判定哪个后端更美观；
- 禁止为风格比较引入新的强制第三方绘图库依赖。
