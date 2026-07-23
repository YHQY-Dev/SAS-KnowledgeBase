(function () {
  var index = null;
  var panel = null;
  var input = null;
  var list = null;
  var open = false;

  function basePath() {
    return (document.documentElement.getAttribute("data-base") || ".").replace(/\/$/, "");
  }

  function join(base, rel) {
    if (!rel) return base;
    if (rel.charAt(0) === "/") rel = rel.slice(1);
    if (base === "." || base === "") return rel;
    return base + "/" + rel;
  }

  function ensureIndex(cb) {
    if (index) {
      cb(index);
      return;
    }
    if (window.SAS_SEARCH_INDEX && window.SAS_SEARCH_INDEX.length) {
      index = window.SAS_SEARCH_INDEX;
      cb(index);
      return;
    }
    // http(s) fallback: fetch JSON
    var url = join(basePath(), "data/search-index.json");
    fetch(url)
      .then(function (r) {
        return r.json();
      })
      .then(function (data) {
        index = data;
        cb(index);
      })
      .catch(function () {
        index = [];
        cb(index);
      });
  }

  function scoreEntry(entry, q) {
    var needle = q.toLowerCase();
    var title = (entry.title || "").toLowerCase();
    var headings = (entry.headings || []).join(" ").toLowerCase();
    var text = (entry.text || "").toLowerCase();
    var s = 0;
    if (title === needle) s += 100;
    if (title.indexOf(needle) === 0) s += 60;
    if (title.indexOf(needle) >= 0) s += 40;
    if (headings.indexOf(needle) >= 0) s += 25;
    if (text.indexOf(needle) >= 0) s += 10;
    // multi-token AND soft score
    var parts = needle.split(/\s+/).filter(Boolean);
    if (parts.length > 1) {
      var ok = parts.every(function (p) {
        return title.indexOf(p) >= 0 || headings.indexOf(p) >= 0 || text.indexOf(p) >= 0;
      });
      if (!ok) return 0;
      s += 5 * parts.length;
    }
    return s;
  }

  function snippet(entry, q) {
    var text = entry.text || "";
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) {
      var h = (entry.headings || [])[0];
      return h || text.slice(0, 90);
    }
    var start = Math.max(0, i - 28);
    var end = Math.min(text.length, i + q.length + 52);
    var sn = text.slice(start, end);
    if (start > 0) sn = "…" + sn;
    if (end < text.length) sn = sn + "…";
    return sn;
  }

  function renderResults(q) {
    if (!list) return;
    var query = (q || "").trim();
    if (query.length < 1) {
      list.innerHTML = '<li class="search-empty">输入关键词搜索学习路径、专题与术语</li>';
      return;
    }
    ensureIndex(function (data) {
      var scored = data
        .map(function (e) {
          return { e: e, s: scoreEntry(e, query) };
        })
        .filter(function (x) {
          return x.s > 0;
        })
        .sort(function (a, b) {
          return b.s - a.s;
        })
        .slice(0, 12);

      if (!scored.length) {
        list.innerHTML = '<li class="search-empty">无匹配结果</li>';
        return;
      }
      var base = basePath();
      list.innerHTML = scored
        .map(function (x) {
          var href = join(base, x.e.url);
          return (
            '<li><a href="' +
            href +
            '"><span class="search-sec">' +
            (x.e.section || "") +
            "</span><span class=\"search-title\">" +
            escapeHtml(x.e.title) +
            '</span><span class="search-snip">' +
            escapeHtml(snippet(x.e, query)) +
            "</span></a></li>"
          );
        })
        .join("");
    });
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function setOpen(v) {
    open = !!v;
    if (!panel) return;
    panel.hidden = !open;
    if (open && input) {
      input.focus();
      input.select();
    }
  }

  function mount() {
    var header = document.getElementById("site-header");
    if (!header || header.querySelector(".site-search")) return;

    var wrap = document.createElement("div");
    wrap.className = "site-search";
    wrap.innerHTML =
      '<button type="button" class="search-toggle" aria-label="搜索" title="搜索 (Ctrl+K)">搜索</button>' +
      '<div class="search-panel" hidden>' +
      '<label class="search-label" for="site-search-input">站内搜索</label>' +
      '<input type="search" id="site-search-input" placeholder="搜索章节、专题、术语…" autocomplete="off" />' +
      '<ul class="search-results" role="listbox"></ul>' +
      '<p class="search-hint">Ctrl+K 打开 · Esc 关闭</p>' +
      "</div>";

    var nav = header.querySelector(".site-nav");
    if (nav) header.insertBefore(wrap, nav);
    else header.appendChild(wrap);

    panel = wrap.querySelector(".search-panel");
    input = wrap.querySelector("#site-search-input");
    list = wrap.querySelector(".search-results");
    var toggle = wrap.querySelector(".search-toggle");

    toggle.addEventListener("click", function (e) {
      e.stopPropagation();
      setOpen(!open);
      if (open) renderResults(input.value);
    });

    var t = null;
    input.addEventListener("input", function () {
      clearTimeout(t);
      var v = input.value;
      t = setTimeout(function () {
        renderResults(v);
      }, 80);
    });

    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        setOpen(false);
        e.preventDefault();
      }
      if (e.key === "Enter") {
        var first = list && list.querySelector("a");
        if (first) {
          window.location.href = first.getAttribute("href");
          e.preventDefault();
        }
      }
    });

    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === "k" || e.key === "K")) {
        e.preventDefault();
        setOpen(true);
        renderResults(input.value);
      }
      if (e.key === "Escape" && open) setOpen(false);
    });

    document.addEventListener("click", function (e) {
      if (!open) return;
      if (!wrap.contains(e.target)) setOpen(false);
    });

    // preload index when available
    ensureIndex(function () {});
  }

  function loadIndexScript(cb) {
    if (window.SAS_SEARCH_INDEX) {
      cb();
      return;
    }
    var s = document.createElement("script");
    s.src = join(basePath(), "data/search-index.js");
    s.onload = function () {
      cb();
    };
    s.onerror = function () {
      cb();
    };
    document.head.appendChild(s);
  }

  function init() {
    loadIndexScript(function () {
      mount();
    });
  }

  window.SASSearch = { init: init };
})();
