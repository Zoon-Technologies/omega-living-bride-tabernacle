# -*- coding: utf-8 -*-
"""
Builds every page with one identical header, footer and <head>.

    python3 build_pages.py

Change something here (menu, footer, address, analytics ID) and re-run:
every page is rewritten. Page CONTENT lives in content_pages.py.
"""

# ------------------------------------------------------------------
# Site-wide settings: the only block most edits need
# ------------------------------------------------------------------

SITE_URL = "https://omegalivingbride.com"
SITE_NAME = "Omega Living Bride Tabernacle"

EMAIL = "omegabridetab@outlook.com"
PHONE_DISPLAY = "+234 704 534 8482"
PHONE_E164 = "+2347045348482"
WHATSAPP = "https://wa.me/2347045348482"

STREET = "11 Ejoyokah Street, Opposite Praise Center, Jakpa Road"
TOWN = "Effurun"
CITY = "Effurun"   # same as TOWN since the address is simply Effurun
REGION = "Delta State"
COUNTRY = "Nigeria"

# What Google is told about the area the church serves. This is reach, not the
# postal address. The address shown to visitors is Effurun everywhere.
AREA_SERVED = "Effurun and the greater Warri area, Delta State, Nigeria"

MAPS_LINK = "https://maps.app.goo.gl/XYi2mtmWdiXzW3t3A"
MAPS_EMBED = (
    "https://www.google.com/maps?q="
    "11+Ejoyokah+Street,+Jakpa+Road,+Effurun,+Delta+State,+Nigeria"
    "&output=embed"
)

YOUTUBE = "https://youtube.com/@omegalivingbridetabernacle"
FACEBOOK = "https://www.facebook.com/share/19QGvEQ5Eq/"
TIKTOK = "https://www.tiktok.com/@omegalivingbride?_r=1&_t=ZS-99py7WfCYy7"

PASTOR = "Pastor Timothy Awowede"

# Google Analytics and the YouTube key now live in js/config.js, so they can
# be changed without rebuilding. Nothing to set here.

SERVICES = [
    ("Sunday service",  "Sunday",    "09:00", "12:30", "9:00 AM – 12:30 PM"),
    ("Midweek service", "Wednesday", "17:00", "18:45", "5:00 PM – 6:45 PM"),
    ("Midweek service", "Friday",    "17:00", "18:45", "5:00 PM – 6:45 PM"),
]

NAV = [
    ("/", "Home", None),
    ("/about.html", "About", None),
    ("/visit.html", "Visit", None),
    (None, "Media", [
        ("/sermons.html", "Sermons (video)"),
        ("/audio.html", "Audio sermons"),
        ("/albums.html", "Photo albums"),
    ]),
    ("/teachings.html", "Teachings", None),
    ("/give.html", "Give", None),
]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500"
         "&family=Source+Sans+3:wght@400;600&display=swap")


# ------------------------------------------------------------------
# Structured data for Google (schema.org)
# ------------------------------------------------------------------

import json as _json


def _hours():
    return [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": "https://schema.org/" + day,
         "opens": opens, "closes": closes}
        for _, day, opens, closes, _ in SERVICES
    ]


def schema_church():
    """Tells Google what this organisation is, where it is and when it meets."""
    return _json.dumps({
        "@context": "https://schema.org",
        "@type": "Church",
        "@id": SITE_URL + "/#church",
        "name": SITE_NAME,
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/logo-dark.png",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "email": EMAIL,
        "telephone": PHONE_E164,
        "description": ("An end-time Message assembly in Effurun, Delta State, Nigeria, "
                        "holding the Bible as the complete Word of God."),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": TOWN,
            "addressRegion": REGION,
            "addressCountry": "NG",
        },
        # The area the church actually serves. Effurun adjoins Warri and the
        # congregation is drawn from across the metropolitan area, so this is a
        # true statement of reach. It is NOT the postal address, which stays
        # Effurun everywhere it is shown to visitors.
        "areaServed": AREA_SERVED,
        "hasMap": MAPS_LINK,
        "sameAs": [YOUTUBE, FACEBOOK, TIKTOK],
        "openingHoursSpecification": _hours(),
        "employee": {"@type": "Person", "name": "Timothy Awowede", "jobTitle": "Pastor"},
    }, indent=2, ensure_ascii=False)


