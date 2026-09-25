# -*- coding: utf-8 -*-
"""Visit, Sermons, Audio, Albums, Contact, Thank-you, Give, About, 404."""

from build_pages import page, MAPS_EMBED, MAPS_LINK, EMAIL, WHATSAPP, PHONE_DISPLAY, PHONE_E164, YOUTUBE

# ------------------------------------------------------------------ VISIT

visit = """
    <section class="page-hero">
      <p class="eyebrow">Plan your visit</p>
      <h1>Your first time with us</h1>
      <p>Everything you need to know before you walk through the door in Effurun, Warri &mdash; no surprises.</p>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="split">
          <div>
            <h2>Service times</h2>
            <table class="times-table">
              <tr><th>Sunday service</th><td>9:00 AM &ndash; 12:30 PM</td></tr>
              <tr><th>Midweek service</th><td>Wednesday, 5:00 PM &ndash; 6:45 PM</td></tr>
              <tr><th>Midweek service</th><td>Friday, 5:00 PM &ndash; 6:45 PM</td></tr>
            </table>

            <h2 style="margin-top:2.5rem;">Where to find us</h2>
            <p>11 Ejoyokah Street, Opposite Praise Centre, Jakpa Road<br />
               Effurun, Warri, Delta State<br />Nigeria</p>
            <p><a href="tel:%(phone_e164)s">%(phone)s</a></p>
            <p>
              <a class="btn btn-gold" href="%(maps)s" rel="noopener">Get directions</a>
              <a class="btn btn-outline" href="%(wa)s" rel="noopener">Ask on WhatsApp</a>
            </p>
          </div>

          <div class="map-frame">
            <iframe src="%(map)s"
                    title="Map to Omega Living Bride Tabernacle, Effurun, Warri"
                    loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
        </div>
      </div>

      <div class="omega-divider" aria-hidden="true"><span>&Omega;</span></div>
    </section>

    <section class="section section-tint">
      <div class="wrap prose">
        <div class="photo-band" style="aspect-ratio:16/10; margin-bottom:2.5rem;">
          <picture>
            <source type="image/webp" srcset="/assets/img/congregation-1000.webp 1000w, /assets/img/congregation-1600.webp 1600w" sizes="(max-width: 700px) 100vw, 68ch" />
            <img src="/assets/img/congregation-1000.jpg"
                 srcset="/assets/img/congregation-1000.jpg 1000w, /assets/img/congregation-1600.jpg 1600w"
                 sizes="(max-width: 700px) 100vw, 68ch" loading="lazy"
                 alt="Inside Omega Living Bride Tabernacle during a Sunday service in Effurun, Warri"
                 width="1600" height="1200" />
          </picture>
        </div>

        <h2>What happens in a service</h2>
        <p>We begin with singing and prayer. There is a time of worship, then the Word is preached &mdash; usually for an hour or more, because the teaching is the heart of what we do. We close in prayer. A Sunday service normally runs until about 12:30.</p>

        <ul class="visit-list">
          <li>
            <h3>What should I wear?</h3>
            <p>Modest, respectful dress. Most of the brothers wear shirts and trousers; the sisters wear dresses or skirts. You will not be turned away or singled out over clothing on your first visit.</p>
          </li>
          <li>
            <h3>Will I be put on the spot?</h3>
            <p>No. Visitors are welcomed warmly, but nobody will be asked to stand, speak, or give. You are free to sit, listen, and leave when you wish.</p>
          </li>
          <li>
            <h3>What about my children?</h3>
            <p>Children are welcome in the service with their parents. We also run Sunday school classes for children, teenagers and adults.</p>
          </li>
          <li>
            <h3>Is there parking?</h3>
            <p>Yes. Church officers are on hand to help you park.</p>
          </li>
          <li>
            <h3>Do I need to bring anything?</h3>
            <p>Bring your Bible if you have one. If you don't, that is no obstacle &mdash; come as you are.</p>
          </li>
          <li>
            <h3>What if I am not a believer?</h3>
            <p>You are welcome. Many people first came in simply to listen. There is no pressure, and no requirement to believe anything before you arrive.</p>
          </li>
        </ul>

        <p style="margin-top:2.5rem;">Still have a question? <a href="/contact.html">Write to us</a> and someone will reply.</p>
      </div>
    </section>
""" % dict(map=MAPS_EMBED, maps=MAPS_LINK, wa=WHATSAPP, phone=PHONE_DISPLAY, phone_e164=PHONE_E164)

