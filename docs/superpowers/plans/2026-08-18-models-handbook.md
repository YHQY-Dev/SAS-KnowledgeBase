# 模型手册 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在静态知识站增加顶栏第五入口「模型手册」，交付 85 篇手册级模型页、9 个分类页、总览、配图与搜索接入。

**Architecture:** 纯静态 HTML，路径 `models/<category>/<model>.html`。导航与现站 `assets/nav.js` 同一套。PNG 由本地 gitignore 的 `tools/model-figures/`（uv + Matplotlib）生成后提交到 `assets/figures/models/`。公开文案禁止拟合软件名。

**Tech Stack:** 静态 HTML、KaTeX、现有 `site.css` / `nav.js` / `glossary.js` / `search.js`；绘图用 uv、numpy、matplotlib。Git：`D:\Git\bin\git.exe`。

## Global Constraints

- 公开页面（HTML、图注、搜索词、README）禁止出现：`SasView`、`sasmodels`、`SASfit`（大小写不敏感）。
- 每篇模型页章节顺序固定：适用场景 → 物理图像 → 示意图 → 核心公式 → 参数表 → 拟合注意 → 相近模型 → 参考文献。
- 图注原文必须是：`配图：按公式计算示意`。
- 七类（sphere, cylinder, ellipsoid, parallelepiped, polyhedron, lamellae, paracrystal）必须有 `{slug}-geometry.png`；除 structure-factor 外必须有 `{slug}-iq.png`；structure-factor 必须有 `{slug}-sq.png`。
- `tools/model-figures/` 整目录 gitignore，不得 `git add`。
- 参考文献只列原始论文/教材，有 DOI 则 `<a href="https://doi.org/...">`；不列软件手册。
- 取向、磁性、多分散写进该模型页「拟合注意」，不另开页。
- `data-base`：`models/index.html` 用 `..`；分类页与模型页用 `../..`。
- 提交信息格式：`[<type>]: <说明>`，正文 `- ` 条目，中文。
- 在分支 `feat/models-handbook` 上实现，不要直接推 main。

**Spec:** `docs/superpowers/specs/2026-08-18-models-handbook-design.md`

---

## File map

**Create**

- `models/index.html` — 栏目总览
- `models/{sphere,cylinder,ellipsoid,parallelepiped,polyhedron,lamellae,shape-independent,paracrystal,structure-factor}/index.html` — 分类页
- `models/<category>/<slug>.html` — 85 篇模型页（清单见 spec §6）
- `assets/figures/models/<category>/*.png` — 配图
- `tools/model-figures/` — 本地绘图工程（不入库）

**Modify**

- `.gitignore` — 忽略 `tools/model-figures/`
- `assets/nav.js` — 顶栏、侧栏、`sectionKey`、`currentHrefTail`
- `index.html` — 五条入口
- `about.html` — 内容结构
- `README.md` — 目录表
- `learn/index.html`、`learn/08-models-polydispersity.html` — 链到模型手册
- `glossary/form-factor.html`、`glossary/structure-factor.html` — 「出现于」
- `data/search-index.js` — 每篇模型一条索引
- `assets/nav.js` `SIDEBARS.home.links` — 增加模型手册

**Do not create:** 在线拟合器、插件模型页、\(P\times S\) 组合页、测试框架。

---

## Shared contracts

### PAGE_SHELL

模型页与分类页（`data-base="../.."`）必须用下列外壳。`BODY` 为正文；`TITLE_ZH` / `TITLE_EN` / `DOC_TITLE` 按页替换。

```html
<!DOCTYPE html>
<html lang="zh-CN" data-base="../..">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DOC_TITLE · 模型手册 · SAS 知识站</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <link rel="stylesheet" href="../../assets/site.css">
</head>
<body>
  <div id="site-header"></div>
  <div class="layout">
    <aside id="site-sidebar"></aside>
    <main class="content">
      BODY
    </main>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <script src="../../assets/nav.js"></script>
  <script src="../../assets/glossary-data.js"></script>
  <script src="../../assets/glossary.js"></script>
  <script src="../../assets/figures-boot.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      if (window.renderMathInElement) {
        renderMathInElement(document.querySelector("main.content"), {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      }
      if (window.SASNav) SASNav.init();
      if (window.SASGlossary) SASGlossary.init();
    });
  </script>
</body>
</html>
```

`models/index.html` 将 `data-base`、CSS/脚本路径改为 `..`。

### MODEL_BODY

`BODY` 内顺序（禁止调换）：

```html
<h1>TITLE_ZH</h1>
<p class="subtitle-en">TITLE_EN</p>
<h2>适用场景</h2>
<!-- 2–4 段：何时用、样品直觉 -->
<h2>物理图像</h2>
<!-- 该 P(q) 或 S(q) 在算什么 -->
<h2>示意图</h2>
<figure class="figure">
  <img src="../../assets/figures/models/CATEGORY/SLUG-geometry.png" alt="ALT_GEOM" width="900">
  <figcaption>CAPTION_GEOM<span class="fig-source">配图：按公式计算示意</span></figcaption>
</figure>
<figure class="figure">
  <img src="../../assets/figures/models/CATEGORY/SLUG-iq.png" alt="ALT_IQ" width="900">
  <figcaption>CAPTION_IQ<span class="fig-source">配图：按公式计算示意</span></figcaption>
</figure>
<h2>核心公式</h2>
<!-- KaTeX $$...$$ ；符号当场定义 -->
<h2>参数表</h2>
<table>
  <thead><tr><th>参数</th><th>符号</th><th>含义</th><th>单位</th><th>典型范围</th></tr></thead>
  <tbody><!-- 行 --></tbody>
</table>
<h2>拟合注意</h2>
<!-- 取向 / 磁性 / 多分散（适用则写）；常见坑；可辨识性 -->
<h2>相近模型</h2>
<ul><!-- <a href="..."> 只链本栏目已规划页面 --></ul>
<h2>参考文献</h2>
<ul><!-- 论文/教材；DOI 用 https://doi.org/ --></ul>
<nav class="pager">
  <a href="PREV.html">← PREV_ZH</a>
  <a href="NEXT.html">NEXT_ZH →</a>
</nav>
```

