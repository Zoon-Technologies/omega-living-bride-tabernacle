/* ============================================================
   Hero carousel: renders from HERO_SLIDES (js/hero-slides.js)
   Auto-advance, pause on hover/focus, arrows, dots, swipe,
   keyboard, and full respect for reduced-motion preferences.
   ============================================================ */

(function () {
  "use strict";

  var hero = document.getElementById("hero");
  if (!hero || typeof HERO_SLIDES === "undefined" || !HERO_SLIDES.length) return;

  var slidesBox = hero.querySelector(".hero-slides");
  var copyBox = hero.querySelector(".hero-copy");
  var dotsBox = hero.querySelector(".hero-dots");
  if (!slidesBox || !copyBox) return;

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var index = 0;
  var timer = null;
  var interval =
    (typeof HERO_INTERVAL_SECONDS === "number" ? HERO_INTERVAL_SECONDS : 7) * 1000;

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* ---------- Build the picture layers ---------- */

  slidesBox.innerHTML = HERO_SLIDES.map(function (s, i) {
    var small = s.imgSmall || s.img;
    var blur =
      s.fit === "contain"
        ? '<img class="slide-blur" src="' + esc(small) + '" alt="" aria-hidden="true" />'
        : "";
    return (
      '<div class="hero-slide' + (i === 0 ? " is-active" : "") + '" data-fit="' +
      esc(s.fit || "cover") + '">' +
      blur +
      '<img class="slide-img" src="' + esc(i === 0 ? s.img : "") + '" ' +
      'data-src="' + esc(s.img) + '" data-src-small="' + esc(small) + '" ' +
      'alt="' + esc(s.alt || "") + '" ' +
      (i === 0 ? 'fetchpriority="high"' : 'loading="lazy"') + " /></div>"
    );
  }).join("");

  var slideEls = Array.prototype.slice.call(slidesBox.querySelectorAll(".hero-slide"));

  // Use the smaller file on narrow screens.
  var narrow = window.matchMedia("(max-width: 860px)");
  function pickSource(img) {
    var want = narrow.matches ? img.getAttribute("data-src-small") : img.getAttribute("data-src");
    if (want && img.getAttribute("src") !== want) img.setAttribute("src", want);
  }
  pickSource(slideEls[0].querySelector(".slide-img"));

  /* ---------- Dots ---------- */

  if (dotsBox && HERO_SLIDES.length > 1) {
    dotsBox.innerHTML = HERO_SLIDES.map(function (s, i) {
      return (
        '<button type="button" class="hero-dot' + (i === 0 ? " is-active" : "") +
        '" data-go="' + i + '" aria-label="Show slide ' + (i + 1) + ': ' +
        esc(s.title || "") + '"></button>'
      );
    }).join("");
  }

  /* ---------- Render the words for a slide ---------- */

  function renderCopy(i) {
    var s = HERO_SLIDES[i];
    var buttons = "";
    if (s.ctaLabel && s.ctaHref) {
      buttons += '<a class="btn btn-gold" href="' + esc(s.ctaHref) + '">' + esc(s.ctaLabel) + "</a>";
    }
    if (s.cta2Label && s.cta2Href) {
      buttons += '<a class="btn btn-outline" href="' + esc(s.cta2Href) + '">' + esc(s.cta2Label) + "</a>";
    }

    // The site name stays a real <h1> on the first paint for SEO; later
    // slides use a visually identical heading that is not a second <h1>.
    var headingTag = i === 0 ? "h1" : "p";
    var headingClass = i === 0 ? "" : ' class="h1"';

    copyBox.innerHTML =
      (s.eyebrow ? '<p class="hero-brandline">' + esc(s.eyebrow) + "</p>" : "") +
      "<" + headingTag + headingClass + ">" + esc(s.title || "") + "</" + headingTag + ">" +
      (s.text ? '<p class="hero-lede">' + esc(s.text) + "</p>" : "") +
      (buttons ? '<div class="hero-actions">' + buttons + "</div>" : "");
  }

  /* ---------- Move to a slide ---------- */

  function show(next) {
    next = (next + HERO_SLIDES.length) % HERO_SLIDES.length;
    if (next === index && slideEls[next].classList.contains("is-active")) return;

    slideEls.forEach(function (el, i) { el.classList.toggle("is-active", i === next); });
    pickSource(slideEls[next].querySelector(".slide-img"));

    // Warm the next picture so the change is not blank on slow connections.
    var after = slideEls[(next + 1) % slideEls.length].querySelector(".slide-img");
    if (after) pickSource(after);

    if (dotsBox) {
      dotsBox.querySelectorAll(".hero-dot").forEach(function (d, i) {
        d.classList.toggle("is-active", i === next);
      });
    }

    index = next;
    renderCopy(index);
  }

  /* ---------- Auto-advance ---------- */

  function start() {
    if (reduceMotion || HERO_SLIDES.length < 2) return;
    stop();
    timer = setInterval(function () { show(index + 1); }, interval);
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }

  hero.addEventListener("mouseenter", stop);
  hero.addEventListener("mouseleave", start);
  hero.addEventListener("focusin", stop);
  hero.addEventListener("focusout", start);
  document.addEventListener("visibilitychange", function () {
    document.hidden ? stop() : start();
  });

  /* ---------- Controls ---------- */

  hero.addEventListener("click", function (e) {
    var dot = e.target.closest("[data-go]");
    if (dot) { show(parseInt(dot.getAttribute("data-go"), 10)); start(); return; }
    if (e.target.closest("[data-prev]")) { show(index - 1); start(); return; }
    if (e.target.closest("[data-next]")) { show(index + 1); start(); }
  });

  hero.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") { show(index - 1); start(); }
    if (e.key === "ArrowRight") { show(index + 1); start(); }
  });

  // Swipe on touch screens
  var startX = null;
  hero.addEventListener("touchstart", function (e) {
    startX = e.changedTouches[0].clientX; stop();
  }, { passive: true });
  hero.addEventListener("touchend", function (e) {
    if (startX === null) return;
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 45) show(index + (dx < 0 ? 1 : -1));
    startX = null;
    start();
  }, { passive: true });

  narrow.addEventListener("change", function () {
    slideEls.forEach(function (el) {
      var img = el.querySelector(".slide-img");
      if (img.getAttribute("src")) pickSource(img);
    });
  });

  renderCopy(0);
  start();
})();
