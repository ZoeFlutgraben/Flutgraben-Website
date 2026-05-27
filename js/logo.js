

(function () {
  const svgs = [
    "car.svg",
    "idk.svg",
    "butterfly.svg",
    "cat.svg",
    "elephant_souris.svg",
    "kartofel.svg",
    "keep_on.svg",
    "birds.svg",
    "bonhomme2.svg",
    "bonhomme3.svg",
    "bonhomme4.svg",
    "chat_araignee.svg",
    "fille_ballon.svg",
    "fille_bombe.svg",
    "garf.svg",
    "lapin.svg",
  ];
  function init() {
    document.querySelectorAll("[data-random-svg]").forEach((el) => {
      const pick = svgs[Math.floor(Math.random() * svgs.length)];
      const img = el.querySelector("img");
      if (img) img.src = "image/svg/" + pick;
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