shape-independent：删除 geometry 的 `<figure>`。  
structure-factor：删除 geometry；曲线图文件名为 `SLUG-sq.png`，alt/caption 写 \(S(q)\)。  
分类内第一篇 PREV 链到 `index.html`（分类总览）；最后一篇 NEXT 链到 `index.html`。

### SEARCH_ENTRY

追加到 `window.SAS_SEARCH_INDEX` 数组：

```javascript
{
  "id": "models/CATEGORY/SLUG",
  "title": "TITLE_ZH",
  "url": "models/CATEGORY/SLUG.html",
  "section": "模型手册",
  "headings": ["适用场景", "物理图像", "示意图", "核心公式", "参数表", "拟合注意", "相近模型", "参考文献"],
  "text": "TITLE_ZH TITLE_EN ...中英文关键词与符号..."
}
```

分类页与总览也各一条，`url` 为对应 `index.html`。

### VERIFY_CATEGORY

在仓库根用 PowerShell（把 `CAT` 换成分类 slug）：

```powershell
$root = "D:\softwareDev\SAS\SAS-KnowledgeBase"
Select-String -Path "$root\models\$env:CAT\*.html","$root\assets\figures\models\$env:CAT\*" -Pattern "SasView|sasmodels|SASfit" -SimpleMatch -ErrorAction SilentlyContinue
Get-ChildItem "$root\models\$env:CAT\*.html" | Measure-Object
Get-ChildItem "$root\assets\figures\models\$env:CAT\*.png" | Select-Object Name
```

期望：禁词零命中；HTML 数量 = 1 个 `index.html` + 该分类模型数；每个模型所需 PNG 都在。

---

### Task 1: 分支、gitignore、导航与栏目骨架

**Files:**
- Create: `models/index.html`
- Create: `models/sphere/index.html`, `models/cylinder/index.html`, `models/ellipsoid/index.html`, `models/parallelepiped/index.html`, `models/polyhedron/index.html`, `models/lamellae/index.html`, `models/shape-independent/index.html`, `models/paracrystal/index.html`, `models/structure-factor/index.html`
- Modify: `.gitignore`
- Modify: `assets/nav.js`
- Modify: `index.html`
- Modify: `about.html`
- Modify: `README.md`

**Interfaces:**
- Consumes: 现站 `PAGE_SHELL` 惯例；spec §3 分类表
- Produces: 顶栏「模型手册」；`SIDEBARS.models`；`sectionKey` 对 `models/` 返回 `"models"`；`currentHrefTail` 能从路径中识别 `models`（不能只用 `parts.slice(-2)`）

- [ ] **Step 1: 建分支**

```powershell
cd D:\softwareDev\SAS\SAS-KnowledgeBase
D:\Git\bin\git.exe checkout -b feat/models-handbook
```

Expected: 当前分支 `feat/models-handbook`。

- [ ] **Step 2: 写失败检查（骨架尚不存在）**

```powershell
Test-Path D:\softwareDev\SAS\SAS-KnowledgeBase\models\index.html
```

Expected: `False`

- [ ] **Step 3: `.gitignore` 追加**

在 `.gitignore` 末尾追加：

```
# Local figure/page generators — do not commit
tools/model-figures/
```

- [ ] **Step 4: 修补 `assets/nav.js`**

将 `NAV` 改为：

```javascript
  var NAV = [
    { href: "learn/index.html", label: "学习路径" },
    { href: "topics/index.html", label: "专题手册" },
    { href: "glossary/index.html", label: "术语表" },
    { href: "catalog/index.html", label: "文献目录" },
    { href: "models/index.html", label: "模型手册" }
  ];
```

在 `SIDEBARS.topics` 之后插入：

```javascript
    models: {
      title: "模型手册",
      links: [
        { href: "models/index.html", label: "总览" },
        { href: "models/sphere/index.html", label: "球" },
        { href: "models/cylinder/index.html", label: "圆柱" },
        { href: "models/ellipsoid/index.html", label: "椭球" },
        { href: "models/parallelepiped/index.html", label: "平行六面体" },
        { href: "models/polyhedron/index.html", label: "多面体" },
        { href: "models/lamellae/index.html", label: "层状" },
        { href: "models/shape-independent/index.html", label: "形状无关" },
        { href: "models/paracrystal/index.html", label: "准晶" },
        { href: "models/structure-factor/index.html", label: "结构因子" }
      ]
    },
```

`SIDEBARS.home.links` 增加 `{ href: "models/index.html", label: "模型手册" }`。