page("visit.html",
     "Plan Your Visit — Omega Living Bride Tabernacle, Effurun, Warri",
     "Service times, address and what to expect on your first visit to Omega Living Bride "
     "Tabernacle, 11 Ejoyokah Street, Effurun, Warri, Delta State. Sunday 9:00 AM.",
     "/visit.html", visit, label="Visit")


# ------------------------------------------------------------------ SERMONS

sermons = """
    <section class="page-hero">
      <p class="eyebrow">The Word</p>
      <h1>Sermons</h1>
      <p>Messages preached at Omega Living Bride Tabernacle in Effurun, Warri &mdash; archived so you can hear the Word wherever you are.</p>
    </section>

    <section class="section section-dark on-dark center">
      <div class="wrap">
        <p class="eyebrow">Now playing</p>
        <h2>Latest message</h2>
      </div>
      <div class="video-frame" id="latest-video"></div>
      <div class="video-caption" id="latest-caption"></div>
    </section>

    <section class="section">
      <div class="wrap">
        <h2 style="text-align:center;">The archive</h2>
        <p style="text-align:center; margin-inline:auto;">New messages appear here automatically as they are uploaded.</p>
        <p style="text-align:center;">
          <a class="btn btn-gold" href="%(yt)s" rel="noopener">Subscribe on YouTube</a>
          <a class="btn btn-outline" href="/audio.html">Audio sermons</a>
        </p>

        <div class="item-grid" id="sermon-grid"></div>

        <p class="feed-note" id="feed-note" hidden style="color:var(--fg-soft)"></p>

        <p id="sermon-empty" style="text-align:center; margin-top:2rem; display:none;">
          Sermons are being added. In the meantime, watch on
          <a href="%(yt)s" rel="noopener">YouTube</a>.
        </p>
      </div>
    </section>
""" % dict(yt=YOUTUBE)

page("sermons.html",
     "Sermons — Omega Living Bride Tabernacle, Effurun, Warri",
     "Sermon archive from Omega Living Bride Tabernacle, Effurun, Warri. Messages on the "
     "Seven Seals, the Seven Church Ages, Revelation and the end-time Message.",
     "/sermons.html", sermons, label="Sermons",
     scripts='  <script src="/js/youtube.js"></script>')


# ------------------------------------------------------------------ AUDIO

audio = """
    <section class="page-hero">
      <p class="eyebrow">Listen</p>
      <h1>Audio sermons</h1>
      <p>Older messages and recordings for listening or download &mdash; light on data, so you can take the Word with you.</p>
    </section>

    <section class="section">
      <div class="wrap">
        <p style="text-align:center; margin-inline:auto;">
          Every recording can be played here or downloaded to your phone.
          Video messages are on the <a href="/sermons.html">sermons page</a>.
        </p>

        <div class="item-grid" id="audio-grid"></div>

        <div id="audio-empty" hidden style="text-align:center; margin-top:2rem;">
          <p style="margin-inline:auto;">The audio archive is being prepared. Messages will
          appear here as they are added.</p>
          <p><a class="btn btn-gold" href="/sermons.html">Watch sermons instead</a></p>
        </div>
      </div>
    </section>
"""

page("audio.html",
     "Audio Sermons — Omega Living Bride Tabernacle, Effurun, Warri",
     "Listen to or download audio sermons from Omega Living Bride Tabernacle, Effurun, "
     "Warri, Delta State. Messages on Revelation, the Seven Seals and the end-time Message.",
     "/audio.html", audio, label="Audio sermons",
     scripts='  <script src="/js/audio-sermons.js"></script>')


