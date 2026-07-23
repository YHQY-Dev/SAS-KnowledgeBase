/**
 * If a figure-slot has data-file and the image loads, replace the placeholder.
 * Uses <img> onload/onerror only — works under file:// (no fetch).
 */
(function () {
  function basePath() {
    return (document.documentElement.getAttribute("data-base") || ".").replace(/\/$/, "");
  }

  function join(base, rel) {
    if (!rel) return base;
    if (rel.charAt(0) === "/") rel = rel.slice(1);
    if (base === "." || base === "") return rel;
    return base + "/" + rel;
  }

  function enhanceSlot(slot) {
    var file = slot.getAttribute("data-file");
    if (!file || slot.querySelector("img.fig-loaded")) return;
    var src = join(basePath(), "assets/figures/" + file);
    var img = new Image();
    img.className = "fig-loaded";
    img.alt = slot.getAttribute("data-alt") || file;
    var need = slot.querySelector(".fig-need");
    if (need && need.textContent) img.alt = need.textContent.replace(/^待配图：/, "");
    img.onload = function () {
      slot.innerHTML = "";
      slot.appendChild(img);
      slot.classList.add("is-filled");
      var fig = slot.closest("figure");
      if (fig) fig.classList.add("has-image");
      var srcLine = fig && fig.querySelector(".fig-source");
      if (srcLine && /生成后放入/.test(srcLine.textContent || "")) {
        srcLine.textContent = "配图：自制示意（" + (slot.getAttribute("data-fig") || file) + "）";
      }
    };
    img.onerror = function () {
      /* keep placeholder */
    };
    img.src = src;
  }

  function init() {
    document.querySelectorAll(".figure-slot[data-file]").forEach(enhanceSlot);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.SASFigures = { init: init };
})();
