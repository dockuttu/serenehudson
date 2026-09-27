# -*- coding: utf-8 -*-
# pages_data_new_zzzzz_evolvex.py — InMode EvolveX refresh, Sep 27, 2026.
#   * patches the /evolve-x/ page from pages_data_new2.py: EvolveX name, Tite/Tone/Transform explained with
#     treatment times from the InMode QRGs, published pricing ($250 / session, series of 6 for $1,350 —
#     Mangomint package 31, sold online), InMode clinical before/afters (clearly labelled: not Serene patients,
#     body only), InMode lifestyle hero photo, updated FAQ (incl. GLP-1).
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Avoid the bare token "OH" outside titles/eyebrows in this file (the Barboursville localizer rewrites it to "WV").

if "_p" not in globals():
    _BV = (globals().get("SITE_LOC") == "barboursville") if "SITE_LOC" in globals() else ("Barboursville" in globals().get("AREA_TOWNS", []))
    def _p(hud, bv): return bv if _BV else hud
if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""

_EVX, _EVX6 = "$250", "$1,350"
_EVX_BUY = "https://clients.mangomint.com/serenemedspa/packages/31"

if "HERO_MAP" in globals():
    HERO_MAP["evolve-x"] = "evolvex-card"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG["evolve-x"] = "/img/evolvex-card.jpg"
    RELATED_META["evolve-x"] = ("EvolveX", "Hands-free Tite, Tone and Transform body contouring.")

_EVX_BA = [
    ("evolvex-ba-abdomen-1", "Abdomen", "Before and after InMode Evolve body contouring of the abdomen"),
    ("evolvex-ba-abdomen-2", "Abdomen &amp; waist", "Before and after InMode Evolve body contouring of the lower abdomen"),
    ("evolvex-ba-arm-1", "Upper arm", "Before and after InMode Evolve skin tightening of the upper arm"),
    ("evolvex-ba-arm-2", "Upper arm", "Before and after InMode Evolve treatment of the upper arm"),
]
_EVX_GALLERY = ('<section class="results" id="evolvex-results"><div class="wrap"><div class="section-head reveal"><div class="eyebrow">Clinical Photos</div>'
                '<h2>EvolveX before &amp; after</h2><p>Clinical photos from InMode. The treating physician is named on each photo.</p></div><div class="res-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));align-items:start">'
                + "".join(f'<figure class="res reveal"><img loading="lazy" src="/img/{f}.jpg" alt="{alt}" style="height:auto;aspect-ratio:auto"><figcaption>{cap} &mdash; InMode Evolve</figcaption></figure>' for f, cap, alt in _EVX_BA)
                + '</div><p class="rev-note">Photos courtesy of InMode, from other practices. They are not Serene Med Spa patients. Individual results vary.</p></div></section>')

_EVX_NOTE = ('The series is a standing price and can&rsquo;t be combined with another discount. Series sessions don&rsquo;t expire. '
             'The consultation is complimentary. See the full <a href="/pricing/">price list</a>.'
             f'<br>Prefer to prepay? <a href="{_EVX_BUY}" target="_blank" rel="noopener">Buy the EvolveX series of 6 online</a>. '
             'We&rsquo;ll still start with a short consultation to choose your areas.')