def schema_breadcrumb(path, label):
    """Shows Google the trail Home > This page, for the search result."""
    if path == "/":
        return ""
    return _json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": label, "item": SITE_URL + path},
        ],
    }, indent=2, ensure_ascii=False)


# ------------------------------------------------------------------
# <head>
# ------------------------------------------------------------------

THEME_BOOT = (
    "<script>(function(){try{var m=localStorage.getItem('olbt-theme');"
    "if(!m)m=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';"
    "document.documentElement.setAttribute('data-theme',m);document.documentElement.classList.add('js');}"
    "catch(e){document.documentElement.setAttribute('data-theme','light');}})();</script>"
)


def head(title, desc, path, label, extra_schema=""):
    canonical = SITE_URL + ("/" if path == "/" else path)
    crumbs = schema_breadcrumb(path, label)
    blocks = [schema_church()]
    if crumbs:
        blocks.append(crumbs)
    if extra_schema:
        blocks.append(extra_schema)
    labels = ["Church: who we are, where, and when we meet",
              "Breadcrumb: the trail shown under the search result",
              "Page-specific"]
    ld = "\n\n".join(
        '  <!-- SCHEMA %d of %d: %s -->\n  <script type="application/ld+json">\n%s\n  </script>'
        % (i + 1, len(blocks), labels[i] if i < len(labels) else "Extra", b)
        for i, b in enumerate(blocks)
    )

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- ============================================================
       SEO: page title, Google search snippet, and the one true
       address of this page. Edit these in the content_*.py files.
       ============================================================ -->
  <title>%(title)s</title>
  <meta name="description" content="%(desc)s" />
  <link rel="canonical" href="%(canonical)s" />

  <!-- SOCIAL SHARING: what appears when the link is pasted into
       WhatsApp, Facebook or X. Image is assets/img/og-image.jpg -->
  <meta property="og:site_name" content="%(site)s" />
  <meta property="og:title" content="%(title)s" />
  <meta property="og:description" content="%(desc)s" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="%(canonical)s" />
  <meta property="og:image" content="%(url)s/assets/img/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#12100E" />

  <!-- ICONS: browser tab and phone home screen -->
  <link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" />
  <link rel="icon" href="/assets/img/favicon-64.png" sizes="64x64" />
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png" />

  <!-- FONTS + STYLES -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="%(fonts)s" rel="stylesheet" />
  <link rel="stylesheet" href="/css/style.css" />

  <!-- THEME: sets light or dark before the page paints, so there is
       no flash of the wrong colours. -->
  %(theme)s

  <!-- ============================================================
       GOOGLE ANALYTICS + YOUTUBE
       The measurement ID and the YouTube key live in js/config.js.
       That file loads the Google tag (gtag.js) for you. There is no
       separate Google snippet pasted into these pages, and nothing
       here to edit. Change the keys in js/config.js only.
       ============================================================ -->
  <script src="/js/config.js"></script>
%(ld)s
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
%(header)s
<main id="main">
""" % dict(title=title, desc=desc, canonical=canonical, site=SITE_NAME,
           url=SITE_URL, fonts=FONTS, theme=THEME_BOOT, ld=ld,
           header=header(path))


# ------------------------------------------------------------------
# Header
# ------------------------------------------------------------------

def header(path):
    items = ""
    for href, labeltext, children in NAV:
        if children:
            active = any(path == c[0] for c in children)
            sub = "".join(
                '            <li><a href="%s"%s>%s</a></li>\n'
                % (c[0], ' aria-current="page"' if path == c[0] else "", c[1])
                for c in children
            )
            items += (
                '          <li>\n'
                '            <button class="submenu-toggle" type="button" '
                'aria-expanded="false" aria-controls="submenu-media"%s>%s</button>\n'
                '            <ul class="submenu" id="submenu-media">\n%s'
                '            </ul>\n'
                '          </li>\n'
                % (' aria-current="true"' if active else "", labeltext, sub)
            )
        else:
            cur = ' aria-current="page"' if href == path else ""
            items += '          <li><a href="%s"%s>%s</a></li>\n' % (href, cur, labeltext)

    return """  <header class="site-header">
    <nav class="nav-bar" aria-label="Main navigation">
      <a class="brand" href="/">
        <img src="/assets/img/logo.png" alt="" width="46" height="46" loading="eager" />
        <span class="brand-name">Omega Living Bride<small>Tabernacle</small></span>
      </a>

      <div class="nav-extra">
        <button class="theme-toggle" type="button" data-theme-toggle
                aria-label="Switch to dark mode" aria-pressed="false">
          <svg class="icon-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
          <svg class="icon-sun" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 17a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-13a1 1 0 0 1 1 1v1a1 1 0 0 1-2 0V5a1 1 0 0 1 1-1zm0 14a1 1 0 0 1 1 1v1a1 1 0 0 1-2 0v-1a1 1 0 0 1 1-1zM4 11h1a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm15 0h1a1 1 0 0 1 0 2h-1a1 1 0 0 1 0-2zM5.6 4.2l.7.7a1 1 0 0 1-1.4 1.4l-.7-.7a1 1 0 0 1 1.4-1.4zm12.1 12.1.7.7a1 1 0 0 1-1.4 1.4l-.7-.7a1 1 0 0 1 1.4-1.4zm.7-12.1a1 1 0 0 1 0 1.4l-.7.7a1 1 0 1 1-1.4-1.4l.7-.7a1 1 0 0 1 1.4 0zM6.3 17.7a1 1 0 0 1 0 1.4l-.7.7a1 1 0 0 1-1.4-1.4l.7-.7a1 1 0 0 1 1.4 0z"/></svg>
        </button>

        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
          <span aria-hidden="true">&#9776;</span>
          <span class="sr-only">Menu</span>
        </button>
      </div>

      <ul class="nav-links" id="nav-menu">
