# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    js = (ROOT / "assets" / "glossary-data.js").read_text(encoding="utf-8")
    ids = set(re.findall(r'"id":\s*"([^"]+)"', js))
    htmls = {p.stem for p in (ROOT / "glossary").glob("*.html") if p.stem != "index"}
    print("data keys", len(ids), "html pages", len(htmls))
    print("in data missing html", sorted(ids - htmls), "count", len(ids - htmls))
    print("html missing data", sorted(htmls - ids), "count", len(htmls - ids))

    unknown: dict[str, list[str]] = {}
    for folder in ("glossary", "models", "learn", "topics"):
        for p in (ROOT / folder).rglob("*.html"):
            for tid in re.findall(r'data-term="([^"]+)"', p.read_text(encoding="utf-8")):
                if tid not in ids:
                    unknown.setdefault(tid, []).append(str(p.relative_to(ROOT)))
    print("unknown term ids", len(unknown))
    for k, v in sorted(unknown.items()):
        print(" ", k, "->", v[:3], ("..." if len(v) > 3 else ""))

    raw = (ROOT / "data" / "search-index.js").read_text(encoding="utf-8")
    prefix = "window.SAS_SEARCH_INDEX = "
    data = json.loads(raw[len(prefix) :].rstrip().rstrip(";"))
    g = [e for e in data if str(e.get("id", "")).startswith("glossary/")]
    print("search glossary entries", len(g), "total", len(data))
    missing_search = sorted(htmls - {e["id"].split("/", 1)[1] for e in g})
    print("html missing search", missing_search, "count", len(missing_search))

    # broken nested term in strong title self-link
    bad_self = []
    for p in (ROOT / "glossary").glob("*.html"):
        t = p.read_text(encoding="utf-8")
        if f'<strong><span data-term="{p.stem}">' in t:
            bad_self.append(p.name)
    print("self-linked strong titles", bad_self)

    # double-escaped latex leftovers
    for rel in ["learn/02-scattering-basics.html", "glossary/form-factor.html"]:
        t = (ROOT / rel).read_text(encoding="utf-8")
        print(rel, "has \\\\", "\\\\" in t)


if __name__ == "__main__":
    main()
