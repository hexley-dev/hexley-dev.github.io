/* Documentary shared nav + footer — single source of truth */

const DOC_NAV_NOW = [
  { href: "../experiments/future_canvas/index.html", label: "Future Canvas" },
  { href: "../experiments/future_canvas/gallery.html", label: "Concept Art" },
  { href: "style_experiments.html", label: "Experiments" },
  { href: "on_our_mind.html", label: "On Our Mind" },
];

const DOC_NAV_ARCHIVE = [
  { href: "index.html", label: "Overview" },
  { href: "pipeline.html", label: "Pipeline" },
  { href: "character_design.html", label: "Characters" },
  { href: "lessons.html", label: "Lessons" },
  { href: "timeline.html", label: "Timeline" },
];

const DOC_FOOTER_HTML = `
<div class="divider"><span>End</span></div>
<section style="text-align: center; padding: 4rem 2rem 6rem;">
  <p style="font-family: var(--mono); font-size: 0.6rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">
    Built with <a href="https://claude.com/product/claude-code" target="_blank" rel="noopener">Claude Code</a> · <a href="https://huggingface.co/Tongyi-MAI/Z-Image-Turbo" target="_blank" rel="noopener">Z-Image-Turbo</a> · <a href="https://huggingface.co/black-forest-labs/FLUX.2-dev" target="_blank" rel="noopener">FLUX.2-dev</a> · <a href="https://huggingface.co/docs/diffusers" target="_blank" rel="noopener">Diffusers</a> · <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noopener">FastAPI</a>
  </p>
</section>`;

function initDocNav() {
  const nav = document.querySelector(".doc-nav");
  if (!nav) return;
  const currentPage = location.pathname.split("/").pop() || "index.html";
  const currentPath = location.pathname;

  function renderLink({ href, label }) {
    const isActive = href === currentPage || currentPath.includes(href.replace(/^\.\./, ""));
    return `<a href="${href}"${isActive ? ' class="active"' : ""}>${label}</a>`;
  }

  nav.innerHTML = `
    <div class="nav-tier nav-now">
      <span class="nav-label">Latest</span>
      ${DOC_NAV_NOW.map(renderLink).join("\n")}
    </div>
    <div class="nav-tier nav-archive">
      <span class="nav-label">Making Of</span>
      ${DOC_NAV_ARCHIVE.map(renderLink).join("\n")}
    </div>`;
}

function initDocFooter() {
  const el = document.getElementById("doc-footer");
  if (el) el.innerHTML = DOC_FOOTER_HTML;
}

document.addEventListener("DOMContentLoaded", () => {
  initDocNav();
  initDocFooter();
});