将 `sectionKey` 改为：

```javascript
  function sectionKey(tail) {
    var t = (tail || "").replace(/\/+$/, "");
    if (t === "learn" || t.indexOf("learn/") === 0) return "learn";
    if (t === "topics" || t.indexOf("topics/") === 0) return "topics";
    if (t === "glossary" || t.indexOf("glossary/") === 0) return "glossary";
    if (t === "catalog" || t.indexOf("catalog/") === 0) return "catalog";
    if (t === "models" || t.indexOf("models/") === 0) return "models";
    return "home";
  }
```

将 `currentHrefTail` 改为（否则 `models/sphere/sphere.html` 会被切成 `sphere/sphere.html`，侧栏错成首页）：

```javascript
  function currentHrefTail() {
    var path = window.location.pathname.replace(/\\/g, "/");
    var parts = path.split("/").filter(Boolean);
    var markers = ["learn", "topics", "glossary", "catalog", "models"];
    for (var i = 0; i < parts.length; i++) {
      if (markers.indexOf(parts[i]) >= 0) {
        return parts.slice(i).join("/");
      }
    }
    return parts.length ? parts[parts.length - 1] : "index.html";
  }
```

- [ ] **Step 5: 写 `models/index.html`**

`data-base=".."`。正文：

- `h1` 模型手册；`subtitle-en`：`Model handbook — form factors, empirical functions, structure factors`
- 一段说明：按几何与函数类型查阅解析模型；链到 `../learn/08-models-polydispersity.html`
- `h2` 分类；九张 `.card`，href 为 `sphere/index.html` 等，文案：
  - 球：等轴粒子、核壳、囊泡
  - 圆柱：棒、管、双层盘、柔性圆柱
  - 椭球：旋转椭球与三轴椭球
  - 平行六面体：砖块与空心棱柱
  - 多面体：棱柱与截角多面体
  - 层状：膜与堆叠
  - 形状无关：Guinier / Porod / 分形 / 聚合物 / 峰
  - 准晶：SC / BCC / FCC 点阵
  - 结构因子：硬球、带电与黏性相互作用
- `h2` 怎么选模型：等轴看球；长径比看圆柱/椭球；膜看层状；只需斜率看形状无关；浓溶液加结构因子。再链学习路径 08。

- [ ] **Step 6: 写九个分类 `index.html`**

每个分类页：该分类物理说明一段 + 「模型条目将按手册页陆续列出」的卡片网格。**本任务**即可把 spec §6 该分类全部模型写成卡片链接（指向尚未存在的 html 也可以，后续任务立刻补上）。卡片 `strong` 为中文名，下一行英文名 + 一句用途。

分类副标题：

| 文件 | h1 | subtitle-en |
|------|----|-------------|
| sphere/index.html | 球 | Sphere form factors |
| cylinder/index.html | 圆柱 | Cylinder form factors |
| ellipsoid/index.html | 椭球 | Ellipsoid form factors |
| parallelepiped/index.html | 平行六面体 | Parallelepiped form factors |
| polyhedron/index.html | 多面体 | Polyhedron form factors |
| lamellae/index.html | 层状 | Lamellar form factors |
| shape-independent/index.html | 形状无关 | Shape-independent functions |
| paracrystal/index.html | 准晶 | Paracrystal structures |
| structure-factor/index.html | 结构因子 | Structure factors S(q) |

- [ ] **Step 7: 改首页 / 关于 / README**

`index.html`：`h2` 改为「五条入口」；hero 段落后补「以及按几何查阅的模型手册」；在文献目录卡片后增加：

```html
        <a class="card" href="models/index.html">
          <strong>模型手册</strong>
          解析形式因子、经验函数与结构因子的中文手册：公式、参数、适用场景与原始文献。
        </a>
```

`about.html` 内容结构增加：

```html
        <li><strong>模型手册：</strong>按球、圆柱、层状、结构因子等分类的解析模型手册，适合选模型与对照公式。</li>
```

`README.md` 表格增加一行：`| \`models/\` | 模型手册：形式因子、形状无关函数、结构因子 |`

「怎么读这个站」增加第 4 条：选形状模型时打开模型手册。

- [ ] **Step 8: 验证骨架**

```powershell
Test-Path D:\softwareDev\SAS\SAS-KnowledgeBase\models\index.html
Select-String -Path D:\softwareDev\SAS\SAS-KnowledgeBase\assets\nav.js -Pattern "模型手册"
Select-String -Path D:\softwareDev\SAS\SAS-KnowledgeBase\models,D:\softwareDev\SAS\SAS-KnowledgeBase\index.html,D:\softwareDev\SAS\SAS-KnowledgeBase\about.html,D:\softwareDev\SAS\SAS-KnowledgeBase\README.md -Pattern "SasView|sasmodels|SASfit"
```

Expected: 总览存在；nav 含模型手册；禁词无命中。

- [ ] **Step 9: Commit**

```powershell
D:\Git\bin\git.exe add .gitignore assets/nav.js index.html about.html README.md models
D:\Git\bin\git.exe commit -m @"
[feat]: 加入模型手册导航与分类骨架

- 顶栏第五入口与九个分类侧栏
- 修正嵌套路径下栏目识别
"@
```

---

### Task 2: 本地 Matplotlib 出图工程（不入库）

