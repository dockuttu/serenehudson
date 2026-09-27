# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzzz_define.py — InMode Define + OptimasMAX device pages (both offices), Sep 27, 2026.
#   Robin: Define at both offices, priced at the low end. Each Define session = hands-free Define Chin or Define Cheek
#   headset + Forma finishing (InMode's own Define + Forma bundles). Morpheus8 is an add-on at Morpheus8 pricing.
#     Hudson:        one zone $199 / 6 for $999;  chin + cheek $329 / 6 for $1,699
#     Barboursville: one zone $179 / 6 for $899;  chin + cheek $279 / 6 for $1,399
#   * new page /define/      (Define Cheek, Define Chin, Forma, Morpheus8 on one workstation)
#   * new page /optimasmax/  (hub: Lumecca Peak, Morpheus8 Burst / Burst Deep, Forma, DiolazeXL, Fusion Light / Dark)
#   * /forma/ gets InMode Forma before/afters, a Forma card image and links to Define + OptimasMAX
#   Facts: InMode Define workstation page (Define Cheek + Define Chin hands-free bipolar RF headsets, Forma, Morpheus8);
#   InMode "benefit selling" sheet (4-8 sessions; read or use your phone during treatment). Lumecca limits as in the
#   OptimasMAX file (not skin types V-VI, not tanned skin, not leg veins). Hair removal wording: "long-term hair reduction".
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Avoid the bare token "OH" outside titles/eyebrows in this file (the Barboursville localizer rewrites it to "WV").

if "_p" not in globals():
    _BV = (globals().get("SITE_LOC") == "barboursville") if "SITE_LOC" in globals() else ("Barboursville" in globals().get("AREA_TOWNS", []))
    def _p(hud, bv): return bv if _BV else hud
if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

# ---- Define prices (Robin, Sep 27, 2026) ----
_DEF1, _DEF16 = _p("$199", "$179"), _p("$999", "$899")
_DEF1_EACH, _DEF1_SAVE = _p("about $167", "about $150"), _p("$195", "$175")
_DEF2, _DEF26 = _p("$329", "$279"), _p("$1,699", "$1,399")
_DEF2_EACH, _DEF2_SAVE = _p("about $283", "about $233"), "$275"
_M8 = "$800"
_LHR_FROM = _p("$59", "$49")

if "HERO_MAP" in globals():
    HERO_MAP.update({"define": "define-hero", "optimasmax": "optimasmax-hero", "forma": "forma-card"})
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.update({"define": "/img/define-hero.jpg", "optimasmax": "/img/optimasmax-hero.jpg", "forma": "/img/forma-card.jpg"})
    RELATED_META["define"] = ("Define by InMode", "Hands-free contouring for the cheeks, jawline and under-chin. From " + _DEF1 + ".")
    RELATED_META["optimasmax"] = ("OptimasMAX by InMode", "Lumecca Peak, Morpheus8 Burst, Forma and laser hair removal on one platform.")
    RELATED_META["forma"] = ("Forma", "Gentle radiofrequency skin tightening, no downtime.")
    RELATED_META.setdefault("lumecca", ("Lumecca Peak IPL", "Sun spots and redness, often cleared in 1&ndash;2 sessions."))
    RELATED_META.setdefault("laser-hair-removal", ("Laser Hair Removal", "Long-term hair reduction for every skin type."))
    IMG.setdefault("lumecca", "/img/lumecca-hero.jpg")
    IMG.setdefault("laser-hair-removal", "/img/fusion-treatment.jpg")

_NOTE = "Photos courtesy of InMode, from other practices. They are not Serene Med Spa patients. Individual results vary."

def _gal2(eyebrow, h2, items, note=_NOTE, intro="Clinical photos from InMode. The treating provider is named on each photo.", sid=""):
    figs = "".join(f'<figure class="res reveal"><img loading="lazy" src="/img/{f}.jpg" alt="{alt}" style="height:auto;aspect-ratio:auto"><figcaption>{cap}</figcaption></figure>'
                   for f, cap, alt in items)
    return ('<section class="results"' + (f' id="{sid}"' if sid else '') + '><div class="wrap"><div class="section-head reveal"><div class="eyebrow">' + eyebrow + '</div>'
            '<h2>' + h2 + '</h2><p>' + intro + '</p></div>'
            '<div class="res-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));align-items:start">' + figs + '</div>'
            '<p class="rev-note">' + note + '</p></div></section>')

