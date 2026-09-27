# -*- coding: utf-8 -*-
# pages_data_new_zzzzzz_ignite.py — InMode IgniteRF (BodyTite, FaceTite, AccuTite, QuantumRF), Sep 27, 2026.
#   Robin: owns FaceTite, BodyTite, AccuTite and QuantumRF (10/25); performed at both offices; publish
#   "starting at" prices (same at both offices): AccuTite $1,500, QuantumRF $2,500, FaceTite $3,500, BodyTite $4,000/area.
#   * patches /bodytite/ and /facetite/ (pages_data_new2.py): RF, not "laser lipo"; accurate RFAL description from the
#     InMode QRGs (tumescent local anesthesia, internal + external electrode, temperature-controlled, usually one treatment)
#   * new pages: /accutite/ and /quantumrf/
#   * InMode clinical before/afters, clearly labelled as courtesy of InMode, not Serene patients; body only (no nude photos).
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Avoid the bare token "OH" outside titles/eyebrows in this file (the Barboursville localizer rewrites it to "WV").

if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_BT, _FT, _AT, _QRF = "$4,000", "$3,500", "$1,500", "$2,500"

if "HERO_MAP" in globals():
    HERO_MAP.update({"bodytite": "ignite-device", "facetite": "ignite-device", "accutite": "ignite-device", "quantumrf": "quantumrf-handpieces"})
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.update({"bodytite": "/img/ignite-device.jpg", "facetite": "/img/ignite-device.jpg", "accutite": "/img/ignite-device.jpg",
                "quantumrf": "/img/quantumrf-handpieces.jpg"})
    RELATED_META.update({
        "bodytite": ("BodyTite", "RF contouring for the body. From " + _BT + " per area."),
        "facetite": ("FaceTite", "RF contouring for the jawline and neck. From " + _FT + "."),
        "accutite": ("AccuTite", "The smallest RF contouring handpiece. From " + _AT + "."),
        "quantumrf": ("QuantumRF", "Skin tightening under local anesthesia. From " + _QRF + "."),
    })

def _gallery(eyebrow, h2, items, note):
    figs = "".join(f'<figure class="res reveal"><img loading="lazy" src="/img/{f}.jpg" alt="{alt}" style="height:auto;aspect-ratio:auto"><figcaption>{cap}</figcaption></figure>'
                   for f, cap, alt in items)
    return ('<section class="results"><div class="wrap"><div class="section-head reveal"><div class="eyebrow">' + eyebrow + '</div>'
            '<h2>' + h2 + '</h2><p>Clinical photos from InMode. The treating physician is named on each photo.</p></div>'
            '<div class="res-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));align-items:start">' + figs + '</div>'
            '<p class="rev-note">' + note + '</p></div></section>')

_INMODE_NOTE = "Photos courtesy of InMode, from other practices. They are not Serene Med Spa patients. Individual results vary."
_BT_GALLERY = _gallery("Clinical Photos", "BodyTite before &amp; after", [
    ("bodytite-ba-abdomen-1", "Abdomen &mdash; BodyTite", "Before and after BodyTite of the abdomen"),
    ("bodytite-ba-flank-1", "Abdomen &amp; flanks &mdash; BodyTite", "Before and after BodyTite of the abdomen and flanks, side view"),
    ("bodytite-ba-arm-1", "Upper arm &mdash; BodyTite", "Before and after BodyTite of the upper arm"),
    ("bodytite-ba-arm-2", "Upper arm &mdash; BodyTite", "Before and after BodyTite of the upper arm, second patient"),
], _INMODE_NOTE)
_QRF_GALLERY = _gallery("Clinical Photos", "QuantumRF before &amp; after", [
    ("quantumrf-ba-1", "Jawline &amp; under-chin &mdash; QuantumRF 10", "Before and after QuantumRF 10 of the jawline and under-chin, side view"),
    ("quantumrf-ba-2", "Jawline &amp; under-chin &mdash; QuantumRF 10", "Before and after QuantumRF 10 of the jawline and under-chin, angled view"),
], "Photos courtesy of InMode (treating physician: Dr. Talon Maningas). Not a Serene Med Spa patient. Individual results vary.")