**Files:**
- Create (untracked): `tools/model-figures/pyproject.toml`
- Create (untracked): `tools/model-figures/src/plotting.py`
- Create (untracked): `tools/model-figures/src/geometry.py`
- Create (untracked): `tools/model-figures/src/iq.py`
- Create (untracked): `tools/model-figures/src/run.py`
- Create: directories `assets/figures/models/{sphere,cylinder,ellipsoid,parallelepiped,polyhedron,lamellae,shape-independent,paracrystal,structure-factor}/`（可先放 `.gitkeep`，有 PNG 后删除 keep）

**Interfaces:**
- Consumes: uv；spec §5 出图规则
- Produces: 函数 `save_png(path, fig)`；`plot_iq(q, I, path, ylabel="$I(q)$")`；`plot_sq(q, S, path)`；几何辅助画圆/圆柱/椭球/矩形/层状/格子。输出目录 `assets/figures/models/<category>/`

- [ ] **Step 1: 确认 tools 被忽略**

```powershell
cd D:\softwareDev\SAS\SAS-KnowledgeBase
D:\Git\bin\git.exe check-ignore -v tools/model-figures/pyproject.toml
```

Expected: 输出指向 `.gitignore` 规则。若失败，先修好 gitignore 再继续。

- [ ] **Step 2: 初始化 uv 工程**

```powershell
New-Item -ItemType Directory -Force -Path D:\softwareDev\SAS\SAS-KnowledgeBase\tools\model-figures\src | Out-Null
cd D:\softwareDev\SAS\SAS-KnowledgeBase\tools\model-figures
uv init --name model-figures
uv add numpy matplotlib
```

`pyproject.toml` 依赖必须含 `numpy`、`matplotlib`。

- [ ] **Step 3: 写入公共绘图函数**

`src/plotting.py`：

```python
from pathlib import Path
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[3]
FIG = REPO / "assets" / "figures" / "models"

def out_path(category: str, filename: str) -> Path:
    p = FIG / category
    p.mkdir(parents=True, exist_ok=True)
    return p / filename

def save_png(path: Path) -> None:
    plt.tight_layout()
    plt.savefig(path, dpi=140, facecolor="white")
    plt.close()

def plot_curve(q, y, path: Path, ylabel: str) -> None:
    plt.figure(figsize=(8.5, 5.2))
    plt.loglog(q, y, color="#1f4e79", lw=2)
    plt.xlabel(r"$q$")
    plt.ylabel(ylabel)
    plt.grid(True, which="both", ls=":", alpha=0.4)
    save_png(path)
```

几何图用 `matplotlib.patches`（Circle, FancyBboxPatch, Polygon, Rectangle），白底，标注 $R$、$L$ 等，宽约 1200 px（`figsize=(8.5, 5.2), dpi=140`）。

- [ ] **Step 4: 冒烟：画一张均匀球 \(I(q)\)**

`src/smoke_sphere.py`：

```python
import numpy as np
from plotting import out_path, plot_curve, save_png
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

q = np.logspace(-2, 0.5, 400)
R = 50.0
x = q * R
P = np.square(3 * (np.sin(x) - x * np.cos(x)) / np.power(x, 3))
P[x < 1e-8] = 1.0
plot_curve(q, P, out_path("sphere", "sphere-iq.png"), r"$I(q)$ / $I(0)$")

fig, ax = plt.subplots(figsize=(8.5, 5.2))
ax.add_patch(Circle((0, 0), 1, fill=False, lw=2, color="#1f4e79"))
ax.annotate(r"$R$", xy=(0.7, 0.1))
ax.set_aspect("equal"); ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.3, 1.3)
ax.axis("off")
save_png(out_path("sphere", "sphere-geometry.png"))
```

Run:

```powershell
cd D:\softwareDev\SAS\SAS-KnowledgeBase\tools\model-figures
uv run python src/smoke_sphere.py
Test-Path D:\softwareDev\SAS\SAS-KnowledgeBase\assets\figures\models\sphere\sphere-iq.png
```

Expected: `True`。后续分类任务把各模型公式加进 `src/iq.py` / `src/geometry.py` / `src/run.py`，一次生成该分类全部 PNG。

- [ ] **Step 5: 确认未暂存 tools**

```powershell
cd D:\softwareDev\SAS\SAS-KnowledgeBase
D:\Git\bin\git.exe status --short
```

Expected: `tools/` 不出现。可将 `sphere-iq.png` 与 `sphere-geometry.png` 留到 Task 3 与 HTML 一并提交。本任务若只有 gitignore 已提交则不必空 commit；若 Step 3 改过已跟踪文件才 commit。

---

### Task 3: 球类 15 篇

**Files:**
- Create: spec §6.1 全部 `models/sphere/*.html`（15）
- Create: `assets/figures/models/sphere/{slug}-geometry.png` 与 `{slug}-iq.png`（15 对）
- Modify: `models/sphere/index.html` 卡片指向真实页面

**Interfaces:**
- Consumes: `PAGE_SHELL`、`MODEL_BODY`、Task 2 出图函数
- Produces: 15 篇完整手册页；pager 按下列顺序

顺序：sphere → core-shell-sphere → vesicle → multilayer-vesicle → fuzzy-sphere → raspberry → polymer-micelle → adsorbed-layer → binary-hard-sphere → core-multi-shell → linear-pearls → onion → spherical-sld → superball → micromagnetic-ff-3d

