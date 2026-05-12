// Random logo picker — selects one of the logo variants on page load.
// Per the brief: random on every page load, logo_vide.png is valid (invisible).
(function () {
  const variants = [
    "logos/v_circle.png",
    "logos/v_cross.png",
    "logos/v_polygone.png",
    "logos/v_polygone8.png",
    "logos/v_square.png",
    "logos/v_trait.png",
    "logos/logo_vide.png",
  ];
  function init() {
    document.querySelectorAll("[data-random-logo]").forEach((el) => {
      const pick = variants[Math.floor(Math.random() * variants.length)];
      const img = document.createElement("img");
      img.src = pick;
      img.alt = "Flutgraben";
      img.style.width = "100%";
      img.style.height = "100%";
      img.style.objectFit = "contain";
      img.style.display = "block";
      el.innerHTML = "";
      el.appendChild(img);
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
