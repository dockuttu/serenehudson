# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzzzz_inbody.py — free InBody 580 body composition scan, both offices (Robin, Oct 10, 2026).
#   Robin: InBody 580 arrives at Hudson and Barboursville; scans start Wed Oct 21, 2026; FREE for everyone, unlimited;
#   15-minute Mangomint service "Free InBody Body Scan" (serviceId 430, Consultations category, all staff, online booking on).
#   Facts (InBody 580 product page): about 30 seconds standing test; 20 impedance measurements at 4 frequencies over 5 body
#   segments; outputs incl. body fat mass, skeletal muscle mass, percent body fat, segmental lean analysis, total body water /
#   ECW-TBW, visceral fat area, basal metabolic rate, phase angle. Not for implanted electronic devices (pacemaker/ICD).
#   No outcome claims; it is not a diagnostic test. Hero image is a Serene graphic (no InBody marketing photos).
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Avoid the bare token "OH" outside titles/eyebrows in this file (the Barboursville localizer rewrites it to "WV").

if "_p" not in globals():
    _BV = (globals().get("SITE_LOC") == "barboursville") if "SITE_LOC" in globals() else ("Barboursville" in globals().get("AREA_TOWNS", []))
    def _p(hud, bv): return bv if _BV else hud
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_IB_BOOK = "https://booking.mangomint.com/serenemedspa?serviceId=430"
if "BOOK_MAP" in globals():
    BOOK_MAP["inbody-body-scan"] = _IB_BOOK
if "HERO_MAP" in globals():
    HERO_MAP["inbody-body-scan"] = "inbody-hero"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG["inbody-body-scan"] = "/img/inbody-hero.jpg"
    RELATED_META["inbody-body-scan"] = ("Free InBody Body Scan", "Muscle, body fat and body water in about a minute. Always free.")

_IB_NOTE = ('The scan is free for everyone, as often as you like, and doesn&rsquo;t require buying anything. '
            'It&rsquo;s a wellness measurement, not a diagnostic test, and it doesn&rsquo;t replace a medical evaluation.')

