# -*- coding: utf-8 -*-
# pages_data_new_zzzz_empower.py — EmpowerRF (InMode) women's wellness, Sep 27, 2026 (Robin OK'd plan + pricing).
#   * new pages: /empowerrf/ (hub) and /morpheus8v/
#   * patches the /vtone/, /formav/ and /womens-sexual-wellness/ pages defined in earlier files:
#     series pricing, cross-links, and FDA-accurate wording (VTone is FDA-cleared for urinary incontinence in women,
#     K200293; FormaV and Morpheus8V are cleared devices but NOT cleared for "vaginal rejuvenation" — see FDA 2018
#     safety communication — so their benefits are phrased as what many women report, not as guaranteed outcomes).
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Loads after pages_data_new_zzz_pricing_gaps.py (sorted glob), so _steps/_price_block/_p already exist there;
# small fallbacks below keep seo_trim.py (which exec's every data file) safe on its own.
# Avoid the bare token "OH" in this file (the Barboursville localizer rewrites it to "WV").

if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""

# ---- EmpowerRF prices (same at both offices) ----
_M8V, _M8V3 = "$800", "$2,100"
_FV, _FV3 = "$500", "$1,350"
_VT, _VT6 = "$350", "$1,500"
_EMP = "$4,200"

_EMP_ROWS = [
    ("Morpheus8V", _M8V + " / session", "Series of 3: " + _M8V3),
    ("FormaV", _FV + " / session", "Series of 3: " + _FV3),
    ("VTone", _VT + " / session", "Series of 6: " + _VT6),
    ("EmpowerRF Complete", _EMP, "Morpheus8V &times;3 + FormaV &times;3 + VTone &times;6 (reg. $6,000)"),
]
_EMP_NOTE = ('Series and EmpowerRF Complete are standing prices and can&rsquo;t be combined with another discount. '
             'The consultation is private and complimentary. See the full <a href="/pricing/">price list</a>.'
             '<br>Prefer to prepay? Buy a series online: '
             '<a href="https://clients.mangomint.com/serenemedspa/packages/27" target="_blank" rel="noopener">Morpheus8V &times;3</a> &middot; '
             '<a href="https://clients.mangomint.com/serenemedspa/packages/28" target="_blank" rel="noopener">FormaV &times;3</a> &middot; '
             '<a href="https://clients.mangomint.com/serenemedspa/packages/29" target="_blank" rel="noopener">VTone &times;6</a> &middot; '
             '<a href="https://clients.mangomint.com/serenemedspa/packages/30" target="_blank" rel="noopener">EmpowerRF Complete</a>. '
             'We&rsquo;ll still start with your private consultation.')
_FDA_NOTE = ('VTone is FDA-cleared to treat stress, urge and mixed urinary incontinence in women. FormaV and Morpheus8V are '
             'FDA-cleared radiofrequency devices; they are not FDA-approved for intimate or sexual-wellness indications, and their use '
             'for intimate wellness is physician-directed. Individual results vary.')

# hero images (InMode EmpowerRF treatment-room photos, courtesy of InMode) + booking (Sexual Wellness Consultation)
if "HERO_MAP" in globals():
    HERO_MAP.update({"empowerrf": "empowerrf-consult", "morpheus8v": "morpheus8v-consult", "formav": "formav-consult"})
if "BOOK_MAP" in globals() and "MM" in globals():
    for _s in ("empowerrf", "morpheus8v", "vtone", "formav"):
        BOOK_MAP[_s] = MM % 325
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.update({"empowerrf": "/img/empowerrf-consult.jpg", "morpheus8v": "/img/morpheus8v-consult.jpg",
                "formav": "/img/formav-consult.jpg", "vtone": "/img/dr-arora.jpg"})
    RELATED_META.update({
        "empowerrf": ("EmpowerRF", "Morpheus8V, FormaV and VTone on one platform."),
        "morpheus8v": ("Morpheus8V", "Radiofrequency microneedling for intimate tissue."),
        "formav": ("FormaV", "Gentle radiofrequency warmth, no downtime."),
        "vtone": ("VTone", "FDA-cleared for bladder leakage in women."),
    })