_IGN_NOTE = ('These are starting prices. Your exact quote depends on the areas treated and is confirmed at your complimentary '
             'consultation with our physician. See the full <a href="/pricing/">price list</a>.')
_IGN_ROWS = [
    ("AccuTite", "From " + _AT, "Small areas: under-chin, jowl, brow, bra line"),
    ("QuantumRF", "From " + _QRF, "Neck, jawline, arms, abdomen, knees"),
    ("FaceTite", "From " + _FT, "Lower face, jawline and neck"),
    ("BodyTite", "From " + _BT + " per area", "Abdomen, flanks, arms, thighs, back"),
]
def _ign_price(h2):
    return _price_block("Pricing", h2, _IGN_ROWS, _IGN_NOTE)

_RFAL_FAQS = [
    ("Is it surgery?", "It&rsquo;s a minimally invasive, in-office procedure. A few tiny openings (about the size of a needle stick) are made, and the "
     "area is numbed with local anesthetic. You&rsquo;re awake, and there are no stitches in most cases. It is still a medical procedure with a short recovery."),
    ("Is this laser lipo?", "No. IgniteRF uses radiofrequency, not a laser. A thin probe under the skin and an electrode on the surface heat the tissue "
     "between them to a precise, monitored temperature, which firms the skin from underneath."),
    ("Who performs it?", "Our physicians perform every IgniteRF procedure, after an in-person evaluation to confirm you&rsquo;re a good candidate."),
]