# ================================================================ DEFINE ================================================================
_DEF_GALLERY = _gal2("Clinical Photos", "Define before &amp; after", [
    ("define-ba-front-1", "Jawline &amp; neck, 3 months &mdash; Define", "Before and after InMode Define of the jawline and neck, front view"),
    ("define-ba-side-1", "Under-chin &amp; jawline, 3 months &mdash; Define", "Before and after InMode Define of the under-chin and jawline, side view"),
    ("define-ba-side-2", "Jawline &amp; neck &mdash; Define", "Before and after InMode Define of the jawline and neck, left side"),
    ("define-forma-ba-side", "Jawline &amp; under-chin &mdash; Define + Forma", "Before and after InMode Define with Forma of the jawline and under-chin"),
    ("define-m8-ba-side", "Jawline &amp; skin texture, 6 weeks &mdash; Define + Morpheus8", "Before and after InMode Define with Morpheus8 of the lower face, right side"),
], sid="define-results")

_DEF_NOTE = ('Each session includes Forma. Series are standing prices and can&rsquo;t be combined with another discount; series sessions don&rsquo;t expire. '
             'The consultation is complimentary. See the full <a href="/pricing/">price list</a>.')
_DEF_ROWS = [
    ("Define &mdash; Chin or Cheek", _DEF1 + " / session", "One zone, hands-free, finished with Forma &middot; about 30&ndash;45 minutes"),
    ("Define &mdash; Series of 6 (one zone)", _DEF16, _DEF1_EACH[0].upper() + _DEF1_EACH[1:] + " a session &middot; save " + _DEF1_SAVE),
    ("Define &mdash; Chin + Cheek", _DEF2 + " / session", "Both zones, finished with Forma &middot; about 45&ndash;60 minutes"),
    ("Define &mdash; Series of 6 (chin + cheek)", _DEF26, _DEF2_EACH[0].upper() + _DEF2_EACH[1:] + " a session &middot; save " + _DEF2_SAVE),
    ("Add Morpheus8", "From " + _M8, "For texture, lines and deeper tightening &middot; <a href=\"/morpheus8/\">Morpheus8 pricing</a>"),
    ("Consultation", "Complimentary", "We map your zones and build the plan"),
]

