# Omega Living Bride Tabernacle — Website

Static site. HTML + CSS + vanilla JS. Deploys to Netlify from Git.
Warri, Delta State, Nigeria.

## Pages

```
index.html                          Homepage
about.html                          About & beliefs
visit.html                          Plan your visit  <- key page for newcomers
sermons.html                        Sermon archive (renders from js/sermons.js)
teachings.html                      Teaching index
teachings/*.html                    One page per topic — PERMANENT URLs
give.html                           Giving
contact.html                        Contact + prayer request (Netlify Forms)
404.html                            Not found
```

## How to add a sermon

Open `js/sermons.js`. Copy one block, paste at the TOP of the list, fill in
the title, date, speaker, scripture, summary, and the YouTube video ID.
The ID is the part of the link after `v=`.

## How to change the menu or footer

Edit `build_pages.py`, then run `python build_pages.py`-generated scripts.
Simplest alternative: find-and-replace across all .html files in VS Code
(Ctrl+Shift+H) — header and footer markup is identical in every file.

## Design system (css/style.css)

- Parchment `#F7F3EA` pages, warm ink `#12100E` anchor sections
- Lampstand gold `#C6A24A`; oxblood `#6B1F2A` used sparingly
- Cormorant Garamond (display) + Source Sans 3 (body)
- Signature element: the Omega divider between sections

## PLACEHOLDER checklist — search all files for "PLACEHOLDER"

Blocking launch:
- [ ] Confirm all service times
- [ ] Full street address + Google Maps embed
- [ ] WhatsApp number (appears in every page footer + float button)
- [ ] Facebook page URL
- [ ] Church bank account details for give.html
- [ ] Pastor's name, bio, and portrait
- [ ] Real sermons in js/sermons.js
- [ ] Pastor approval of every line on about.html
- [ ] Teaching page content written/approved

Assets needed in assets/img/:
- [ ] logo.png — transparent background, 512px
- [ ] favicon.png — 64px
- [ ] og-image.jpg — 1200x630, for WhatsApp link previews
- [ ] Congregation, building, and pastor photographs

## Deploy

Netlify: build command blank, publish directory blank.
Free tier is credit-metered — batch pushes, don't deploy every small edit.
