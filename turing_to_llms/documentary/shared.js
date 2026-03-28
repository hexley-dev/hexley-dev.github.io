/* Documentary shared nav + footer — single source of truth */
/* Works from any page depth — detects base path automatically */

(function() {

// Detect base path relative to turing_to_llms/
function getBasePath() {
  var path = location.pathname;
  var idx = path.indexOf("turing_to_llms/");
  if (idx >= 0) {
    // Count slashes after turing_to_llms/ to determine depth
    var after = path.substring(idx + "turing_to_llms/".length);
    var depth = (after.match(/\//g) || []).length;
    // If the path ends with a filename, depth is number of slashes
    // e.g. documentary/index.html = 1 slash = depth 1
    // e.g. experiments/future_canvas/index.html = 2 slashes = depth 2
    var prefix = "";
    for (var i = 0; i < depth; i++) prefix += "../";
    return prefix;
  }
  // Fallback for file:// or unknown structure
  return "../";
}

var BASE = getBasePath();

var DOC_NAV_NOW = [
  { href: BASE + "experiments/future_canvas/index.html", label: "Future Canvas" },
  { href: BASE + "experiments/future_canvas/gallery.html", label: "Concept Gallery" },
  { href: BASE + "documentary/style_experiments.html", label: "Experiments" },
  { href: BASE + "documentary/on_our_mind.html", label: "On Our Mind" },
];

var DOC_NAV_ARCHIVE = [
  { href: BASE + "documentary/index.html", label: "Overview" },
  { href: BASE + "documentary/why_we_build.html", label: "Why We Build" },
  { href: BASE + "documentary/pipeline.html", label: "Pipeline" },
  { href: BASE + "documentary/character_design.html", label: "Characters" },
  { href: BASE + "documentary/lessons.html", label: "Lessons" },
  { href: BASE + "documentary/timeline.html", label: "Timeline" },
];

var DOC_FOOTER_HTML =
  '<div class="divider"><span>End</span></div>' +
  '<section style="text-align: center; padding: 4rem 2rem 6rem;">' +
  '<p style="font-family: var(--mono); font-size: 0.6rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">' +
  'Built with <a href="https://claude.com/product/claude-code" target="_blank" rel="noopener">Claude Code</a> · ' +
  '<a href="https://huggingface.co/Tongyi-MAI/Z-Image-Turbo" target="_blank" rel="noopener">Z-Image-Turbo</a> · ' +
  '<a href="https://huggingface.co/black-forest-labs/FLUX.2-dev" target="_blank" rel="noopener">FLUX.2-dev</a> · ' +
  '<a href="https://huggingface.co/docs/diffusers" target="_blank" rel="noopener">Diffusers</a> · ' +
  '<a href="https://fastapi.tiangolo.com/" target="_blank" rel="noopener">FastAPI</a>' +
  '</p></section>';

function initDocNav() {
  var nav = document.querySelector(".doc-nav");
  if (!nav) return;
  var currentPath = location.pathname;

  // Resolve current path relative to turing_to_llms/
    var tlIdx = currentPath.indexOf("turing_to_llms/");
    var currentRel = tlIdx >= 0 ? currentPath.substring(tlIdx + "turing_to_llms/".length) : currentPath;

    // Check if current page exactly matches any nav item
    var allItems = DOC_NAV_NOW.concat(DOC_NAV_ARCHIVE);
    var hasExactMatch = allItems.some(function(item) {
      return item.href.replace(/\.\.\//g, "") === currentRel;
    });

  function isActive(href) {
    var resolved = href.replace(/\.\.\//g, "");
    // Exact filename match
    if (currentRel === resolved) return true;
    // Directory matching for sub-pages (e.g. future_canvas/v2/report.html → Future Canvas),
    // but only when the current page isn't an exact match for another nav item
    if (!hasExactMatch) {
      var slashes = (resolved.match(/\//g) || []).length;
      if (slashes >= 2) {
        var resolvedDir = resolved.replace(/[^/]*$/, "");
        if (currentRel.indexOf(resolvedDir) === 0) return true;
      }
    }
    return false;
  }

  function renderLink(item) {
    var cls = isActive(item.href) ? ' class="active"' : "";
    return '<a href="' + item.href + '"' + cls + '>' + item.label + '</a>';
  }

  nav.innerHTML =
    '<div class="nav-tier nav-now">' +
    '<span class="nav-label">Latest</span>' +
    DOC_NAV_NOW.map(renderLink).join("\n") +
    '</div>' +
    '<div class="nav-tier nav-archive">' +
    '<span class="nav-label">Making Of</span>' +
    DOC_NAV_ARCHIVE.map(renderLink).join("\n") +
    '</div>';
}

function initDocFooter() {
  var el = document.getElementById("doc-footer");
  if (el) el.innerHTML = DOC_FOOTER_HTML;
}

document.addEventListener("DOMContentLoaded", function() {
  initDocNav();
  initDocFooter();
});

})();
