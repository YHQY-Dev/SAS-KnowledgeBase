# -*- coding: utf-8 -*-
"""One-shot: new glossary pages, data, search index, and first-mention wrapping."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGE_TAIL = r"""    </main>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <script src="../assets/nav.js"></script>
  <script src="../assets/glossary-data.js"></script>
  <script src="../assets/glossary.js"></script>
  <script src="../assets/figures-boot.js"></script>
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
"""


def page(title_zh: str, title_en: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-base="..">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_zh} · 术语表 · SAS 知识站</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <link rel="stylesheet" href="../assets/site.css">
</head>
<body>
  <div id="site-header"></div>
  <div class="layout">
    <aside id="site-sidebar"></aside>
    <main class="content">
      <h1>{title_zh}</h1>
      <p class="subtitle-en">{title_en}</p>
{body}
{PAGE_TAIL}"""


TERMS: dict[str, dict] = {}


def add(tid, **kw):
    TERMS[tid] = {"id": tid, **kw}


add(
    "scattering-amplitude",
    titleZh="散射振幅",
    titleEn="scattering amplitude",
    abbr="F(q)",
    tip="衬度对平面波相位的体积分；强度是它的模方。形式因子 P(q) 是归一化后的 |F|^2。",
    aliases=["F(q)", "F(q)", "散射振幅", "form amplitude"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "learn/08-models-polydispersity.html",
        "models/index.html",
        "models/sphere/sphere.html",
        "glossary/form-factor.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>散射振幅</strong> $F(\\mathbf{q})$ 是稀释极限、一阶<span data-term="born-approximation">玻恩近似</span>下，样品各体积元二次波的相干叠加。入射平面波 $e^{i\\mathbf{k}_i\\cdot\\mathbf{r}}$ 在 $\\mathbf{r}$ 处被<span data-term="scattering-length-density">散射长度密度</span> $\\rho(\\mathbf{r})$ 散射，出射方向波矢为 $\\mathbf{k}_s$。相对相位由<span data-term="scattering-vector-q">散射矢量</span> $\\mathbf{q}=\\mathbf{k}_s-\\mathbf{k}_i$ 决定，于是</p>
      $$F(\\mathbf{q})=\\int \\rho(\\mathbf{r})\\,e^{i\\mathbf{q}\\cdot\\mathbf{r}}\\,\\mathrm{d}V.$$
      <p>均匀溶剂（或基体）$\\rho_s$ 的傅里叶变换只落在 $\\mathbf{q}=0$（未被散射的入射束，由<span data-term="beamstop">束阻</span>挡住）。进入小角探测器的是过剩密度 $\\Delta\\rho=\\rho-\\rho_s$，即<span data-term="contrast">衬度</span>场：</p>
      $$F(\\mathbf{q})=\\int \\Delta\\rho(\\mathbf{r})\\,e^{i\\mathbf{q}\\cdot\\mathbf{r}}\\,\\mathrm{d}V.$$
      <p>探测器测强度不测相位，故 $I\\propto\\lvert F\\rvert^2$。</p>

      <h2>物理直觉</h2>
      <p>可把 $F$ 看成「谁在散射、相位差多少」的记账：体积元贡献 $\\Delta\\rho\\,\\mathrm{d}V$，再乘平面波相位。模型手册里球、柱、核壳的闭式，都是对这个积分在特定 $\\Delta\\rho(\\mathbf{r})$ 上求出来的。</p>
      <p>与<span data-term="form-factor">形式因子</span>的关系（均匀粒子、约定 $P(0)=1$）：</p>
      $$P(q)=\\left\\lvert\\frac{F(q)}{F(0)}\\right\\rvert^2.$$
      <p>$F(0)=\\Delta\\rho\\,V$ 是超额散射长度。稀释、单分散强度常写 $I(q)=n\\lvert F(q)\\rvert^2+B=n(\\Delta\\rho)^2 V^2 P(q)+B$，其中 $n$ 为<span data-term="number-density">数密度</span>。</p>
      <p>各向异性粒子还须对取向做<span data-term="powder-average">粉末平均</span>：$I(q)=\\langle\\lvert F(\\mathbf{q})\\rvert^2\\rangle$。掠入射几何下入射场已不是简单平面波，应改用<span data-term="dwba">DWBA</span>，而不是本页的透射 Born 积分。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>$F$ 是振幅，$P$ 是归一化强度：$P$ 不含 $n$ 与 $(\\Delta\\rho)^2$，拟合标度因子里才有它们。</li>
        <li>晶体学结构因子 $F_{hkl}$ 与本页 $F(\\mathbf{q})$ 名称相近：前者是晶胞求和，后者是连续衬度的傅里叶变换。</li>
        <li>$\\Delta\\rho$ 写成常数从积分里提出，只对均匀粒子合法；核壳、径向剖面必须留在积分号内。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="born-approximation">玻恩近似</span>（本积分的适用条件）</li>
        <li><span data-term="form-factor">形式因子</span> $P(q)$</li>
        <li><span data-term="structure-factor">结构因子</span> $S(q)$</li>
        <li><span data-term="contrast">衬度</span> $\\Delta\\rho$</li>
        <li><span data-term="powder-average">粉末平均</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/02-scattering-basics.html">学习路径 02 · 散射基础</a></li>
        <li><a href="../learn/08-models-polydispersity.html">学习路径 08 · 模型与多分散</a></li>
        <li><a href="../models/index.html">模型手册</a>（各篇「出发点」）</li>
        <li><a href="../models/sphere/sphere.html">均匀球</a></li>
      </ul>
""",
)

add(
    "born-approximation",
    titleZh="玻恩近似",
    titleEn="Born approximation",
    abbr="BA",
    tip="弱散射、单次散射时，把入射波当未畸变平面波，散射振幅化为衬度的傅里叶变换。",
    aliases=["Born", "运动学近似", "一阶玻恩", "kinematic"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "glossary/scattering-amplitude.html",
        "glossary/dwba.html",
        "topics/gisaxs/index.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>玻恩近似</strong>（Born approximation，运动学近似）假定：入射波穿过样品时几乎不被衰减或折射畸变，每个体积元只散射一次。此时二次波的源就是未扰动平面波，总<span data-term="scattering-amplitude">散射振幅</span>化为</p>
      $$F(\\mathbf{q})=\\int\\Delta\\rho(\\mathbf{r})\\,e^{i\\mathbf{q}\\cdot\\mathbf{r}}\\,\\mathrm{d}V.$$
      <p>这是透射 <span data-term="saxs">SAXS</span> / <span data-term="sans">SANS</span> 形式因子推导的默认出发点。模型手册里的闭式都建立在这一假设上。</p>

      <h2>物理直觉</h2>
      <p>「弱」的判据是多次散射可忽略：透射率不要太低、颗粒衬度与厚度的乘积不要太大。实验室软物质溶液通常满足；厚、强散射的 USAXS 样品或浓浆料可能偏离，见<span data-term="multiple-scattering">多重散射</span>。</p>
      <p>掠入射靠近临界角时，反射/折射已把入射场改成「畸变波」，必须升级为<span data-term="dwba">DWBA</span>。DWBA 仍是对侧向结构做一阶玻恩微扰，只是参考波不再是真空平面波。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>玻恩近似 ≠ 「公式里可以随便忽略相位」：相位 $e^{i\\mathbf{q}\\cdot\\mathbf{r}}$ 正是干涉的来源。</li>
        <li>满足 Born 仍可能有仪器<span data-term="instrument-smearing">模糊</span>与<span data-term="polydispersity">多分散</span>，那些是实验效应，不是动力学散射。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="scattering-amplitude">散射振幅</span> $F(\\mathbf{q})$</li>
        <li><span data-term="dwba">畸变波玻恩近似</span></li>
        <li><span data-term="multiple-scattering">多重散射</span></li>
        <li><span data-term="coherent-scattering">相干散射</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/02-scattering-basics.html">学习路径 02 · 散射基础</a></li>
        <li><a href="../topics/gisaxs/index.html">专题 · GISAXS</a></li>
      </ul>
""",
)

add(
    "powder-average",
    titleZh="粉末平均",
    titleEn="powder / orientational average",
    abbr="",
    tip="对各向异性粒子相对 q 的取向做无规平均；溶液与粉末样品的 I(q) 只依赖 q 的模长。",
    aliases=["取向平均", "取向无规", "粉末平均", "orientational average"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "learn/08-models-polydispersity.html",
        "models/cylinder/cylinder.html",
        "models/ellipsoid/ellipsoid.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>粉末平均</strong>（取向平均）指粒子取向相对 <span data-term="scattering-vector-q">$\\mathbf{q}$</span> 均匀无规时，把振幅模方对取向积分。各向同性溶液、无规粉末都用这一步，使测得强度只依赖 $q=\\lvert\\mathbf{q}\\rvert$：</p>
      $$I(q)=\\bigl\\langle \\lvert F(\\mathbf{q})\\rvert^2 \\bigr\\rangle_{\\hat{u}} = \\int \\lvert F(q,\\hat{u})\\rvert^2 \\,\\mathrm{d}\\Omega_{\\hat{u}}\\Big/\\int \\mathrm{d}\\Omega_{\\hat{u}}.$$
      <p>球对称粒子取向平均是平凡的。圆柱常用轴与 $\\mathbf{q}$ 的夹角 $\\alpha$：$\\langle\\cdots\\rangle=\\int_0^{\\pi/2}\\lvert F(q,\\alpha)\\rvert^2\\sin\\alpha\\,\\mathrm{d}\\alpha$。</p>

      <h2>物理直觉</h2>
      <p>单取向粒子的 $F$ 依赖 $\\mathbf{q}$ 的方向（例如棒沿轴向与径向完全不同）。探测器若对所有取向一视同仁，看到的是这些曲线的权重混合，振荡变钝、各向异性信息被洗掉。流动、磁场或掠入射薄膜可以打破无规取向，此时不要用粉末平均公式去套 2D 图。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>粉末平均 ≠ <span data-term="polydispersity">尺寸多分散</span>：前者混取向，后者混半径；两者都会抹平振荡，但物理不同。</li>
        <li>层状粉末还有额外的 <span data-term="lorentz-factor">Lorentz 因子</span>（横向无限片的取向权重），不只是对 $F$ 做球面平均。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="scattering-amplitude">散射振幅</span></li>
        <li><span data-term="form-factor">形式因子</span></li>
        <li><span data-term="lorentz-factor">Lorentz 因子</span></li>
        <li><span data-term="polydispersity">多分散</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/cylinder/cylinder.html">圆柱</a></li>
        <li><a href="../models/ellipsoid/ellipsoid.html">椭球</a></li>
        <li><a href="../models/lamellae/lamellar.html">层状</a></li>
      </ul>
""",
)

add(
    "number-density",
    titleZh="数密度",
    titleEn="number density",
    abbr="n",
    tip="单位体积内的粒子数。稀释强度 I(q)=n|F(q)|²；与体积分数的关系是 φ=nV。",
    aliases=["n", "数密度", "粒子数密度"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "learn/05-absolute-calibration.html",
        "learn/08-models-polydispersity.html",
        "glossary/volume-fraction.html",
        "glossary/absolute-intensity.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>数密度</strong> $n$ 是单位体积内散射体的个数。稀释、互不相关时</p>
      $$I(q)=n\\,\\lvert F(q)\\rvert^2+B=n(\\Delta\\rho)^2 V^2 P(q)+B.$$
      <p>与<span data-term="volume-fraction">体积分数</span>的关系是 $\\phi=nV$（单分散）。绝对强度标定后，若已知 <span data-term="contrast">$\\Delta\\rho$</span> 与 $V$，可由 <span data-term="forward-scattering">$I(0)$</span> 反推 $n$ 或分子量。</p>

      <h2>物理直觉</h2>
      <p>$n$ 只把曲线整体抬升或压低，不改变 $P(q)$ 的形状。拟合里常把 $n(\\Delta\\rho)^2 V^2$ 收成无量纲「scale」：相对单位下 $n$ 与衬度平方不可分。</p>
      <p>液体理论里的 $n$ 还出现在 <span data-term="ornstein-zernike">Ornstein–Zernike</span> 方程和 $S(q)=[1-n\\hat{c}(q)]^{-1}$ 中，那里它是相互作用流体的密度，不一定等于「拟合标度里的那个 $n$」。硬球常用体积分数 $\\eta=n\\pi\\sigma^3/6$ 代替。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>质量浓度 $c$（mg/mL）不是 $n$：还须分子量或比体积才能换算。</li>
        <li>浓溶液 $I\\neq n\\lvert F\\rvert^2$，还要乘 <span data-term="structure-factor">$S(q)$</span>；把 $S(0)&lt;1$ 的压低当成 $n$ 变小会系统偏差。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="volume-fraction">体积分数</span> $\\phi$</li>
        <li><span data-term="scattering-amplitude">散射振幅</span></li>
        <li><span data-term="absolute-intensity">绝对强度</span></li>
        <li><span data-term="forward-scattering">前向散射</span> $I(0)$</li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/02-scattering-basics.html">学习路径 02 · 散射基础</a></li>
        <li><a href="../learn/05-absolute-calibration.html">学习路径 05 · 绝对标定</a></li>
      </ul>
""",
)

add(
    "ornstein-zernike",
    titleZh="Ornstein–Zernike 方程",
    titleEn="Ornstein–Zernike equation",
    abbr="OZ",
    tip="把全相关 h=g−1 分解为直接相关 c 与间接链；傅里叶空间给出 S(q)=[1−n ĉ(q)]⁻¹。",
    aliases=["OZ", "Ornstein-Zernike", "OZ 方程"],
    appearsIn=[
        "models/structure-factor/hard-sphere.html",
        "models/structure-factor/hayter-msa.html",
        "glossary/structure-factor.html",
        "glossary/pair-correlation.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>Ornstein–Zernike（OZ）方程</strong>是液体理论的出发点。全相关 $h(r)=g(r)-1$ 写成直接相关 $c(r)$ 加上经第三个粒子传递的间接相关：</p>
      $$h(r)=c(r)+n\\int c(\\lvert\\mathbf{r}-\\mathbf{r}'\\rvert)\\,h(r')\\,\\mathrm{d}^3r'.$$
      <p>傅里叶变换后变成代数式 $\\hat{h}=\\hat{c}+n\\hat{c}\\,\\hat{h}$。各向同性流体的<span data-term="structure-factor">结构因子</span>就是密度涨落谱</p>
      $$S(q)=1+n\\hat{h}(q)=\\bigl[1-n\\hat{c}(q)\\bigr]^{-1}.$$
      <p>OZ 本身不闭合：还须一条连接 $c$、$g$ 与相互作用势 $u(r)$ 的闭包，例如 <span data-term="percus-yevick">Percus–Yevick</span> 或 <span data-term="mean-spherical-approximation">平均球近似</span>。</p>

      <h2>物理直觉</h2>
      <p>$c(r)$ 描述「两个粒子直接看见对方」的那一段，通常比 $g(r)$ 更短程。知道 $c$ 就能用上式算出整个 $S(q)$，包括低 $q$ 的压缩率 $S(0)$ 和第一相关峰。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>OZ 不是一种 $S(q)$ 模型，而是所有液体闭包共享的骨架。</li>
        <li>$\\hat{h}(q)$ 与单粒子 <span data-term="scattering-amplitude">$F(q)$</span> 不是一回事：前者是粒间关联，后者是粒内衬度。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="pair-correlation">对关联函数</span> $g(r)$</li>
        <li><span data-term="percus-yevick">Percus–Yevick 闭包</span></li>
        <li><span data-term="mean-spherical-approximation">平均球近似</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/structure-factor/hard-sphere.html">硬球结构因子</a></li>
        <li><a href="../models/structure-factor/hayter-msa.html">Hayter–MSA</a></li>
        <li><a href="../models/structure-factor/index.html">结构因子分类</a></li>
      </ul>
""",
)

add(
    "pair-correlation",
    titleZh="对关联函数",
    titleEn="pair correlation function",
    abbr="g(r)",
    tip="找到一个粒子后，距离 r 处再找到另一个粒子的相对概率。h=g−1 的傅里叶变换给出 S(q)。",
    aliases=["g(r)", "径向分布函数", "rdf", "对分布"],
    appearsIn=[
        "glossary/ornstein-zernike.html",
        "glossary/structure-factor.html",
        "models/structure-factor/hard-sphere.html",
        "learn/08-models-polydispersity.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>对关联函数</strong>（径向分布函数）$g(r)$ 给出：以一个粒子为原点，距它 $r$ 处出现另一个粒子中心的概率密度，相对理想气体的倍数。理想气 $g=1$；硬核内 $g=0$。全相关 $h=g-1$ 的傅里叶变换进入 <span data-term="structure-factor">结构因子</span></p>
      $$S(q)=1+n\\int [g(r)-1]\\,e^{i\\mathbf{q}\\cdot\\mathbf{r}}\\,\\mathrm{d}V.$$
      <p>这与单粒子距离分布 <span data-term="pair-distance-distribution">$p(r)$</span> 不是同一个量：$p(r)$ 描述<strong>一个</strong>粒子内部的点–点距离，$g(r)$ 描述<strong>不同</strong>粒子中心之间的距离。</p>

      <h2>物理直觉</h2>
      <p>硬球流体的 $g(r)$ 在接触 $r=\\sigma$ 有一个峰，随后振荡并回到 1，对应壳层堆积。峰越锐，$S(q)$ 的第一相关峰越强。IFT / GIFT 一类方法有时从实验 $I(q)$ 同时抽取粒内 $p(r)$ 与有效 $g(r)$，前提是相互作用不太复杂。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>$g(r)$ ≠ $p(r)$：一个是粒间，一个是粒内。</li>
        <li>$S(q)$ 的峰位 $\\sim 2\\pi/d$ 对应 $g(r)$ 的主周期 $d$，不是形式因子极小。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="ornstein-zernike">Ornstein–Zernike 方程</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
        <li><span data-term="pair-distance-distribution">距离分布</span> $p(r)$</li>
        <li><span data-term="number-density">数密度</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/structure-factor/hard-sphere.html">硬球结构因子</a></li>
        <li><a href="../learn/08-models-polydispersity.html">学习路径 08 · 模型与多分散</a></li>
      </ul>
""",
)

add(
    "percus-yevick",
    titleZh="Percus–Yevick 闭包",
    titleEn="Percus–Yevick closure",
    abbr="PY",
    tip="液体理论常用闭包；硬球势下给出 Wertheim–Thiele 解析 c(r)，从而有闭式 S(q)。",
    aliases=["PY", "Percus-Yevick", "PY 闭包"],
    appearsIn=[
        "models/structure-factor/hard-sphere.html",
        "models/sphere/binary-hard-sphere.html",
        "glossary/ornstein-zernike.html",
        "glossary/structure-factor.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>Percus–Yevick（PY）闭包</strong>把直接相关与对关联、势函数连起来：</p>
      $$c(r)=\\bigl[1-e^{\\beta u(r)}\\bigr] g(r).$$
      <p>对硬球势（$r&lt;\\sigma$ 时 $u=\\infty$，核外 $u=0$），它给出核内 $g=0$、核外 $c=0$。代入 <span data-term="ornstein-zernike">OZ</span> 后，$c(r)$ 在核内是三次多项式（Wertheim–Thiele），傅里叶变换有闭式，即胶体散射里常用的 Ashcroft–Lekner 硬球 $S(q)$。</p>

      <h2>物理直觉</h2>
      <p>PY 对短程排斥很准，对长程库仑并不好——带电胶体应改用 <span data-term="mean-spherical-approximation">MSA</span>（Hayter–Penfold）。PY 硬球只有一个无量纲密度 $\\eta$，所以「一个体积分数就能解释低 $q$ 压低和第一峰」时，它是最省参数的选择。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>PY 是闭包名称，不是「硬球」的同义词：硬球还可以用其他闭包；PY 也可以形式地写给别的势，只是硬球才有著名解析解。</li>
        <li>二元混合物要用 Ashcroft–Langreth 的部分结构因子 $S_{ij}$，不是把一元 PY 平均两次。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="ornstein-zernike">Ornstein–Zernike 方程</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
        <li><span data-term="volume-fraction">体积分数</span></li>
        <li><span data-term="mean-spherical-approximation">平均球近似</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/structure-factor/hard-sphere.html">硬球结构因子</a></li>
        <li><a href="../models/sphere/binary-hard-sphere.html">二元硬球</a></li>
      </ul>
""",
)

add(
    "mean-spherical-approximation",
    titleZh="平均球近似",
    titleEn="mean spherical approximation",
    abbr="MSA",
    tip="硬核加长程尾势的液体闭包；Hayter–Penfold 用它给出带电胶体的 Yukawa 结构因子。",
    aliases=["MSA", "平均球近似", "mean spherical"],
    appearsIn=[
        "models/structure-factor/hayter-msa.html",
        "models/structure-factor/two-yukawa.html",
        "glossary/ornstein-zernike.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>平均球近似</strong>（mean spherical approximation, MSA）是硬核流体的闭包：核内 $g=0$（不可穿透），核外 $c(r)=-\\beta u(r)$。当尾势 $u$ 取屏蔽库仑（Yukawa）时，Hayter 与 Penfold 给出解析 $S(q)$，即带电胶体常用的 Hayter–MSA 结构因子。</p>
      <p>它与 <span data-term="percus-yevick">PY</span> 硬球的差别：PY 核外 $c=0$（无吸引/长程尾）；MSA 允许核外有 $u(r)$，因此能描述静电排斥造成的低 $q$ 更强压低、相关峰随盐浓度移动。</p>

      <h2>物理直觉</h2>
      <p>Debye 长度变短（加盐）时，Yukawa 尾变短，$S(q)$ 向硬球极限靠拢。电荷与体积分数、直径高度相关：没有盐或浓度系列时不要同时放开所有势参数。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>MSA ≠ 「球的形式因子」：这是粒间势的闭包，乘的是已经算好的 $P(q)$。</li>
        <li>两段 Yukawa（短程吸引 + 长程排斥）仍用同一 MSA 骨架，只是 $u(r)$ 更复杂，更易过拟合。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="ornstein-zernike">Ornstein–Zernike 方程</span></li>
        <li><span data-term="percus-yevick">Percus–Yevick 闭包</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/structure-factor/hayter-msa.html">Hayter–MSA</a></li>
        <li><a href="../models/structure-factor/two-yukawa.html">双 Yukawa</a></li>
      </ul>
""",
)

add(
    "correlation-function",
    titleZh="相关函数",
    titleEn="Debye correlation function",
    abbr="γ(r)",
    tip="衬度涨落的空间自相关；I(q) 是它的傅里叶变换。两相介质的 Porod 不变量与比表面积都从 γ 来。",
    aliases=["γ(r)", "gamma(r)", "Debye 相关", "特征函数"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "glossary/porod-law.html",
        "glossary/porod-invariant.html",
        "models/shape-independent/dab.html",
        "models/shape-independent/porod.html",
    ],
    body="""
      <h2>定义</h2>
      <p>Debye <strong>相关函数</strong> $\\gamma(r)$ 是衬度涨落 $\\Delta\\rho(\\mathbf{x})$ 的空间自相关（常归一化 $\\gamma(0)=1$）：</p>
      $$\\gamma(r)=\\frac{\\langle \\Delta\\rho(\\mathbf{x})\\Delta\\rho(\\mathbf{x}+\\mathbf{r})\\rangle}{\\langle(\\Delta\\rho)^2\\rangle}.$$
      <p>各向同性时强度是它的正弦变换，这就是 Debye 公式。均匀粒子的 $\\gamma$ 可由自相关体积（characteristic function）得到，与 <span data-term="pair-distance-distribution">$p(r)$</span> 只差几何权重：$p(r)\\propto r^2\\gamma(r)$（有限支撑时）。</p>

      <h2>物理直觉</h2>
      <p>$\\gamma(r)$ 回答「分开 $r$ 的两点，衬度还相不相关」。相关在短程就断 → 高 $q$ 慢衰减；相关延伸很远 → 低 $q$ 很陡。指数型 $\\gamma=e^{-r/\\xi}$ 给出 Debye–Bueche / 洛伦兹形式，即无规两相介质的经典闭式。</p>
      <p>尖锐界面使 $\\gamma$ 在 $r\\to 0$ 有线性项，傅里叶后就是 <span data-term="porod-law">Porod</span> $q^{-4}$。界面有限厚度会改变小 $r$ 的展开，高 $q$ 比 $q^{-4}$ 衰减更快。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>$\\gamma(r)$ 是衬度涨落的相关；<span data-term="pair-correlation">$g(r)$</span> 是粒子中心的相关。两相多孔介质用 $\\gamma$，硬球流体用 $g$。</li>
        <li><span data-term="correlation-length">关联长度</span> $\\xi$ 常被取作 $\\gamma$ 的衰减长度，但不同模型对 $\\xi$ 的定义差一个数值因子。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="two-phase-model">两相模型</span></li>
        <li><span data-term="porod-law">Porod 定律</span></li>
        <li><span data-term="porod-invariant">Porod 不变量</span></li>
        <li><span data-term="pair-distance-distribution">$p(r)$</span></li>
        <li><span data-term="interfacial-thickness">界面厚度</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/shape-independent/dab.html">Debye–Anderson–Brumberger</a></li>
        <li><a href="../models/shape-independent/porod.html">Porod</a></li>
        <li><a href="../learn/07-real-space-ift.html">学习路径 07 · IFT</a></li>
      </ul>
""",
)

add(
    "babinet-principle",
    titleZh="巴比涅原理",
    titleEn="Babinet's principle",
    abbr="",
    tip="均匀粒子与「同等形状的孔」只差衬度符号；强度 |Δρ|² 相同。SAS 只看见衬度差，分不清物质与空洞。",
    aliases=["Babinet", "巴比涅", "互补原理"],
    appearsIn=[
        "learn/02-scattering-basics.html",
        "glossary/contrast.html",
        "glossary/scattering-amplitude.html",
        "models/sphere/vesicle.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>巴比涅原理</strong>（光学互补原理在 SAS 中的版本）：把 $\\Delta\\rho\\to -\\Delta\\rho$ 只改变 <span data-term="scattering-amplitude">振幅</span>的符号，强度 $\\lvert F\\rvert^2$ 不变。因此「溶剂中的均匀颗粒」与「同样形状的孔洞（颗粒 SLD 换成溶剂、孔内为原颗粒）」给出相同 $I(q)$。</p>
      <p>更一般地，整体加上常数密度不改变 $q\\neq 0$ 的散射。实验只对衬度差敏感。</p>

      <h2>物理直觉</h2>
      <p>这就是为什么空洞、气泡、多孔材料可以用与实心颗粒相同的形式因子来拟合——只是把 $\\Delta\\rho$ 理解成孔相对基体的差。核壳、囊泡没有整体变号那么简单：内部还有第二段衬度，正负壳层会在极小位置上表现出来，不能只靠巴比涅把核壳说成「实心球」。 </p>

      <h2>常见混淆</h2>
      <ul>
        <li>巴比涅不意味着「正衬度与负衬度的核壳曲线一样」：分层剖面变号后，$F(q)$ 的零点一般会动。</li>
        <li>吸收、多重散射、磁散射通道不满足这条简单互补。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="contrast">衬度</span></li>
        <li><span data-term="scattering-amplitude">散射振幅</span></li>
        <li><span data-term="form-factor">形式因子</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/02-scattering-basics.html">学习路径 02 · 散射基础</a></li>
        <li><a href="../models/sphere/vesicle.html">囊泡</a></li>
      </ul>
""",
)

add(
    "kuhn-length",
    titleZh="Kuhn 长度",
    titleEn="Kuhn length",
    abbr="b",
    tip="把半柔顺链改写成等效自由连接链时的链段长度；与持续长度通常差一个因子 2。",
    aliases=["b", "Kuhn", "库恩长度"],
    appearsIn=[
        "glossary/persistence-length.html",
        "glossary/wormlike-chain.html",
        "models/cylinder/flexible-cylinder.html",
        "models/shape-independent/polymer-excl-volume.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>Kuhn 长度</strong> $b$ 是把蠕虫状链（Kratky–Porod）映射为等效自由连接链时的链段长。轮廓长度 $L$、段数 $N=L/b$。对理想蠕虫链，Kuhn 长度与<span data-term="persistence-length">持续长度</span> $\\ell_p$ 的关系是 $b=2\\ell_p$。</p>
      <p>散射上：$q\\ll 1/R_g$ 看整链回转半径；$1/R_g\\ll q\\ll 1/b$ 是高斯或排除体积链的 Debye 区；$q\\gtrsim 1/b$ 看到局部棒状（$I\\sim q^{-1}$）。</p>

      <h2>物理直觉</h2>
      <p>$\\ell_p$ 描述切向关联 $e^{-s/\\ell_p}$ 的衰减；$b$ 是「从多远开始可以当成独立链段」的同一物理的另一种尺子。读文献时先看作者用的是 $b$ 还是 $\\ell_p$，不要混用数值。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>$b$ 不是化学单体长度：一个 Kuhn 段通常含许多单体。</li>
        <li>排除体积链的 $R_g$ 标度是 $N^{\\nu}$（$\\nu\\approx 0.588$），理想链才是 $N^{1/2}$；Kuhn 定义本身不自动包含排除体积。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="persistence-length">持续长度</span></li>
        <li><span data-term="wormlike-chain">蠕虫状链</span></li>
        <li><span data-term="debye-function">Debye 函数</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/cylinder/flexible-cylinder.html">柔性圆柱</a></li>
        <li><a href="../models/shape-independent/mono-gauss-coil.html">单分散高斯链</a></li>
      </ul>
""",
)

add(
    "debye-function",
    titleZh="Debye 函数",
    titleEn="Debye function",
    abbr="D(x)",
    tip="理想高斯链（无规线团）的形式因子。中间 q 呈 q⁻²，是聚合物稀溶液的默认曲线。",
    aliases=["Debye", "高斯链", "无规线团"],
    appearsIn=[
        "models/shape-independent/mono-gauss-coil.html",
        "models/shape-independent/poly-gauss-coil.html",
        "models/shape-independent/star-polymer.html",
        "learn/08-models-polydispersity.html",
    ],
    body="""
      <h2>定义</h2>
      <p>理想高斯链的<span data-term="form-factor">形式因子</span>是 <strong>Debye 函数</strong>。令 $x=q^2 R_g^2$，</p>
      $$P(q)=D(x)=\\frac{2}{x^2}\\bigl(e^{-x}-1+x\\bigr).$$
      <p>$q\\to 0$ 时 $D=1-x/3+\\cdots$，回到 Guinier（链的 $R_g^2=Nb^2/6$）。$x\\gg 1$ 时 $D\\sim 2/x\\propto q^{-2}$，即无规线团的 Kratky 坪 $q^2 I(q)\\to$ 常数。</p>
      <p>推导：把链写成 $N$ 个高斯弹簧，对所有单体对 $e^{-q^2\\langle r_{ij}^2\\rangle/6}$ 求和，连续极限就是上式。排除体积链要用其他闭式（如聚合物排除体积模型），不能硬套 Debye。</p>

      <h2>物理直觉</h2>
      <p>高斯链没有明确外表面，所以没有球那样的振荡极小，也没有 Porod $q^{-4}$。高 $q$ 若看到 $q^{-1}$，说明已经分辨到局部棒状，应改用<span data-term="wormlike-chain">蠕虫状链</span>。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>Debye 相关函数 $\\gamma(r)$（两相介质）与 Debye 链形式因子同名不同物。</li>
        <li>多分散链要把 $D(x)$ 对分子量分布平均，不能只用一个 $R_g$ 的 Debye 去拟合宽分布。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="kuhn-length">Kuhn 长度</span></li>
        <li><span data-term="wormlike-chain">蠕虫状链</span></li>
        <li><span data-term="kratky-plot">Kratky 图</span></li>
        <li><span data-term="correlation-function">相关函数</span> $\\gamma(r)$（易混）</li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/shape-independent/mono-gauss-coil.html">单分散高斯链</a></li>
        <li><a href="../models/shape-independent/poly-gauss-coil.html">多分散高斯链</a></li>
      </ul>
""",
)

add(
    "wormlike-chain",
    titleZh="蠕虫状链",
    titleEn="wormlike chain",
    abbr="WLC",
    tip="Kratky–Porod 半柔顺链：持续长度介于刚性棒与高斯线团之间。柔性圆柱模型用它做骨架。",
    aliases=["WLC", "Kratky-Porod", "半柔顺链", "蠕虫链"],
    appearsIn=[
        "models/cylinder/flexible-cylinder.html",
        "models/cylinder/flexible-cylinder-elliptical.html",
        "glossary/persistence-length.html",
        "glossary/kuhn-length.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>蠕虫状链</strong>（wormlike chain, Kratky–Porod）用轮廓长度 $L$ 与<span data-term="persistence-length">持续长度</span> $\\ell_p$ 描述半柔顺聚合物或纤维。切向关联 $\\langle \\mathbf{u}(0)\\cdot\\mathbf{u}(s)\\rangle=e^{-s/\\ell_p}$。极限：$L\\ll \\ell_p$ 像刚性棒；$L\\gg \\ell_p$ 像高斯线团，等效 <span data-term="kuhn-length">Kuhn 长度</span> $b=2\\ell_p$。</p>
      <p>散射还要乘上有限截面（圆或椭圆）的形状因子。模型手册中的柔性圆柱，就是把蠕虫骨架的 $P_{\\mathrm{chain}}(q)$ 与圆柱截面因子组合。</p>

      <h2>物理直觉</h2>
      <p>$\log I$–$\\log q$ 上常出现三段：低 $q$ Guinier（整链 $R_g$）→ 中间 $q^{-2}$（无规线团）或直接 $q^{-1}$（更刚）→ 高 $q$ 截面振荡 / Porod。持续长度大致落在 $q^{-2}$ 转到 $q^{-1}$ 的交叉附近。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>蠕虫链的 $R_g$ 不是 $L/\\sqrt{12}$（那是刚性细棒）；有插值公式，依赖 $L/\\ell_p$。</li>
        <li>排除体积（良溶剂溶胀）会改变中间区指数，单纯 Kratky–Porod 是无排除体积的。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="persistence-length">持续长度</span></li>
        <li><span data-term="kuhn-length">Kuhn 长度</span></li>
        <li><span data-term="debye-function">Debye 函数</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/cylinder/flexible-cylinder.html">柔性圆柱</a></li>
        <li><a href="../topics/polymers-bcp/index.html">专题 · 聚合物与嵌段共聚物</a></li>
      </ul>
""",
)

add(
    "caille",
    titleZh="Caillé 理论",
    titleEn="Caillé theory",
    abbr="",
    tip="层状相中层法向热起伏破坏长程 Bragg 阶：峰变幂律翼，用无量纲 η 描述柔性。",
    aliases=["Caille", "Caillé", "Caille 参数"],
    appearsIn=[
        "models/lamellae/lamellar-stack-caille.html",
        "models/lamellae/lamellar-hg-stack-caille.html",
        "models/lamellae/index.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>Caillé 理论</strong>描述溶胀层状相（脂质体多层、表面活性剂 $L_\\alpha$）中，层法向位移 $u_n$ 的热起伏。层不再是理想晶体，Bragg 峰失去 $\\delta$ 函数，变成幂律奇点，翼部 $I\\propto \\lvert q-q_m\\rvert^{-1+\\eta_m}$。无量纲 Caillé 参数 $\\eta$ 由弯曲模量 $K$ 与压缩模量 $\\bar{B}$ 决定：$\\eta$ 越大，层越软、高阶峰衰减越快。</p>
      <p>粉末样品还要乘层状 <span data-term="lorentz-factor">Lorentz 因子</span>，并乘双层本身的 <span data-term="form-factor">形式因子</span> $\\lvert F_{\\mathrm{bilayer}}(q)\\rvert^2$。</p>

      <h2>物理直觉</h2>
      <p>二维层状相在热涨落下没有真正的三维长程序（Peierls–Landau），但有代数衰减的准长程序——这就是「峰有幂律翅膀」而不是高斯宽化。准晶（Hosemann）用的是静态位移无序，物理不同，不要把 $\\eta$ 与准晶 $g$ 因子混用。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>Caillé $\\eta$ 不是多分散：尺寸分布也会压高阶峰，但峰形不是幂律翼。</li>
        <li>单层囊泡没有层间堆叠，不必上 Caillé；那是单层形式因子问题。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="paracrystal">准晶</span>（另一类峰宽化）</li>
        <li><span data-term="lorentz-factor">Lorentz 因子</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/lamellae/lamellar-stack-caille.html">层状堆叠（Caillé）</a></li>
        <li><a href="../models/lamellae/lamellar-hg-stack-caille.html">头基–层状堆叠（Caillé）</a></li>
      </ul>
""",
)

add(
    "paracrystal",
    titleZh="准晶",
    titleEn="paracrystal",
    abbr="",
    tip="Hosemann 准晶：点阵间距有累积无序，Bragg 峰随阶数变宽、高阶消失。用于层堆与胶体晶体。",
    aliases=["Hosemann", "准晶体", "次晶"],
    appearsIn=[
        "models/paracrystal/index.html",
        "models/lamellae/lamellar-stack-paracrystal.html",
        "models/paracrystal/fcc-paracrystal.html",
        "glossary/caille.html",
    ],
    body="""
      <h2>定义</h2>
      <p>Hosemann <strong>准晶</strong>（paracrystal）让相邻点阵间距成为随机变量：误差沿晶列累积，第 $m$ 阶反射的宽度 $\\propto m^2$。高阶峰迅速消失，只剩低阶宽峰。一维层堆、以及 SC / BCC / FCC 胶体晶体都可以写成准晶格子乘单粒子 <span data-term="form-factor">形式因子</span>。</p>
      <p>无序程度常用无量纲 $g=\\sigma_d/\\bar{d}$（间距相对标准偏差）。$g\\to 0$ 回到理想晶体；$g$ 过大则只剩液体样相关峰。</p>

      <h2>物理直觉</h2>
      <p>与热起伏的 <span data-term="caille">Caillé</span> 不同：准晶是静态几何无序（堆积缺陷、多分散占位），峰形接近变宽的 Bragg，而不是膜柔性的幂律翼。选哪一种要看样品：柔软溶胀膜 → Caillé；固体胶体晶体、硬层堆 → 准晶更常见。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>名称里的「准」不是准晶材料（quasicrystal，五次对称）。这里是 paracrystal。</li>
        <li>液体 <span data-term="structure-factor">$S(q)$</span>（PY / MSA）没有点阵；准晶假定仍有可编号的格点。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="caille">Caillé 理论</span></li>
        <li><span data-term="structure-factor">结构因子</span></li>
        <li><span data-term="polydispersity">多分散</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/paracrystal/index.html">准晶分类</a></li>
        <li><a href="../models/lamellae/lamellar-stack-paracrystal.html">层状准晶堆叠</a></li>
      </ul>
""",
)

add(
    "lorentz-factor",
    titleZh="Lorentz 因子",
    titleEn="Lorentz factor",
    abbr="",
    tip="粉末层状（或纤维）取向平均时，倒易空间环的几何权重，常给出额外的 1/q²。不是 Lorentzian 峰形。",
    aliases=["Lorentz correction", "洛伦兹因子", "Lorentz 校正"],
    appearsIn=[
        "models/lamellae/lamellar.html",
        "models/lamellae/lamellar-stack-caille.html",
        "glossary/powder-average.html",
        "glossary/caille.html",
    ],
    body="""
      <h2>定义</h2>
      <p>粉末样品中，层法向均匀分布在球面上。无限片的散射集中在倒易空间的法向尖刺上，取向平均后还要乘几何权重——即层状 <strong>Lorentz 因子</strong>，理想无限片常给出 $\\propto 1/q^2$。观测强度是</p>
      $$I(q)\\propto \\frac{\\lvert F_{\\mathrm{bilayer}}(q)\\rvert^2}{q^2}\\,S_{\\mathrm{inter}}(q).$$
      <p>有限横向尺寸会把 $1/q^2$ 截断或改成其他幂。纤维取向有另一套 Lorentz 校正。</p>

      <h2>物理直觉</h2>
      <p>这是<span data-term="powder-average">粉末平均</span>在「散射集中在低维倒易流形」时的特例：不是把 $|F|^2$ 在球面上均匀抹开，而是尖刺扫过 Ewald 球的时间（或立体角）不同，低 $q$ 权更大。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>Lorentz <em>因子</em> ≠ Lorentzian <em>峰形</em>（后者是 $1/(1+q^2\\xi^2)$ 那样的相关峰）。</li>
        <li>对溶液中的有限颗粒不要额外除 $q^2$；那一步只属于层状/纤维粉末几何。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="powder-average">粉末平均</span></li>
        <li><span data-term="form-factor">形式因子</span></li>
        <li><span data-term="caille">Caillé 理论</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/lamellae/lamellar.html">层状</a></li>
        <li><a href="../models/lamellae/index.html">层状分类</a></li>
      </ul>
""",
)

add(
    "interfacial-thickness",
    titleZh="界面厚度",
    titleEn="interfacial thickness",
    abbr="σ",
    tip="两相之间密度过渡层的宽度。模糊界面使高 q 比理想 Porod q⁻⁴ 衰减更快，常乘 e^{−q²σ²}。",
    aliases=["界面宽度", "模糊度", "扩散界面", "σ"],
    appearsIn=[
        "models/sphere/fuzzy-sphere.html",
        "models/shape-independent/porod.html",
        "glossary/porod-law.html",
        "glossary/correlation-function.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>界面厚度</strong>描述 $\\Delta\\rho$ 从一相变到另一相所跨越的距离。理想两相是阶跃，<span data-term="porod-law">Porod</span> 为 $q^{-4}$。有限厚度（误差函数、tanh、高斯卷积）使 <span data-term="correlation-function">$\\gamma(r)$</span> 的小 $r$ 展开改变，高强度区多乘一个衰减因子。常见约定：振幅乘 $e^{-q^2\\sigma^2/2}$，强度乘 $e^{-q^2\\sigma^2}$（Debye–Waller 式界面因子）。</p>

      <h2>物理直觉</h2>
      <p>$\\sigma$ 越大，越看不清锐利边界，高 $q$ 振荡被抹掉。低 $q$ / Guinier 几乎不动，因为整体尺寸仍由外轮廓决定。核壳若壳厚与 $\\sigma$ 同量级，二者高度相关，需要对比变分或固定其一。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>界面厚度 ≠ <span data-term="polydispersity">尺寸多分散</span>：多分散改变极小位置的叠加；界面因子主要压高 $q$ 振幅。</li>
        <li>仪器 <span data-term="instrument-smearing">smearing</span> 也会钝化振荡，须用分辨率函数区分。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="porod-law">Porod 定律</span></li>
        <li><span data-term="two-phase-model">两相模型</span></li>
        <li><span data-term="polydispersity">多分散</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/sphere/fuzzy-sphere.html">模糊球</a></li>
        <li><a href="../models/shape-independent/porod.html">Porod</a></li>
      </ul>
""",
)

add(
    "two-phase-model",
    titleZh="两相模型",
    titleEn="two-phase model",
    abbr="",
    tip="样品由两种近似均匀的 SLD 组成，中间是界面。Porod、不变量、DAB 都建立在这一图像上。",
    aliases=["两相介质", "Debye 两相", "多孔两相"],
    appearsIn=[
        "glossary/porod-law.html",
        "glossary/porod-invariant.html",
        "glossary/correlation-function.html",
        "models/shape-independent/dab.html",
        "models/shape-independent/porod.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>两相模型</strong>假定样品体积由相 1、相 2 填满，各相内部 $\\rho$ 近似常数，差别集中在界面。体积分数 $\\phi$、衬度 $\\Delta\\rho=\\rho_1-\\rho_2$。此时 <span data-term="porod-invariant">Porod 不变量</span></p>
      $$Q=\\int_0^\\infty q^2 I(q)\\,\\mathrm{d}q \\propto \\phi(1-\\phi)(\\Delta\\rho)^2,$$
      <p>高 $q$ 的 $q^4 I(q)$ 给出比表面积（Porod）。相关函数常取 $\\gamma(r)=e^{-r/\\xi}$，即 Debye–Anderson–Brumberger（DAB）形式。</p>

      <h2>物理直觉</h2>
      <p>多孔固体、相分离聚合物、浓乳液在「只关心界面与体积分数、不关心单个粒子外形」时，用两相语言比用球/柱形式因子更直接。一旦有第三相或连续密度梯度，不变量与 Porod 常数的解释就要改。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>稀释颗粒在溶剂中也是两相，但通常改用单粒子 $F(q)$，把溶剂当均匀本底。</li>
        <li>$\\phi(1-\\phi)$ 在 $\\phi=1/2$ 最大：不是「浓度越高信号越强」。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="correlation-function">相关函数</span> $\\gamma(r)$</li>
        <li><span data-term="porod-law">Porod 定律</span></li>
        <li><span data-term="porod-invariant">Porod 不变量</span></li>
        <li><span data-term="volume-fraction">体积分数</span></li>
        <li><span data-term="babinet-principle">巴比涅原理</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../models/shape-independent/dab.html">DAB</a></li>
        <li><a href="../models/shape-independent/porod.html">Porod</a></li>
        <li><a href="../learn/06-guinier-porod.html">学习路径 06 · Guinier / Porod</a></li>
      </ul>
""",
)

add(
    "schultz-zimm",
    titleZh="Schulz–Zimm 分布",
    titleEn="Schulz–Zimm distribution",
    abbr="",
    tip="胶体和聚合物常用的尺寸（或分子量）分布；相对宽度 σ/⟨R⟩ 会抹平形式因子振荡。",
    aliases=["Schulz", "Zimm", "Schulz-Zimm", "伽马分布"],
    appearsIn=[
        "glossary/polydispersity.html",
        "learn/08-models-polydispersity.html",
        "models/sphere/sphere.html",
        "models/shape-independent/poly-gauss-coil.html",
    ],
    body="""
      <h2>定义</h2>
      <p><strong>Schulz–Zimm 分布</strong>是伽马型的尺寸或分子量分布，由均值 $\\langle R\\rangle$ 与相对宽度 $p=\\sigma_R/\\langle R\\rangle$（或 Zimm 参数 $z=1/p^2-1$）刻画。对球等形式因子，观测曲线是</p>
      $$I(q)=n\\int_0^\\infty f(R)\\,\\lvert F(q;R)\\rvert^2\\,\\mathrm{d}R+B.$$
      <p>权重 $f(R)$ 必须声明是数均、体积加权还是强度（$z$）加权：Guinier 得到的 $R_g$ 偏大端。</p>
      <p>对数正态是另一常见选择；双峰混合物不是单峰 Schulz 能代替的。</p>

      <h2>物理直觉</h2>
      <p>$p\\gtrsim 10\\%$ 时均匀球的第一极小就会显著变钝。这常被误判为「不是球」或「界面很糊」。先试分布，再改形状。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>Schulz 分布的 $z$ 与 Zimm 图、Zimm 方程不是同一个 $z$。</li>
        <li>仪器模糊与多分散都会抹振荡，见 <span data-term="instrument-smearing">smearing</span>。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="polydispersity">多分散</span></li>
        <li><span data-term="form-factor">形式因子</span></li>
        <li><span data-term="radius-of-gyration">回转半径</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/08-models-polydispersity.html">学习路径 08 · 模型与多分散</a></li>
        <li><a href="../models/sphere/sphere.html">均匀球</a></li>
      </ul>
""",
)

add(
    "differential-cross-section",
    titleZh="微分散射截面",
    titleEn="differential scattering cross-section",
    abbr="dΣ/dΩ",
    tip="绝对强度的物理含义：单位体积、单位立体角的散射概率。标定后的 I(q) 常用 cm⁻¹。",
    aliases=["dΣ/dΩ", "微分散面", "绝对截面"],
    appearsIn=[
        "glossary/absolute-intensity.html",
        "learn/05-absolute-calibration.html",
        "topics/calibration/index.html",
        "learn/02-scattering-basics.html",
    ],
    body="""
      <h2>定义</h2>
      <p>宏观 <strong>微分散射截面</strong> $\\mathrm{d}\\Sigma/\\mathrm{d}\\Omega$ 是：样品单位体积、向单位立体角散射的概率，单位 $\\mathrm{cm}^{-1}$（有时对每个粒子用 $\\mathrm{d}\\sigma/\\mathrm{d}\\Omega$，单位 $\\mathrm{cm}^2$）。<span data-term="absolute-intensity">绝对强度</span>标定就是把探测器计数换成这个量。稀释相干部分</p>
      $$\\frac{\\mathrm{d}\\Sigma}{\\mathrm{d}\\Omega}=n\\,\\lvert F(q)\\rvert^2.$$
      <p>文献里的 $I(q)$ 若已绝对标定，通常指 $\\mathrm{d}\\Sigma/\\mathrm{d}\\Omega$。</p>

      <h2>物理直觉</h2>
      <p>相对单位只比较形状；要谈体积分数、分子量、比表面积，必须把 $I$ 放到截面尺度，并与 <span data-term="contrast">$\\Delta\\rho$</span> 的单位一致（SAXS 电子密度 vs SANS 的 $\\mathrm{cm}^{-2}$）。</p>

      <h2>常见混淆</h2>
      <ul>
        <li>$\\mathrm{d}\\sigma/\\mathrm{d}\\Omega$（每粒子）与 $\\mathrm{d}\\Sigma/\\mathrm{d}\\Omega$（单位体积）差一个 $n$。</li>
        <li>「归一化到入射束监视器」还不是绝对截面，还缺厚度、透射、立体角、探测器效率。</li>
      </ul>

      <h2>相关词条</h2>
      <ul>
        <li><span data-term="absolute-intensity">绝对强度</span></li>
        <li><span data-term="number-density">数密度</span></li>
        <li><span data-term="scattering-amplitude">散射振幅</span></li>
        <li><span data-term="forward-scattering">前向散射</span></li>
      </ul>

      <h2>出现于</h2>
      <ul>
        <li><a href="../learn/05-absolute-calibration.html">学习路径 05 · 绝对标定</a></li>
        <li><a href="../topics/calibration/index.html">专题 · 绝对标定</a></li>
      </ul>
""",
)


def write_pages():
    gdir = ROOT / "glossary"
    for tid, t in TERMS.items():
        html = page(t["titleZh"], t["titleEn"], t["body"].strip("\n"))
        (gdir / f"{tid}.html").write_text(html, encoding="utf-8", newline="\n")
        print("wrote", tid)


def meta_dict(t):
    return {
        "id": t["id"],
        "titleZh": t["titleZh"],
        "titleEn": t["titleEn"],
        "abbr": t["abbr"],
        "tip": t["tip"],
        "aliases": t["aliases"],
        "appearsIn": t["appearsIn"],
    }


def update_glossary_data():
    path = ROOT / "assets" / "glossary-data.js"
    text = path.read_text(encoding="utf-8")
    new = {k: meta_dict(v) for k, v in TERMS.items()}
    blob = json.dumps(new, ensure_ascii=False, indent=2)
    inner = blob[1:-1].rstrip()
    text = text.rstrip()
    if not text.endswith("};"):
        raise SystemExit("glossary-data.js: unexpected ending")
    # avoid duplicating if re-run
    for k in TERMS:
        if f'"{k}":' in text:
            print("skip existing key in js", k)
            new.pop(k, None)
    if not new:
        print("glossary-data.js already has all keys")
        return
    blob = json.dumps(new, ensure_ascii=False, indent=2)
    inner = blob[1:-1].rstrip()
    text = text[:-2].rstrip()
    if not text.endswith("}"):
        raise SystemExit("bad splice point")
    text = text + ",\n" + inner + "\n};\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    print("updated glossary-data.js", len(new), "keys")

    jpath = ROOT / "assets" / "glossary.json"
    if jpath.exists():
        data = json.loads(jpath.read_text(encoding="utf-8"))
        for k, t in TERMS.items():
            data[k] = meta_dict(t)
        jpath.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print("updated glossary.json")


def search_entry(t):
    body = re.sub(r"<[^>]+>", " ", t["body"])
    body = re.sub(r"\s+", " ", body).strip()
    return {
        "id": f"glossary/{t['id']}",
        "title": t["titleZh"],
        "url": f"glossary/{t['id']}.html",
        "section": "术语表",
        "headings": ["定义", "物理直觉", "相关词条", "出现于"],
        "text": f"{t['titleZh']} {t['titleEn']} {t['tip']} {body}"[:1200],
    }


def update_search_index():
    path = ROOT / "data" / "search-index.js"
    raw = path.read_text(encoding="utf-8")
    prefix = "window.SAS_SEARCH_INDEX = "
    if not raw.startswith(prefix):
        raise SystemExit("search-index prefix mismatch")
    data = json.loads(raw[len(prefix) :].rstrip().rstrip(";"))
    existing = {e.get("id") for e in data}
    added = 0
    for t in TERMS.values():
        eid = f"glossary/{t['id']}"
        if eid in existing:
            continue
        data.append(search_entry(t))
        added += 1
    out = prefix + json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    path.write_text(out, encoding="utf-8", newline="\n")
    print("search-index added", added, "total", len(data))


WRAP = [
    ("Percus–Yevick", "percus-yevick"),
    ("Percus-Yevick", "percus-yevick"),
    ("Ornstein–Zernike", "ornstein-zernike"),
    ("Ornstein-Zernike", "ornstein-zernike"),
    ("平均球近似", "mean-spherical-approximation"),
    ("微分散射截面", "differential-cross-section"),
    ("散射长度密度", "scattering-length-density"),
    ("间接傅里叶变换", "indirect-fourier-transform"),
    ("回转半径", "radius-of-gyration"),
    ("前向散射", "forward-scattering"),
    ("结构因子", "structure-factor"),
    ("形式因子", "form-factor"),
    ("散射振幅", "scattering-amplitude"),
    ("粉末平均", "powder-average"),
    ("取向平均", "powder-average"),
    ("玻恩近似", "born-approximation"),
    ("Born 近似", "born-approximation"),
    ("数密度", "number-density"),
    ("体积分数", "volume-fraction"),
    ("对关联", "pair-correlation"),
    ("巴比涅", "babinet-principle"),
    ("Kuhn 长度", "kuhn-length"),
    ("Debye 函数", "debye-function"),
    ("蠕虫状链", "wormlike-chain"),
    ("持续长度", "persistence-length"),
    ("Caillé", "caille"),
    ("Lorentz 因子", "lorentz-factor"),
    ("界面厚度", "interfacial-thickness"),
    ("两相模型", "two-phase-model"),
    ("Schulz–Zimm", "schultz-zimm"),
    ("Schulz-Zimm", "schultz-zimm"),
    ("多分散", "polydispersity"),
    ("相关函数", "correlation-function"),
    ("准晶", "paracrystal"),
]


def wrap_first_in_main(html: str, needle: str, term_id: str) -> str:
    start = html.find("<main")
    end = html.find("</main>")
    if start < 0 or end < 0:
        return html
    main = html[start:end]
    if f'data-term="{term_id}"' in main:
        return html
    idx = 0
    while True:
        i = main.find(needle, idx)
        if i < 0:
            return html
        lt = main.rfind("<", 0, i)
        gt = main.rfind(">", 0, i)
        if lt > gt:
            idx = i + len(needle)
            continue
        before = main[:i]
        open_h = max(before.rfind("<h1"), before.rfind("<h2"), before.rfind("<h3"), before.rfind("<h4"))
        close_h = max(before.rfind("</h1>"), before.rfind("</h2>"), before.rfind("</h3>"), before.rfind("</h4>"))
        if open_h > close_h:
            idx = i + len(needle)
            continue
        last_close = max(before.rfind("</span>"), before.rfind("</a>"))
        open_span = before.rfind("<span")
        open_a = before.rfind("<a ")
        open_tag = max(open_span, open_a)
        if open_tag > last_close and "data-term=" in main[open_tag:i]:
            idx = i + len(needle)
            continue
        wrapped = f'<span data-term="{term_id}">{needle}</span>'
        new_main = main[:i] + wrapped + main[i + len(needle) :]
        return html[:start] + new_main + html[end:]


def wrap_tree(rel: str):
    n = 0
    for path in (ROOT / rel).rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        orig = html
        for needle, tid in WRAP:
            html = wrap_first_in_main(html, needle, tid)
        if html != orig:
            path.write_text(html, encoding="utf-8", newline="\n")
            n += 1
    print("wrapped files in", rel, n)


def main():
    write_pages()
    update_glossary_data()
    update_search_index()
    wrap_tree("models")
    wrap_tree("learn")
    wrap_tree("topics")
    wrap_tree("glossary")


if __name__ == "__main__":
    main()
