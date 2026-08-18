# 模型手册栏目设计

日期：2026-08-18  
状态：待用户审阅后进入实施计划

## 1. 目标

在 SAS 知识站增加顶栏第五条入口 **「模型手册」**：为常见解析小角散射模型提供中文手册级页面。读者按几何/函数类型查阅，每篇讲清何时用、公式、参数、拟合注意与原始文献。

公开页面（HTML、可见文案、图注、搜索词）**不出现任何拟合软件名**。后续若加入其他来源的模型，沿用同一分类与同一页模板。

## 2. 非目标

- 不做成可在线拟合或参数调节的计算器。
- 不写用户插件、自定义模型。
- 不把 \(P(q)\times S(q)\) 组合写成独立模型页（组合是拟合操作）。
- 不把分辨率 / smearing、通用 `scale` / `background` 写成独立模型。
- 不把取向、磁性 SLD、尺寸多分散拆成独立页。
- 不提交绘图/生成用的 Python 代码。

## 3. 架构

沿用现站纯静态 HTML，无构建步骤。新增：

```
models/index.html
models/<category>/index.html
models/<category>/<model>.html
assets/figures/models/<category>/*-geometry.png   # 七类形状/格子
assets/figures/models/<category>/*-iq.png         # 非结构因子
assets/figures/models/<category>/*-sq.png         # 结构因子
tools/model-figures/          # 本地 uv 工程，gitignore，不入库
```

分类 slug（侧栏与 URL）：

| slug | 中文 |
|------|------|
| sphere | 球 |
| cylinder | 圆柱 |
| ellipsoid | 椭球 |
| parallelepiped | 平行六面体 |
| polyhedron | 多面体 |
| lamellae | 层状 |
| shape-independent | 形状无关 |
| paracrystal | 准晶 |
| structure-factor | 结构因子 |

侧栏只列「总览 + 九个分类」，不罗列全部模型。分类页与模型页用卡片和「上一篇 / 下一篇」在同类内翻页。

`data-base`：`models/index.html` 为 `..`；`models/<category>/index.html` 与模型页为 `../..`。

### 站点接入

- `assets/nav.js`：顶栏增加 `{ href: "models/index.html", label: "模型手册" }`；`SIDEBARS.models` 为总览 + 九分类；`sectionKey` 识别 `models/`。
- `index.html`：五条入口卡片。
- `about.html`、`README.md`：增加模型手册说明。
- `learn/08-models-polydispersity.html`、`learn/index.html`：链到模型手册总览。
- `glossary/form-factor.html`、`glossary/structure-factor.html` 等：在「出现于」中增加模型手册入口。
- `data/search-index.js`：每一篇模型页一条记录（`section: "模型手册"`），`title` 含中文名，`text`/`headings` 含英文名与关键符号，保证 Ctrl+K 可检索。

### Git

`.gitignore` 增加：

```
tools/model-figures/
```

提交：HTML、CSS/JS 改动、`assets/figures/models/**/*.png`、本 spec。不提交 `tools/model-figures/` 下任何文件（含 `pyproject.toml`、`.venv`、脚本、中间数据）。

## 4. 页面模板

外壳与现有专题页相同：KaTeX、术语虚线（`data-term`）、搜索、页脚脚本。

### 4.1 总览 `models/index.html`

- 标题「模型手册」，英文副标题说明这是形状与结构模型的查阅手册。
- 九个分类卡片（中文名 + 一句适用范围）。
- 「怎么选模型」短列表，链到学习路径 08。
- 不出现软件名。

### 4.2 分类页 `models/<category>/index.html`

- 分类中文名 + 英文副标题。
- 一段分类物理说明（该几何/函数在 \(I(q)\) 上的共同特征）。
- 该分类全部模型的卡片：中文名、英文名、一句用途。

### 4.3 模型页（固定章节顺序）

1. 中文 `<h1>` + `.subtitle-en` 英文名  
2. **适用场景**  
3. **物理图像**  
4. **示意图**：七类形状/格子嵌入 `*-geometry.png`；除结构因子外嵌入 `*-iq.png`；结构因子嵌入 `*-sq.png`  
5. **核心公式**：主表达式，符号在当页定义；多种约定并存时选定一种并写明  
6. **参数表**：列「参数 / 符号 / 含义 / 单位 / 典型范围」；取向角、磁 SLD、分布宽度若该模型物理上需要，列在表中并在第 7 节展开  
7. **拟合注意**：取向平均、磁性衬度、多分散；常见坑与可辨识性  
8. **相近模型**：链到易混淆的 2–5 篇  
9. **参考文献**：原始论文/教材；有 DOI 则做成可点击链接；不列软件用户手册  

图注统一：「配图：按公式计算示意」。

## 5. 出图

