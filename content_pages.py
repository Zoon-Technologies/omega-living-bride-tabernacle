# -*- coding: utf-8 -*-
"""About, Give, Teachings index, and the individual teaching pages."""

from build_pages import page, EMAIL, WHATSAPP

# ------------------------------------------------------------------ ABOUT

about = """
    <section class="page-hero">
      <p class="eyebrow">About us</p>
      <h1>Who we are</h1>
      <p>An end-time Message assembly in Effurun, Delta State, gathered around the Word of God.</p>
    </section>

    <section class="section">
      <div class="wrap prose">

        <h2>In plain words</h2>
        <p>Omega Living Bride Tabernacle is a church in Effurun. We meet on Sundays and midweek to pray, to sing, and above all to hear the Bible taught.</p>
        <p>We believe the Bible is the complete and infallible Word of God. We believe that God has always sent prophets to call His people back to that Word, and that in this last age He sent such a ministry through William Marrion Branham. He came not to add to Scripture, but to open it, and to make ready a people prepared for the return of Jesus Christ.</p>
        <p>If that is unfamiliar to you, you are still welcome. You do not have to agree with us to sit with us. Come, listen, and search the Scriptures for yourself.</p>

        <blockquote>Prove all things; hold fast that which is good.<cite>1 Thessalonians 5:21</cite></blockquote>

        <h2>What we believe</h2>
        <!-- ****************************************************************
             PLACEHOLDER - every line below is a draft and must be confirmed
             or rewritten by Pastor Timothy Awowede before launch.
             **************************************************************** -->
        <ul class="belief-list">
          <li><strong>The Word of God</strong>The Bible is the inspired, complete and infallible Word of God, and the final authority for all faith and conduct.</li>
          <li><strong>One God</strong>There is one God, who revealed Himself fully in Jesus Christ: God manifested in flesh.</li>
          <li><strong>Salvation in Christ</strong>Salvation is by grace through faith in the finished work of Jesus Christ at Calvary, and by no other means.</li>
          <li><strong>Water baptism</strong>Believers are baptised by immersion in the Name of the Lord Jesus Christ.</li>
          <li><strong>The Holy Spirit</strong>The baptism of the Holy Spirit is the promise of the Father to every believer.</li>
          <li><strong>The end-time Message</strong>God sent the prophetic ministry of Malachi 4:5&ndash;6 and Revelation 10:7 in this last age to restore the hearts of the children to the faith of the apostolic fathers.</li>
          <li><strong>The return of Christ</strong>Jesus Christ is coming again, bodily and visibly, for a Bride made ready by His Word.</li>
        </ul>

        <h2>Our name</h2>
        <p>&ldquo;Omega&rdquo; speaks of the last: the final age of the church before the coming of the Lord. &ldquo;Living Bride&rdquo; speaks of what the Scripture calls the true church: not a building or an organisation, but a people joined to Christ as a wife to a husband. &ldquo;Tabernacle&rdquo; is the place of meeting, where God comes down to dwell among His people.</p>
      </div>
    </section>

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
          <p class="eyebrow">Our pastor</p>
          <h2>Timothy Awowede</h2>
          <!-- PLACEHOLDER - a short account of the pastor's calling and ministry,
               in his own words or approved by him, replaces the paragraph below. -->
          <p>Pastor Timothy Awowede leads the assembly at Omega Living Bride Tabernacle, Effurun, where he teaches through the Scriptures week by week.</p>
          <p>[A short account of his calling and ministry, to be supplied by the pastor.]</p>
          <p><a class="btn btn-outline" href="/sermons.html">Hear him teach</a></p>
        </div>
      </div>
    </section>

    <section class="section center">
      <div class="wrap">
        <p>Come and see for yourself. You will not be singled out, and nothing is asked of you.</p>
        <p><a class="btn btn-gold" href="/visit.html">Plan your visit</a></p>
      </div>
    </section>
"""

page("about.html",
     "About | Omega Living Bride Tabernacle, Effurun",
     "Who we are and what we believe. An end-time Message assembly in Effurun, "
     "Delta State, Nigeria, pastored by Timothy Awowede. All are welcome.",
     "/about.html", about, label="About")


# ------------------------------------------------------------------ GIVE