%s          <li><a class="btn btn-gold" href="/contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
""" % items


# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------

def footer(scripts=""):
    return """</main>

  <footer class="site-footer">
    <div class="footer-grid">
      <div>
        <h4>%(site)s</h4>
        <ul>
          <li>%(street)s</li>
          <li>%(town)s, %(region)s, %(country)s</li>
          <li><a href="tel:%(phone_e164)s">%(phone)s</a></li>
          <li><a href="mailto:%(email)s">%(email)s</a></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/about.html">About &amp; beliefs</a></li>
          <li><a href="/visit.html">Plan your visit</a></li>
          <li><a href="/sermons.html">Sermons</a></li>
          <li><a href="/audio.html">Audio sermons</a></li>
          <li><a href="/albums.html">Photo albums</a></li>
          <li><a href="/teachings.html">Teachings</a></li>
          <li><a href="/give.html">Give</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul>
          <li><a href="%(yt)s" rel="noopener">YouTube</a></li>
          <li><a href="%(fb)s" rel="noopener">Facebook</a></li>
          <li><a href="%(tt)s" rel="noopener">TikTok</a></li>
          <li><a href="%(wa)s" rel="noopener">WhatsApp</a></li>
          <li><a href="/contact.html">Contact us</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> %(site)s, %(town)s, %(region)s.</span>
      <span>&ldquo;Even so, come, Lord Jesus.&rdquo; &middot; Revelation 22:20</span>
    </div>
  </footer>

  <a class="wa-float" href="%(wa)s" aria-label="Chat with us on WhatsApp" rel="noopener">
    <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.6.8 5 2.3 7L4 29l7.2-2.2c1.9 1 4 1.6 6.3 1.6 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-2 0-3.9-.6-5.5-1.6l-.4-.2-4.3 1.3 1.3-4.1-.3-.4C5.6 18.3 5 16.7 5 15 5 9 9.9 4.1 16 4.1S27 9 27 15s-4.9 9.8-11 9.8zm6-7.3c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2-.2.3-.8 1.1-1 1.3-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-2-1.8-2.3-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6-.1-.2-.7-1.8-1-2.4-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.1 1.3 3.3c.2.2 2.3 3.5 5.5 4.9.8.3 1.4.5 1.9.7.8.2 1.5.2 2 .1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>
  </a>
%(scripts)s
  <script src="/js/main.js"></script>
</body>
</html>
""" % dict(site=SITE_NAME, street=STREET, town=TOWN, city=CITY, region=REGION,
           country=COUNTRY, email=EMAIL, phone=PHONE_DISPLAY, phone_e164=PHONE_E164,
           yt=YOUTUBE, fb=FACEBOOK, tt=TIKTOK, wa=WHATSAPP, scripts=scripts)


# ------------------------------------------------------------------

def page(filename, title, desc, path, body, label=None, scripts="", extra_schema=""):
    import os
    d = os.path.dirname(filename)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(head(title, desc, path, label or title.split(" | ")[0], extra_schema)
                + body + footer(scripts))
    print("wrote", filename)
