/* ============================================================
   OMEGA LIVING BRIDE TABERNACLE: SETTINGS
   ------------------------------------------------------------
   The two keys the website needs. Paste them between the
   quotation marks, save, then push to GitHub. Nothing else.

   Leave either one empty and that feature simply stays off.
   nothing breaks, and no broken code is sent to visitors.
   ============================================================ */

window.OLBT_CONFIG = {

  /* ---- 1. Google Analytics ------------------------------------
     Looks like  G-ABC1234XYZ
     Found in Analytics: Admin -> Data streams -> click the web
     stream -> "Measurement ID" on the first row.
     ------------------------------------------------------------ */
  GA4_ID: "G-FV83RYREJG",

  /* ---- 2. YouTube ---------------------------------------------
     Lets the website show the latest sermons by itself.
     Made at console.cloud.google.com (see js/youtube.js for the
     full walkthrough). Remember to restrict the key to this
     website before you use it.
     ------------------------------------------------------------ */
  YOUTUBE_API_KEY: "AIzaSyCv9pfzaF8dhqKAUVnTcmg3c1A0brp6hp4",

  /* The church's YouTube channel. Only change this if the
     channel itself ever changes. */
  YOUTUBE_CHANNEL_ID: "UClKBeXx4kDf8QKllZlFo-hg",
  YOUTUBE_CHANNEL_URL: "https://youtube.com/@omegalivingbridetabernacle"
};

/* ---------------- nothing below needs editing ---------------- */

(function (cfg) {
  "use strict";
  var id = (cfg.GA4_ID || "").trim();
  if (!/^G-[A-Z0-9]+$/i.test(id)) return;   // not set, or mistyped, so stay off

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag("js", new Date());
  window.gtag("config", id);
})(window.OLBT_CONFIG);