_DEF_PAGE = {
 "slug":"define","crumb":"Define by InMode","area_kw":"Define by InMode facial contouring",
 "title":"Define by InMode in Hudson, OH | " + _DEF1 + " or 6 for " + _DEF16 + " | Serene",
 "desc":("Define by InMode in Hudson, Ohio: hands-free radiofrequency that firms the cheeks, jawline and under-chin, finished with Forma. "
         "No needles, no downtime. " + _DEF1 + " a session or 6 for " + _DEF16 + "."),
 "ogtitle":"Define by InMode in Hudson, OH",
 "ogdesc":"Hands-free facial contouring for the cheeks, jawline and under-chin. " + _DEF1 + " a session, or six for " + _DEF16 + ".",
 "proc_name":"Define by InMode","proc_alt":"Hands-free bipolar radiofrequency facial contouring (Define Cheek, Define Chin) with Forma",
 "how":("Define uses hands-free headsets that deliver bipolar radiofrequency heat to the cheeks, jowls, jawline and under-chin. "
        "The tissue is warmed to a controlled temperature, which firms the skin and remodels the tissue beneath it over a series. "
        "A Forma handpiece then treats the rest of the face and neck."),
 "body":"Cheeks, Jowls, Jawline, Under-Chin, Neck",
 "eyebrow":"Define by InMode &middot; Facial Contouring &middot; Hudson, OH","h1":"Define by InMode in Hudson, Ohio",
 "hero":("Hands-free radiofrequency that firms the cheeks, jowls, jawline and under-chin, finished with Forma. "
         "No needles and no downtime. " + _DEF1 + " a session, or six for " + _DEF16 + "."),
 "trust":["Hands-Free","No Downtime","Cheeks &middot; Jawline &middot; Under-Chin","6 Sessions for " + _DEF16],
 "introh2":"A sharper jawline without surgery",
 "introlead":("Define is InMode&rsquo;s facial contouring workstation. Two hands-free headsets, Define Cheek and Define Chin, warm the "
              "lower face and under-chin evenly while you relax, and Forma finishes the treatment by hand."),
 "intropara":("At Serene Med Spa in Hudson, Define is for softening jowls, a less defined jawline, fullness under the chin and early "
              "laxity in the cheeks and neck. The headset stays in place, so you can read, answer email or scroll while it works. "
              "Most people do a series of six weekly sessions. Results build gradually as the tissue firms, and they vary from person to person. "
              "For fine lines, acne scars or crepey texture, we add <a href=\"/morpheus8/\">Morpheus8</a> from the same workstation. "
              "For more laxity than a non-invasive device can help, we&rsquo;ll talk you through <a href=\"/facetite/\">FaceTite</a>."),
 "treyebrow":"How Define Works","treh2":"Four technologies on one workstation",
 "cards":[
   ("Define Cheek","A hands-free headset for the <strong>cheeks, jowls and lower face</strong>."),
   ("Define Chin","A hands-free headset for the <strong>under-chin and jawline</strong>."),
   ("<a href=\"/forma/\">Forma</a>","A handheld radiofrequency tip that <strong>firms the rest of the face and neck</strong>. Included in every session."),
   ("<a href=\"/morpheus8/\">Morpheus8</a>","RF microneedling for <strong>texture, lines and deeper tightening</strong>. An optional add-on."),
   ("Temperature Controlled","The system tracks skin temperature and eases off once the target is reached, so treatment stays comfortable."),
   ("Relax While It Works","No needles, no numbing and no downtime. Most people go right back to their day."),
 ],
 "steps":_steps(
   "We look at your cheeks, jawline, under-chin and neck and choose one zone or both.",
   "The Define headset is fitted and runs hands-free while you feel gentle warmth, then we finish with Forma. About 30 to 60 minutes.",
   "Skin can look a little tighter right away. Firmness and definition build over the weeks of your series. Results vary.",
   "Six weekly sessions for most people, then an occasional maintenance session to keep your results."),
 "whyh2":"Why choose Serene for Define in Hudson",
 "whypara":("Serene is physician-led. We&rsquo;ll tell you honestly whether Define, Morpheus8, filler or a procedure like FaceTite "
            "is the right tool for your jawline, and we price Define so a full series is within reach."),
 "faqh2":"Define FAQ",
 "faqs":[
   ("How much does Define cost?", _DEF1 + " a session for one zone (chin or cheek) at Serene Med Spa in Hudson, or " + _DEF16 + " for a series of six. "
    "Both zones are " + _DEF2 + " a session or " + _DEF26 + " for six. Every session includes Forma."),
   ("How many sessions will I need?", "Most people do six sessions, about a week apart. InMode&rsquo;s protocols range from four to eight, "
    "depending on your skin and goals. We&rsquo;ll recommend a number at your consultation."),
   ("Does it hurt?", "No. You&rsquo;ll feel steady warmth, a bit like a hot stone massage. The system eases off once your skin reaches the "
    "target temperature."),
   ("Is there downtime?", "None. You may look a little flushed for an hour or so. Makeup is fine right after."),
   ("Who is a good candidate?", "Adults with mild to moderate softening of the jawline, jowls or under-chin who want a gradual, natural result "
    "without needles. Radiofrequency isn&rsquo;t used during pregnancy or with an implanted electronic device such as a pacemaker; "
    "we&rsquo;ll review your health history first."),
   ("How is Define different from Morpheus8?", "Define is non-invasive and hands-free: it firms and contours with heat alone. Morpheus8 "
    "uses fine needles plus radiofrequency to also improve texture, lines and scars, with a few days of redness. Many plans use both."),
   ("When will I see results?", "Some people see a tighter look soon after a session. Most of the change shows over the one to three months "
    "after the series as the tissue remodels."),
 ],
 "related":["forma","morpheus8","optimasmax"],
 "pricing_html":_DEF_GALLERY + _price_block("Pricing","Define pricing",_DEF_ROWS,_DEF_NOTE),
 "ctah2":"Ready for a more defined jawline?",
 "ctapara":"Book a free Define consultation with our Hudson team. We&rsquo;ll map your zones and build your six-session plan.",
}

# ============================================================== OPTIMASMAX ==============================================================
_OPT_GALLERY = _gal2("Clinical Photos", "OptimasMAX before &amp; after", [
    ("lumecca-ba-face-2", "Sun damage &amp; redness &mdash; Lumecca Peak", "Before and after Lumecca Peak IPL of the cheek"),
    ("forma-ba-face-1", "Lines &amp; firmness, lower face &mdash; Forma", "Before and after Forma radiofrequency of the lower face"),
    ("formaplus-ba-abdomen-1", "Abdomen &mdash; Forma Plus", "Before and after Forma Plus radiofrequency of the abdomen"),
    ("formaplus-ba-arm-1", "Upper arm &mdash; Forma Plus", "Before and after Forma Plus radiofrequency of the upper arm"),
    ("fusion-ba-back", "Back &mdash; Fusion hair removal", "Before and after Fusion laser hair removal on the back"),
], sid="optimasmax-results")

