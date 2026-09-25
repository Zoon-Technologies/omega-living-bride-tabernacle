/* ============================================================
   AUDIO SERMON ARCHIVE
   ------------------------------------------------------------
   Add a sermon by copying one block below and pasting it at the
   TOP of the list. Newest first.

   WHERE TO PUT THE MP3 FILES  — please read this once
   ---------------------------------------------------
   Do NOT put mp3 files in this website folder. Audio is large,
   and the hosting plan is metered: one popular sermon could take
   the whole site offline for the rest of the month.

   Use archive.org instead. It is free, permanent, unlimited, and
   built for exactly this:

     1. archive.org/account/signup  (use the church email)
     2. Click "Upload" -> drag the mp3 in
     3. Title it, set the collection to "Community Audio",
        then click "Upload and Create Your Item"
     4. The finished page has an address like
            archive.org/details/olbt-2026-07-19-seven-thunders
        The last part is the IDENTIFIER. Paste it below.

   Fields
   ------
   title       name of the message
   date        "2026-07-19"  (year-month-day)
   speaker     who preached
   scripture   optional, e.g. "Revelation 10"
   summary     one or two sentences
   archiveId   the identifier from archive.org  (preferred)
   fileUrl     OR a direct link to an mp3 hosted somewhere else
   ============================================================ */

const AUDIO_SERMONS = [
  // {
  //   title: "The Sealing And Unsealing Of The Uttered Thunders",
  //   date: "2026-07-19",
  //   speaker: "Pastor Timothy Awowede",
  //   scripture: "Revelation 10",
  //   summary: "A study of what was sealed in Revelation 10 and why it matters now.",
  //   archiveId: "olbt-2026-07-19-seven-thunders"
  // },
];

/* ---------------- nothing below needs editing ---------------- */

(function () {
  "use strict";

  var grid = document.getElementById("audio-grid");
  if (!grid) return;

  var empty = document.getElementById("audio-empty");

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function niceDate(v) {
    var d = new Date(v);
    if (isNaN(d)) return "";
    return d.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  }

  var live = AUDIO_SERMONS.filter(function (s) { return s && (s.archiveId || s.fileUrl); });

  if (!live.length) {
    grid.innerHTML = "";
    if (empty) empty.hidden = false;
    return;
  }

  if (empty) empty.hidden = true;

  live.sort(function (a, b) { return new Date(b.date) - new Date(a.date); });

  grid.innerHTML = live
    .map(function (s) {
      var meta = [niceDate(s.date), s.scripture].filter(Boolean).join(" · ");

      var player, download;
      if (s.archiveId) {
        player =
          '<div class="archive-frame"><iframe src="https://archive.org/embed/' +
          esc(s.archiveId) + '" title="Listen: ' + esc(s.title) +
          '" loading="lazy" allowfullscreen></iframe></div>';
        download =
          '<a href="https://archive.org/download/' + esc(s.archiveId) +
          '" rel="noopener" target="_blank">Download &darr;</a>';
      } else {
        player =
          '<audio class="audio-player" controls preload="none" src="' +
          esc(s.fileUrl) + '">Your browser cannot play audio. ' +
          '<a href="' + esc(s.fileUrl) + '">Download the file</a> instead.</audio>';
        download = '<a href="' + esc(s.fileUrl) + '" download rel="noopener">Download &darr;</a>';
      }

      return (
        '<article class="item audio-item">' +
        '<div class="item-body">' +
        (meta ? '<p class="item-meta">' + esc(meta) + "</p>" : "") +
        "<h3>" + esc(s.title) + "</h3>" +
        (s.speaker ? '<p style="margin-bottom:.5rem;color:var(--fg-soft);font-size:.9rem">' +
          esc(s.speaker) + "</p>" : "") +
        (s.summary ? "<p>" + esc(s.summary) + "</p>" : "") +
        player +
        '<div class="audio-actions">' + download + "</div>" +
        "</div></article>"
      );
    })
    .join("");
})();