_COMPARE = '''<section id="compare" class="tint-sand"><div class="wrap"><div class="section-head reveal"><div class="eyebrow">Compare</div><h2>Morpheus8V, FormaV or VTone?</h2><p>Most women need one or two of these, not all three. Your physician matches the treatment to the cause.</p></div>
<div class="grid g3">
 <div class="card reveal"><div class="ico">&#10022;</div><h3><a href="/vtone/">VTone</a></h3><p><strong>Muscle.</strong> Electrical stimulation strengthens the pelvic floor.<br><br><strong>For:</strong> leaking with a laugh, cough or run; urgency.<br><strong>FDA:</strong> cleared for urinary incontinence in women.<br><strong>Plan:</strong> 6 sessions, about 30 minutes each.<br><strong>Downtime:</strong> none.<br><strong>Price:</strong> $350, or 6 for $1,500.</p></div>
 <div class="card reveal"><div class="ico">&#10022;</div><h3><a href="/formav/">FormaV</a></h3><p><strong>Tissue warmth.</strong> Gentle, temperature-controlled radiofrequency.<br><br><strong>For:</strong> comfort, dryness and tone concerns many women notice after childbirth or menopause.<br><strong>Plan:</strong> 3 sessions, about 20 minutes each.<br><strong>Downtime:</strong> none.<br><strong>Price:</strong> $500, or 3 for $1,350.</p></div>
 <div class="card reveal"><div class="ico">&#10022;</div><h3><a href="/morpheus8v/">Morpheus8V</a></h3><p><strong>Deeper remodeling.</strong> Radiofrequency delivered through fine micro-needles.<br><br><strong>For:</strong> more pronounced laxity and external skin changes.<br><strong>Plan:</strong> 3 sessions, 4&ndash;6 weeks apart, with numbing.<br><strong>Downtime:</strong> 2&ndash;3 days of avoiding intimacy and hot baths.<br><strong>Price:</strong> $800, or 3 for $2,100.</p></div>
</div></div></section>'''