_OPT_NOTE = ('Consultations are complimentary. Standing series prices can&rsquo;t be combined with another discount. '
             'See the full <a href="/pricing/">price list</a>.')
_OPT_ROWS = [
    ("Lumecca Peak IPL &mdash; Full Face", "$400 / session", "Series of 3: $1,050 &middot; <a href=\"/lumecca/\">Lumecca Peak</a>"),
    ("Morpheus8 &amp; Morpheus8 Burst", _M8 + " / session", "Series of 3: $2,100 &middot; <a href=\"/morpheus8/\">Morpheus8</a>"),
    ("Laser Hair Removal", "From " + _LHR_FROM + " / session", "DiolazeXL or Fusion &middot; <a href=\"/laser-hair-removal/\">pricing by area</a>"),
    ("Forma", "Included with Define", "Or as part of a custom plan &middot; <a href=\"/define/\">Define from " + _DEF1 + "</a>"),
]

_OPT_PAGE = {
 "slug":"optimasmax","crumb":"OptimasMAX by InMode","area_kw":"InMode OptimasMAX",
 "title":"OptimasMAX by InMode in Hudson, OH | Serene Med Spa",
 "desc":("InMode OptimasMAX at Serene Med Spa in Hudson, Ohio: Lumecca Peak IPL, Morpheus8 Burst, Forma, DiolazeXL and Fusion laser hair "
         "removal on one platform. Physician-led plans, free consultation."),
 "ogtitle":"OptimasMAX by InMode in Hudson, OH",
 "ogdesc":"Clear, firm, smooth skin from one InMode platform: Lumecca Peak IPL, Morpheus8 Burst, Forma and laser hair removal.",
 "proc_name":"InMode OptimasMAX","proc_alt":"Multi-technology aesthetic workstation: IPL, fractional RF microneedling, RF skin tightening and diode laser hair removal",
 "how":("OptimasMAX is an InMode workstation with interchangeable handpieces: Lumecca Peak intense pulsed light for pigment and redness, "
        "Morpheus8 Burst radiofrequency microneedling for texture and tightening, Forma radiofrequency for firming, and DiolazeXL and "
        "Fusion lasers for hair removal."),
 "body":"Face, Neck, Chest, Arms, Abdomen, Legs, Back",
 "eyebrow":"InMode OptimasMAX &middot; Hudson, OH","h1":"OptimasMAX by InMode in Hudson, Ohio",
 "hero":("One InMode platform for clearer, firmer and smoother skin: Lumecca Peak IPL, Morpheus8 Burst, Forma and laser hair removal "
         "for every skin type. We choose the handpiece to match your skin and goals."),
 "trust":["5 Technologies","All Skin Types for Hair Removal","Physician-Led Plans","Free Consultation"],
 "introh2":"One platform, many treatments",
 "introlead":("OptimasMAX lets us treat tone, texture, firmness and unwanted hair from one workstation, so a single plan can cover more than "
              "one concern."),
 "intropara":("At Serene Med Spa in Hudson, OptimasMAX powers our <a href=\"/lumecca/\">Lumecca Peak photofacials</a>, "
              "<a href=\"/morpheus8/\">Morpheus8 Burst</a>, <a href=\"/forma/\">Forma</a> skin tightening and "
              "<a href=\"/laser-hair-removal/\">laser hair removal</a>. A common plan clears sun spots and redness with Lumecca, then "
              "improves texture and firmness with Morpheus8 or Forma. For the jawline and under-chin, see our "
              "<a href=\"/define/\">Define</a> workstation. Your provider matches each technology to your skin type; results vary."),
 "treyebrow":"What&rsquo;s on OptimasMAX","treh2":"Choose the right technology",
 "cards":[
   ("<a href=\"/lumecca/\">Lumecca Peak IPL</a>","Clears <strong>sun spots, freckles, redness and small facial vessels</strong>, often in 1&ndash;3 sessions. For light to olive, untanned skin."),
   ("<a href=\"/morpheus8/#burst\">Morpheus8 Burst</a>","RF microneedling at several depths in one pulse for <strong>texture, lines, scars and loose skin</strong>. Burst Deep treats larger body areas."),
   ("<a href=\"/forma/\">Forma &amp; Forma Plus</a>","Gentle radiofrequency heat that <strong>firms skin with no downtime</strong>: Forma for the face and neck, Forma Plus for the body."),
   ("<a href=\"/laser-hair-removal/\">DiolazeXL</a>","A fast diode laser with a large cooled tip for <strong>long-term hair reduction</strong> on legs, back and other large areas."),
   ("<a href=\"/laser-hair-removal/\">Fusion Light &amp; Dark</a>","Two wavelengths for <strong>fair and deeper skin tones</strong>, including coarse hair on darker skin."),
   ("Combination Plans","Tone, texture and firmness in one plan, spaced safely by your provider."),
 ],
 "steps":_steps(
   "A skin assessment: your skin type, concerns and any recent sun exposure decide which handpiece is safest and most effective.",
   "Treatment with the chosen handpiece. IPL and laser feel like a warm snap; Forma feels warm; Morpheus8 is done with numbing cream.",
   "Lumecca pigment flakes off in about a week, Morpheus8 redness settles in a few days, and Forma has no downtime. Hair sheds over 1&ndash;3 weeks.",
   "A short series for most treatments, then periodic maintenance. We space combination treatments so your skin can recover."),
 "whyh2":"Why choose Serene for OptimasMAX in Hudson",
 "whypara":("More technology only helps if it&rsquo;s used well. Our physician-led team tests settings on your skin, tells you when one "
            "treatment is the better fit, and builds a plan you can afford."),
 "faqh2":"OptimasMAX FAQ",
 "faqs":[
   ("What is OptimasMAX?", "An InMode workstation that runs several handpieces: Lumecca Peak IPL, Morpheus8 Burst and Burst Deep, Forma, "
    "DiolazeXL and Fusion Light / Fusion Dark. It&rsquo;s the machine; each handpiece is its own treatment."),
   ("Which treatment is right for me?", "Brown spots and redness: Lumecca Peak. Texture, lines, scars or loose skin: Morpheus8. Gentle "
    "no-downtime firming: Forma. Unwanted hair: DiolazeXL or Fusion. Many people combine two; we&rsquo;ll plan it at your free consultation."),
   ("Is it safe for all skin types?", "Morpheus8, Forma and Fusion can be used across skin tones. Lumecca Peak isn&rsquo;t used on tanned skin "
    "or deeper skin tones (types V and VI); we&rsquo;ll suggest a safer option if IPL isn&rsquo;t right for you."),
   ("Is laser hair removal permanent?", "It gives long-term hair reduction. Most people need a series, and an occasional touch-up keeps "
    "results."),
   ("Can I combine treatments in one visit?", "Sometimes. It depends on your skin and the treatments. Your provider will set the order and "
    "spacing so your skin heals well between sessions."),
 ],
 "related":["lumecca","morpheus8","laser-hair-removal"],
 "pricing_html":_OPT_GALLERY + _price_block("Pricing","OptimasMAX treatment pricing",_OPT_ROWS,_OPT_NOTE),
 "ctah2":"Not sure which treatment you need?",
 "ctapara":"Book a free consultation with our Hudson team. We&rsquo;ll match the right OptimasMAX handpiece to your skin.",
}