每篇必须写满 9 节。公式与文献（不得抄软件文档原文，中文改写）：

| slug | 主公式要点 | 相近 | 文献 |
|------|------------|------|------|
| sphere | Rayleigh \(P=(3(\sin x-x\cos x)/x^3)^2\), \(x=qR\); \(R_g=R\sqrt{3/5}\) | core-shell-sphere, fuzzy-sphere | Guinier & Fournet 1955; Rayleigh 1911 |
| core-shell-sphere | 核壳振幅相加，\(R_c,R_s,\rho_c,\rho_s,\rho_{solv}\) | vesicle, onion | Pedersen J. Appl. Cryst. 1997 10.1107/S0021889897002532 |
| vesicle | 薄球壳 / 内外半径 | multilayer-vesicle, core-shell-sphere | 同上 Pedersen 1997 |
| multilayer-vesicle | 多层同心壳求和 | vesicle, onion | Bergström et al.; Pedersen 1997 |
| fuzzy-sphere | 球 × 高斯界面模糊因子 | sphere | Stieger et al. J. Chem. Phys. 2004 |
| raspberry | 大核 + 表面小球 | sphere | Larson-Smith & Pozzo Soft Matter 2011 |
| polymer-micelle | 核球 + 高斯链冠状 | star-polymer, core-shell-sphere | Pedersen & Gerstenberg Macromolecules 1996 10.1021/ma951646z |
| adsorbed-layer | 球表面吸附层 | core-shell-sphere | 吸附层形式因子文献 / Pedersen 综述 |
| binary-hard-sphere | 二元混合物 \(P\) 与交叉项 | hard-sphere（结构因子分类） | Ashcroft–Langreth / Vrij |
| core-multi-shell | \(N\) 层壳振幅 | onion, core-shell-sphere | Pedersen 1997 |
| linear-pearls | 直线串珠 | pearl-necklace | 珠粒链形式因子 |
| onion | 径向多层 SLD 剖面 | core-multi-shell, spherical-sld | 多层球 |
| spherical-sld | 任意径向 \(\rho(r)\) 数值/分层 | onion | 径向傅里叶变换 |
| superball | \(\lvert x\rvert^{2p}+\lvert y\rvert^{2p}+\lvert z\rvert^{2p}=R^{2p}\) | sphere, parallelepiped | Baus & Colot / Jiao et al. |
| micromagnetic-ff-3d | 核磁矩三维微磁形式因子；拟合注意写磁性 SLD | sphere | Mühlbauer et al. Rev. Mod. Phys. 2019 10.1103/RevModPhys.91.015004 |

均匀球页必须含表行：半径 \(R\) / Å 或 nm / 典型 10–1000 Å；scale；background。拟合注意写 Schulz/logN 多分散抹平第一极小；取向对球无关；磁性则核/壳磁 SLD。

- [ ] **Step 1: 生成 15 对 PNG**（`uv run` Task 2 的 runner）
- [ ] **Step 2: 确认 PNG 存在且无禁词**
- [ ] **Step 3: 按 `MODEL_BODY` 写 15 个 HTML**
- [ ] **Step 4: VERIFY_CATEGORY（CAT=sphere）** Expected: 16 个 html（含 index），30 张 png
- [ ] **Step 5: Commit** 只 add `models/sphere` 与 `assets/figures/models/sphere/*.png`

```powershell
D:\Git\bin\git.exe add models/sphere assets/figures/models/sphere
D:\Git\bin\git.exe commit -m @"
[feat]: 完成球类模型手册与配图

- 15 篇手册页与几何 / I(q) 图
"@
```

---

### Task 4: 圆柱类 16 篇

**Files:** `models/cylinder/` 下 spec §6.2 全部 html + `assets/figures/models/cylinder/` PNG

**Interfaces:** Consumes `PAGE_SHELL`/`MODEL_BODY`。Produces 16 篇。Pager 顺序：cylinder → core-shell-cylinder → hollow-cylinder → barbell → capped-cylinder → core-shell-bicelle → core-shell-bicelle-elliptical → core-shell-bicelle-elliptical-belt-rough → elliptical-cylinder → flexible-cylinder → flexible-cylinder-elliptical → pearl-necklace → pringle → stacked-disks → tetrapod → torus-elliptical-shell

| slug | 要点 | 相近 | 文献 |
|------|------|------|------|
| cylinder | 取向平均有限圆柱；中区 \(\sim q^{-1}\) | elliptical-cylinder, hollow-cylinder | Fournet; Pedersen 1997 |
| core-shell-cylinder | 核壳圆柱振幅 | cylinder, core-shell-bicelle | Livsey; Pedersen 1997 |
| hollow-cylinder | 内外半径管 | cylinder | 空心圆柱 |
| barbell | 圆柱 + 两端球 | capped-cylinder | Kaya J. Appl. Cryst. 2004 |
| capped-cylinder | 半球帽圆柱 | barbell, cylinder | Kaya & de Souza |
| core-shell-bicelle | 核芯+带+帽的双层盘 | stacked-disks, lamellar | Watson & Trewhella / bicelle 文献 |
| core-shell-bicelle-elliptical | 椭圆盘面 bicelle | core-shell-bicelle | 同上 |
| core-shell-bicelle-elliptical-belt-rough | 腰带粗糙 | core-shell-bicelle-elliptical | 粗糙界面 bicelle |
| elliptical-cylinder | 椭圆截面 | cylinder, flexible-cylinder-elliptical | 椭圆圆柱 |
| flexible-cylinder | 蠕虫链 + 圆柱截面 | flexible-cylinder-elliptical, polymer-excl-volume | Pedersen & Schurtenberger 1996 10.1021/ma9607630 |
| flexible-cylinder-elliptical | 椭圆截面蠕虫 | flexible-cylinder | 同上 |
| pearl-necklace | 珠链（可弯曲） | linear-pearls | Schweins & Huber |
| pringle | 马鞍形盘 | stacked-disks | 弯曲盘 |
| stacked-disks | 一维堆叠圆盘 | lamellar-stack-paracrystal | Kotlarchyk; Guinier |
| tetrapod | 四臂圆柱 | cylinder | 纳米四足 |
| torus-elliptical-shell | 椭圆环壳 | hollow-cylinder, vesicle | 环面 |

