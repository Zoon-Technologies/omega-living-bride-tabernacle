/* ============================================================
   YOUTUBE — pulls the church's latest uploads automatically
   ------------------------------------------------------------
   Once the key below is filled in, the website updates itself:
   upload to YouTube as normal and the new message appears here.

   HOW TO GET THE KEY  (about five minutes, free)
   1. console.cloud.google.com  ->  sign in with the church Google account
   2. Create a project, call it "Omega Living Bride website"
   3. Menu -> APIs & Services -> Library -> search "YouTube Data API v3"
      -> Enable
   4. Menu -> APIs & Services -> Credentials -> Create credentials
      -> API key. Copy it into YT_API_KEY below.
   5. On that same key click "Edit", then under
      "Application restrictions" choose "Websites" and add:
          https://omegalivingbride.netlify.app/*
          https://omegalivingbride.com/*        (once the domain is live)
      Under "API restrictions" choose "Restrict key" -> YouTube Data API v3.
      Save.

   The free allowance is 10,000 units a day. Each page view costs 1.
   ============================================================ */

var YT_API_KEY = "";                                   // <-- paste the key here
var YT_CHANNEL_ID = "UClKBeXx4kDf8QKllZlFo-hg";        // Omega Living Bride Tabernacle
var YT_CHANNEL_URL = "https://youtube.com/@omegalivingbridetabernacle";

/* ---------------- nothing below needs editing ---------------- */