# ------------------------------------------------------------------ ALBUMS

albums = """
    <section class="page-hero">
      <p class="eyebrow">Our life together</p>
      <h1>Photo albums</h1>
      <p>Conferences, services and gatherings at Omega Living Bride Tabernacle, Effurun, Warri.</p>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="album-grid" id="album-grid"></div>

        <div id="album-empty" hidden style="text-align:center; margin-top:1rem;">
          <p style="margin-inline:auto;">Albums are being prepared. Photographs from our
          services and conferences will appear here soon.</p>
          <p><a class="btn btn-gold" href="/visit.html">Plan a visit instead</a></p>
        </div>
      </div>
    </section>
"""

page("albums.html",
     "Photo Albums — Omega Living Bride Tabernacle, Effurun, Warri",
     "Photographs from conferences, services and gatherings at Omega Living Bride "
     "Tabernacle, Effurun, Warri, Delta State.",
     "/albums.html", albums, label="Photo albums",
     scripts='  <script src="/js/albums.js"></script>')


# ------------------------------------------------------------------ CONTACT

contact = """
    <section class="page-hero">
      <p class="eyebrow">Get in touch</p>
      <h1>Contact us</h1>
      <p>Write to us with a question, a prayer request, or to ask about visiting the Tabernacle in Effurun, Warri.</p>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="split">
          <div>
            <h2>Send a message</h2>

            <!-- Netlify Forms. Submissions are stored in the Netlify dashboard AND
                 emailed to the church. To switch the email on (once only):
                 Netlify -> Forms -> "contact" -> Settings & usage ->
                 Form notifications -> Add notification -> Email notification ->
                 send to %(email)s -->
            <form name="contact" id="contact-form" method="POST"
                  data-netlify="true" netlify-honeypot="website"
                  action="/thank-you.html">
              <input type="hidden" name="form-name" value="contact" />
              <p hidden><label>Leave this field empty: <input name="website" /></label></p>

              <p>
                <label for="f-name">Your name</label>
                <input id="f-name" type="text" name="Name" autocomplete="name" required />
                <span class="form-error" data-for="f-name">Please tell us your name.</span>
              </p>

              <p>
                <label for="f-email">Email address</label>
                <input id="f-email" type="email" name="Email" autocomplete="email" required />
                <span class="form-error" data-for="f-email">Please enter an email address we can reply to.</span>
              </p>

              <p>
                <label for="f-phone">Phone or WhatsApp <span style="font-weight:400;color:var(--fg-soft)">(optional)</span></label>
                <input id="f-phone" type="tel" name="Phone" autocomplete="tel" />
              </p>

              <p>
                <label for="f-subject">What is this about?</label>
                <select id="f-subject" name="Subject">
                  <option>General enquiry</option>
                  <option>Prayer request</option>
                  <option>Planning a visit</option>
                  <option>A question about the Bible</option>
                  <option>Melchizedec's Conference</option>
                  <option>Giving</option>
                </select>
              </p>

              <p>
                <label for="f-message">Your message</label>
                <textarea id="f-message" name="Message" rows="6" required></textarea>
                <span class="form-error" data-for="f-message">Please write your message before sending.</span>
              </p>

              <p><button class="btn btn-gold" type="submit">Send message</button></p>
            </form>

            <p class="form-hint">Messages go straight to the church inbox at
              <a href="mailto:%(email)s">%(email)s</a>.
              Prayer requests are treated confidentially and shared only with those who pray.</p>
          </div>

          <div>
            <h2>Other ways to reach us</h2>
            <ul class="visit-list">
              <li>
                <h3>WhatsApp</h3>
                <p><a href="%(wa)s" rel="noopener">Chat with us</a> &mdash; usually the fastest reply.</p>
              </li>
              <li>
                <h3>Phone</h3>
                <p><a href="tel:%(phone_e164)s">%(phone)s</a></p>
              </li>
              <li>
                <h3>Email</h3>
                <p><a href="mailto:%(email)s">%(email)s</a></p>
              </li>
              <li>
                <h3>Visit us in Effurun</h3>
                <p>11 Ejoyokah Street, Opposite Praise Centre, Jakpa Road<br />
                   Effurun, Warri, Delta State, Nigeria</p>
                <p><a href="/visit.html">See service times and what to expect</a></p>
              </li>
              <li>
                <h3>YouTube</h3>
                <p><a href="%(yt)s" rel="noopener">Watch our services</a></p>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <script>
    (function () {
      var form = document.getElementById("contact-form");
      if (!form) return;
      function errFor(el) { return form.querySelector('[data-for="' + el.id + '"]'); }
      form.addEventListener("submit", function (e) {
        var bad = null;
        ["f-name", "f-email", "f-message"].forEach(function (id) {
          var el = document.getElementById(id);
          var err = errFor(el);
          var ok = el.value.trim() !== "" && el.checkValidity();
          if (err) err.classList.toggle("show", !ok);
          if (!ok && !bad) bad = el;
        });
        if (bad) { e.preventDefault(); bad.focus(); }
      });
      form.addEventListener("input", function (e) {
        if (!e.target.id) return;
        var err = errFor(e.target);
        if (err) err.classList.remove("show");
      });
    })();
    </script>
""" % dict(email=EMAIL, wa=WHATSAPP, yt=YOUTUBE, phone=PHONE_DISPLAY, phone_e164=PHONE_E164)

