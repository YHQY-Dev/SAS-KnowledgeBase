# -*- coding: utf-8 -*-
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def unwrap_self_links() -> int:
    n = 0
    for p in (ROOT / "glossary").glob("*.html"):
        if p.stem == "index":
            continue
        tid = p.stem
        t = p.read_text(encoding="utf-8")
        # only unwrap inside definition-like <strong>...</strong> that self-links
        pat = re.compile(
            rf'(<strong[^>]*>)\s*<span data-term="{re.escape(tid)}">(.*?)</span>',
            re.S,
        )
        nt, c = pat.subn(r"\1\2", t)
        # also: <strong>Hosemann <span ...>准晶</span>
        pat2 = re.compile(
            rf'(<strong[^>]*>[^<]*)<span data-term="{re.escape(tid)}">(.*?)</span>',
            re.S,
        )
        nt2, c2 = pat2.subn(r"\1\2", nt)
        # broken: 多分散</span>性
        nt2 = nt2.replace(f'</span>性</strong>', "性</strong>")
        # babinet: 巴比涅</span>原理
        nt2 = re.sub(
            rf'<strong><span data-term="{re.escape(tid)}">([^<]*)</span>([^<]*)</strong>',
            r"<strong>\1\2</strong>",
            nt2,
        )
        if nt2 != t:
            p.write_text(nt2, encoding="utf-8", newline="\n")
            n += 1
            print("unself", p.name, c + c2)
    return n


def wrap_models() -> int:
    replacements = [
        (
            "相干振幅是衬度对平面波相位的体积分",
            '相干<span data-term="scattering-amplitude">散射振幅</span>是<span data-term="contrast">衬度</span>对平面波相位的体积分',
        ),
        (
            "相干振幅仍是衬度的傅里叶变换",
            '相干<span data-term="scattering-amplitude">散射振幅</span>仍是<span data-term="contrast">衬度</span>的傅里叶变换',
        ),
        (
            "相干振幅是衬度对平面波相位的体积分",
            '相干<span data-term="scattering-amplitude">散射振幅</span>是<span data-term="contrast">衬度</span>对平面波相位的体积分',
        ),
        (
            "球对称下散射振幅是径向衬度的正弦变换",
            '球对称下<span data-term="scattering-amplitude">散射振幅</span>是径向<span data-term="contrast">衬度</span>的正弦变换',
        ),
        (
            "均匀超球的振幅仍是衬度对平面波相位的体积分",
            '均匀超球的<span data-term="scattering-amplitude">散射振幅</span>仍是<span data-term="contrast">衬度</span>对平面波相位的体积分',
        ),
        (
            "多层囊泡是溶剂与膜沿半径交替的球对称剖面。相干振幅",
            '多层囊泡是溶剂与膜沿半径交替的球对称剖面。相干<span data-term="scattering-amplitude">散射振幅</span>',
        ),
        (
            "稀释球对称粒子的振幅是径向衬度的正弦变换",
            '稀释球对称粒子的<span data-term="scattering-amplitude">散射振幅</span>是径向<span data-term="contrast">衬度</span>的正弦变换',
        ),
        (
            "均匀核加高斯模糊界面，等价于硬球密度与三维高斯的卷积。稀释振幅仍从傅里叶变换出发",
            '均匀核加高斯模糊界面，等价于硬球密度与三维高斯的卷积。稀释<span data-term="scattering-amplitude">散射振幅</span>仍从傅里叶变换出发',
        ),
        (
            "由 Ornstein–Zernike（OZ）方程联系",
            '由 <span data-term="ornstein-zernike">Ornstein–Zernike（OZ）</span> 方程联系',
        ),
        (
            "OZ 与结构因子",
            'OZ 与<span data-term="structure-factor">结构因子</span>',
        ),
        (
            "OZ 方程与结构因子",
            '<span data-term="ornstein-zernike">OZ</span> 方程与<span data-term="structure-factor">结构因子</span>',
        ),
        (
            "Percus–Yevick（PY）闭包",
            '<span data-term="percus-yevick">Percus–Yevick（PY）</span> 闭包',
        ),
        (
            "平均球近似（MSA）",
            '<span data-term="mean-spherical-approximation">平均球近似（MSA）</span>',
        ),
    ]
    n = 0
    for p in (ROOT / "models").rglob("*.html"):
        t = p.read_text(encoding="utf-8")
        orig = t
        for old, new in replacements:
            if old in t and f'data-term="' not in old:
                # only replace if target term not already present for that phrase context
                if new.split("data-term=")[1].split('"')[1] not in t or old in t:
                    # avoid double wrap: if old already partially wrapped skip
                    if "<span data-term=" in old:
                        continue
                    # if the distinctive unwrapped text still exists
                    if old in t:
                        t = t.replace(old, new, 1)
        if t != orig:
            p.write_text(t, encoding="utf-8", newline="\n")
            n += 1
            print("wrap", p.relative_to(ROOT))
    return n


def wrap_oz_structure_pages() -> None:
    for p in (ROOT / "models" / "structure-factor").glob("*.html"):
        if p.name == "index.html":
            continue
        t = p.read_text(encoding="utf-8")
        orig = t
        if 'data-term="ornstein-zernike"' not in t and "Ornstein–Zernike" in t:
            t = t.replace(
                "Ornstein–Zernike",
                '<span data-term="ornstein-zernike">Ornstein–Zernike</span>',
                1,
            )
        if 'data-term="ornstein-zernike"' not in t and "OZ" in t and "<h3>出发点</h3>" in t:
            t = t.replace(
                "OZ 与",
                '<span data-term="ornstein-zernike">OZ</span> 与',
                1,
            )
            t = t.replace(
                "OZ 方程",
                '<span data-term="ornstein-zernike">OZ</span> 方程',
                1,
            )
        if t != orig:
            p.write_text(t, encoding="utf-8", newline="\n")
            print("oz", p.name)


def main() -> None:
    print("unself", unwrap_self_links())
    print("wrap models", wrap_models())
    wrap_oz_structure_pages()


if __name__ == "__main__":
    main()
