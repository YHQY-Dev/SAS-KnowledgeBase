# -*- coding: utf-8 -*-
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SUBS = {
    "glossary/caille.html": "Caillé theory",
    "glossary/ornstein-zernike.html": "Ornstein–Zernike equation",
    "glossary/percus-yevick.html": "Percus–Yevick closure",
    "glossary/schultz-zimm.html": "Schulz–Zimm distribution",
}

ANCHOR = re.compile(r'(<a href="([^"]+)"[^>]*>)(.*?)(</a>)', re.S)
SPAN = re.compile(r'<span data-term="[^"]+">(.*?)</span>')


def unwrap_in_anchors(html: str) -> str:
    def repl(m):
        href, inner = m.group(2), m.group(3)
        if "glossary/" in href:
            return m.group(0)
        inner = SPAN.sub(r"\1", inner)
        return m.group(1) + inner + m.group(4)

    return ANCHOR.sub(repl, html)


def main() -> None:
    for rel, en in SUBS.items():
        p = ROOT / rel
        t = p.read_text(encoding="utf-8")
        t = re.sub(r'<p class="subtitle-en">.*?</p>', f'<p class="subtitle-en">{en}</p>', t, count=1)
        p.write_text(t, encoding="utf-8", newline="\n")
        print("subtitle", rel)

    n = 0
    needle = '模型与<span data-term="polydispersity">多分散</span>'
    for p in (ROOT / "glossary").glob("*.html"):
        t = p.read_text(encoding="utf-8")
        if needle in t:
            t = t.replace(needle, "模型与多分散")
            p.write_text(t, encoding="utf-8", newline="\n")
            n += 1
            print("unwrapped 08", p.name)
    print("08 unwrap files", n)

    old = "相干散射振幅是衬度对平面波相位的体积分"
    new = (
        "相干<span data-term=\"scattering-amplitude\">散射振幅</span>"
        "是<span data-term=\"contrast\">衬度</span>对平面波相位的体积分"
    )
    n2 = 0
    for p in (ROOT / "models").rglob("*.html"):
        t = p.read_text(encoding="utf-8")
        if old in t:
            t = t.replace(old, new, 1)
            p.write_text(t, encoding="utf-8", newline="\n")
            n2 += 1
    print("出发点 wrapped", n2)


if __name__ == "__main__":
    main()