page("contact.html",
     "Contact — Omega Living Bride Tabernacle, Effurun, Warri",
     "Contact Omega Living Bride Tabernacle in Effurun, Warri, Delta State. Send a prayer "
     "request, ask a question about the Bible, or plan your visit.",
     "/contact.html", contact, label="Contact")


# ------------------------------------------------------------------ THANK YOU

thanks = """
    <section class="page-hero">
      <p class="eyebrow">Message sent</p>
      <h1>Thank you &mdash; we have your message</h1>
      <p>It has gone to the church inbox. Someone will read it and reply.</p>
    </section>

    <section class="section center">
      <div class="wrap">
        <p>If your message is urgent, WhatsApp is the fastest way to reach us.</p>
        <p>
          <a class="btn btn-gold" href="%(wa)s" rel="noopener">Chat on WhatsApp</a>
          <a class="btn btn-outline" href="/">Back to the homepage</a>
        </p>
      </div>
      <div class="omega-divider" aria-hidden="true"><span>&Omega;</span></div>
    </section>

    <section class="section center">
      <div class="wrap">
        <p class="eyebrow">While you are here</p>
        <h2>Come and worship with us</h2>
        <p>Sunday 9:00 AM &middot; Wednesday and Friday 5:00 PM<br />
           11 Ejoyokah Street, Opposite Praise Centre, Jakpa Road, Effurun, Warri</p>
        <p><a class="btn btn-outline" href="/visit.html">Plan your visit</a></p>
      </div>
    </section>
""" % dict(wa=WHATSAPP)

page("thank-you.html", "Message sent — Omega Living Bride Tabernacle",
     "Your message has been sent to Omega Living Bride Tabernacle, Effurun, Warri.",
     "/thank-you.html", thanks, label="Message sent")


# ------------------------------------------------------------------ 404

notfound = """
    <section class="page-hero">
      <p class="eyebrow">Page not found</p>
      <h1>That page isn't here</h1>
      <p>The link may be old, or the address mistyped.</p>
    </section>

    <section class="section center">
      <div class="wrap">
        <p>Try one of these instead:</p>
        <p>
          <a class="btn btn-gold" href="/">Home</a>
          <a class="btn btn-outline" href="/sermons.html">Sermons</a>
          <a class="btn btn-outline" href="/visit.html">Plan a visit</a>
          <a class="btn btn-outline" href="/contact.html">Contact us</a>
        </p>
      </div>
    </section>
"""

page("404.html", "Page not found — Omega Living Bride Tabernacle",
     "This page could not be found.", "/404.html", notfound, label="Not found")
