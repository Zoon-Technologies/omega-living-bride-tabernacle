/* ============================================================
   PHOTO ALBUMS
   ------------------------------------------------------------
   Add an album by copying one block below and pasting it at the
   TOP of the list.

   HOW TO ADD PHOTOS
   1. Put the pictures in   assets/img/albums/<album-folder>/
      Keep each file under about 400 KB. Resize before uploading:
      1600 pixels on the long edge is plenty for a website.
   2. Fill in the block below. "cover" is the picture shown on the
      album tile; "photos" is everything inside it.

   Fields
   ------
   title    album name
   date     "December 2026"  (free text, shown under the title)
   cover    path to the tile picture
   photos   list of { src, caption }
   ============================================================ */

const PHOTO_ALBUMS = [
  // {
  //   title: "Melchizedec's Conference '26",
  //   date: "December 2026",
  //   cover: "/assets/img/albums/conference-26/cover.jpg",
  //   photos: [
  //     { src: "/assets/img/albums/conference-26/01.jpg", caption: "Opening night" },
  //     { src: "/assets/img/albums/conference-26/02.jpg", caption: "Morning session" }
  //   ]
  // },
];

/* ---------------- nothing below needs editing ---------------- */

(function () {
  "use strict";

  var grid = document.getElementById("album-grid");
  if (!grid) return;

  var empty = document.getElementById("album-empty");

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  var live = PHOTO_ALBUMS.filter(function (a) {
    return a && a.photos && a.photos.length;
  });

  if (!live.length) {
    grid.innerHTML = "";
    if (empty) empty.hidden = false;
    return;
  }
  if (empty) empty.hidden = true;

  /* ---------- Album tiles ---------- */

  grid.innerHTML = live
    .map(function (a, i) {
      var cover = a.cover || a.photos[0].src;
      var count = a.photos.length + (a.photos.length === 1 ? " photo" : " photos");
      return (
        '<a class="album" href="#" data-album="' + i + '">' +
        '<img src="' + esc(cover) + '" alt="' + esc(a.title) + '" loading="lazy" />' +
        '<span class="album-label">' +
        '<span class="al-title">' + esc(a.title) + "</span>" +
        '<span class="al-meta">' + esc([a.date, count].filter(Boolean).join(" · ")) + "</span>" +
        "</span></a>"
      );
    })
    .join("");

  /* ---------- Lightbox ---------- */

  var lb = document.createElement("div");
  lb.className = "lightbox";
  lb.setAttribute("role", "dialog");
  lb.setAttribute("aria-modal", "true");
  lb.setAttribute("aria-label", "Photo viewer");
  lb.innerHTML =
    '<button class="lb-btn lb-close" type="button" aria-label="Close">&times;</button>' +
    '<button class="lb-btn lb-prev" type="button" aria-label="Previous photo">&#8249;</button>' +
    '<img alt="" />' +
    '<button class="lb-btn lb-next" type="button" aria-label="Next photo">&#8250;</button>' +
    '<p class="lb-caption"></p>';
  document.body.appendChild(lb);

  var lbImg = lb.querySelector("img");
  var lbCap = lb.querySelector(".lb-caption");
  var album = null;
  var pos = 0;
  var lastFocus = null;

  function paint() {
    var p = album.photos[pos];
    lbImg.src = p.src;
    lbImg.alt = p.caption || album.title;
    lbCap.textContent =
      (p.caption ? p.caption + " — " : "") +
      album.title + " (" + (pos + 1) + " of " + album.photos.length + ")";
  }

  function open(i) {
    album = live[i];
    pos = 0;
    lastFocus = document.activeElement;
    paint();
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
    lb.querySelector(".lb-close").focus();
  }

  function close() {
    lb.classList.remove("open");
    document.body.style.overflow = "";
    lbImg.src = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function step(n) {
    if (!album) return;
    pos = (pos + n + album.photos.length) % album.photos.length;
    paint();
  }

  grid.addEventListener("click", function (e) {
    var tile = e.target.closest("[data-album]");
    if (!tile) return;
    e.preventDefault();
    open(parseInt(tile.getAttribute("data-album"), 10));
  });

  lb.addEventListener("click", function (e) {
    if (e.target.closest(".lb-close") || e.target === lb) return close();
    if (e.target.closest(".lb-prev")) return step(-1);
    if (e.target.closest(".lb-next")) return step(1);
  });

  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "ArrowRight") step(1);
  });

  var sx = null;
  lb.addEventListener("touchstart", function (e) { sx = e.changedTouches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (sx === null) return;
    var dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 45) step(dx < 0 ? 1 : -1);
    sx = null;
  }, { passive: true });
})();