- 本地目录 `tools/model-figures/`：`uv` 管理依赖（matplotlib、numpy）。
- 几何图 `{model}-geometry.png`：球、圆柱、椭球、平行六面体、多面体、层状、准晶七类必须有；用 Matplotlib patches 画截面、立体或格子示意（白底，约 1200 px 宽，标注关键尺寸）。形状无关类与结构因子类不强制几何图。
- 曲线图：除结构因子外一律 `{model}-iq.png`（log–log \(I(q)\)）；若多分散是该模型的核心讨论，可叠一条分布平均曲线。结构因子页用 `{model}-sq.png`，纵轴标明 \(S(q)\)。
- 导出到 `assets/figures/models/<category>/`。页面上线条件：该模型所需 PNG 已生成，禁止缺图占位。

## 6. 覆盖清单（85 篇）

每行：`slug.html` — 中文名 — 英文名。

### 6.1 球（15）`models/sphere/`

- `sphere.html` — 均匀球 — sphere  
- `core-shell-sphere.html` — 核壳球 — core-shell sphere  
- `vesicle.html` — 囊泡 — vesicle  
- `multilayer-vesicle.html` — 多层囊泡 — multilayer vesicle  
- `fuzzy-sphere.html` — 模糊球 — fuzzy sphere  
- `raspberry.html` — 树莓 — raspberry  
- `polymer-micelle.html` — 聚合物胶束 — polymer micelle  
- `adsorbed-layer.html` — 吸附层 — adsorbed layer  
- `binary-hard-sphere.html` — 二元硬球 — binary hard sphere  
- `core-multi-shell.html` — 核–多层壳 — core multi-shell  
- `linear-pearls.html` — 直线珍珠串 — linear pearls  
- `onion.html` — 洋葱球 — onion  
- `spherical-sld.html` — 径向 SLD 球 — spherical SLD  
- `superball.html` — 超球 — superball  
- `micromagnetic-ff-3d.html` — 三维微磁形式因子 — micromagnetic form factor 3D  

### 6.2 圆柱（16）`models/cylinder/`

- `cylinder.html` — 圆柱 — cylinder  
- `core-shell-cylinder.html` — 核壳圆柱 — core-shell cylinder  
- `hollow-cylinder.html` — 空心圆柱 — hollow cylinder  
- `barbell.html` — 哑铃 — barbell  
- `capped-cylinder.html` — 端帽圆柱 — capped cylinder  
- `core-shell-bicelle.html` — 核壳双层盘 — core-shell bicelle  
- `core-shell-bicelle-elliptical.html` — 椭圆核壳双层盘 — elliptical core-shell bicelle  
- `core-shell-bicelle-elliptical-belt-rough.html` — 粗糙腰带椭圆双层盘 — elliptical core-shell bicelle with rough belt  
- `elliptical-cylinder.html` — 椭圆截面圆柱 — elliptical cylinder  
- `flexible-cylinder.html` — 柔性圆柱 — flexible cylinder  
- `flexible-cylinder-elliptical.html` — 椭圆截面柔性圆柱 — flexible elliptical cylinder  
- `pearl-necklace.html` — 珍珠项链 — pearl necklace  
- `pringle.html` — 马鞍形圆盘 — pringle  
- `stacked-disks.html` — 堆叠圆盘 — stacked disks  
- `tetrapod.html` — 四足体 — tetrapod  
- `torus-elliptical-shell.html` — 椭圆环壳 — elliptical torus shell  

### 6.3 椭球（3）`models/ellipsoid/`

- `ellipsoid.html` — 椭球 — ellipsoid  
- `core-shell-ellipsoid.html` — 核壳椭球 — core-shell ellipsoid  
- `triaxial-ellipsoid.html` — 三轴椭球 — triaxial ellipsoid  

### 6.4 平行六面体（5）`models/parallelepiped/`

- `parallelepiped.html` — 平行六面体 — parallelepiped  
- `core-shell-parallelepiped.html` — 核壳平行六面体 — core-shell parallelepiped  
- `rectangular-prism.html` — 矩形棱柱 — rectangular prism  
- `hollow-rectangular-prism.html` — 空心矩形棱柱 — hollow rectangular prism  
- `hollow-rectangular-prism-thin-walls.html` — 薄壁空心矩形棱柱 — hollow rectangular prism (thin walls)  

### 6.5 多面体（4）`models/polyhedron/`

- `prism.html` — 三棱柱 — prism  
- `tetrahedron.html` — 四面体 — tetrahedron  
- `truncated-tetrahedron.html` — 截角四面体 — truncated tetrahedron  
- `truncated-octahedron.html` — 截角八面体 — truncated octahedron  

### 6.6 层状（5）`models/lamellae/`

- `lamellar.html` — 层状 — lamellar  
- `lamellar-hg.html` — 头基–尾链层状 — lamellar headgroup  
- `lamellar-stack-caille.html` — Caille 层状堆叠 — lamellar stack Caille  
- `lamellar-hg-stack-caille.html` — 头基–尾链 Caille 堆叠 — lamellar HG stack Caille  
- `lamellar-stack-paracrystal.html` — 准晶层状堆叠 — lamellar stack paracrystal  

### 6.7 形状无关（29）`models/shape-independent/`

