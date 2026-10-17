/* ============================================================
   Omega Living Bride Tabernacle: main.js
   Theme toggle · navigation · submenus · scroll reveal
   ============================================================ */

(function () {
  "use strict";

  /* ---------- Theme ---------- */
  // The initial theme is set by a tiny inline script in <head> so the page
  // never flashes the wrong colours. This only handles the toggle.

  var root = document.documentElement;

  function setTheme(mode) {
    root.setAttribute("data-theme", mode);
    try { localStorage.setItem("olbt-theme", mode); } catch (e) {}
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.setAttribute(
        "aria-label",
        mode === "dark" ? "Switch to light mode" : "Switch to dark mode"
      );
      btn.setAttribute("aria-pressed", mode === "dark" ? "true" : "false");
    });
  }

  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
    });
  });

  setTheme(root.getAttribute("data-theme") || "light");

  /* ---------- Mobile navigation ---------- */

  var navToggle = document.querySelector(".nav-toggle");
  var navMenu = document.getElementById("nav-menu");

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      var open = navMenu.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(open));
    });

    navMenu.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        navMenu.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- Dropdown submenus ---------- */

  var submenus = document.querySelectorAll(".submenu-toggle");

  function closeAllSubmenus(except) {
    submenus.forEach(function (t) {
      if (t === except) return;
      t.setAttribute("aria-expanded", "false");
      var m = document.getElementById(t.getAttribute("aria-controls"));
      if (m) m.classList.remove("open");
    });
  }

  submenus.forEach(function (toggle) {
    var menu = document.getElementById(toggle.getAttribute("aria-controls"));
    if (!menu) return;

    toggle.addEventListener("click", function (e) {
      e.preventDefault();
      var open = toggle.getAttribute("aria-expanded") === "true";
      closeAllSubmenus(toggle);
      toggle.setAttribute("aria-expanded", String(!open));
      menu.classList.toggle("open", !open);
    });

    // Hover on pointer devices with room for a dropdown
    var parent = toggle.parentElement;
    if (parent && window.matchMedia("(min-width: 961px) and (hover: hover)").matches) {
      parent.addEventListener("mouseenter", function () {
        closeAllSubmenus(toggle);
        toggle.setAttribute("aria-expanded", "true");
        menu.classList.add("open");
      });
      parent.addEventListener("mouseleave", function () {
        toggle.setAttribute("aria-expanded", "false");
        menu.classList.remove("open");
      });
    }
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav-links li")) closeAllSubmenus(null);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeAllSubmenus(null);
      if (navMenu && navMenu.classList.contains("open")) {
        navMenu.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.focus();
      }
    }
  });

  /* ---------- Reveal on scroll ---------- */

  var revealItems = document.querySelectorAll(".reveal");

  if ("IntersectionObserver" in window && revealItems.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealItems.forEach(function (el) { observer.observe(el); });
    // Safety net. Nothing stays invisible if the observer never fires.
    setTimeout(function () {
      revealItems.forEach(function (el) { el.classList.add("visible"); });
    }, 2500);
  } else {
    revealItems.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- Current year in footer ---------- */

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