(function (global) {
  "use strict";

  var CACHE_KEY = "olbt-yt-cache-v1";
  var CACHE_MINUTES = 30;

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function niceDate(iso) {
    var d = new Date(iso);
    if (isNaN(d)) return "";
    return d.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  }

  function readCache() {
    try {
      var raw = sessionStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      if (Date.now() - obj.at > CACHE_MINUTES * 60000) return null;
      return obj.items;
    } catch (e) { return null; }
  }

  function writeCache(items) {
    try {
      sessionStorage.setItem(CACHE_KEY, JSON.stringify({ at: Date.now(), items: items }));
    } catch (e) {}
  }

  // The uploads playlist of any channel is its ID with UC swapped for UU.
  function uploadsPlaylist(channelId) {
    return "UU" + channelId.replace(/^UC/, "");
  }

  var pending = null;

  function fetchVideos(max) {
    var cached = readCache();
    if (cached) return Promise.resolve(cached);
    if (pending) return pending;

    if (!YT_API_KEY) return Promise.reject(new Error("no-key"));

    var url =
      "https://www.googleapis.com/youtube/v3/playlistItems" +
      "?part=snippet&maxResults=" + (max || 12) +
      "&playlistId=" + encodeURIComponent(uploadsPlaylist(YT_CHANNEL_ID)) +
      "&key=" + encodeURIComponent(YT_API_KEY);

    pending = fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("http-" + r.status);
        return r.json();
      })
      .then(function (data) {
        var items = (data.items || [])
          .map(function (it) {
            var sn = it.snippet || {};
            var id = sn.resourceId && sn.resourceId.videoId;
            if (!id) return null;
            var th = sn.thumbnails || {};
            var thumb = (th.maxres || th.standard || th.high || th.medium || th.default || {}).url;
            return {
              id: id,
              title: sn.title || "Untitled message",
              date: sn.publishedAt || "",
              thumb: thumb || "https://i.ytimg.com/vi/" + id + "/hqdefault.jpg",
              description: sn.description || ""
            };
          })
          .filter(Boolean)
          // YouTube hides deleted/private videos behind this title
          .filter(function (v) { return !/^(Deleted|Private) video$/i.test(v.title); });
        writeCache(items);
        return items;
      })
      .catch(function (err) { pending = null; throw err; });

    return pending;
  }

  /* ---------- Renderers ---------- */

  function renderLatest(box, v) {
    box.classList.remove("is-skeleton");
    box.innerHTML =
      '<iframe src="https://www.youtube-nocookie.com/embed/' + esc(v.id) + '?rel=0"' +
      ' title="' + esc(v.title) + '" loading="lazy"' +
      ' allow="accelerometer; encrypted-media; picture-in-picture; web-share"' +
      " allowfullscreen></iframe>";

    var cap = document.getElementById("latest-caption");
    if (cap) {
      cap.innerHTML =
        '<p class="vc-date">' + esc(niceDate(v.date)) + "</p>" +
        '<p class="vc-title">' + esc(v.title) + "</p>";
    }
  }

  function railCard(v) {
    return (
      '<a class="rail-card" href="https://www.youtube.com/watch?v=' + esc(v.id) +
      '" rel="noopener" target="_blank">' +
      '<span class="rail-thumb"><img src="' + esc(v.thumb) + '" alt="" loading="lazy" ' +
      'width="480" height="270" /></span>' +
      '<span class="rail-body">' +
      '<span class="rc-date">' + esc(niceDate(v.date)) + "</span>" +
      '<span class="rc-title">' + esc(v.title) + "</span>" +
      "</span></a>"
    );
  }

  function gridCard(v) {
    return (
      '<article class="item">' +
      '<div class="item-thumb"><img src="' + esc(v.thumb) + '" alt="" loading="lazy" ' +
      'width="480" height="270" /></div>' +
      '<div class="item-body">' +
      '<p class="item-meta">' + esc(niceDate(v.date)) + "</p>" +
      "<h3>" + esc(v.title) + "</h3>" +
      '<a class="item-link" href="https://www.youtube.com/watch?v=' + esc(v.id) +
      '" rel="noopener" target="_blank">Watch</a>' +
      "</div></article>"
    );
  }

  function fallback(msg) {
    var latest = document.getElementById("latest-video");
    var rail = document.getElementById("recent-rail");
    var grid = document.getElementById("sermon-grid");
    var note = document.getElementById("feed-note");

    if (latest) {
      latest.classList.remove("is-skeleton");
      latest.innerHTML =
        '<iframe src="https://www.youtube-nocookie.com/embed?listType=playlist&list=' +
        esc(uploadsPlaylist(YT_CHANNEL_ID)) + '"' +
        ' title="Sermons from Omega Living Bride Tabernacle" loading="lazy"' +
        ' allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    }
    if (rail) rail.innerHTML = "";
    if (grid && !grid.children.length) grid.innerHTML = "";
    if (note) {
      note.hidden = false;
      note.innerHTML =
        esc(msg) + ' <a href="' + esc(YT_CHANNEL_URL) + '" rel="noopener">Open the channel on YouTube</a>.';
    }
  }

  function init() {
    var latest = document.getElementById("latest-video");
    var rail = document.getElementById("recent-rail");
    var grid = document.getElementById("sermon-grid");
    if (!latest && !rail && !grid) return;

    if (rail) {
      rail.innerHTML = new Array(4)
        .fill('<span class="rail-card is-skeleton" style="min-height:190px"></span>')
        .join("");
    }
    if (latest) latest.classList.add("is-skeleton");

    fetchVideos(grid ? 24 : 12)
      .then(function (items) {
        if (!items.length) { fallback("No uploads found yet."); return; }

        if (latest) renderLatest(latest, items[0]);

        if (rail) {
          var rest = items.slice(latest ? 1 : 0, (latest ? 1 : 0) + 8);
          rail.innerHTML = rest.map(railCard).join("");
          if (!rest.length) rail.innerHTML = "";
        }

        if (grid) {
          grid.innerHTML = items.map(gridCard).join("");
          var empty = document.getElementById("sermon-empty");
          if (empty) empty.style.display = "none";
        }
      })
      .catch(function (err) {
        if (err && err.message === "no-key") {
          fallback("The sermon feed is not connected yet.");
        } else {
          fallback("The sermon feed could not be loaded just now.");
        }
      });
  }

  global.OLBTYouTube = { fetchVideos: fetchVideos };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})(window);
