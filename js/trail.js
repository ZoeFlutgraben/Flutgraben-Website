// Pixel mouse-trail effect — shared across directions.
// Render ~10 ghost cursors trailing behind the real one. Hard pixel copies, no fade.
(function () {
  if (window.__flut_trail_init) return;
  window.__flut_trail_init = true;

  const GHOST_COUNT = 10;
  const SVG = "data:image/svg+xml;utf8," + encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20' shape-rendering='crispEdges'>
       <path d='M2 1 L2 14 L5 11 L7 16 L10 15 L8 10 L13 10 Z' fill='#573835' stroke='#e5e9ed' stroke-width='0.5'/>
     </svg>`
  );

  const ghosts = [];
  for (let i = 0; i < GHOST_COUNT; i++) {
    const g = document.createElement("img");
    g.src = SVG;
    g.className = "trail-ghost";
    g.style.opacity = "1";
    document.body.appendChild(g);
    ghosts.push({ el: g, x: -50, y: -50 });
  }

  const history = [];
  let lastX = -50, lastY = -50;

  document.addEventListener("mousemove", (e) => {
    lastX = e.clientX;
    lastY = e.clientY;
    history.unshift({ x: lastX, y: lastY });
    if (history.length > GHOST_COUNT * 3) history.pop();
  });

  function tick() {
    for (let i = 0; i < GHOST_COUNT; i++) {
      const sample = history[Math.min(i * 2, history.length - 1)];
      if (!sample) continue;
      const g = ghosts[i];
      g.el.style.transform = `translate(${sample.x - 2}px, ${sample.y - 1}px)`;
    }
    requestAnimationFrame(tick);
  }
  tick();
})();