_EMP_PAGES = [
# ============================================================ EmpowerRF hub ============================================================
{
 "slug":"empowerrf","crumb":"EmpowerRF","area_kw":"EmpowerRF women's wellness",
 "title":"EmpowerRF Intimate Wellness in Hudson, OH | Serene",
 "desc":"EmpowerRF women's wellness in Hudson, Ohio: Morpheus8V, FormaV and VTone on one InMode platform. Non-surgical, non-hormonal. Private, complimentary consultation.",
 "ogtitle":"EmpowerRF Women's Wellness in Hudson, OH","ogdesc":"Morpheus8V, FormaV and VTone: non-surgical, non-hormonal care for bladder leakage, comfort and confidence. Series from $1,350.",
 "proc_name":"EmpowerRF Women's Wellness","proc_alt":"InMode EmpowerRF platform: Morpheus8V fractional radiofrequency, FormaV radiofrequency and VTone pelvic-floor electrical muscle stimulation",
 "how":"EmpowerRF combines three treatments on one platform: VTone uses electrical muscle stimulation to strengthen the pelvic floor, FormaV delivers gentle temperature-controlled radiofrequency, and Morpheus8V delivers radiofrequency through fine micro-needles for deeper remodeling.","body":"Pelvic floor and intimate tissue",
 "eyebrow":"Women&rsquo;s Wellness &middot; Hudson, OH","h1":"EmpowerRF in Hudson, Ohio",
 "hero":"Bladder leaks, dryness and changes after childbirth or menopause are common, and you don&rsquo;t have to just live with them. EmpowerRF brings three non-surgical, non-hormonal treatments together under one physician-led plan.",
 "trust":["Non-Surgical","Non-Hormonal","FDA-Cleared VTone","Private Consultation"],
 "introh2":"One platform, three treatments, one plan",
 "introlead":"About one in three women deal with urinary leakage at some point, and many more notice changes in comfort and confidence after childbirth or menopause. EmpowerRF by InMode puts three different tools on one platform so the plan can fit the cause: muscle, tissue, or both.",
 "intropara":"At Serene Med Spa in Hudson, EmpowerRF treatments are performed in a private room and planned by our board-certified physicians. VTone strengthens the pelvic-floor muscles and is FDA-cleared for urinary incontinence in women. FormaV and Morpheus8V use radiofrequency energy, gentle warmth and microneedling respectively, and many women report better comfort, tone and confidence over a series. We&rsquo;ll also tell you when pelvic-floor physical therapy, hormone therapy or a urology referral is the better first step. Individual results vary.",
 "treyebrow":"Who It Helps","treh2":"What EmpowerRF Can Address",
 "cards":[
   ("Bladder Leakage","Leaking with a laugh, cough, sneeze or workout; <a href=\"/vtone/\">VTone</a> is FDA-cleared for it."),
   ("Urgency","The sudden need to go, and going more often than you&rsquo;d like."),
   ("After Childbirth","Changes in tone and control, once your OB has cleared you."),
   ("Menopause","Dryness and discomfort many women notice as hormones change."),
   ("Laxity","From gentle <a href=\"/formav/\">FormaV</a> warmth to deeper <a href=\"/morpheus8v/\">Morpheus8V</a> remodeling."),
   ("Can&rsquo;t Use Estrogen","A non-hormonal option to discuss with your physician (and oncologist, if you&rsquo;ve had cancer)."),
 ],
 "steps":_steps(
   "A private, complimentary consultation with a physician: your symptoms, history and goals, and which of the three treatments fits.",
   "VTone and FormaV need no numbing; Morpheus8V uses numbing cream. Sessions take 20&ndash;30 minutes in a private room.",
   "Many women notice a difference after two or three sessions, with more improvement as the series finishes.",
   "A maintenance session once a year (VTone every few months) helps keep results."),
 "whyh2":"Why choose Serene for EmpowerRF in Hudson",
 "whypara":"EmpowerRF is one part of a physician-led women&rsquo;s wellness program that also includes V-Renew PRP, Alma Duo and hormone optimization, so the plan fits the cause rather than the device. Published prices, candid advice about what each treatment can and can&rsquo;t do, and consultations that stay private.",
 "faqh2":"EmpowerRF FAQ",
 "faqs":[
   ("What is EmpowerRF?","EmpowerRF is InMode&rsquo;s women&rsquo;s wellness platform. At Serene it includes three treatments: VTone (pelvic-floor muscle stimulation), FormaV (gentle radiofrequency) and Morpheus8V (radiofrequency microneedling)."),
   ("Is EmpowerRF FDA-approved?","VTone is FDA-cleared to treat stress, urge and mixed urinary incontinence in women. FormaV and Morpheus8V are FDA-cleared radiofrequency devices, but they are not FDA-approved for intimate or sexual-wellness indications; their use for intimate wellness is physician-directed, and we&rsquo;ll explain the evidence honestly at your consultation."),
   ("Which treatment do I need?","Leaking points to VTone. Comfort, dryness and mild tone concerns usually start with FormaV. More pronounced laxity is where Morpheus8V comes in. Many women combine two; your physician will recommend a plan after a private consultation."),
   ("How much does EmpowerRF cost?","VTone is $350 a session or $1,500 for six. FormaV is $500 or $1,350 for three. Morpheus8V is $800 or $2,100 for three. EmpowerRF Complete (all three series) is $4,200. The consultation is complimentary."),
   ("Does it hurt?","VTone feels like strong muscle contractions and FormaV like a warm massage; neither needs numbing. Morpheus8V is done with numbing cream and feels like warmth and pressure."),
   ("Is there downtime?","None for VTone or FormaV. After Morpheus8V, avoid intimacy, hot baths and hot tubs for two to three days."),
   ("Who shouldn&rsquo;t have EmpowerRF?","Anyone pregnant, with a pacemaker or implanted electrical device, an active pelvic infection or outbreak, or cancer in the treatment area. Your physician screens for these."),
 ],
 "related":["vtone","formav","morpheus8v"],
 "pricing_html":_COMPARE + _price_block("Pricing","EmpowerRF pricing",_EMP_ROWS, _EMP_NOTE) + '<p class="rev-note" style="text-align:center;max-width:860px;margin:0 auto 34px;font-size:.85rem">' + _FDA_NOTE + '</p>',
 "ctah2":"Ready for a private conversation?","ctapara":"Book a complimentary, confidential EmpowerRF consultation with our Hudson physicians.",
},
# ============================================================ Morpheus8V ============================================================
{
 "slug":"morpheus8v","crumb":"Morpheus8V","area_kw":"Morpheus8V radiofrequency microneedling",
 "title":"Morpheus8V in Hudson, OH | $800 or 3 for $2,100 | Serene",
 "desc":"Morpheus8V in Hudson, Ohio: fractional radiofrequency microneedling for intimate tissue on the InMode EmpowerRF platform. $800 a session or 3 for $2,100. Private, physician-led.",
 "ogtitle":"Morpheus8V in Hudson, OH","ogdesc":"Radiofrequency microneedling for intimate wellness on the EmpowerRF platform. $800, or a series of 3 for $2,100.",
 "proc_name":"Morpheus8V Fractional Radiofrequency","proc_alt":"Fractional radiofrequency microneedling of vaginal and vulvar tissue (InMode EmpowerRF Morpheus8V)",
 "how":"Fine insulated micro-needles deliver radiofrequency energy 1 to 3 millimeters into vaginal and vulvar tissue, creating controlled heat that prompts the body&rsquo;s own collagen remodeling over the following weeks.","body":"Vaginal and vulvar tissue",
 "eyebrow":"Women&rsquo;s Wellness &middot; Hudson, OH","h1":"Morpheus8V in Hudson, Ohio",
 "hero":"The deepest of the EmpowerRF treatments. Morpheus8V brings Morpheus8&rsquo;s radiofrequency microneedling to intimate tissue, for women whose concerns go beyond what gentle warmth can reach. $800 a session, or three for $2,100.",
 "trust":["Physician-Performed","Numbing for Comfort","3-Session Series","$800 per Session"],
 "introh2":"Remodeling, not just warming",
 "introlead":"Childbirth, menopause and time can leave intimate tissue looser and thinner. Morpheus8V uses the same fractional radiofrequency idea as Morpheus8 on the face: tiny needles place heat below the surface, and the body responds by remodeling collagen over the next weeks.",
 "intropara":"At Serene Med Spa in Hudson, Morpheus8V is performed by our physicians in a private room on the InMode EmpowerRF platform. After numbing cream, a slim handpiece treats the internal and, when needed, external tissue in about 20 to 30 minutes. The usual plan is three sessions four to six weeks apart, often paired with <a href=\"/formav/\">FormaV</a> or <a href=\"/vtone/\">VTone</a>. Many women report improved tone and confidence after the series; individual results vary. Morpheus8V is an FDA-cleared radiofrequency device, but it is not FDA-approved for intimate or sexual-wellness indications, and we&rsquo;ll talk through what the evidence does and doesn&rsquo;t show.",
 "treyebrow":"Who It Helps","treh2":"Good Candidates",
 "cards":[
   ("Laxity After Childbirth","Looser tone that didn&rsquo;t come back, once your OB has cleared you."),
   ("Menopause Changes","Thinner, less resilient tissue as estrogen declines."),
   ("External Skin","Laxity or texture of the external (vulvar) skin."),
   ("Mild Leakage","Often combined with <a href=\"/vtone/\">VTone</a>, which is FDA-cleared for incontinence."),
   ("Beyond FormaV","Women who want more than gentle warmth can deliver."),
   ("Prefer Non-Surgical","No incisions and no general anesthesia."),
 ],
 "steps":_steps(
   "A private consultation and exam with a physician to confirm Morpheus8V (alone or with FormaV or VTone) is right for you.",
   "Numbing cream, then about 20&ndash;30 minutes of treatment. You feel warmth and pressure.",
   "Mild warmth or spotting for a day or two. Avoid intimacy, hot baths and hot tubs for two to three days.",
   "Three sessions four to six weeks apart, then a yearly maintenance session if needed."),
 "whyh2":"Why choose Serene for Morpheus8V in Hudson",
 "whypara":"Our physicians already perform Morpheus8 on the face and body, and bring the same control of depth and energy to Morpheus8V. It&rsquo;s one option in a women&rsquo;s wellness program that also includes FormaV, VTone, V-Renew PRP and hormone therapy, so you get the plan that fits, with published pricing and a private, complimentary consultation.",
 "faqh2":"Morpheus8V FAQ",
 "faqs":[
   ("How much does Morpheus8V cost?","$800 per session at Serene Med Spa in Hudson, or $2,100 for a series of three. EmpowerRF Complete (Morpheus8V &times;3, FormaV &times;3 and VTone &times;6) is $4,200."),
   ("Does it hurt?","Numbing cream is applied first. Most women describe warmth and pressure rather than pain, and energy is adjusted for comfort."),
   ("What is the downtime?","Very little. Avoid intimacy, hot baths and hot tubs for two to three days. Most women return to work the same or next day."),
   ("How many sessions will I need?","Usually three, four to six weeks apart. Some women need one or two; your physician decides based on how your tissue responds."),
   ("How is Morpheus8V different from FormaV?","FormaV is gentle, even warmth with no downtime. Morpheus8V adds micro-needles to place radiofrequency deeper, for more pronounced laxity. They are often combined."),
   ("Is Morpheus8V FDA-approved for intimate wellness?","No. Morpheus8V is an FDA-cleared radiofrequency device, and the FDA has cautioned that no energy-based device is approved for intimate or sexual-wellness indications. Its use for intimate wellness is physician-directed, and we&rsquo;ll be candid about expected results."),
   ("Who shouldn&rsquo;t have Morpheus8V?","Anyone pregnant, with a pacemaker or implanted electrical device, an active infection or herpes outbreak in the area, or cancer in the treatment area. Your physician screens for these."),
 ],
 "related":["empowerrf","formav","vtone"],
 "pricing_html":_price_block("Pricing","Morpheus8V pricing",[("Morpheus8V", _M8V + " / session", "Numbing included"),("Morpheus8V &mdash; Series of 3", _M8V3, "Most women need 3"),("EmpowerRF Complete", _EMP, "Morpheus8V &times;3 + FormaV &times;3 + VTone &times;6"),("Consultation","Complimentary &amp; confidential","")], _EMP_NOTE),
 "ctah2":"Ready for a private conversation?","ctapara":"Book a complimentary, confidential Morpheus8V consultation in Hudson.",
},
]
PAGES6 += _EMP_PAGES

