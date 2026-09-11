# Rendering Backend Selection Gate：Python / MATLAB 自适应绘图后端

本模板只实现 `modules/04_figure_evidence.md` 的 Rendering Backend Selection Gate，**不拥有独立 Figure Authority**。它只回答：在 Figure 的 Core conclusion、Evidence Structure、Visual Mapping、候选视觉结构和事实源已经确定后，Python 与 MATLAB 哪一个更适合把该 Figure 渲染得清楚、成熟、美观且可复现。

## 1. 核心原则：不强制 MATLAB，也不强制 Python

数据驱动 Figure 的正式渲染后端在 `Python / MATLAB` 中按当前 Figure 实际需要选择。不得因为仓库历史模板、个人习惯、已有代码语言或“竞赛图通常用 MATLAB”而机械锁定后端；也不得因为 Python 在某些图型上更灵活就机械锁定 Python。

**后端是渲染手段，不是证据来源。**无论选择哪一个：

- Core conclusion、Evidence level、Evidence Structure、Visual Mapping、Main-text Admission 均不改变；
- 具体数值仍来自 accepted workbook / 当前允许的数据事实源；
- 绘图脚本不得重新求解、重新做敏感性/统计分析、重新预处理或从摘要数字反推底层序列；
- 不得为了换后端而改变模型、参数、阈值、样本、时间窗、排序、插值或统计口径；
- 不增加 SciencePlots、gramm、第三方 colormap、export_fig 等仅为“风格”服务的新强制运行依赖。

## 2. 后端选择维度

正式选择前按当前 Figure 逐项比较：

| 维度 | 需要判断的问题 |
|---|---|
| Evidence Structure 适配 | 当前图是 contour/heatmap、distribution、dense scatter、network、Pareto、dynamic、multi-panel 还是普通 Cartesian？哪个后端能更自然地保留证据结构？ |
| 线条与直接标注 | 等值线数值、阈值、关键点、direct label、dash、marker、band 是否容易做到清楚且不过度拥挤？ |
| 前景—背景对比 | 深浅背景、连续色场、等值线和边界线的颜色/明度能否稳定控制？ |
| Layout / Panel | shared legend、colorbar、small multiples、inset、global-detail、复杂 panel spacing 哪个后端更容易达到最终版面要求？ |
| Typography | 中文、数学符号、单位、上下标、字体 fallback 在论文实际插入尺寸下哪个更稳定？ |
| Scientific color | sequential / centered diverging / restrained qualitative / cyclic 语义能否可靠实现且不过饱和？ |
| Transparency / uncertainty | CI band、背景轨迹、semantic region、alpha 对象导出后哪个更可靠？ |
| Final-size readability | 缩到 Word/LaTeX 真实插图宽度后，线、字、marker、dash、contour label、legend 是否仍清楚？ |
| Export fidelity | PDF/SVG/EPS/PNG 的字体、裁切、透明度、色彩和最细线是否稳定？ |
| Paper-level consistency | 与论文已有 Figure 的字体、色义、线条语法、panel 和留白是否更容易保持一致？ |
| Reproducibility / environment | 当前环境已有依赖、字体和工具链哪个更可靠；是否需要为了美观额外安装包？ |

所谓“更美观”必须同时包含**清晰、层级、协调、留白、字体、线条、配色和最终尺寸表现**，不能只比较大窗口截图的视觉冲击。

## 3. 默认决策逻辑

```text
Figure structure 已确定
→ 比较 Python / MATLAB 对当前结构的表达能力
→ 检查 Clarity & Visibility
→ 检查 Aesthetic maturity
→ 检查 Final-size / Export
→ 选择综合表现更好的生产后端
```

如果一个后端在视觉上稍好，但会引入不可复现字体、额外强制依赖、事实源漂移或导出不稳定，则不得仅凭“更漂亮”选它。

若两者最终质量实质相当，优先使用：

1. 当前项目已经稳定可复现的后端；
2. 不新增依赖、字体或转换步骤的后端；
3. 更容易维持整篇 Figure 视觉一致性的后端。

这只是 tie-breaker，不构成 MATLAB 或 Python 的固定默认。

## 4. 何时需要双后端小样比较

**不要求每张 Figure 都同时写 Python 和 MATLAB 两份生产代码。**只有以下情况之一成立时，才建议做低成本小样比较：

- F3 / MAIN_TEXT 核心 Figure，且两个后端在理论上都很合适；
- contour / heatmap / dense multi-panel /复杂 direct labeling 等视觉结果明显受后端布局能力影响；
- 当前后端经过一次合理修正后仍无法通过 Clarity & Visibility Review 或 Aesthetic Review；
- 用户明确要求比较两个后端的成图质量。

比较时必须使用同一 accepted 数据、同一 Visual Mapping、同一 caption duty 和相近最终插入尺寸；不得通过改变数据范围、色义或信息层来让某一后端“赢”。

比较完成后只保留**一个正式生产后端**。另一份若只是试验小样，不进入默认交付目录和正式证据链。

## 5. 推荐但非强制的后端倾向

以下只是经验起点，不是硬规则：

- Python 往往适合：复杂 multi-panel、精细 typography/layout、密集统计图、透明 band、复杂 annotation、需要较强 Figure-level 组合控制的场景；
- MATLAB 往往适合：工程数值场、规则网格 contour/surface、矩阵/场数据、已有成熟 MATLAB 数值结果接口、需要快速交互检查的场景；
- contour / heatmap / surface **不能按图型直接锁后端**。等值线标签、背景对比、colorbar、字体和最终插图效果必须实际通过审查；
- 同一论文允许不同 Figure 使用不同后端，但 Paper-level Consistency Gate 必须保证它们看起来属于同一篇论文。

## 6. 正式脚本命名

数据驱动结果图在后端确定后，每问正式生产脚本二选一：

- `问题X求解/qX_plot.py`
- `问题X求解/qX_plot.m`

同一问默认只保留一个正式生产脚本；另一个后端的小样不得伪装成第二个正式 Figure pipeline。

若 `preprocessing_decision=project_level`，项目级预处理证据图的正式生产脚本二选一：

- `数据预处理/data_process_plot.py`
- `数据预处理/data_process.m`

两者都只能读取 `数据预处理结果.xlsx` 中已验收的底层证据，不得重新清洗、插值、滤波、重采样、预测填补、训练模型或重新确定参数。

## 7. 与其他 Gate 的关系

- `Literature-Guided Figure Reference` 决定可借鉴的证据表达原则，不决定软件；
- `Visual Mapping` 决定变量如何映射到视觉通道，不决定软件；
- `Line Style Engine` 决定线条语义和层级，不绑定软件；
- `Clarity & Visibility Review` 可以要求调整颜色、线宽、标签、对比或后端；
- `Aesthetic Review` 检查整体成熟度与协调性；
- `Main-text Admission` 决定 Figure 是否值得进入正文，不能由后端或美感改变；
- `Final-size / Export QA` 是最终裁决依据之一，大窗口截图不能替代。

## 8. 禁止事项

- 禁止固定写成“工作簿驱动结果图一律 MATLAB”或“一律 Python”；
- 禁止因为换后端而修改 accepted 数据、统计量或模型结论；
- 禁止为了比较后端额外制造两套不同 Visual Mapping；
- 禁止把“软件更高级”当成 Figure 准入理由；
- 禁止仅凭默认主题、默认 colormap 或默认线宽判定哪个后端更美观；
- 禁止为风格比较引入新的强制第三方绘图库依赖。
