# -*- coding: utf-8 -*-
"""Homepage, Visit, Sermons — run via build_all.py"""

from build_pages import page, MAPS_EMBED, MAPS_LINK, SERVICES, PASTOR

TIMES_BAR = """
    <section class="times-bar" aria-label="Service times and location">
      <div class="wrap">
        <span class="tb-item"><span class="tb-label">Sunday</span><span class="tb-value">9:00 AM</span></span>
        <span class="tb-item"><span class="tb-label">Wednesday</span><span class="tb-value">5:00 PM</span></span>
        <span class="tb-item"><span class="tb-label">Friday</span><span class="tb-value">5:00 PM</span></span>
        <span class="tb-item"><span class="tb-label">Where</span><span class="tb-value"><a href="/visit.html">11 Ejoyokah Street, Effurun</a></span></span>
      </div>
    </section>
"""

# ------------------------------------------------------------------ HOME

home = """
    <!-- ============ HERO CAROUSEL: edit js/hero-slides.js ============ -->
    <section class="hero" id="hero" aria-roledescription="carousel"
             aria-label="Omega Living Bride Tabernacle highlights" tabindex="-1">
      <div class="hero-slides" aria-hidden="true"></div>

      <div class="hero-inner">
        <div class="hero-copy" aria-live="polite">
          <!-- Rendered by js/hero.js. Static fallback for no-JS visitors: -->
          <p class="hero-brandline">Effurun &middot; Delta State &middot; Nigeria</p>
          <h1>Omega Living Bride Tabernacle</h1>
          <p class="hero-lede">An end-time Message assembly gathered around the Word of God. Whoever you are, you are welcome here.</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="/visit.html">Plan your visit</a>
            <a class="btn btn-outline" href="/sermons.html">Watch sermons</a>
          </div>
        </div>
      </div>

      <div class="hero-controls">
        <div class="hero-dots" role="group" aria-label="Choose a slide"></div>
        <button class="hero-arrow" type="button" data-prev aria-label="Previous slide">&#8249;</button>
        <button class="hero-arrow" type="button" data-next aria-label="Next slide">&#8250;</button>
      </div>
    </section>
""" + TIMES_BAR + """
    <!-- ============ WHO WE ARE ============ -->
    <section class="section center">
      <div class="wrap">
        <p class="eyebrow">Who we are</p>
        <h2>A Word-centred assembly in Effurun</h2>
        <p>We are a family of believers in Effurun who hold the Bible to be the complete, infallible Word of God, and who believe that God has sent a prophetic Message in this last age to restore His people to that Word and make ready a Bride for the coming of Jesus Christ.</p>
        <p>Whether you have walked with the Lord for decades, are searching honestly for truth, or are simply curious, you are welcome here.</p>
        <a class="btn btn-outline" href="/about.html">Read what we believe</a>
      </div>
      <div class="omega-divider" aria-hidden="true"><span>&Omega;</span></div>
    </section>

    <!-- ============ FROM THE PASTOR'S DESK ============ -->
    <!-- ****************************************************************
         PLACEHOLDER - THE WORDS BELOW ARE A DRAFT ONLY.
         They must be replaced with, or approved by, Pastor Timothy
         Awowede himself before this site is shown to the congregation.
         His name is signed underneath, so the words must be his.
         Replace the photo too once an office portrait is taken.
         **************************************************************** -->
    <section class="section section-tint pastor-desk">
      <div class="wrap">
        <div class="pastor-photo">
          <picture>
            <source type="image/webp" srcset="/assets/img/pastor-820.webp" />
            <img src="/assets/img/pastor-820.jpg"
                 alt="Pastor Timothy Awowede preaching at Omega Living Bride Tabernacle, Effurun"
                 width="820" height="1026" loading="lazy" />
          </picture>
        </div>

        <div>
          <p class="eyebrow">From the pastor's desk</p>
          <blockquote>
            &ldquo;The Word of God is not a tradition we inherited and keep out of habit.
            It is living, and it is able to find a man where he is and change him.
            That is why we open the Bible here without hurry.
            If you are searching, come and sit with us. Bring your questions,
            and let the Scriptures answer them.&rdquo;
            <span class="pastor-sig">
              <strong>Timothy Awowede</strong>
              Pastor, Omega Living Bride Tabernacle
            </span>
          </blockquote>
          <a class="btn btn-outline" href="/about.html">More about the church</a>
        </div>
      </div>
    </section>

    <div class="photo-band">
      <picture>
        <source type="image/webp" srcset="/assets/img/worship-1000.webp 1000w, /assets/img/worship-1600.webp 1600w" sizes="100vw" />
        <img src="/assets/img/worship-1000.jpg"
             srcset="/assets/img/worship-1000.jpg 1000w, /assets/img/worship-1600.jpg 1600w"
             sizes="100vw" loading="lazy"
             alt="Believers gathered together during a service at Omega Living Bride Tabernacle, Effurun"
             width="1600" height="731" />
      </picture>
    </div>

    <!-- ============ LATEST SERMON (pulled from YouTube) ============ -->
    <section class="section section-dark on-dark center">
      <div class="wrap">
        <p class="eyebrow">The Word</p>
        <h2>Latest sermon</h2>
        <p>Every service is uploaded to our YouTube channel, and this page updates itself.</p>
      </div>

      <div class="video-frame" id="latest-video"></div>
      <div class="video-caption" id="latest-caption"></div>

      <div class="rail-head">
        <h3>Recent messages</h3>
        <a href="/sermons.html">All sermons &rarr;</a>
      </div>
      <div class="rail" id="recent-rail" aria-label="Recent uploads"></div>

      <p class="feed-note" id="feed-note" hidden></p>

      <div class="wrap" style="margin-top:1.5rem;">
        <a class="btn btn-outline" href="/sermons.html">Browse the sermon archive</a>
        <a class="btn btn-outline" href="/audio.html">Audio sermons</a>
      </div>
    </section>

    <!-- ============ QUESTIONS ============ -->
    <section class="section">
      <div class="wrap">
        <p class="eyebrow" style="text-align:center;">Honest questions</p>
        <h2 style="text-align:center;">Questions people ask</h2>
        <p style="text-align:center; margin-inline:auto;">Deep things deserve honest answers from the Scriptures. Start with the questions people bring most often.</p>

        <div class="card-grid">
          <article class="card reveal">
            <h3>Who was William Branham?</h3>
            <p>Why we believe God sent a prophet in this generation, and what the Scriptures say about it.</p>
            <a href="/teachings/who-was-william-branham.html">Read the answer</a>
          </article>

          <article class="card reveal">
            <h3>What are the Seven Thunders?</h3>
            <p>Revelation 10 speaks of seven thunders that uttered their voices. What was sealed, and why it matters now.</p>
            <a href="/teachings/seven-thunders.html">Read the answer</a>
          </article>

          <article class="card reveal">
            <h3>What happens after death?</h3>
            <p>What the Bible actually teaches about the soul, eternity, and the hope of the resurrection.</p>
            <a href="/teachings/after-death.html">Read the answer</a>
          </article>

          <article class="card reveal">
            <h3>Is the Bible reliable?</h3>
            <p>An honest look at why we trust the Scriptures as the infallible Word of God.</p>
            <a href="/teachings/is-the-bible-reliable.html">Read the answer</a>
          </article>
        </div>
      </div>
      <div class="omega-divider" aria-hidden="true"><span>&Omega;</span></div>
    </section>

    <!-- ============ VISIT ============ -->
    <section class="section section-tint">
      <div class="wrap">
        <p class="eyebrow">Visit us</p>
        <h2>Worship with us this week</h2>

        <div class="split">
          <div>
            <table class="times-table">
              <tr><th>Sunday service</th><td>9:00 AM &ndash; 12:30 PM</td></tr>
              <tr><th>Midweek service</th><td>Wednesday, 5:00 PM &ndash; 6:45 PM</td></tr>
              <tr><th>Midweek service</th><td>Friday, 5:00 PM &ndash; 6:45 PM</td></tr>
            </table>

            <p style="margin-top:1.5rem;"><strong>Address</strong><br />
            11 Ejoyokah Street, Opposite Praise Center, Jakpa Road<br />
            Effurun, Delta State, Nigeria</p>

            <a class="btn btn-gold" href="/visit.html">Plan your visit</a>
          </div>

          <div class="map-frame">
            <iframe src="%(map)s"
                    title="Map to Omega Living Bride Tabernacle, Effurun"
                    loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
        </div>
      </div>
    </section>
""" % dict(map=MAPS_EMBED)

page("index.html",
     "Omega Living Bride Tabernacle | Church in Effurun, Delta State",
     "Omega Living Bride Tabernacle is an end-time Message assembly in Effurun, "
     "Delta State, Nigeria. Sunday service 9:00 AM, midweek Wednesday and Friday 5:00 PM. "
     "Sermons, teachings and everything you need for a first visit.",
     "/", home, label="Home",
     scripts='  <script src="/js/hero-slides.js"></script>\n'
             '  <script src="/js/hero.js"></script>\n'
             '  <script src="/js/youtube.js"></script>')