拟合注意：取向 \(\theta,\phi\) 与 2D 各向异性；长度多分散 vs 半径多分散。

- [ ] **Step 1: 生成 16 对 PNG**（geometry + iq）
- [ ] **Step 2: 按 MODEL_BODY 写 16 个 HTML 并更新分类 index 卡片**
- [ ] **Step 3: VERIFY_CATEGORY CAT=cylinder** Expected: 17 html，32 png，禁词为零
- [ ] **Step 4: Commit** `models/cylinder` 与 `assets/figures/models/cylinder`

```powershell
D:\Git\bin\git.exe add models/cylinder assets/figures/models/cylinder
D:\Git\bin\git.exe commit -m @"
[feat]: 完成圆柱类模型手册与配图

- 16 篇手册页与几何 / I(q) 图
"@
```

---

### Task 5: 椭球、平行六面体、多面体（3+5+4）

**Files:** spec §6.3–6.5 全部 html 与三类 PNG

**Interfaces:** Consumes `MODEL_BODY`。Produces 12 篇。

椭球顺序：ellipsoid → core-shell-ellipsoid → triaxial-ellipsoid  
平行六面体：parallelepiped → core-shell-parallelepiped → rectangular-prism → hollow-rectangular-prism → hollow-rectangular-prism-thin-walls  
多面体：prism → tetrahedron → truncated-tetrahedron → truncated-octahedron

| slug | 要点 | 文献 |
|------|------|------|
| ellipsoid | 旋转椭球取向平均 | Guinier; Feigin & Svergun |
| core-shell-ellipsoid | 共焦核壳椭球 | Chen / Pedersen |
| triaxial-ellipsoid | \(R_a,R_b,R_c\) 三轴 | Mittelbach–Porod |
| parallelepiped | \(A,B,C\) 取向平均 | Mittelbach & Porod 1961 |
| core-shell-parallelepiped | 核壳砖块 | 同上传统 |
| rectangular-prism | 矩形棱柱 | 与 parallelepiped 对照写清约定 |
| hollow-rectangular-prism | 空心 | |
| hollow-rectangular-prism-thin-walls | 薄壁极限 | |
| prism | 等边三棱柱 | Nayuk & Huber 2012 10.1107/S0021889812019068 |
| tetrahedron | 正四面体 | 同上系列 |
| truncated-tetrahedron | 截角四面体 | |
| truncated-octahedron | 截角八面体 | |

相近模型：椭球↔圆柱（长径比极限）；平行六面体↔超球 \(p\to\infty\)；棱柱↔圆柱。

- [ ] **Step 1: 生成三类全部 geometry + iq PNG**
- [ ] **Step 2: 按 MODEL_BODY 写 12 个 HTML 并更新三份分类 index**
- [ ] **Step 3: VERIFY_CATEGORY** 对 ellipsoid（4 html，6 png）、parallelepiped（6 html，10 png）、polyhedron（5 html，8 png）
- [ ] **Step 4: Commit**

```powershell
D:\Git\bin\git.exe add models/ellipsoid models/parallelepiped models/polyhedron assets/figures/models/ellipsoid assets/figures/models/parallelepiped assets/figures/models/polyhedron
D:\Git\bin\git.exe commit -m @"
[feat]: 完成椭球、平行六面体与多面体手册

- 12 篇手册页与几何 / I(q) 图
"@
```

---

### Task 6: 层状 5 篇

**Files:** spec §6.6 + `assets/figures/models/lamellae/`

顺序：lamellar → lamellar-hg → lamellar-stack-caille → lamellar-hg-stack-caille → lamellar-stack-paracrystal

| slug | 要点 | 文献 |
|------|------|------|
| lamellar | 无限片层 \(I\sim q^{-2}\) × 厚度形式因子 | Nallet; Caille |
| lamellar-hg | 头基–尾链两段 SLD | 双层膜 |
| lamellar-stack-caille | Caille 热起伏堆叠 | Caille C. R. Acad. Sci. 1972 |
| lamellar-hg-stack-caille | 头基 + Caille | |
| lamellar-stack-paracrystal | Hosemann 准晶堆叠 | Hosemann |

相近：stacked-disks、sc-paracrystal。拟合注意：片层取向、畴大小、Caille \(\eta\) 与仪器分辨率强相关。

- [ ] **Step 1: 生成 5 对 PNG**
- [ ] **Step 2: 按 MODEL_BODY 写 5 个 HTML 并更新分类 index**
- [ ] **Step 3: VERIFY_CATEGORY CAT=lamellae** Expected: 6 html，10 png
- [ ] **Step 4: Commit**

