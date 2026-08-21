/* ============================================================
   SERMON ARCHIVE
   To add a sermon, copy one block and paste it at the TOP of the
   list. Only the YouTube video ID is needed — not the full link.

   A YouTube link looks like:
     https://www.youtube.com/watch?v=dQw4w9WgXcQ
   The ID is the part after "v=" :  dQw4w9WgXcQ
   ============================================================ */

const SERMONS = [
  {
    title: "PLACEHOLDER — replace with a real sermon title",
    date: "2026-08-09",
    speaker: "Pastor [name]",
    scripture: "Revelation 10",
    videoId: "VIDEO_ID",
    summary: "One or two sentences describing what this message covers."
  },
  {
    title: "PLACEHOLDER — second sermon",
    date: "2026-08-02",
    speaker: "Pastor [name]",
    scripture: "Revelation 5",
    videoId: "VIDEO_ID",
    summary: "One or two sentences describing what this message covers."
  }
];

/* ---------- Renderer — no need to edit below this line ---------- */

(function renderSermons() {
  const grid = document.getElementById("sermon-grid");
  const empty = document.getElementById("sermon-empty");
  if (!grid) return;

  const live = SERMONS.filter((s) => s.videoId && s.videoId !== "VIDEO_ID");

  if (!live.length) {
    if (empty) empty.style.display = "block";
    return;
  }

  live.sort((a, b) => new Date(b.date) - new Date(a.date));

  grid.innerHTML = live
    .map((s) => {
      const when = new Date(s.date).toLocaleDateString("en-GB", {
        day: "numeric",
        month: "long",
        year: "numeric"
      });
      return `
      <article class="item">
        <div class="item-thumb">
          <img src="https://i.ytimg.com/vi/${s.videoId}/hqdefault.jpg"
               alt="" loading="lazy" width="480" height="360" />
        </div>
        <div class="item-body">
          <p class="item-meta">${when}${s.scripture ? " &middot; " + s.scripture : ""}</p>
          <h3>${s.title}</h3>
          <p>${s.summary || ""}</p>
          <a class="item-link"
             href="https://www.youtube.com/watch?v=${s.videoId}"
             rel="noopener">Watch</a>
        </div>
      </article>`;
    })
    .join("");
})();