give = """
    <section class="page-hero">
      <p class="eyebrow">Giving</p>
      <h1>Give</h1>
      <p>Supporting the work of the Lord at Omega Living Bride Tabernacle, Effurun.</p>
    </section>

    <section class="section">
      <div class="wrap prose">
        <p>Giving is an act of worship between you and God, offered freely and without compulsion. Nothing here is a requirement of fellowship, and no one is pressured to give.</p>

        <blockquote>Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver.<cite>2 Corinthians 9:7</cite></blockquote>

        <h2>Bank transfer</h2>
        <p>Tap any line below to copy it.</p>

        <ul class="bank-details">
          <li>
            <span class="bd-label">Account name</span>
            <span class="bd-value" id="bd-name">Omega Living Bride Tabernacle</span>
            <button type="button" class="copy-btn" data-copy="Omega Living Bride Tabernacle"
                    aria-label="Copy the account name">Copy</button>
          </li>
          <li>
            <span class="bd-label">Bank</span>
            <span class="bd-value">Guaranty Trust Bank (GTB)</span>
            <button type="button" class="copy-btn" data-copy="Guaranty Trust Bank (GTB)"
                    aria-label="Copy the bank name">Copy</button>
          </li>
          <li>
            <span class="bd-label">Account number</span>
            <span class="bd-value bd-account">0243683348</span>
            <button type="button" class="copy-btn" data-copy="0243683348"
                    aria-label="Copy the account number">Copy</button>
          </li>
        </ul>

        <p class="bank-actions">
          <button type="button" class="btn btn-gold copy-btn"
                  data-copy="Omega Living Bride Tabernacle&#10;Guaranty Trust Bank (GTB)&#10;0243683348"
                  aria-label="Copy all three bank details together">Copy all details</button>
        </p>

        <p class="bank-note">Always check the account name reads <strong>Omega Living Bride Tabernacle</strong> before you send anything. If a message or flyer gives you different details for this church, confirm with us first on <a href="%(wa)s" rel="noopener">WhatsApp</a> or by <a href="/contact.html">writing to us</a>.</p>

        <h2>In person</h2>
        <p>Offerings may also be given during any service at the Tabernacle in Effurun.</p>

        <p style="margin-top:2rem; font-size:0.94rem; color:var(--fg-soft);">If you have a question about giving, or wish to designate a gift for a particular purpose, please <a href="/contact.html">write to us</a>.</p>
      </div>
    </section>

    <script>
    (function () {
      function flash(btn, text) {
        var original = btn.getAttribute("data-label") || btn.textContent;
        btn.setAttribute("data-label", original);
        btn.textContent = text;
        btn.classList.add("is-copied");
        clearTimeout(btn._t);
        btn._t = setTimeout(function () {
          btn.textContent = btn.getAttribute("data-label");
          btn.classList.remove("is-copied");
        }, 1800);
      }

      function legacyCopy(value) {
        var box = document.createElement("textarea");
        box.value = value;
        box.setAttribute("readonly", "");
        box.style.position = "fixed";
        box.style.opacity = "0";
        document.body.appendChild(box);
        box.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
        document.body.removeChild(box);
        return ok;
      }

      document.addEventListener("click", function (e) {
        var btn = e.target.closest(".copy-btn");
        if (!btn) return;
        var value = btn.getAttribute("data-copy");
        if (!value) return;

        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(value).then(
            function () { flash(btn, "Copied"); },
            function () { flash(btn, legacyCopy(value) ? "Copied" : "Press Ctrl+C"); }
          );
        } else {
          flash(btn, legacyCopy(value) ? "Copied" : "Press Ctrl+C");
        }
      });
    })();
    </script>
""" % dict(wa=WHATSAPP)

page("give.html",
     "Give | Omega Living Bride Tabernacle, Effurun",
     "Supporting the work of Omega Living Bride Tabernacle in Effurun, Delta State. "
     "Bank transfer details and giving information.",
     "/give.html", give, label="Give")


# ------------------------------------------------------------------ TEACHINGS INDEX

TOPICS = [
    ("is-the-bible-reliable", "Is the Bible reliable?", "Foundations",
     "Why we hold the Scriptures to be the complete and infallible Word of God."),
    ("who-was-william-branham", "Who was William Branham?", "Foundations",
     "A plain account of the ministry, and the Scriptures we believe it fulfils."),
    ("seven-thunders", "The Seven Thunders", "Revelation",
     "Revelation 10 speaks of seven thunders that uttered their voices. What was sealed, and why it matters."),
    ("seven-church-ages", "The Seven Church Ages", "Revelation",
     "The seven churches of Asia and the seven ages of church history they portray."),
    ("seven-seals", "The Seven Seals", "Revelation",
     "The opening of the sealed book of Revelation 5 and 6."),
    ("after-death", "What happens after death?", "Last things",
     "What the Bible teaches about the soul, eternity, and the hope of the resurrection."),
]

cards = "".join(
    """
          <article class="item">
            <div class="item-body">
              <p class="item-meta">%s</p>
              <h3>%s</h3>
              <p>%s</p>
              <a class="item-link" href="/teachings/%s.html">Read</a>
            </div>
          </article>
""" % (cat, title, blurb, slug)
    for slug, title, cat, blurb in TOPICS
)

