# -*- coding: utf-8 -*-
# pages_data_new_zz_biote_labs.py — Biote hormone & wellness lab panels section for /hormone-optimization/.
# Loaded last by gen_pages.py (alphabetical glob). Identical in both repos; Barboursville localizes the copy.
# Public page shows the Labcorp test code and Serene's internal SKU only — no prices.
# Avoid the bare token "OH" in this file (Barboursville's localizer rewrites it to "WV").
import os as _os
exec(open("labs_data.py", encoding="utf-8").read())   # CHIP_SLUG, TESTS

_BL_PANELS = {
 "Women": [
  ("Expanded Baseline Panel", "Before your first treatment", "260103", "9295",
   ["CBC", "CMP", "Estradiol (LC-MS/MS)", "FSH", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG",
    "TSH", "Free T3", "Free T4", "TPO Antibodies", "Vitamin B12", "Vitamin D (25-hydroxy)", "Ferritin"]),
  ("Expanded Follow-Up Panel", "After treatment, no thyroid care", "260108", "4075",
   ["Estradiol (LC-MS/MS)", "FSH", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG"]),
  ("Expanded Follow-Up + Thyroid", "After treatment, if we also treat your thyroid", "260181", "5715",
   ["Estradiol (LC-MS/MS)", "FSH", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG", "TSH", "Free T3", "Free T4"]),
  ("Basic Baseline Panel", "Before your first treatment", "248634", "6675",
   ["CBC", "CMP", "Estradiol", "FSH", "Total Testosterone", "TSH", "Free T3", "Free T4", "TPO Antibodies", "Vitamin B12", "Vitamin D (25-hydroxy)"]),
  ("Basic Follow-Up Panel", "After treatment", "242625", "1745",
   ["Estradiol", "FSH", "Total Testosterone"]),
  ("Basic Follow-Up + Thyroid", "After treatment, if we also treat your thyroid", "248671", "3430",
   ["Estradiol", "FSH", "Total Testosterone", "TSH", "Free T3", "Free T4"]),
 ],
 "Men": [
  ("Expanded Baseline Panel", "Before your first treatment", "260104", "9795",
   ["CBC", "CMP", "Estradiol (LC-MS/MS)", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG", "LH", "Prolactin",
    "PSA", "TSH", "Free T3", "Free T4", "TPO Antibodies", "Vitamin B12", "Vitamin D (25-hydroxy)"]),
  ("Expanded Follow-Up Panel", "After treatment, no thyroid care", "260106", "3790",
   ["CBC", "Estradiol (LC-MS/MS)", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG"]),
  ("Expanded Follow-Up + Thyroid", "After treatment, if we also treat your thyroid", "260105", "5430",
   ["CBC", "Estradiol (LC-MS/MS)", "Total Testosterone (LC-MS/MS)", "Free Testosterone (calculated)", "SHBG", "TSH", "Free T3", "Free T4"]),
  ("Basic Baseline Panel", "Before your first treatment", "248692", "7635",
   ["CBC", "CMP", "Estradiol", "Total Testosterone", "Free Testosterone", "PSA", "TSH", "Free T3", "Free T4", "TPO Antibodies", "Vitamin B12", "Vitamin D (25-hydroxy)"]),
  ("Basic Follow-Up Panel", "After treatment", "248622", "2420",
   ["CBC", "Estradiol", "Total Testosterone", "Free Testosterone"]),
  ("Basic Follow-Up + Thyroid", "After treatment, if we also treat your thyroid", "248683", "4105",
   ["CBC", "Estradiol", "Total Testosterone", "Free Testosterone", "TSH", "Free T3", "Free T4"]),
 ],
}

_BL_TESTS = [
 ("CBC (complete blood count)", "Red and white blood cells, hemoglobin, hematocrit and platelets.",
  "Screens for anemia and infection. Hormone therapy, especially testosterone, can raise red blood cell counts, so we check hematocrit before and during treatment."),
 ("CMP (comprehensive metabolic panel)", "Kidney and liver function, blood sugar, electrolytes and protein.",
  "A baseline safety check of the organs that process medications, plus an early look at blood sugar."),
 ("Estradiol", "The main estrogen in women and men.",
  "Guides dosing and balance. The LC-MS/MS method in our expanded panels measures low levels more accurately, which matters for men and postmenopausal women."),
 ("FSH and LH", "Pituitary signals that tell the ovaries and testes to work.",
  "FSH helps show where a woman is in the menopause transition. In men, LH helps show whether low testosterone starts in the testes or the pituitary."),
 ("Total testosterone", "All the testosterone in your blood.",
  "Confirms whether levels are truly low, then keeps treatment in a healthy range instead of too high."),
 ("Free testosterone and SHBG", "SHBG is a protein that binds hormones; free testosterone is the active, unbound part.",
  "Two people with the same total testosterone can feel very different. These two numbers explain why."),
 ("TSH, Free T3 and Free T4", "How well your thyroid is working.",
  "Thyroid problems cause fatigue, weight gain, brain fog and low mood, the same symptoms people blame on hormones. We rule them out first."),
 ("TPO antibodies", "Antibodies that attack the thyroid.",
  "An early marker of Hashimoto&rsquo;s thyroiditis, a common cause of an underactive thyroid, especially in women."),
 ("Vitamin B12", "A vitamin needed for nerves and red blood cells.",
  "Low B12 can cause tiredness, numbness and trouble concentrating."),
 ("Vitamin D (25-hydroxy)", "Your body&rsquo;s vitamin D stores.",
  "Vitamin D supports bone, muscle and immune health, and low levels are common."),
 ("Ferritin", "Iron stores (women&rsquo;s expanded panel).",
  "Low iron can cause fatigue and hair shedding even before anemia shows up."),
 ("PSA", "Prostate-specific antigen (men).",
  "A prostate health check before starting testosterone and again during treatment."),
 ("Prolactin", "A pituitary hormone (men&rsquo;s expanded panel).",
  "High prolactin can lower testosterone and libido and needs its own workup."),
]

def _bl_badge():
    for f in ("biote-certified-provider.png", "biote-certified-provider.webp", "biote-certified-provider.svg", "biote-certified.png"):
        if _os.path.exists(_os.path.join("bundle", "site", "img", "badges", f)):
            return '<img src="/img/badges/%s" alt="Biote Certified Provider" class="bl-badge" loading="lazy">' % f
    return ""

def _bl_card(name, when, code, sku, tests):
    chips = "".join(('<a href="/labs/%s/">%s</a>' % (CHIP_SLUG[t], t)) if t in CHIP_SLUG else ('<span>%s</span>' % t) for t in tests)
    return ('<div class="bl-card reveal"><div class="bl-when">%s</div><h4>%s</h4>'
            '<div class="bl-codes"><span>Labcorp test <b>%s</b></span><span>Serene SKU <b>%s</b></span></div>'
            '<div class="bl-chips">%s</div></div>') % (when, name, code, sku, chips)

_BL_CSS = """<style>
.bl{padding:70px 0;background:#fff}
.bl .bl-lead{max-width:820px;margin:0 auto 26px;text-align:center;font-size:1.12rem;line-height:1.65;color:var(--ink);font-weight:500}
.bl .bl-badge{display:block;height:92px;width:auto;margin:0 auto 18px}
.bl-tabs{display:flex;justify-content:center;gap:10px;margin:0 0 22px}
.bl-tabs button{font:inherit;font-weight:600;font-size:1rem;padding:10px 26px;border-radius:999px;border:1.5px solid rgba(63,43,61,.2);background:#fff;color:var(--ink);cursor:pointer}
.bl-tabs button[aria-selected=true]{background:var(--plum);border-color:var(--plum);color:#fff}
.bl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}
.bl-card{border:1.5px solid rgba(63,43,61,.12);border-radius:18px;padding:22px;background:#fffdfc}
.bl-when{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--rose-deep);font-weight:700}
.bl-card h4{font-family:'Cormorant Garamond',serif;font-size:1.55rem;color:var(--ink);margin:4px 0 10px}
.bl-codes{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.bl-codes span{font-size:.92rem;background:var(--blush,#fbeae6);border-radius:8px;padding:5px 10px;color:var(--ink);font-weight:500}
.bl-chips{display:flex;flex-wrap:wrap;gap:6px}
.bl-chips a{font-size:.93rem;border:1px solid rgba(201,79,116,.35);border-radius:999px;padding:4px 11px;color:var(--ink);font-weight:500;background:#fff;text-decoration:none;transition:background .15s,border-color .15s}
.bl-chips a:hover{background:var(--blush,#fbeae6);border-color:var(--rose-deep)}
.bl-table td a{color:var(--rose-deep);text-decoration:none;border-bottom:1px dotted currentColor}
.bl-chips span{font-size:.93rem;border:1px solid rgba(63,43,61,.16);border-radius:999px;padding:4px 11px;color:var(--ink);font-weight:500;background:#fff}
.bl-note{font-size:1rem;color:var(--ink);font-weight:500;margin:16px 0 0;line-height:1.6}
.bl-table{width:100%;border-collapse:collapse;margin-top:10px;font-size:1.02rem;color:var(--ink)}
.bl-table th,.bl-table td{text-align:left;padding:12px 14px;border-bottom:1px solid rgba(63,43,61,.12);vertical-align:top;line-height:1.55}
.bl-table th{font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;color:var(--rose-deep)}
.bl-table td:first-child{font-weight:700;white-space:nowrap}
.bl-why{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:10px}
.bl-why div{background:var(--blush,#fbeae6);border-radius:16px;padding:20px}
.bl-why h4{margin:0 0 6px;font-size:1.1rem;color:var(--ink)}
.bl-why p{margin:0;font-size:1rem;line-height:1.6;color:var(--ink);font-weight:500}
.bl-src{font-size:.88rem;color:var(--ink);opacity:.8;margin-top:14px;line-height:1.6}
@media(max-width:700px){.bl-table td:first-child{white-space:normal}.bl-table th:nth-child(2),.bl-table td:nth-child(2){display:none}}
</style>"""

def _bl_section():
    women = "".join(_bl_card(*c) for c in _BL_PANELS["Women"])
    men = "".join(_bl_card(*c) for c in _BL_PANELS["Men"])
    _row_slugs = ["cbc","cmp","estradiol","fsh","total-testosterone","free-testosterone","tsh","tpo-antibodies","vitamin-b12","vitamin-d","ferritin","psa","prolactin"]
    rows = "".join('<tr><td><a href="/labs/%s/">%s</a></td><td>%s</td><td>%s</td></tr>' % ((sl,) + t) for sl, t in zip(_row_slugs, _BL_TESTS))
    return _BL_CSS + '''
<section class="bl" id="labs">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Wellness Lab Panels</div><h2>Biote Hormone &amp; Wellness Labs</h2></div>
    ''' + _bl_badge() + '''
    <p class="bl-lead reveal">Every hormone plan at Serene starts with blood work, processed by <strong>Labcorp</strong>. We use Biote&rsquo;s lab panels for women and men: a <strong>baseline panel</strong> before your first treatment and a shorter <strong>follow-up panel</strong> after, so your plan is guided by your numbers, not guesswork. Lab fees are reviewed with you at your consultation.</p>
    <div class="bl-tabs" role="tablist">
      <button type="button" role="tab" aria-selected="true" data-bl="bl-women">Women</button>
      <button type="button" role="tab" aria-selected="false" data-bl="bl-men">Men</button>
    </div>
    <div class="bl-grid" id="bl-women" role="tabpanel">''' + women + '''</div>
    <div class="bl-grid" id="bl-men" role="tabpanel" hidden>''' + men + '''</div>
    <p class="bl-note">Women&rsquo;s basic panels can add a free testosterone test (Labcorp 70130) when your physician needs it. Your physician chooses the panel that fits your history, symptoms and treatment. <strong>Tap any test</strong> to learn what it measures, or browse the <a href="/labs/">full lab test guide</a>.</p>

    <div class="section-head reveal" style="margin-top:56px"><div class="eyebrow">What we check</div><h2>What each test tells us</h2></div>
    <div style="overflow-x:auto"><table class="bl-table">
      <thead><tr><th>Test</th><th>What it measures</th><th>Why it matters</th></tr></thead>
      <tbody>''' + rows + '''</tbody>
    </table></div>

    <div class="section-head reveal" style="margin-top:56px"><div class="eyebrow">Why labs matter</div><h2>Why we test before and during treatment</h2></div>
    <div class="bl-why">
      <div class="reveal"><h4>Confirm the diagnosis</h4><p>Symptoms alone aren&rsquo;t enough. Urology guidelines, for example, call for two early-morning testosterone tests plus symptoms before diagnosing low testosterone.</p></div>
      <div class="reveal"><h4>Rule out look-alikes</h4><p>Thyroid disease, anemia, low iron and low B12 or vitamin D can all mimic hormone imbalance. The baseline panel checks for them.</p></div>
      <div class="reveal"><h4>Keep treatment safe</h4><p>Endocrine Society guidance calls for checking hematocrit before testosterone therapy, again at 3&ndash;6 months and then yearly, and for PSA checks in many men. For women, experts advise a baseline testosterone level and repeat testing to avoid levels that run too high.</p></div>
      <div class="reveal"><h4>Personalize your dose</h4><p>Follow-up labs show how your body responded, so your physician can adjust the next dose to how you feel and what your numbers show.</p></div>
    </div>
    <p class="bl-src">References: Bhasin S, et al. Testosterone therapy in men with hypogonadism: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2018;103(5):1715&ndash;1744. &middot; Mulhall JP, et al. Evaluation and management of testosterone deficiency: AUA guideline. J Urol. 2018;200(2):423&ndash;432. &middot; Davis SR, et al. Global consensus position statement on the use of testosterone therapy for women. J Clin Endocrinol Metab. 2019;104(10):4660&ndash;4666. Lab tests are ordered only after a consultation with a licensed provider.</p>
  </div>
</section>
<script>
(function(){var b=document.querySelectorAll('.bl-tabs button');b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.setAttribute('aria-selected',y===x?'true':'false');document.getElementById(y.getAttribute('data-bl')).hidden=(y!==x);});});});})();
</script>'''

_BL_FAQS = [
 ("What labs do you run before hormone therapy?",
  "We start with a Biote baseline panel through Labcorp. Depending on the panel, it checks estradiol, testosterone, SHBG, FSH or LH, thyroid function, vitamin B12, vitamin D, a complete blood count and a metabolic panel, plus PSA for men and ferritin in the women&rsquo;s expanded panel."),
 ("How often are labs repeated?",
  "A shorter follow-up panel is drawn after treatment to see how your body responded, and then at intervals your physician sets. Guidelines for testosterone therapy recommend checking blood counts at 3&ndash;6 months and then yearly."),
 ("Why do you check my blood count on hormone therapy?",
  "Testosterone can raise red blood cell levels (hematocrit). Checking it before and during treatment lets your physician catch and manage that early."),
 ("Do I have to pay separately for labs?",
  "Lab fees are separate from your treatment and are reviewed with you at your consultation before anything is ordered."),
]

for _lst in (PAGES, PAGES2, PAGES3, PAGES4, PAGES5, PAGES6):
    for _p in _lst:
        if _p.get("slug") != "hormone-optimization" or _p.get("_bl_done"):
            continue
        _p["_bl_done"] = True
        _p["title"] = "Biote Hormone Optimization &amp; Lab Testing | Hudson, OH"
        _p["desc"] = ("Physician-led Biote hormone optimization in Hudson, Ohio, guided by Labcorp lab panels for hormones, thyroid, "
                      "vitamins and blood counts. Book a consultation.")
        _p["ogtitle"] = "Biote Hormone Optimization &amp; Lab Testing in Hudson, OH"
        _p["ogdesc"] = "Physician-led hormone optimization guided by Labcorp lab panels for women and men."
        _p["trust"] = ["Physician-Led", "Biote Certified Provider", "Labcorp Lab Panels", "Ongoing Monitoring"]
        _p["pricing_html"] = _bl_section() + _p.get("pricing_html", "")
        _p["faqs"] = list(_p["faqs"]) + _BL_FAQS