def _bodytite(p):
    p["crumb"] = "BodyTite"
    p["title"] = "BodyTite in Hudson, OH | From $4,000 per Area | Serene"
    p["desc"] = ("BodyTite in Hudson, Ohio: minimally invasive radiofrequency contouring that firms loose skin and reduces stubborn fat under "
                 "local anesthesia. From " + _BT + " per area. Physician-performed.")
    p["ogtitle"] = "BodyTite in Hudson, OH"
    p["ogdesc"] = "Firm loose skin and reduce stubborn fat in one in-office procedure under local anesthesia. From " + _BT + " per area."
    p["proc_name"] = "BodyTite"
    p["proc_alt"] = "Radiofrequency-assisted lipocoagulation (RFAL), InMode IgniteRF"
    p["how"] = ("Through a tiny opening, a thin radiofrequency probe is placed under the skin while a matching electrode glides on the surface. "
                "Energy flows between them and heats fat and connective tissue to a precise, monitored temperature, which contracts and "
                "firms the skin from underneath. Loosened fat can be removed with gentle suction in the same visit.")
    p["eyebrow"] = "BodyTite &middot; InMode IgniteRF &middot; Hudson, OH"
    p["hero"] = ("Firm loose skin and reduce stubborn fat in one in-office procedure, under local anesthesia and without a tummy tuck or arm lift. "
                 "Physician-performed. From " + _BT + " per area.")
    p["trust"] = ["Physician-Performed", "Local Anesthesia", "Usually One Treatment", "From " + _BT + " per Area"]
    p["introh2"] = "Tighten from the inside, not just remove fat"
    p["introlead"] = ("Liposuction removes fat but can leave skin looser. BodyTite adds controlled radiofrequency heat under the skin, so the "
                      "tissue contracts as the area is contoured.")
    p["intropara"] = ("At Serene Med Spa in Hudson, BodyTite is performed by our physicians on the InMode IgniteRF platform, usually in a single "
                      "visit under local anesthesia. It suits the abdomen, flanks, back, arms and thighs, especially after weight loss or "
                      "pregnancy when skin hasn&rsquo;t bounced back. For smaller or more delicate areas we use "
                      "<a href=\"/accutite/\">AccuTite</a> or <a href=\"/quantumrf/\">QuantumRF</a>, and many patients add Morpheus8 Body to "
                      "refine the skin surface. Results develop over several months and vary from person to person.")
    p["cards"] = [
        ("Abdomen", "Loose skin and stubborn fat after weight loss or pregnancy."),
        ("Flanks &amp; Back", "Love handles and bra-line rolls."),
        ("Arms", "Upper-arm laxity without the long scar of an arm lift."),
        ("Thighs", "Inner-thigh looseness and outer-thigh fullness."),
        ("After Weight Loss", "Including weight loss on a GLP-1 medication, once your weight is stable."),
        ("Pairs With Morpheus8 Body", "BodyTite works underneath; Morpheus8 refines the surface."),
    ]
    p["steps"] = _steps(
        "An in-person exam with our physician: pinch test, skin quality and goals. You&rsquo;ll get a written quote and a plan.",
        "The area is numbed with tumescent local anesthesia. BodyTite typically takes one to two hours depending on the number of areas.",
        "Swelling and bruising for one to two weeks and a compression garment for a few weeks. Most people return to desk work within a few days.",
        "Skin continues to tighten for six to twelve months. Most people need only one treatment per area.")
    p["whyh2"] = "Why choose Serene for BodyTite in Hudson"
    p["whypara"] = ("BodyTite is a medical procedure, and we treat it like one: a physician exam, honest candidacy advice, published starting "
                    "prices and close follow-up. If a surgical tummy tuck or arm lift would serve you better, we&rsquo;ll tell you.")
    p["faqs"] = [
        ("How much does BodyTite cost?", "BodyTite starts at " + _BT + " per area at Serene Med Spa in Hudson. Your exact price depends on the "
         "size and number of areas and whether liposuction is added, and is confirmed at your free consultation."),
    ] + _RFAL_FAQS + [
        ("What is the downtime?", "Expect swelling, bruising and some tenderness for one to two weeks, and you&rsquo;ll wear a compression garment "
         "for a few weeks. Most people are back at desk work in a few days and back to exercise in about two weeks."),
        ("When will I see results?", "Some change is visible once swelling settles, and skin keeps tightening for six to twelve months as collagen remodels."),
        ("Am I a candidate?", "Good candidates have mild to moderate loose skin with some fat underneath and a stable weight. Very loose, hanging skin "
         "may be better served by surgery; our physician will tell you honestly."),
    ]
    p["related"] = ["quantumrf", "accutite", "evolve-x"]
    p["ctah2"] = "Ready to tighten from the inside?"
    p["ctapara"] = "Book a free BodyTite consultation with our Hudson physicians and get a written quote."
    p["pricing_html"] = _BT_GALLERY + _ign_price("IgniteRF pricing")

