# -*- coding: utf-8 -*-
"""
Rebuild the whole website.

    python3 build_all.py

Run this after editing build_pages.py (menu, footer, address, analytics)
or any of the content_*.py files. It rewrites every .html page plus
sitemap.xml and robots.txt.
"""

import datetime
import glob

import content_home    # noqa: F401  homepage
import content_rest    # noqa: F401  visit, sermons, audio, albums, contact, 404
import content_pages   # noqa: F401  about, give, teachings

from build_pages import SITE_URL


def sitemap():
    skip = {"404.html", "thank-you.html"}
    priority = {
        "index.html": "1.0", "visit.html": "0.9", "sermons.html": "0.9",
        "about.html": "0.8", "teachings.html": "0.8", "contact.html": "0.7",
        "audio.html": "0.7", "albums.html": "0.6", "give.html": "0.6",
    }
    today = datetime.date.today().isoformat()

    rows = []
    for f in sorted(glob.glob("*.html") + glob.glob("teachings/*.html")):
        if f in skip:
            continue
        loc = SITE_URL + ("/" if f == "index.html" else "/" + f)
        rows.append(
            "  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
            % (loc, today, priority.get(f, "0.7"))
        )

    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 + "\n".join(rows) + "\n</urlset>\n")

    with open("robots.txt", "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)

    print("wrote sitemap.xml (%d pages) and robots.txt" % len(rows))


sitemap()
print("\nAll pages rebuilt.")
