(function () {
  var glossaryData = null;
  var tooltipEl = null;
  var scrollListenerAttached = false;

  function basePath() {
    return (document.documentElement.getAttribute("data-base") || ".").replace(/\/$/, "");
  }

  function join(base, rel) {
    if (!rel) return base;
    if (rel.charAt(0) === "/") rel = rel.slice(1);
    if (base === "." || base === "") return rel;
    return base + "/" + rel;
  }

  function getTooltip() {
    if (!tooltipEl) {
      tooltipEl = document.createElement("div");
      tooltipEl.className = "term-tooltip";
      tooltipEl.setAttribute("role", "tooltip");
      tooltipEl.innerHTML =
        '<span class="en"></span><span class="tip"></span><span class="hint"></span>';
      tooltipEl.style.display = "none";
      document.body.appendChild(tooltipEl);
    }
    return tooltipEl;
  }

  function hideTooltip() {
    if (tooltipEl) tooltipEl.style.display = "none";
  }

  function positionTooltip(anchor) {
    var tip = getTooltip();
    var rect = anchor.getBoundingClientRect();
    var margin = 8;
    var left = rect.left;
    var top = rect.bottom + margin;

    tip.style.display = "block";
    var tipRect = tip.getBoundingClientRect();

    if (left + tipRect.width > window.innerWidth - margin) {
      left = Math.max(margin, window.innerWidth - tipRect.width - margin);
    }
    if (top + tipRect.height > window.innerHeight - margin) {
      top = rect.top - tipRect.height - margin;
    }
    if (top < margin) top = margin;

    tip.style.left = left + "px";
    tip.style.top = top + "px";
  }

  function showTooltip(anchor, entry) {
    var tip = getTooltip();
    tip.querySelector(".en").textContent = entry.titleEn || "";
    tip.querySelector(".tip").textContent = entry.tip || "";
    tip.querySelector(".hint").textContent = "点击查看词条";
    positionTooltip(anchor);
  }

  function termHref(base, id) {
    return join(base, "glossary/" + id + ".html");
  }

  function makeTermLink(el, id, entry, base) {
    var href = termHref(base, id);
    var link;

    if (el.tagName === "A" && el.classList.contains("term")) {
      link = el;
      if (!link.getAttribute("href")) link.setAttribute("href", href);
    } else if (el.tagName === "A") {
      link = el;
      link.classList.add("term");
      link.setAttribute("href", href);
    } else {
      link = document.createElement("a");
      link.className = "term";
      link.href = href;
      link.innerHTML = el.innerHTML;
      if (el.parentNode) el.parentNode.replaceChild(link, el);
    }

    link.setAttribute("data-term", id);
    if (entry && entry.titleEn) {
      link.setAttribute("title", entry.titleEn + (entry.tip ? " — " + entry.tip : ""));
    }

    link.addEventListener("mouseenter", function () {
      if (entry) showTooltip(link, entry);
    });
    link.addEventListener("mouseleave", hideTooltip);
    link.addEventListener("focus", function () {
      if (entry) showTooltip(link, entry);
    });
    link.addEventListener("blur", hideTooltip);

    return link;
  }

  function enhanceTerms(base, data) {
    document.querySelectorAll("[data-term]").forEach(function (el) {
      var id = el.getAttribute("data-term");
      if (!id) return;
      var entry = data ? data[id] : null;
      if (data && !entry) {
        console.warn("[SASGlossary] Unknown term id:", id);
      }
      makeTermLink(el, id, entry || { titleEn: id, tip: "" }, base);
    });
  }

  function attachScrollHide() {
    if (scrollListenerAttached) return;
    scrollListenerAttached = true;
    window.addEventListener("scroll", hideTooltip, true);
    window.addEventListener("resize", hideTooltip);
  }

  function loadData() {
    // Prefer script-tag data (works under file://). glossary-data.js sets SAS_GLOSSARY_DATA.
    if (window.SAS_GLOSSARY_DATA && typeof window.SAS_GLOSSARY_DATA === "object") {
      return window.SAS_GLOSSARY_DATA;
    }
    console.error(
      "[SASGlossary] Missing SAS_GLOSSARY_DATA. Include assets/glossary-data.js before glossary.js."
    );
    return null;
  }

  function init() {
    var base = basePath();
    attachScrollHide();
    glossaryData = loadData();
    enhanceTerms(base, glossaryData);
  }

  window.SASGlossary = {
    init: init,
    getData: function () {
      return glossaryData || window.SAS_GLOSSARY_DATA || null;
    }
  };
})();