def _facetite(p):
    p["crumb"] = "FaceTite"
    p["title"] = "FaceTite in Hudson, OH | From $3,500 | Serene"
    p["desc"] = ("FaceTite in Hudson, Ohio: minimally invasive radiofrequency contouring for the jawline, jowls and neck under local anesthesia. "
                 "From " + _FT + ". Physician-performed.")
    p["ogtitle"] = "FaceTite in Hudson, OH"
    p["ogdesc"] = "Define the jawline and tighten the neck without a facelift, under local anesthesia. From " + _FT + "."
    p["proc_name"] = "FaceTite"
    p["proc_alt"] = "Radiofrequency-assisted lipocoagulation (RFAL) of the face and neck, InMode IgniteRF"
    p["how"] = ("Through a tiny opening, a slim radiofrequency probe is placed under the skin of the jawline and neck while a matching electrode "
                "glides on the surface. Energy flows between them to a precise, monitored temperature, contracting the tissue and softening "
                "small fat pockets.")
    p["eyebrow"] = "FaceTite &middot; InMode IgniteRF &middot; Hudson, OH"
    p["hero"] = ("A sharper jawline and a tighter neck without a facelift. FaceTite is done in the office under local anesthesia, usually in one "
                 "visit. Physician-performed. From " + _FT + ".")
    p["trust"] = ["Physician-Performed", "Local Anesthesia", "No Facelift Scars", "From " + _FT]
    p["introh2"] = "The step between injectables and a facelift"
    p["introlead"] = ("Jowls, a softening jawline and a full or loose neck often don&rsquo;t respond to filler or skin treatments alone. FaceTite "
                      "works underneath the skin, where the laxity starts.")
    p["intropara"] = ("At Serene Med Spa in Hudson, FaceTite is performed by our physicians on the InMode IgniteRF platform, usually in one "
                      "visit under local anesthesia. It&rsquo;s often combined with Morpheus8 to improve the skin surface at the same time. For "
                      "very small areas we use <a href=\"/accutite/\">AccuTite</a>, and <a href=\"/quantumrf/\">QuantumRF</a> is another "
                      "option for the neck and jawline. Results develop over several months and vary from person to person.")
    p["cards"] = [
        ("Jowls &amp; Jawline", "Restore a cleaner line from chin to ear."),
        ("Under the Chin", "Reduce fullness and tighten the skin beneath it."),
        ("Neck", "Firm early neck laxity."),
        ("Lower Face", "Soften heaviness around the mouth and lower cheeks."),
        ("With Morpheus8", "FaceTite tightens underneath; Morpheus8 refines the surface."),
        ("Not Ready for a Facelift", "A smaller step with a shorter recovery."),
    ]
    p["steps"] = _steps(
        "An in-person exam with our physician to check skin quality, fat and laxity. You&rsquo;ll get a written quote.",
        "Local anesthetic numbs the area. Treatment of the jawline and neck usually takes about an hour.",
        "Swelling and some bruising for about a week, and a chin strap for several days. Most people are back to work within a few days.",
        "Tightening continues for six to twelve months. Most people need one treatment.")
    p["whyh2"] = "Why choose Serene for FaceTite in Hudson"
    p["whypara"] = ("FaceTite is a physician procedure. At Serene you&rsquo;re examined by a physician, told plainly whether FaceTite, "
                    "AccuTite, QuantumRF, Morpheus8 or a surgical referral is right for you, and given a written price before you decide.")
    p["faqs"] = [
        ("How much does FaceTite cost?", "FaceTite starts at " + _FT + " at Serene Med Spa in Hudson. The exact price depends on the areas "
         "(for example jawline only or jawline and neck) and whether Morpheus8 is added, and is confirmed at your free consultation."),
    ] + _RFAL_FAQS + [
        ("What is the downtime?", "Swelling and some bruising for about a week, with a chin strap for several days. Most people are back at work "
         "within a few days."),
        ("When will I see results?", "Some tightening is visible once swelling settles, and results keep improving for six to twelve months."),
        ("How is FaceTite different from a facelift?", "A facelift removes excess skin through longer incisions. FaceTite tightens from underneath "
         "through tiny openings, so it suits mild to moderate laxity. For very loose skin, surgery may be the better choice."),
    ]
    p["related"] = ["accutite", "quantumrf", "morpheus8"]
    p["ctah2"] = "Ready for a sharper jawline?"
    p["ctapara"] = "Book a free FaceTite consultation with our Hudson physicians and get a written quote."
    p["pricing_html"] = _QRF_GALLERY + _ign_price("IgniteRF pricing")

for _pg in [x for n in ("PAGES6", "PAGES5", "PAGES4", "PAGES3", "PAGES2") for x in globals().get(n, [])]:
    if _pg.get("slug") == "bodytite":
        _bodytite(_pg)
    elif _pg.get("slug") == "facetite":
        _facetite(_pg)