teachings = """
    <section class="page-hero">
      <p class="eyebrow">Search the Scriptures</p>
      <h1>Teachings</h1>
      <p>Honest answers to the questions people actually ask, taken from the Bible and set out plainly.</p>
    </section>

    <section class="section">
      <div class="wrap">
        <h2 style="text-align:center;">Questions people ask</h2>
        <p style="text-align:center; margin-inline:auto;">Start anywhere. Each answer stands on its own.</p>

        <div class="item-grid">%s        </div>

        <p style="text-align:center; margin-top:2.5rem;">Have a question that isn't answered here? <a href="/contact.html">Write to us.</a></p>
      </div>
    </section>
""" % cards

page("teachings.html",
     "Teachings | Omega Living Bride Tabernacle, Effurun",
     "Bible teachings and answers to difficult questions: the Seven Seals, the Seven Church "
     "Ages, the Seven Thunders of Revelation 10, and more.",
     "/teachings.html", teachings, label="Teachings")


# ------------------------------------------------------------------ TEACHING PAGES

BODIES = {
    "seven-thunders": """
        <blockquote>And when the seven thunders had uttered their voices, I was about to write: and I heard a voice from heaven saying unto me, Seal up those things which the seven thunders uttered, and write them not.<cite>Revelation 10:4</cite></blockquote>

        <h2>The passage</h2>
        <p>[Set out what John saw in Revelation 10: the mighty angel, the little book, the seven thunders, and the command to seal.]</p>

        <h2>Why they were sealed</h2>
        <p>[Explain the sealing and what it implies about the timing of their revelation.]</p>

        <h2>What this means for us</h2>
        <p>[The practical and prophetic significance for the believer today.]</p>
""",
    "who-was-william-branham": """
        <h2>If you have never heard the name</h2>
        <p>[A short, plain-English introduction for a complete newcomer: who he was, when he lived, what he did. Assume no prior knowledge and no shared vocabulary.]</p>

        <h2>The Scriptures we believe this fulfils</h2>
        <blockquote>Behold, I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD.<cite>Malachi 4:5</cite></blockquote>
        <p>[Set out Malachi 4:5&ndash;6 and Revelation 10:7, and explain the connection.]</p>

        <h2>What we do not claim</h2>
        <p>[Important for honest readers: state plainly what is <em>not</em> being claimed, namely that nothing is added to Scripture that the Bible remains the final authority.]</p>

        <h2>Judge it for yourself</h2>
        <p>[Invite the reader to examine the recorded ministry directly rather than take anyone's word for it. Link to Voice of God Recordings.]</p>
""",
    "is-the-bible-reliable": """
        <h2>The question honestly stated</h2>
        <p>[State the objection fairly, as a sceptic would put it. Readers trust a page that does this.]</p>

        <h2>The manuscript evidence</h2>
        <p>[Manuscript transmission, and what it does and does not prove.]</p>

        <h2>Fulfilled prophecy</h2>
        <p>[Prophecy as internal evidence.]</p>

        <h2>The witness of the Spirit</h2>
        <p>[The believer's own confirmation.]</p>
""",
}

GENERIC = """
        <h2>The passage</h2>
        <p>[Scripture and context.]</p>

        <h2>What it means</h2>
        <p>[Exposition.]</p>

        <h2>Why it matters</h2>
        <p>[Application for the believer today.]</p>
"""

for slug, title, cat, blurb in TOPICS:
    body = """
    <section class="page-hero">
      <p class="eyebrow">%s</p>
      <h1>%s</h1>
    </section>

    <section class="section">
      <div class="wrap prose">
        <p style="color:var(--fg-soft)"><em>This page is written and ready for its content. The
        teaching below must be written or approved by Pastor Timothy Awowede before publication.</em></p>
%s
        <p style="margin-top:3rem; padding-top:1.5rem; border-top:1px solid var(--line);">
          <a href="/teachings.html">&larr; All teachings</a> &nbsp;&middot;&nbsp;
          <a href="/contact.html">Ask us a question</a> &nbsp;&middot;&nbsp;
          <a href="/sermons.html">Hear it preached</a>
        </p>
      </div>
    </section>
""" % (cat, title, BODIES.get(slug, GENERIC))

    page("teachings/%s.html" % slug,
         "%s | Omega Living Bride Tabernacle, Effurun" % title,
         "%s A Bible teaching from Omega Living Bride Tabernacle, Effurun, Delta State."
         % blurb,
         "/teachings/%s.html" % slug, body, label=title)
