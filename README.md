# Omega Living Bride Tabernacle — Website

Static site. HTML + CSS + vanilla JavaScript. No build step, no framework.
Deploys to Netlify straight from GitHub.

11 Ejoyokah Street, Opposite Praise Centre, Jakpa Road, Effurun, Delta State.

---

## The five files you will actually edit

| To change this | Open this |
|---|---|
| Google Analytics ID and YouTube key | `js/config.js` |
| Homepage banner pictures | `js/hero-slides.js` |
| Audio sermons | `js/audio-sermons.js` |
| Photo albums | `js/albums.js` |
| Menu, footer, address | `build_pages.py`, then run `python3 build_all.py` |

Each of those files begins with plain-English instructions. Nothing else needs touching.

**Important:** page content lives in `content_home.py`, `content_rest.py` and
`content_pages.py`. If you edit a `.html` file by hand, running `build_all.py`
will overwrite it. Either edit the Python and rebuild, or stop using the builder.

---

## Pages

```
index.html            Homepage — carousel, pastor's desk, live YouTube feed
about.html            About, beliefs, pastor
visit.html            Plan your visit — the key page for newcomers
sermons.html          Video sermon archive (pulls from YouTube)
audio.html            Audio sermons (archive.org)
albums.html           Photo albums with lightbox
teachings.html        Teaching index
teachings/*.html      One page per topic — permanent web addresses
give.html             Giving
contact.html          Contact + prayer request (Netlify Forms)
thank-you.html        Shown after the form is sent
404.html              Not found
sitemap.xml           Generated — for Google
robots.txt            Generated
```

---

## Light and dark mode

Light is the site's canonical look. On a first visit the site follows the
visitor's own device setting; the moon/sun button in the header overrides it,
and that choice is remembered on their device.

All colours are CSS variables at the top of `css/style.css`. Change a value
once and both themes follow.

---

## Still to do before launch

**Must be approved by Pastor Timothy Awowede — his name is on them:**
- [ ] The "From the pastor's desk" message on the homepage (currently a DRAFT)
- [ ] His biography on the About page
- [ ] Every line of the beliefs list on the About page
- [ ] All six teaching pages

**Still missing:**
- [ ] Church bank details for `give.html` — get these in writing
- [ ] Google Analytics measurement ID → `GA4_ID` in `js/config.js`
- [ ] YouTube API key → `YOUTUBE_API_KEY` in `js/config.js`
- [ ] A proper office portrait of the pastor (the current photo is an interim
      crop from a preaching shot — replace `assets/img/pastor-820.jpg`)
- [ ] A photograph of the building from outside, for the Visit page
- [ ] Turn the contact form's email notification on (one dashboard setting,
      see below)

**Two details to confirm:**
- The flyer prints the street as "Egoyokah"; the website says "Ejoyokah".
  One of them is wrong.
- Sunday service was listed as ending at both 12:00 and 12:30 in different
  places. The site now says 12:30 everywhere.

**When the real domain goes live:** change `SITE_URL` in `build_pages.py`,
run `python3 build_all.py`, and add the new domain to the YouTube API key
restrictions.

---

## Contact form → church inbox

The form uses Netlify Forms. Submissions are stored in the Netlify dashboard
already. To also have them emailed:

Netlify → **Forms** → **contact** → **Settings & usage** →
**Form notifications** → **Add notification** → **Email notification** →
send to `omegabridetab@outlook.com`.

The fields are named Name, Email, Phone, Subject and Message, so the email
arrives properly laid out rather than as raw code.

---

## A note on privacy

Once Google Analytics is switched on, the site sets cookies and sends visit
data to Google. Nigeria's data protection rules expect a site that does this
to say so. A short privacy page covering analytics, the contact form and the
prayer requests is worth adding before the site is promoted widely.

---

## Two hosting rules that matter

**Never put mp3 or video files in this folder.** The Netlify plan is metered
by the gigabyte. One popular sermon downloaded a hundred times could take the
whole site offline for the rest of the month. Audio goes on archive.org;
video goes on YouTube. `js/audio-sermons.js` explains how.

**Batch your deploys.** Every `git push` spends 15 of the account's 300
monthly credits. Use Live Server locally while working, and push when
something is genuinely finished.

---

## Deploy

```
git add .
git commit -m "describe what changed"
git push
```

Netlify rebuilds within about a minute. Build command: blank.
Publish directory: blank.