# ---------------------------------------------------------------- patches to existing pages
def _patch(slug, fn):
    for _pg in PAGES6 + PAGES5 + PAGES4 + PAGES3 + PAGES2:
        if _pg.get("slug") == slug:
            fn(_pg)

def _vtone(p):
    p["title"] = "VTone in Hudson, OH | FDA-Cleared for Bladder Leakage | Serene"
    p["desc"] = ("VTone in Hudson, Ohio: FDA-cleared electrical muscle stimulation for stress, urge and mixed urinary incontinence in women. "
                 "$350 a session or 6 for $1,500. Painless, no downtime.")
    p["ogdesc"] = "FDA-cleared for bladder leakage in women. Thirty painless minutes, no downtime. $350, or 6 sessions for $1,500."
    p["trust"] = ["FDA-Cleared for Incontinence","Painless","No Downtime","6 Sessions for $1,500"]
    p["hero"] = ("The pelvic floor is a muscle, and VTone trains it. Thirty painless minutes of guided stimulation, FDA-cleared to treat "
                 "urinary incontinence in women. $350 a session, or six for $1,500.")
    p["intropara"] = p["intropara"].replace("VTone is part of our EmpowerRF women&rsquo;s wellness platform.",
        "VTone is part of our <a href=\"/empowerrf/\">EmpowerRF</a> women&rsquo;s wellness platform and is FDA-cleared to treat stress, urge and mixed urinary incontinence in women.")
    p["faqs"] = [(q, "$350 per session at Serene Med Spa in Hudson, or $1,500 for the standard series of six. EmpowerRF Complete (VTone &times;6, FormaV &times;3 and Morpheus8V &times;3) is $4,200.")
                 if q.startswith("How much") else (q, a) for q, a in p["faqs"]]
    p["faqs"].insert(1, ("Is VTone FDA-cleared?","Yes. VTone is FDA-cleared to provide electrical stimulation and neuromuscular re-education of weak pelvic-floor muscles for the treatment of stress, urge and mixed urinary incontinence in women."))
    p["related"] = ["empowerrf","formav","morpheus8v"]
    p["pricing_html"] = _price_block("Pricing","VTone pricing",[("VTone", _VT + " / session", "30 minutes, no downtime"),("VTone &mdash; Series of 6", _VT6, "The standard program"),("EmpowerRF Complete", _EMP, "VTone &times;6 + FormaV &times;3 + Morpheus8V &times;3"),("Consultation","Complimentary &amp; confidential","")], _EMP_NOTE)
