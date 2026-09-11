# Clarity & Visibility Review：表述清晰度与视觉可见性审查

本模板实现 `modules/04_figure_evidence.md` 的 Clarity & Visibility Review，**不拥有独立 Figure Authority**。它专门检查：Figure 已经科学成立以后，读者能否在论文真实插入尺寸下清楚看到、迅速识别并正确理解关键线条、等值线、边界、标签、色场和注释。

它与 Aesthetic Review 分工不同：

- Clarity & Visibility Review 先回答“**看不看得清、懂不懂得快**”；
- Aesthetic Review 再回答“**在清楚的前提下是否协调、成熟、美观**”。

清晰性优先于默认颜色和默认软件风格，但清晰性修正也必须保持整体美感与论文一致性。

## 1. Direct Label / Contour Label Gate

当线条本身承担可读数值或状态语义时，必须判断是否需要直接标注，而不是默认只让读者来回对照 colorbar / legend。

优先考虑直接标注的对象：

- contour / isoline 的关键数值；
- 关键阈值、可行边界、风险边界；
- 推荐点、极值、重要交点；
- 策略切换、事件触发、阶段分界；
- 单条或少量主曲线在 direct label 后可显著降低 legend 搜索成本的情况。

### Contour label 原则

- 等值线承担定量解释时，优先评估添加 contour labels；
- 不要求每一条等值线都标数字，只标足以降低读图负担的代表值或关键值；
- 标签不能互相重叠、压住关键区域或让图变成“数字墙”；
- 若单位已由 colorbar / axis / caption 明确，可只标数值；若脱离单位会产生歧义，再补单位；
- 若 contour 极密，宁可降低 contour 数量、稀疏标注或保留 colorbar，也不能为了“信息完整”把所有线都塞满数字。

典型判断：如果读者必须频繁在等值线与 colorbar 之间来回猜值，而少量数字标注可以明显降低认知负担，则应标。

## 2. Foreground–Background Contrast Gate

关键前景元素必须与其实际背景保持足够视觉对比。**黑色不是默认正确答案，白色也不是。**线条颜色需要结合局部背景的亮度、色相和饱和度判断。

重点检查：

- 黑色 contour 是否陷入深蓝、深紫、深绿等暗背景；
- 白色/浅灰线是否消失在浅色背景；
- reference / threshold / boundary 与数据线是否互相混淆；
- CI band、semantic background 是否吞没中心线；
- colorbar 两端对应的线条颜色是否在整个色场范围内仍可辨。

若关键线条不可辨识，允许并要求优先尝试：

1. 调整线条明度或颜色，使其与背景形成更稳定对比；
2. 适度调整线宽；
3. 更换有语义的 dash / marker；
4. 必要时增加轻微描边、halo 或局部直接标签，但不得产生花哨发光效果；
5. 若单一线色无法跨整个连续色场保持清楚，可采用与背景自适应的局部标注策略、分段线色或重新选择更合适的底图 colormap，但必须保持语义一致。

颜色替换必须优先选择与整体 palette 协调的高对比中性色或同色系明暗变化，不得因为“更清楚”就直接换成刺眼荧光色。

## 3. Critical Element Visibility Check

每张 Figure 至少检查以下实际存在的关键元素：

- 主结果线 / 推荐方案；
- contour / boundary / threshold；
- marker / error bar / CI band；
- annotation / direct label；
- legend / colorbar；
- panel label；
- 关键网格或 reference；
- 地图边界、路径、网络关键节点等。

若某个元素承担 Core conclusion 的证据职责，但需要放大截图、反复寻找或依赖猜测才能识别，则该元素视为 **FAIL**。

## 4. Semantic Clarity Check

不仅要“看得见”，还要“知道它是什么”。检查：

- 一条线是否存在但读者不知道它代表模型、观测、基准还是阈值；
- 颜色是否存在但类别/方向/状态语义不明确；
- contour 是否有线但完全无法估计对应数值；
- shaded region 是否不知道表示 CI、风险区、阶段还是装饰背景；
- 多 panel 是否需要反复重新学习颜色与线型。

承担证据职责的视觉元素必须通过 legend、direct label、caption、轴/单位或稳定的跨图语义之一明确解释。不得依赖“读者应该能猜到”。

## 5. Final-size Visibility

审查必须在预计 Word/LaTeX 插入宽度执行，而不是只看 MATLAB/Python 大窗口。

至少检查：

- 最细线是否仍存在；
- dash pattern 是否仍能区分；
- contour label 是否仍能读；
- marker 是否缩成噪点或互相粘连；
- colorbar tick 与单位是否清楚；
- annotation 是否重叠；
- 深色/浅色区域上的关键线是否仍有对比；
- panel label 是否醒目但不过大。

如果大窗口 PASS、论文尺寸 FAIL，则最终结论是 FAIL。

## 6. Clarity Repair Order

当 Figure 不清楚时，按“最小改动、最大信息增益”修正：

```text
先补必要标签 / 直接标注
→ 调整主次线宽与视觉权重
→ 调整前景—背景明度/颜色对比
→ 调整 line style / marker / band
→ 调整 legend / colorbar / annotation 位置
→ 调整 layout / local zoom / small multiples
→ 必要时重新进入 Rendering Backend Selection Gate
```

不得第一反应就是“所有线都加粗”“所有元素换鲜艳颜色”或“把字体全部变大”。

## 7. 与审美的平衡

可见性修正后必须继续通过 Aesthetic Review：

- 清楚但刺眼，不通过；
- 清楚但颜色与全篇语义冲突，不通过；
- 清楚但标签过密、留白崩坏，不通过；
- 很漂亮但关键线看不见，同样不通过。

最终目标是：**清楚 + 克制 + 协调 + 有焦点**。

## 8. Backend Escalation

如果当前 Python 或 MATLAB 后端经过一次合理的颜色、线宽、标注和布局修正后，核心元素仍无法通过本 Review，可以返回 `Rendering Backend Selection Gate` 比较另一后端。

换后端时 Visual Mapping、数据范围、阈值、统计口径和 Core conclusion 必须保持不变；后端不能通过改变证据来解决视觉问题。

## 9. PASS / FAIL

### PASS

- 关键元素在最终尺寸下可清楚识别；
- 定量线条在需要时有足够直接标注或可快速映射到 colorbar/legend；
- 前景与背景有稳定对比；
- 不需要靠猜测理解视觉语义；
- 修正没有破坏科学配色、数据诚实和整体审美。

### FAIL

- 核心 contour / boundary / line 融入背景；
- 重要等值线无法快速读值且合理 direct label 缺失；
- 标签、legend、colorbar 或 annotation 遮挡证据；
- 缩小后关键线、dash、marker、文字消失；
- 颜色虽然漂亮但语义难辨；
- 为了清楚使用刺眼、高噪声或破坏整篇统一性的颜色；
- 为了美观隐藏、淡化到不可见或删除对结论不利的真实证据。

**Clarity & Visibility FAIL 的 Figure 不得视为通过最终图像质量审查，也不得仅凭 Aesthetic Review PASS 进入正式正文。**
