(function () {
  function basePath() {
    var b = document.documentElement.getAttribute("data-base") || ".";
    return b.replace(/\/$/, "");
  }

  function join(base, rel) {
    if (!rel) return base;
    if (rel.charAt(0) === "/") rel = rel.slice(1);
    if (base === "." || base === "") return rel;
    return base + "/" + rel;
  }

  function currentFile() {
    var path = window.location.pathname.replace(/\\/g, "/");
    var parts = path.split("/");
    return parts[parts.length - 1] || "index.html";
  }

  function currentHrefTail() {
    var path = window.location.pathname.replace(/\\/g, "/");
    var marker = "/SAS-web/";
    var idx = path.lastIndexOf(marker);
    if (idx >= 0) return path.slice(idx + marker.length);
    // file:// or odd hosts: best-effort from last segments
    var parts = path.split("/").filter(Boolean);
    var i = parts.lastIndexOf("SAS-web");
    if (i >= 0) return parts.slice(i + 1).join("/");
    return parts.slice(-2).join("/");
  }

  var NAV = [
    { href: "learn/index.html", label: "学习路径" },
    { href: "topics/index.html", label: "专题手册" },
    { href: "glossary/index.html", label: "术语表" },
    { href: "catalog/index.html", label: "文献目录" }
  ];

  var SIDEBARS = {
    learn: {
      title: "学习路径",
      links: [
        { href: "learn/index.html", label: "总览" },
        { href: "learn/01-what-is-sas.html", label: "01 什么是 SAS" },
        { href: "learn/02-scattering-basics.html", label: "02 散射基础" },
        { href: "learn/03-instruments.html", label: "03 仪器与几何" },
        { href: "learn/04-data-reduction.html", label: "04 数据还原" },
        { href: "learn/05-absolute-calibration.html", label: "05 绝对标定" },
        { href: "learn/06-guinier-porod.html", label: "06 Guinier / Porod" },
        { href: "learn/07-real-space-ift.html", label: "07 实空间与 IFT" },
        { href: "learn/08-models-polydispersity.html", label: "08 模型与多分散" },
        { href: "learn/09-application-paths.html", label: "09 应用岔路" }
      ]
    },
    topics: {
      title: "专题手册",
      links: [
        { href: "topics/index.html", label: "总览" },
        { href: "topics/calibration/index.html", label: "绝对标定" },
        { href: "topics/data-reduction/index.html", label: "数据还原" },
        { href: "topics/ift/index.html", label: "IFT" },
        { href: "topics/biosas/index.html", label: "生物 SAS" },
        { href: "topics/atsas/index.html", label: "ATSAS" },
        { href: "topics/sans-contrast/index.html", label: "SANS 衬度" },
        { href: "topics/gisaxs/index.html", label: "GISAXS" },
        { href: "topics/asaxs/index.html", label: "ASAXS" },
        { href: "topics/magnetic-sans/index.html", label: "磁性 SANS" },
        { href: "topics/polymers-bcp/index.html", label: "聚合物 / BCP" },
        { href: "topics/usaxs/index.html", label: "USAXS" },
        { href: "topics/sample-env/index.html", label: "样品环境" }
      ]
    },
    glossary: {
      title: "术语表",
      links: null // filled at runtime from SAS_GLOSSARY_DATA
    },
    catalog: {
      title: "文献目录",
      links: [
        { href: "catalog/index.html", label: "浏览与筛选" }
      ]
    },
    home: {
      title: "开始",
      links: [
        { href: "index.html", label: "首页" },
        { href: "about.html", label: "关于本站" },
        { href: "learn/index.html", label: "学习路径" },
        { href: "topics/index.html", label: "专题手册" }
      ]
    }
  };

  function sectionKey(tail) {
    var t = (tail || "").replace(/\/+$/, "");
    if (t === "learn" || t.indexOf("learn/") === 0) return "learn";
    if (t === "topics" || t.indexOf("topics/") === 0) return "topics";
    if (t === "glossary" || t.indexOf("glossary/") === 0) return "glossary";
    if (t === "catalog" || t.indexOf("catalog/") === 0) return "catalog";
    return "home";
  }

  function isActive(linkHref, tail) {
    var norm = linkHref.replace(/^\.\//, "");
    var t = (tail || "").replace(/\/+$/, "");
    if (t === norm) return true;
    if (norm.endsWith("/index.html") && (t === norm || t + "/index.html" === norm)) return true;
    // glossary/foo.html exact
    if (norm.indexOf("glossary/") === 0 && t === norm) return true;
    return false;
  }

  function glossaryLinks() {
    var links = [{ href: "glossary/index.html", label: "总览" }];
    var data = window.SAS_GLOSSARY_DATA;
    if (!data) return links;
    Object.keys(data)
      .map(function (id) {
        return data[id];
      })
      .filter(function (t) {
        return t && t.id && t.titleZh;
      })
      .sort(function (a, b) {
        return String(a.titleZh).localeCompare(String(b.titleZh), "zh");
      })
      .forEach(function (t) {
        var label = t.titleZh;
        if (t.abbr && String(t.abbr).length <= 14 && String(t.abbr) !== t.titleZh) {
          label = t.abbr + " · " + t.titleZh;
        }
        links.push({ href: "glossary/" + t.id + ".html", label: label });
      });
    return links;
  }

  function renderHeader(base) {
    var host = document.getElementById("site-header");
    if (!host) return;
    var navHtml = NAV.map(function (item) {
      return '<a href="' + join(base, item.href) + '">' + item.label + "</a>";
    }).join("");
    host.className = "site-header";
    host.innerHTML =
      '<a class="site-brand" href="' +
      join(base, "index.html") +
      '">SAS 知识站<span>Small-Angle Scattering</span></a>' +
      '<button type="button" class="nav-toggle" aria-expanded="false" aria-label="菜单">菜单</button>' +
      '<nav class="site-nav">' +
      navHtml +
      '<a href="' +
      join(base, "about.html") +
      '">关于</a></nav>';

    var toggle = host.querySelector(".nav-toggle");
    if (toggle) {
      toggle.addEventListener("click", function () {
        var open = host.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    var tail = currentHrefTail();
    host.querySelectorAll(".site-nav a").forEach(function (a) {
      var href = a.getAttribute("href") || "";
      var rel = href.replace(base + "/", "").replace(/^\.\//, "");
      if (base === ".") rel = href;
      if (tail.indexOf(rel.replace(/index\.html$/, "")) === 0 || tail === rel) {
        a.classList.add("is-active");
      }
    });
  }

  function renderSidebar(base) {
    var host = document.getElementById("site-sidebar");
    if (!host) return;
    var tail = currentHrefTail();
    var key = sectionKey(tail);
    var conf = SIDEBARS[key] || SIDEBARS.home;
    var linkItems = conf.links;
    if (key === "glossary") linkItems = glossaryLinks();
    var links = (linkItems || [])
      .map(function (item) {
        if (!item.href) {
          return '<li><span class="nav-planned">' + item.label + "</span></li>";
        }
        var href = join(base, item.href);
        var cls = isActive(item.href, tail) ? ' class="is-active"' : "";
        return "<li><a href=\"" + href + "\"" + cls + ">" + item.label + "</a></li>";
      })
      .join("");
    host.className = "site-sidebar" + (key === "glossary" ? " is-glossary" : "");
    host.innerHTML = "<h2>" + conf.title + "</h2><ul>" + links + "</ul>";

    // Keep active glossary term visible in a long list
    if (key === "glossary") {
      var active = host.querySelector("a.is-active");
      if (active && active.scrollIntoView) {
        try {
          active.scrollIntoView({ block: "nearest" });
        } catch (e) {
          active.scrollIntoView();
        }
      }
    }
  }

  function ensureGlossaryData(base, done) {
    if (window.SAS_GLOSSARY_DATA) {
      done();
      return;
    }
    var s = document.createElement("script");
    s.src = join(base, "assets/glossary-data.js");
    s.onload = function () {
      done();
    };
    s.onerror = function () {
      done();
    };
    document.head.appendChild(s);
  }

  function init() {
    var base = basePath();
    renderHeader(base);
    var key = sectionKey(currentHrefTail());
    if (key === "glossary") {
      ensureGlossaryData(base, function () {
        renderSidebar(base);
      });
    } else {
      renderSidebar(base);
    }
    loadSearch(base);
  }

  function loadSearch(base) {
    if (window.SASSearch) {
      window.SASSearch.init();
      return;
    }
    var s = document.createElement("script");
    s.src = join(base, "assets/search.js");
    s.onload = function () {
      if (window.SASSearch) window.SASSearch.init();
    };
    document.head.appendChild(s);
  }

  window.SASNav = {
    init: init,
    basePath: basePath,
    join: join
  };
})();