```powershell
D:\Git\bin\git.exe add models/lamellae assets/figures/models/lamellae
D:\Git\bin\git.exe commit -m @"
[feat]: 完成层状模型手册与配图

- 5 篇手册页与几何 / I(q) 图
"@
```

---

### Task 7: 形状无关 29 篇

**Files:** spec §6.7；仅 `{slug}-iq.png`（无 geometry）

顺序与要点：

| slug | 要点 | 文献 |
|------|------|------|
| guinier | \(I(0)\exp(-q^2R_g^2/3)\) | Guinier 1939 |
| porod | \(I\sim 2\pi(\Delta\rho)^2 S/q^4\) | Porod |
| power-law | \(I\sim q^{-m}\) | |
| guinier-porod | Hammouda 三段 | Hammouda J. Appl. Cryst. 2010 10.1107/S0021889810025250 |
| unified-power-rg | Beaucage 统一 | Beaucage J. Appl. Cryst. 1995 10.1107/S0021889895005292 |
| two-power-law | 两段幂律 + 转折 | |
| lorentz | \(1/(1+\xi^2 q^2)\) 或 Ornstein–Zernike | |
| two-lorentzian | 双洛伦兹 | |
| gaussian-peak | 高斯峰 | |
| peak-lorentz | 洛伦兹峰 | |
| broad-peak | 关联峰经验式 | |
| dab | Debye–Anderson–Brumberger 两相 | DAB J. Appl. Phys. 1957 10.1063/1.1722748 |
| correlation-length | 关联长度经验式 | |
| fractal | 分形聚集体 | Teixeira J. Appl. Cryst. 1988 |
| mass-fractal | 质量分形 | Sinha; Teixeira |
| surface-fractal | 表面分形 \(D_s\) | Bale–Schmidt |
| mass-surface-fractal | 质量+表面 | |
| fractal-core-shell | 核壳分形 | |
| mono-gauss-coil | Debye \(D(x)=(e^{-x}-1+x)/x^2\), \(x=q^2R_g^2\) | Debye 1947 |
| poly-gauss-coil | Zimm 多分散 Debye | Zimm |
| polymer-excl-volume | 排除体积链 | Pedersen & Schurtenberger |
| star-polymer | 星形 | Benoit; Dozier |
| be-polyelectrolyte | 半柔性聚电解质 | Barrat–Joanny / Dobrynin |
| gauss-lorentz-gel | 凝胶两分量 | Shibayama |
| gel-fit | 凝胶经验拟合 | |
| teubner-strey | 微乳 \(I\sim 1/(a+cq^2+dq^4)\) | Teubner & Strey J. Chem. Phys. 1987 10.1063/1.453006 |
| spinodal | 旋节 Cahn–Hilliard 型 | |
| rpa | de Gennes 聚合物共混 RPA | de Gennes |
| line | \(I=A+B q\) 或 \(A+Bq^2\)（页内写明选定线性 \(A+Bq\)） | 背景/线性项，不是形状 |

相近模型互相链接（Guinier↔guinier-porod↔unified-power-rg；fractal 三篇互链；gauss coil 两篇互链）。

- [ ] **Step 1: 生成 29 张 iq PNG（无 geometry）**
- [ ] **Step 2: 按 MODEL_BODY 写 29 个 HTML（删除 geometry figure）并更新分类 index**
- [ ] **Step 3: VERIFY_CATEGORY CAT=shape-independent** Expected: 30 html，29 png
- [ ] **Step 4: Commit**

```powershell
D:\Git\bin\git.exe add models/shape-independent assets/figures/models/shape-independent
D:\Git\bin\git.exe commit -m @"
[feat]: 完成形状无关模型手册与配图

- 29 篇手册页与 I(q) 图
"@
```

---

### Task 8: 准晶 3 篇 + 结构因子 5 篇

**Files:** spec §6.8–6.9；准晶 geometry+iq；结构因子仅 sq

准晶顺序：sc-paracrystal → bcc-paracrystal → fcc-paracrystal  
结构因子：hard-sphere → sticky-hard-sphere → square-well → hayter-msa → two-yukawa

| slug | 要点 | 文献 |
|------|------|------|
| sc/bcc/fcc-paracrystal | Hosemann 准晶：晶格 + 高斯位移阻尼 | Matsuoka / Hosemann；Guinier |
| hard-sphere | Percus–Yevick \(S(q)\) | Percus–Yevick; Ashcroft & Lekner 1966 |
| sticky-hard-sphere | Baxter 黏性硬球 | Baxter J. Chem. Phys. 1968 10.1063/1.1669410 |
| square-well | 方阱闭包 | Sharma & Sharma |
| hayter-msa | 带电胶体 RMSA | Hayter & Penfold Mol. Phys. 1981 10.1080/00268978100100091 |
| two-yukawa | 双 Yukawa | Liu et al. |

相近：三种准晶互链；五种 \(S(q)\) 互链；hard-sphere ↔ binary-hard-sphere。拟合注意：\(S(q)\) 与 \(P(q)\) 同时自由拟合会退化；Hayter 需体积分数与 Debye 长度约束。