_patch("vtone", _vtone)

def _formav(p):
    p["title"] = "FormaV in Hudson, OH | $500 or 3 for $1,350 | Serene"
    p["desc"] = ("FormaV in Hudson, Ohio: gentle, temperature-controlled radiofrequency for intimate wellness with no downtime. "
                 "$500 a session or 3 for $1,350. Physician-led EmpowerRF.")
    p["ogdesc"] = "Gentle radiofrequency warmth for intimate comfort and confidence, no downtime. $500, or a series of 3 for $1,350."
    p["how"] = ("A slim applicator delivers gentle, temperature-controlled radiofrequency warmth to vaginal and vulvar tissue. "
                "FormaV is an FDA-cleared radiofrequency device; its use for intimate wellness is physician-directed.")
    p["hero"] = ("Gentle, warming radiofrequency that many women say improves comfort and confidence &mdash; a 20-minute session with no downtime. "
                 "FormaV, $500 a session or three for $1,350, physician-led.")
    p["trust"] = ["No Downtime","Comfortable Warmth","No Numbing Needed","3 Sessions for $1,350"]
    p["introlead"] = ("Childbirth, menopause and time can change intimate tissue and how it feels. FormaV warms the tissue to a precise, "
                      "comfortable temperature, and many women report better comfort, moisture and tone over a series of treatments.")
    p["intropara"] = (p["intropara"].replace("FormaV is performed on the EmpowerRF platform", "FormaV is performed on the <a href=\"/empowerrf/\">EmpowerRF</a> platform")
                      + " FormaV is an FDA-cleared radiofrequency device, but it is not FDA-approved for intimate or sexual-wellness indications; individual results vary.")
    p["cards"] = [(h, d) if h != "Cancer Survivors" else ("Can&rsquo;t Use Estrogen","A non-hormonal option to discuss with your physician &mdash; and your oncologist, if you&rsquo;ve had cancer.")
                  for h, d in p["cards"]]
    p["cards"] = [(h, d.replace("Improved blood flow means improved responsiveness.", "Many women report feeling more responsive after a series."))
                  for h, d in p["cards"]]
    def _fa(q, a):
        if q.startswith("How much"):
            return (q, "$500 per session at Serene Med Spa in Hudson, or $1,350 for a series of three. Morpheus8V is $800 (3 for $2,100), and EmpowerRF Complete is $4,200.")
        if q.startswith("How long do results"):
            return (q, "Many women keep their results with a maintenance session every 6&ndash;12 months. Results vary from person to person.")
        if q.startswith("How is FormaV different"):
            return (q, a.replace("MorpheusV", "<a href=\"/morpheus8v/\">Morpheus8V</a>"))
        return (q, a)
    p["faqs"] = [_fa(q, a) for q, a in p["faqs"]]
    p["faqs"].append(("Is FormaV FDA-approved for vaginal tightening?","No. FormaV is an FDA-cleared radiofrequency device, and the FDA has cautioned that no energy-based device is approved for intimate or sexual-wellness indications. Its use for intimate wellness is physician-directed, and we&rsquo;ll be candid about what to expect."))
    p["related"] = ["empowerrf","morpheus8v","vtone"]
    p["pricing_html"] = _price_block("Pricing","FormaV pricing",[("FormaV", _FV + " / session", "About 20 minutes, no downtime"),("FormaV &mdash; Series of 3", _FV3, "The standard program"),("Morpheus8V", _M8V + " / session", "3 for " + _M8V3),("EmpowerRF Complete", _EMP, "FormaV &times;3 + Morpheus8V &times;3 + VTone &times;6")], _EMP_NOTE)
_patch("formav", _formav)

def _wsw(p):
    p["cards"] = [
        ("V-Renew PRP","Our physician-administered PRP treatment using components from your own blood &mdash; also known as the O-Shot&reg;. <a href=\"/v-renew/\">V-Renew &rarr;</a>"),
        ("EmpowerRF","Morpheus8V, FormaV and VTone on one InMode platform, with series pricing. <a href=\"/empowerrf/\">EmpowerRF &rarr;</a>"),
        ("VTone","FDA-cleared pelvic-floor stimulation for urinary incontinence in women. <a href=\"/vtone/\">VTone &rarr;</a>"),
        ("FormaV &amp; Morpheus8V","Radiofrequency options many women use for comfort and tone. <a href=\"/formav/\">FormaV</a> &middot; <a href=\"/morpheus8v/\">Morpheus8V</a>"),
        ("After Childbirth or Menopause","Support for changes many women experience."),
        ("Private &amp; Physician-Led","Care in a comfortable, judgment-free setting, guided by our board-certified physicians."),
    ]
    p["related"] = ["empowerrf","vtone","hormone-optimization"]
_patch("womens-sexual-wellness", _wsw)