- `guinier.html` — Guinier — Guinier  
- `porod.html` — Porod — Porod  
- `power-law.html` — 幂律 — power law  
- `guinier-porod.html` — Guinier–Porod — Guinier–Porod  
- `unified-power-rg.html` — 统一幂律–Rg — unified power Rg  
- `two-power-law.html` — 双幂律 — two power law  
- `lorentz.html` — 洛伦兹 — Lorentz  
- `two-lorentzian.html` — 双洛伦兹 — two Lorentzian  
- `gaussian-peak.html` — 高斯峰 — Gaussian peak  
- `peak-lorentz.html` — 洛伦兹峰 — peak Lorentz  
- `broad-peak.html` — 宽峰 — broad peak  
- `dab.html` — Debye–Anderson–Brumberger — DAB  
- `correlation-length.html` — 关联长度 — correlation length  
- `fractal.html` — 分形 — fractal  
- `mass-fractal.html` — 质量分形 — mass fractal  
- `surface-fractal.html` — 表面分形 — surface fractal  
- `mass-surface-fractal.html` — 质量–表面分形 — mass-surface fractal  
- `fractal-core-shell.html` — 核壳分形 — fractal core-shell  
- `mono-gauss-coil.html` — 单分散高斯链 — monodisperse Gaussian coil  
- `poly-gauss-coil.html` — 多分散高斯链 — polydisperse Gaussian coil  
- `polymer-excl-volume.html` — 聚合物排除体积 — polymer excluded volume  
- `star-polymer.html` — 星形聚合物 — star polymer  
- `be-polyelectrolyte.html` — 聚电解质 — polyelectrolyte  
- `gauss-lorentz-gel.html` — 高斯–洛伦兹凝胶 — Gauss–Lorentz gel  
- `gel-fit.html` — 凝胶拟合 — gel fit  
- `teubner-strey.html` — Teubner–Strey — Teubner–Strey  
- `spinodal.html` — 旋节分解 — spinodal  
- `rpa.html` — 无规相近似 — RPA  
- `line.html` — 线性 — line  

### 6.8 准晶（3）`models/paracrystal/`

- `sc-paracrystal.html` — 简单立方准晶 — simple cubic paracrystal  
- `bcc-paracrystal.html` — 体心立方准晶 — BCC paracrystal  
- `fcc-paracrystal.html` — 面心立方准晶 — FCC paracrystal  

### 6.9 结构因子（5）`models/structure-factor/`

- `hard-sphere.html` — 硬球结构因子 — hard sphere  
- `sticky-hard-sphere.html` — 黏性硬球结构因子 — sticky hard sphere  
- `square-well.html` — 方阱结构因子 — square well  
- `hayter-msa.html` — Hayter–MSA 结构因子 — Hayter MSA  
- `two-yukawa.html` — 双 Yukawa 结构因子 — two Yukawa  

合计：15+16+3+5+4+5+29+3+5 = **85** 篇模型页，外加 1 总览 + 9 分类页 = **95** 个 HTML。

## 7. 写作口径

- 中文正文，专业术语保留英文；与现站术语表用 `data-term` 挂钩（形式因子、结构因子、多分散、衬度、回转半径等）。
- 公式与参数以原始文献为准，不翻译软件对话框里的参数名作为唯一命名；参数表用物理符号（\(R\)、\(L\)、\(\phi\)、\(\eta\) 等）。
- 参考文献只列论文与教材；有 DOI 则链接。查不到 DOI 时引用 Guinier & Fournet、Feigin & Svergun、Pedersen 综述等标准来源，不编造条目。
- 「相近模型」必须是本栏目内真实页面，禁止悬空链接。
- 全文禁词（大小写不敏感）：SasView、sasmodels、SASfit 等具体拟合软件名（实施结束前用检索确认）。

## 8. 质量与验收

实施完成的判定（明天验收）：

1. 顶栏第五条「模型手册」可进入总览；九个分类均可进入对应模型页。  
2. 第 6 节 85 篇均存在，且含第 4.3 节全部章节。  
3. 七类形状/格子有 `*-geometry.png`；除结构因子外有 `*-iq.png`；结构因子有 `*-sq.png`；图注不含软件名。  
4. 公开文件检索不到第 7 节禁词。  
5. Ctrl+K 能搜到中文名与英文名。  
6. `git status` 中无 `tools/model-figures/`。  
7. 学习路径 08 与形式因子/结构因子词条能链到本栏目。

本地检查（实施过程中执行，不引入新测试框架）：

- 核对 `models/` 下 HTML 数量与第 6 节清单一致。  
- 核对每个模型页引用的 PNG 文件存在。  
- 抽查每类一篇页面：KaTeX 渲染、侧栏高亮、上一篇/下一篇、术语悬停。  
- 检索禁词；检索 `TODO`/`TBD`/`占位`。

缺图、缺参考文献、缺相近模型链接的页面不得当作完成。

## 9. 风险与取舍

- 体量大：公开产物是静态 HTML + PNG；本地可用 gitignore 的 Python 辅助出图与生成页面，但入库文件必须可独立阅读。  
- 公式复杂（多层洋葱、RPA、微磁）：仍给定义式与参数表，推导不写成教材全书；指向原始文献。  
- 几何示意无法做到出版插画级：以能辨认几何参数为合格线。
