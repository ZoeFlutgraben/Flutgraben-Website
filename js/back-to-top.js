// Back to top button — shared across all interior pages (excludes index.html)
// Detects the scroll container for the current page, shows the button after
// 150px of scroll, and scrolls back to top smoothly on click.

(function () {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  // Each page has its own scroll container — detect it
  const scroller =
    document.querySelector('.page-content') ||
    document.querySelector('.impressum-outer') ||
    document.documentElement;

  // Toggle visibility based on scroll position
  scroller.addEventListener('scroll', () => {
    btn.classList.toggle('is-visible', scroller.scrollTop > 150);
  });

  // Scroll to top on click
  btn.addEventListener('click', () => {
    scroller.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