for _new in (_DEF_PAGE, _OPT_PAGE):
    if not any(pg.get("slug") == _new["slug"] for pg in PAGES6):
        PAGES6.append(_new)

# ================================================================ FORMA ================================================================
_FORMA_GALLERY = _gal2("Clinical Photos", "Forma before &amp; after", [
    ("forma-ba-face-1", "Lines &amp; firmness, lower face &mdash; Forma", "Before and after Forma radiofrequency of the lower face"),
    ("forma-ba-neck-1", "Jawline &amp; neck &mdash; Forma", "Before and after Forma radiofrequency of the jawline and neck"),
], sid="forma-results")

def _forma(p):
    add = (" Forma runs on both of our InMode workstations: it finishes every <a href=\"/define/\">Define</a> session and is one of the "
           "handpieces on <a href=\"/optimasmax/\">OptimasMAX</a>.")
    if "/define/" not in p.get("intropara", ""):
        p["intropara"] = p.get("intropara", "") + add
    p["related"] = ["define", "morpheus8", "optimasmax"]
    p["pricing_html"] = _FORMA_GALLERY + p.get("pricing_html", "")

for _pg in [x for n in ("PAGES6", "PAGES5", "PAGES4", "PAGES3", "PAGES2", "PAGES") for x in globals().get(n, [])]:
    if _pg.get("slug") == "forma" and not _pg.get("_define"):
        _forma(_pg); _pg["_define"] = True