def _evolvex(p):
    p["crumb"] = "EvolveX"
    p["title"] = "EvolveX in Hudson, OH | $250 or 6 for $1,350 | Serene"
    p["desc"] = ("InMode EvolveX body contouring in Hudson, Ohio: hands-free Tite, Tone and Transform to tighten skin, tone muscle "
                 "and reduce stubborn fat. $250 a session or 6 for $1,350. No downtime.")
    p["ogtitle"] = "EvolveX in Hudson, OH"
    p["ogdesc"] = "Hands-free body contouring from InMode: tighten skin, tone muscle, reduce stubborn fat. $250, or 6 sessions for $1,350."
    p["proc_name"] = "EvolveX"
    p["proc_alt"] = "InMode EvolveX Tite, Tone and Transform"
    p["how"] = ("EvolveX by InMode uses hands-free applicators that deliver radiofrequency heat to skin and fat (Tite and Transform) "
                "and electrical muscle stimulation to muscle (Tone and Transform) in targeted body areas.")
    p["eyebrow"] = "InMode EvolveX &middot; Body Contouring &middot; Hudson, OH"
    p["h1"] = "EvolveX in Hudson, Ohio"
    p["hero"] = ("Hands-free body contouring from InMode. Tite tightens skin, Tone builds muscle, and Transform works on both "
                 "while reducing stubborn fat. $250 a session, or six for $1,350.")
    p["trust"] = ["Hands-Free", "No Downtime", "Tite &middot; Tone &middot; Transform", "6 Sessions for $1,350"]
    p["introh2"] = "Three treatments on one hands-free platform"
    p["introlead"] = ("EvolveX treats the body in layers. Radiofrequency heat works on skin and fat, and electrical muscle stimulation "
                      "works the muscle underneath, so one visit can target more than one concern.")
    p["intropara"] = ("At Serene Med Spa in Hudson, EvolveX treats the abdomen, flanks, thighs, buttocks and arms. The applicators strap in place, "
                      "so you can relax, read or scroll while it works. Most people do a series of about six sessions, a week or two apart. "
                      "It&rsquo;s a strong fit after weight loss, including weight loss on a GLP-1 medication, when you want firmer skin and "
                      "better muscle tone. Results build over the series and vary from person to person.")
    p["treyebrow"] = "Tite, Tone or Transform"
    p["treh2"] = "Which EvolveX treatment is right for you?"
    p["cards"] = [
        ("Tite", "Radiofrequency heat for <strong>loose or crepey skin</strong>. About 30&ndash;60 minutes."),
        ("Tone", "Electrical muscle stimulation to <strong>build and firm muscle</strong>. About 20&ndash;30 minutes."),
        ("Transform", "Radiofrequency plus muscle stimulation for <strong>thicker areas with stubborn fat</strong>. About an hour."),
        ("Abdomen &amp; Flanks", "Our most-requested areas, for a firmer, tighter midsection."),
        ("Thighs, Buttocks &amp; Arms", "Firm and tone the areas that are hardest to change with exercise alone."),
        ("After Weight Loss", "Tighten skin and support muscle tone as your body changes, including on a GLP-1 medication."),
    ]
    p["steps"] = _steps(
        "Your provider looks at your skin, muscle and target areas and chooses Tite, Tone, Transform or a combination.",
        "Applicators strap onto the area and run hands-free for 20 to 60 minutes. You feel warmth, and with Tone, strong muscle contractions.",
        "Skin firms and muscle tone builds over the weeks after your series. Results vary.",
        "Most people do about six sessions, weekly or every other week, then an occasional maintenance session.")
    p["whyh2"] = "Why choose Serene for EvolveX in Hudson"
    p["whypara"] = ("Serene is physician-led. We plan EvolveX around your goals, pair it with Morpheus8 Body or medical weight loss when that "
                    "helps, and tell you plainly what it can and can&rsquo;t do.")
    p["faqh2"] = "EvolveX FAQ"
    faqs = [
        ("How much does EvolveX cost?", "$250 per session at Serene Med Spa in Hudson, or $1,350 for a series of six ($225 a session). "
         f"You can <a href=\"{_EVX_BUY}\" target=\"_blank\" rel=\"noopener\">buy the series online</a> or at your visit."),
        ("Is EvolveX a weight-loss treatment?", "No. It tightens skin, tones muscle and reduces stubborn fat in targeted areas. It works alongside "
         "healthy habits or a medical weight-loss plan, not in place of them."),
        ("How many sessions will I need?", "Most people do a series of about six, a week or two apart. Larger or multiple areas can take more; "
         "your provider will tell you at the consultation."),
        ("Does it hurt, and is there downtime?", "There&rsquo;s no downtime. Tite and Transform feel warm, and Tone feels like a strong workout "
         "contraction. Most people go right back to their day."),
        ("I&rsquo;m losing weight on a GLP-1 medication. Can EvolveX help?", "Often, yes. Fast weight loss can leave loose skin and cost some muscle. "
         "Tite can firm skin and Tone can strengthen muscle in targeted areas. Keep up protein and strength training too, and ask about our "
         "<a href=\"/weight-loss/\">medical weight-loss program</a>."),
        ("When will I see results?", "Some people notice firmer skin within a few sessions. Most results show over the one to three months "
         "after the series as skin remodels and muscle builds."),
    ]
    if not _p(False, True):
        faqs.insert(5, ("How is it different from EMSCULPT NEO?", "Both combine heat and muscle stimulation. EvolveX can treat several areas "
                        "at once with hands-free applicators and has a dedicated skin-tightening mode (Tite). We&rsquo;ll help you choose or combine them."))
    p["faqs"] = faqs
    p["related"] = ["morpheus8", "weight-loss"] + [s for s in p.get("related", []) if s not in ("morpheus8", "weight-loss", "fillers")][:1]
    p["ctah2"] = "Ready to tighten and tone?"
    p["ctapara"] = "Book a free EvolveX consultation with our Hudson team, or buy a six-session series online."
    p["pricing_html"] = _EVX_GALLERY + _price_block("Pricing", "EvolveX pricing", [
        ("EvolveX", _EVX + " / session", "Tite, Tone or Transform &middot; 20&ndash;60 minutes"),
        ("EvolveX &mdash; Series of 6", _EVX6, "$225 a session &middot; save $150"),
        ("Consultation", "Complimentary", "We match the treatment to your goals"),
    ], _EVX_NOTE)

if "PAGES2" in globals():
    for _pg in [x for n in ("PAGES6", "PAGES5", "PAGES4", "PAGES3", "PAGES2") for x in globals().get(n, [])]:
        if _pg.get("slug") == "evolve-x":
            _evolvex(_pg)