_IGN_PAGES = [
{
 "slug":"accutite","crumb":"AccuTite","area_kw":"AccuTite radiofrequency skin tightening",
 "title":"AccuTite in Hudson, OH | From $1,500 | Serene",
 "desc":"AccuTite in Hudson, Ohio: the smallest InMode radiofrequency contouring handpiece, for under-chin, jowl, brow and bra-line areas, under local anesthesia. From " + _AT + ".",
 "ogtitle":"AccuTite in Hudson, OH","ogdesc":"Precise radiofrequency contouring for small, delicate areas, under local anesthesia. From " + _AT + ".",
 "proc_name":"AccuTite","proc_alt":"Radiofrequency-assisted lipocoagulation (RFAL) of small areas, InMode IgniteRF",
 "how":"AccuTite is the smallest of InMode&rsquo;s radiofrequency contouring handpieces. A very fine probe under the skin and an electrode on the surface heat the tissue between them to a precise, monitored temperature, tightening small areas that larger handpieces can&rsquo;t reach.",
 "body":"Under-Chin, Jowls, Brow, Nasolabial Folds, Bra Line, Underarm, Knees",
 "eyebrow":"AccuTite &middot; InMode IgniteRF &middot; Hudson, OH","h1":"AccuTite in Hudson, Ohio",
 "hero":"Precise radiofrequency tightening for small, delicate areas: under the chin, the jowls, the brow line, the bra line and above the knees. Done in the office under local anesthesia. From " + _AT + ".",
 "trust":["Physician-Performed","Local Anesthesia","Small, Precise Areas","From " + _AT],
 "introh2":"Precision for the small areas",
 "introlead":"Some problem areas are too small for BodyTite or FaceTite. AccuTite uses the same radiofrequency idea on a much finer probe.",
 "intropara":"At Serene Med Spa in Hudson, AccuTite is performed by our physicians on the InMode IgniteRF platform, usually in a single visit under local anesthesia. It&rsquo;s often used with <a href=\"/facetite/\">FaceTite</a> or Morpheus8 when one area needs extra precision. Results develop over several months and vary from person to person.",
 "treyebrow":"Where It Works","treh2":"Areas We Treat",
 "cards":[
   ("Under the Chin","A small pocket of fullness with mild looseness."),
   ("Jowls","Early jowling along the jawline."),
   ("Brow &amp; Nasolabial Folds","Small, delicate areas of the face."),
   ("Bra Line &amp; Underarm","The roll that pushes over a bra strap."),
   ("Above the Knees","Loose skin over the inner knee."),
   ("With FaceTite or Morpheus8","Extra precision where it&rsquo;s needed."),
 ],
 "steps":_steps(
   "An in-person exam with our physician to choose the right handpiece. You&rsquo;ll get a written quote.",
   "Local anesthetic numbs the area. Small areas usually take under an hour.",
   "Mild swelling and possible bruising for several days. Most people are back to normal activities within a day or two.",
   "Tightening develops over several months. Most areas need one treatment."),
 "whyh2":"Why choose Serene for AccuTite in Hudson",
 "whypara":"We own the full IgniteRF lineup, so our physicians can choose the right handpiece for each area instead of fitting you to one device.",
 "faqh2":"AccuTite FAQ",
 "faqs":[
   ("How much does AccuTite cost?","AccuTite starts at " + _AT + " at Serene Med Spa in Hudson. The exact price depends on the area and is confirmed at your free consultation."),
 ] + _RFAL_FAQS + [
   ("What is the downtime?","Usually mild: some swelling and possible bruising for several days. Most people return to normal activities within a day or two."),
   ("AccuTite or FaceTite?","FaceTite covers larger zones like the full jawline and neck. AccuTite is for small, delicate spots. They&rsquo;re often used together."),
 ],
 "related":["facetite","quantumrf","morpheus8"],
 "pricing_html":_ign_price("IgniteRF pricing"),
 "ctah2":"Have one small area that bothers you?","ctapara":"Book a free AccuTite consultation with our Hudson physicians.",
},
{
 "slug":"quantumrf","crumb":"QuantumRF","area_kw":"QuantumRF minimally invasive skin tightening",
 "title":"QuantumRF in Hudson, OH | From $2,500 | Serene",
 "desc":"QuantumRF in Hudson, Ohio: InMode's newest minimally invasive radiofrequency skin tightening for the neck, jawline, arms, abdomen and knees, under local anesthesia. From " + _QRF + ".",
 "ogtitle":"QuantumRF in Hudson, OH","ogdesc":"Minimally invasive skin tightening for the neck, jawline and body, under local anesthesia and without liposuction. From " + _QRF + ".",
 "proc_name":"QuantumRF","proc_alt":"Subdermal radiofrequency soft-tissue contraction, InMode QuantumRF 10 and 25",
 "how":"A slim QuantumRF probe is placed just under the skin through a tiny opening and delivers controlled radiofrequency pulses to the fat and connective tissue, contracting and firming it from underneath. QuantumRF 10 is sized for the face, neck and small areas; QuantumRF 25 for larger body areas.",
 "body":"Neck, Jawline, Under-Chin, Arms, Abdomen, Bra Line, Thighs, Knees",
 "eyebrow":"QuantumRF &middot; InMode IgniteRF &middot; Hudson, OH","h1":"QuantumRF in Hudson, Ohio",
 "hero":"InMode&rsquo;s newest minimally invasive skin tightening. QuantumRF firms the neck, jawline, arms and abdomen from underneath, in one office visit under local anesthesia. From " + _QRF + ".",
 "trust":["Physician-Performed","Local Anesthesia","No Liposuction Needed","From " + _QRF],
 "introh2":"Tightening that starts under the skin",
 "introlead":"Surface treatments can only reach so deep. QuantumRF places radiofrequency energy in the layer just beneath the skin, where laxity begins, through an opening the size of a needle stick.",
 "intropara":"At Serene Med Spa in Hudson, QuantumRF is performed by our physicians, usually in one visit with local numbing and no liposuction. QuantumRF 10 treats the jawline, under-chin, neck and knees; QuantumRF 25 treats larger areas like the abdomen, arms and thighs. It pairs well with Morpheus8 for the skin surface. Results develop over several months and vary from person to person.",
 "treyebrow":"Where It Works","treh2":"Areas We Treat",
 "cards":[
   ("Jawline &amp; Under-Chin","Define the jawline and firm mild fullness."),
   ("Neck","Early neck laxity and crepiness."),
   ("Upper Arms","Loose skin on the back of the arm."),
   ("Abdomen","Mild looseness after weight loss or pregnancy."),
   ("Bra Line &amp; Thighs","Soft, loose areas that don&rsquo;t respond to exercise."),
   ("Above the Knees","Crepey skin over the inner knee."),
 ],
 "steps":_steps(
   "An in-person exam with our physician, including a pinch test to plan the energy. You&rsquo;ll get a written quote.",
   "The area is numbed with local anesthetic. Most areas take about an hour.",
   "Swelling and tenderness for several days and possibly a compression garment. Most people are back to work within a few days.",
   "Skin keeps tightening for several months. Most areas need one treatment."),
 "whyh2":"Why choose Serene for QuantumRF in Hudson",
 "whypara":"Our physicians use the full IgniteRF lineup, so you get the right handpiece for each area.",
 "faqh2":"QuantumRF FAQ",
 "faqs":[
   ("How much does QuantumRF cost?","QuantumRF starts at " + _QRF + " at Serene Med Spa in Hudson. The exact price depends on the area and size and is confirmed at your free consultation."),
   ("QuantumRF 10 or 25?","QuantumRF 10 is sized for the face, neck and small areas; QuantumRF 25 covers larger body areas like the abdomen and thighs. Your physician chooses based on the area."),
 ] + _RFAL_FAQS + [
   ("What is the downtime?","Swelling and tenderness for several days, sometimes a compression garment. Most people are back to work within a few days."),
   ("How is it different from BodyTite?","BodyTite pairs internal and external electrodes and can be combined with fat removal. QuantumRF delivers energy from a single slim probe, usually without liposuction, and suits areas where tightening matters more than fat reduction."),
 ],
 "related":["facetite","bodytite","morpheus8"],
 "ctah2":"Ready to tighten from underneath?","ctapara":"Book a free QuantumRF consultation with our Hudson physicians.",
},
]
_IGN_PAGES[1]["pricing_html"] = _QRF_GALLERY + _ign_price("IgniteRF pricing")
if not any(pg.get("slug") == "accutite" for pg in PAGES6):
    PAGES6 += _IGN_PAGES
