/* ============================================================
   HOMEPAGE HERO SLIDES
   ------------------------------------------------------------
   This is the ONLY file you edit to change the homepage pictures.

   To add a slide, copy one block { ... } and paste it where you
   want it to appear. The first block in the list shows first.

   Fields
   ------
   img       the picture, e.g. "/assets/img/slide-conference-1100.jpg"
   imgSmall  optional smaller copy for phones (falls back to img)
   fit       "cover"   fills the whole banner  (use for photographs)
             "contain" shows the WHOLE picture (use for flyers/posters)
   alt       plain description, for screen readers and Google
   eyebrow   small gold line above the heading
   title     the big heading
   text      one or two sentences underneath
   ctaLabel  button text            (leave out for no button)
   ctaHref   where the button goes
   cta2Label optional second button
   cta2Href

   TIP for flyers: save them as-is and use fit: "contain".
   ============================================================ */

const HERO_SLIDES = [
  {
    img: "/assets/img/slide-conference-1100.jpg",
    imgSmall: "/assets/img/slide-conference-760.jpg",
    fit: "contain",
    alt: "Melchizedec's Conference 2026 — Where are we at in this Abrahamic age? 22 to 27 December 2026 at Omega Living Bride Tabernacle, Effurun",
    eyebrow: "22 – 27 December 2026 · Free feeding",
    title: "Melchizedec's Conference '26",
    text: "“Where are we at in this Abrahamic age?” Six days of the Word — mornings 8:30, evenings 4:30. You are cordially invited.",
    ctaLabel: "Plan your visit",
    ctaHref: "/visit.html",
    cta2Label: "Ask about the conference",
    cta2Href: "/contact.html"
  },
  {
    img: "/assets/img/slide-preaching-1920.jpg",
    imgSmall: "/assets/img/slide-preaching-800.jpg",
    fit: "cover",
    alt: "Pastor Timothy Awowede preaching from the pulpit at Omega Living Bride Tabernacle, Effurun",
    eyebrow: "Effurun · Delta State · Nigeria",
    title: "Omega Living Bride Tabernacle",
    text: "An end-time Message assembly gathered around the Word of God. Whoever you are, you are welcome here.",
    ctaLabel: "Plan your visit",
    ctaHref: "/visit.html",
    cta2Label: "Watch sermons",
    cta2Href: "/sermons.html"
  },
  {
    img: "/assets/img/slide-worship-1920.jpg",
    imgSmall: "/assets/img/slide-worship-800.jpg",
    fit: "cover",
    alt: "The congregation of Omega Living Bride Tabernacle standing together in worship",
    eyebrow: "Sundays at 9:00 AM",
    title: "Come and worship with us",
    text: "Singing, prayer, and the Word preached without hurry — because the teaching is the heart of what we do.",
    ctaLabel: "What to expect",
    ctaHref: "/visit.html"
  },
  {
    img: "/assets/img/slide-family-1920.jpg",
    imgSmall: "/assets/img/slide-family-800.jpg",
    fit: "cover",
    alt: "Families and children worshipping together at Omega Living Bride Tabernacle",
    eyebrow: "Every age, every family",
    title: "Room for your whole family",
    text: "Sunday school for children, teenagers and adults. Little ones are welcome in the service with their parents.",
    ctaLabel: "Bringing children?",
    ctaHref: "/visit.html"
  }
];

/* How many seconds each slide stays before the next one. */
const HERO_INTERVAL_SECONDS = 7;