- [ ] **Step 1: 生成准晶 3 对 geometry+iq，结构因子 5 张 sq PNG**
- [ ] **Step 2: 按 MODEL_BODY 写 8 个 HTML（结构因子用 sq 图、无 geometry）并更新两份分类 index**
- [ ] **Step 3: VERIFY** 准晶 4 html + 6 png；结构因子 6 html + 5 png；禁词为零
- [ ] **Step 4: Commit** 两条

```powershell
D:\Git\bin\git.exe add models/paracrystal assets/figures/models/paracrystal
D:\Git\bin\git.exe commit -m @"
[feat]: 完成准晶模型手册与配图

- SC / BCC / FCC 三篇
"@
D:\Git\bin\git.exe add models/structure-factor assets/figures/models/structure-factor
D:\Git\bin\git.exe commit -m @"
[feat]: 完成结构因子手册与配图

- 硬球、黏性硬球、方阱、Hayter–MSA、双 Yukawa
"@
```

---

### Task 9: 搜索索引与交叉链接

**Files:**
- Modify: `data/search-index.js` — 总览 + 9 分类 + 85 模型
- Modify: `learn/index.html` — 08 条 muted 文案加「详见模型手册」链接 `../models/index.html`
- Modify: `learn/08-models-polydispersity.html` — 导语段落后加一段链到模型手册；表格「均匀球」等链到对应模型页
- Modify: `glossary/form-factor.html` — 「出现于」加 `<li><a href="../models/index.html">模型手册</a></li>`
- Modify: `glossary/structure-factor.html` — 同上并特指 `../models/structure-factor/index.html`

**Interfaces:**
- Consumes: 全部模型 `TITLE_ZH`/`TITLE_EN`/`url`
- Produces: Ctrl+K 可搜「核壳球」「Teubner」「Hayter」

- [ ] **Step 1: 写检查** — `Select-String data/search-index.js -Pattern '"section": "模型手册"' | Measure-Object` 当前应远小于 95
- [ ] **Step 2: 追加全部 SEARCH_ENTRY**（95 条：1+9+85）。`text` 字段包含中文名、英文名、关键符号（如 `Rg`、`Caille`、`Percus-Yevick`）
- [ ] **Step 3: 交叉链接** 按上列 Modify
- [ ] **Step 4: 验证**

```powershell
(Select-String -Path D:\softwareDev\SAS\SAS-KnowledgeBase\data\search-index.js -Pattern '"section": "模型手册"' ).Count
Select-String -Path D:\softwareDev\SAS\SAS-KnowledgeBase\learn\08-models-polydispersity.html -Pattern "models/index.html"
Select-String -Path D:\softwareDev\SAS\SAS-KnowledgeBase\models,D:\softwareDev\SAS\SAS-KnowledgeBase\data\search-index.js -Pattern "SasView|sasmodels|SASfit"
```

Expected: 模型手册条目 ≥ 95；08 章含链接；禁词无命中。

- [ ] **Step 5: Commit** `[feat]: 接入模型手册搜索与交叉链接`

---

### Task 10: 全库验收

**Files:** 只读检查；若缺页/缺图则回到对应 Task 补齐后再提交修复。

- [ ] **Step 1: HTML 计数**

```powershell
$m = Get-ChildItem D:\softwareDev\SAS\SAS-KnowledgeBase\models -Recurse -Filter *.html
$m.Count
$m | Where-Object { $_.Name -ne "index.html" } | Measure-Object
```

Expected: 总计 95；非 index 的模型页 85。

- [ ] **Step 2: PNG 与引用一致**

对每个模型 html，检查其 `<img src>` 指向的文件存在。缺一则修图或修 src，不得留空 figure。

- [ ] **Step 3: 禁词与占位**

```powershell
Get-ChildItem D:\softwareDev\SAS\SAS-KnowledgeBase\models -Recurse -Filter *.html | Select-String -Pattern "SasView|sasmodels|SASfit|TODO|TBD|占位|模型条目将按"
Get-ChildItem D:\softwareDev\SAS\SAS-KnowledgeBase\assets\figures\models -Recurse | Select-String -Pattern "SasView" -ErrorAction SilentlyContinue
D:\Git\bin\git.exe status --short
```

Expected: 无禁词/TODO/分类页占位句；`tools/` 不在 status 里。

- [ ] **Step 4: 抽查章节标题**

每个模型 html 必须同时含 `<h2>适用场景</h2>` `<h2>物理图像</h2>` `<h2>示意图</h2>` `<h2>核心公式</h2>` `<h2>参数表</h2>` `<h2>拟合注意</h2>` `<h2>相近模型</h2>` `<h2>参考文献</h2>`。缺则补。

- [ ] **Step 5: 若有修复则 commit** `[fix]: 补齐模型手册缺页缺图与禁词`

---

## Self-review vs spec

| Spec 节 | 对应任务 |
|---------|----------|
| §1 目标第五入口 | Task 1 |
| §2 非目标 | Global Constraints；不创建拟合器 |
| §3 目录/nav/gitignore/data-base | Task 1–2 |
| §4 页面模板 | Shared `MODEL_BODY`；Task 3–8 |
| §5 出图 | Task 2 + 每类出图步骤 |
| §6.1–6.9 85 篇 | Task 3–8 |
| §7 写作口径/禁词 | Global + Task 10 |
| §8 验收 | Task 9–10 |
| §9 本地生成器不入库 | Task 2 Step 1/5、Task 10 status |