_IB_PAGE = {
 "slug":"inbody-body-scan","crumb":"Free InBody Body Scan","area_kw":"InBody body composition scan",
 "title":"Free InBody Body Scan in Hudson, OH | Serene Med Spa",
 "desc":("Free InBody 580 body composition scan at Serene Med Spa in Hudson, Ohio, starting October 21. See muscle, body fat and "
         "body water in about a minute, with a printout to keep."),
 "ogtitle":"Free InBody Body Scan in Hudson, OH",
 "ogdesc":"See your muscle, body fat and body water, not just your weight. About a minute, printed results, always free.",
 "proc_name":"InBody 580 body composition analysis","proc_alt":"Multi-frequency bioelectrical impedance body composition scan",
 "how":("The InBody 580 sends a very low, painless electrical signal through your body from hand and foot electrodes while you stand on "
        "the platform. It takes 20 readings at four frequencies across your arms, legs and trunk and uses them to estimate muscle, "
        "fat and body water."),
 "body":"Whole body, arms, legs, trunk",
 "eyebrow":"InBody 580 &middot; Body Composition &middot; Hudson, OH","h1":"Free InBody Body Scan in Hudson, Ohio",
 "hero":("Your scale shows one number. An InBody scan shows what&rsquo;s behind it: muscle, body fat and body water, arm by arm and leg by leg. "
         "It takes about a minute, you get a printout to keep, and it&rsquo;s free, starting Wednesday, October 21."),
 "trust":["Always Free","About 1 Minute","Printed Results","No Needles, No Undressing"],
 "introh2":"Weight is only part of the story",
 "introlead":("Two people can weigh the same and have very different amounts of muscle and fat. When you&rsquo;re losing weight, the scale "
              "can&rsquo;t tell you whether you&rsquo;re losing fat, muscle or water. An InBody scan can."),
 "intropara":("Serene Med Spa in Hudson now has an InBody 580 body composition analyzer, and scans are free for everyone, as often as you "
              "like. It&rsquo;s a helpful starting point and check-in if you&rsquo;re on our <a href=\"/weight-loss/\">medical weight-loss program</a> "
              "(including a GLP-1 medication), building strength, working on body contouring like <a href=\"/evolve-x/\">EvolveX</a>, "
              "or just curious where you stand. Repeat scans under the same conditions show how your body is changing over time. "
              "Results are estimates and vary with hydration, food and time of day."),
 "treyebrow":"What the Scan Measures","treh2":"What you&rsquo;ll see on your results",
 "cards":[
   ("Skeletal Muscle Mass","How much <strong>muscle</strong> you carry, so you can protect it while you lose weight."),
   ("Body Fat Mass &amp; Percent","Your <strong>fat</strong> in pounds and as a percentage of your weight."),
   ("Arms, Legs &amp; Trunk","<strong>Segmental analysis</strong> shows muscle and fat by body area, including left-right balance."),
   ("Visceral Fat","An estimate of the <strong>fat around your organs</strong>, reported as visceral fat area."),
   ("Body Water","<strong>Total body water</strong> and the balance between water inside and outside your cells."),
   ("Basal Metabolic Rate","An estimate of the <strong>calories your body uses at rest</strong>, useful for planning meals."),
 ],
 "steps":[
   ("Book", "Book a free 15-minute visit online or call us. Come a few hours after eating, before any workout."),
   ("Scan", "Take off your shoes and socks, step on the platform and hold the hand electrodes. The scan itself takes about a minute."),
   ("Review", "A member of our team walks you through your printout: muscle, fat, body water and what the numbers mean."),
   ("Re-check", "Scan again every few weeks, at the same time of day, to see how your body composition is changing."),
 ],
 "whyh2":"Why get scanned at Serene in Hudson",
 "whypara":("Serene is physician-led. Your scan is free with no strings attached, and if you want help with your results, our team can "
            "talk you through medical weight loss, strength and nutrition, or body contouring, and tell you plainly what each can and "
            "can&rsquo;t do."),
 "faqh2":"InBody scan FAQ",
 "faqs":[
   ("Is the InBody scan really free?", "Yes. It&rsquo;s free for everyone, as often as you like, with no purchase required. Just book a 15-minute visit."),
   ("When can I get scanned?", "Scans start Wednesday, October 21, 2026, at both Serene Med Spa offices. "
    f"You can <a href=\"{_IB_BOOK}\" target=\"_blank\" rel=\"noopener\">book online</a> now for October 21 or later."),
   ("How do I prepare?", "For the most consistent results: don&rsquo;t eat for 2 to 3 hours before, use the restroom first, skip exercise, "
    "caffeine and alcohol beforehand, don&rsquo;t put lotion on your hands or feet, and wear clothes you can stand comfortably in. "
    "You&rsquo;ll take off your shoes and socks."),
   ("Does it hurt?", "No. The electrical signal is very low and you won&rsquo;t feel it. You simply stand still for about a minute."),
   ("Who shouldn&rsquo;t have an InBody scan?", "Don&rsquo;t have a scan if you have a pacemaker, defibrillator or other implanted electronic "
    "device. If you&rsquo;re pregnant, please call us before booking. Results can be less reliable during your period or if you&rsquo;re "
    "dehydrated or swollen."),
   ("Is it accurate?", "The InBody 580 uses multiple frequencies and measures each arm, leg and the trunk separately. Like any body "
    "composition scan, results are estimates, so the most useful view is the trend over repeat scans taken the same way."),
   ("Is this a medical test?", "No. It&rsquo;s a wellness measurement, not a diagnosis, and it doesn&rsquo;t replace a visit with a clinician."),
 ],
 "related":["weight-loss","evolve-x","hormone-optimization"],
 "pricing_html":_price_block("Pricing","InBody body composition scan",[
    ("InBody 580 Body Scan","Free","About 15 minutes &middot; printed results to take home"),
    ("Repeat scans","Free","As often as you like &middot; same time of day is best"),
 ], _IB_NOTE),
 "book_label":"Book Your Free Scan",
 "ctah2":"Get your free InBody scan",
 "ctapara":"Book a free 15-minute scan with our Hudson team, starting October 21.",
}

if not any(pg.get("slug") == _IB_PAGE["slug"] for pg in PAGES6):
    PAGES6.append(_IB_PAGE)
