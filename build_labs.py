# -*- coding: utf-8 -*-
# build_labs.py — /labs/ index + /labs/<test>/ guide pages (one per lab test). Identical in both repos.
import json, os, html as _h
ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
exec(open("labs_data.py", encoding="utf-8").read(), ns)
NAV, FOOTER, SCRIPTS, CONSULT, STICKY = ns["NAV"], ns["FOOTER"], ns["SCRIPTS"], ns["CONSULT_SECTION"], ns.get("STICKY_BAR", "")
TESTS, CHIP_SLUG = ns["TESTS"], ns["CHIP_SLUG"]
HORMONE_BOOK = ns.get("BOOK_MAP", {}).get("hormone-optimization", ns["BOOK"])

# panel membership (from the hormone page data)
_pd = {"PAGES": [], "PAGES2": [], "PAGES3": [], "PAGES4": [], "PAGES5": [], "PAGES6": []}
exec(open("pages_data_new_zz_biote_labs.py", encoding="utf-8").read(), _pd)
PANELS = _pd["_BL_PANELS"]

if "barboursville" in os.path.basename(os.getcwd()).lower():
    SITE, CITY, CITY_LONG, REGION = "https://barboursville.serenemedspas.com", "Barboursville, WV", "Barboursville, West Virginia", "US-WV"
    AREA = "Barboursville, Huntington and the Tri-State"
else:
    SITE, CITY, CITY_LONG, REGION = "https://hudson.serenemedspas.com", "Hudson, OH", "Hudson, Ohio", "US-OH"
    AREA = "Hudson, Akron and Northeast Ohio"

HEAD_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

CSS = """<style>
.lt-body{padding:48px 0 60px}
.lt-body .wrap{max-width:860px}
.lt-body h2{font-family:'Cormorant Garamond',serif;font-size:2rem;color:var(--ink);margin:36px 0 10px}
.lt-body p,.lt-body li{font-size:1.1rem;line-height:1.7;color:var(--ink);font-weight:500}
.lt-body ul{padding-left:22px}
.lt-back{display:inline-flex;align-items:center;gap:8px;font-weight:600;color:var(--rose-deep);text-decoration:none;border:1.5px solid rgba(201,79,116,.35);border-radius:999px;padding:9px 18px;margin:0 0 18px;background:#fff}
.lt-back:hover{background:var(--blush,#fbeae6)}
.lt-grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:8px}
.lt-box{background:var(--blush,#fbeae6);border-radius:16px;padding:18px 20px}
.lt-box h3{margin:0 0 6px;font-size:1.15rem;color:var(--ink)}
.lt-box p{margin:0}
.lt-panels{display:flex;flex-wrap:wrap;gap:8px}
.lt-panels a,.lt-panels span{font-size:.98rem;border:1px solid rgba(63,43,61,.18);border-radius:999px;padding:6px 12px;color:var(--ink);font-weight:500;background:#fff;text-decoration:none}
.lt-rel{display:flex;flex-wrap:wrap;gap:8px}
.lt-rel a{font-weight:600;color:var(--rose-deep);border:1px solid rgba(201,79,116,.3);border-radius:999px;padding:6px 14px;text-decoration:none;background:#fff}
.lt-src{font-size:.95rem!important;opacity:.85}
.lt-cta{background:var(--plum);color:#fff;border-radius:20px;padding:26px;margin-top:36px}
.lt-cta p,.lt-cta h2{color:#fff!important;margin-top:0}
.lt-index{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.lt-index a{display:block;border:1.5px solid rgba(63,43,61,.12);border-radius:16px;padding:16px 18px;text-decoration:none;background:#fff}
.lt-index a b{display:block;color:var(--ink);font-size:1.12rem}
.lt-index a span{display:block;color:var(--ink);opacity:.85;font-size:.98rem;margin-top:4px;line-height:1.5}
@media(max-width:700px){.lt-grid2{grid-template-columns:1fr}}
</style>"""

BACK_JS = """<script>
(function(){var b=document.querySelectorAll('.lt-back');b.forEach(function(a){a.addEventListener('click',function(e){
try{var r=document.referrer?new URL(document.referrer):null;if(r&&r.host===location.host&&r.pathname.indexOf('/hormone-optimization/')===0&&history.length>1){e.preventDefault();history.back();}}catch(x){}});});})();
</script>"""

def clean(s):
    return _h.unescape(s)

def panels_for(slug):
    out = []
    for sex, lst in PANELS.items():
        for name, when, code, sku, tests in lst:
            if any(CHIP_SLUG.get(t) == slug for t in tests):
                out.append('<span>%s &middot; %s &middot; Labcorp %s</span>' % (sex, name, code))
    return "".join(out)

def page(title, desc, url, body, schemas, robots="index, follow, max-image-preview:large"):
    sj = "\n".join('<script type="application/ld+json">\n%s\n</script>' % json.dumps(s, ensure_ascii=False) for s in schemas)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="{REGION}"><meta name="geo.placename" content="{CITY}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
{HEAD_FONTS}
{sj}
{CSS}
</head>
<body>

{NAV}

{body}

{CONSULT}

{FOOTER}
{STICKY}
{SCRIPTS}
{BACK_JS}
</body>
</html>'''

def fit_title(seo):
    t = f"{seo} Explained | {CITY} | Serene Med Spa"
    return t if len(clean(t)) <= 60 else f"{seo} Explained | {CITY}"

n = 0
for i, t in enumerate(TESTS):
    url = f"{SITE}/labs/{t['slug']}/"
    title = fit_title(t["seo"])
    desc = f"What the {t['short']} test measures, why it matters in hormone and wellness care, and what high or low results can mean. Serene Med Spa, {CITY}."
    if len(clean(desc)) > 158:
        desc = f"What the {t['short']} test measures and why it matters in hormone and wellness care, from Serene Med Spa in {CITY}."
    rel = [x for x in TESTS if x["slug"] != t["slug"]]
    rel = (rel[i:] + rel[:i])[:5]
    faq_html = "".join(f'<div class="faq reveal"><button>{q}<span class="plus">+</span></button><div class="ans"><p>{a}</p></div></div>' for q, a in t["faqs"])
    src = " &middot; ".join(f'<a href="{u}" target="_blank" rel="noopener">{n_}</a>' for n_, u in t["sources"])
    body = f'''<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/hormone-optimization/">Hormone Optimization</a> &nbsp;&#8250;&nbsp; <a href="/labs/">Lab Test Guide</a> &nbsp;&#8250;&nbsp; {t["short"]}</div>
    <div class="svc-hero-txt" style="max-width:820px">
      <a class="lt-back" href="/hormone-optimization/#labs">&larr; Back to lab panels</a>
      <div class="eyebrow">Lab Test Guide &middot; {CITY}</div>
      <h1>{t["name"]} Test: What It Measures and Why It Matters</h1>
      <p style="font-size:1.15rem;font-weight:500;color:var(--ink)">{t["lead"]}</p>
    </div>
  </div>
</section>

<section class="lt-body">
  <div class="wrap">
    <h2>What the {t["short"]} test measures</h2>
    <ul>{"".join(f"<li>{m}</li>" for m in t["measures"])}</ul>

    <h2>Why we check it at Serene</h2>
    <p>{t["why"]}</p>
    <p>At Serene Med Spa in {CITY_LONG}, every hormone and wellness plan starts with Labcorp lab work reviewed by a board-certified physician.</p>

    <h2>What your results can mean</h2>
    <div class="lt-grid2">
      <div class="lt-box"><h3>Higher than normal</h3><p>{t["high"]}</p></div>
      <div class="lt-box"><h3>Lower than normal</h3><p>{t["low"]}</p></div>
    </div>
    <p style="margin-top:14px">Normal ranges vary by lab, age and sex. Your physician reads every result together with your symptoms, history and other tests.</p>

    <h2>How to prepare</h2>
    <p>{t["prep"]}</p>

    <h2>Serene panels that include {t["short"]}</h2>
    <div class="lt-panels">{panels_for(t["slug"])}</div>
    <p style="margin-top:12px"><a href="/hormone-optimization/#labs">See all Biote lab panels &rsaquo;</a></p>

    <h2>Frequently asked questions</h2>
    <div class="faq-list">{faq_html}</div>

    <div class="lt-cta reveal">
      <h2>Have questions about your labs?</h2>
      <p>Book a hormone and wellness consultation at Serene Med Spa in {CITY}. We&rsquo;ll review your symptoms, order the right panel and walk you through every result.</p>
      <a class="btn" href="{HORMONE_BOOK}" target="_blank" rel="noopener">Book a Consultation</a>
    </div>

    <h2>Other lab tests</h2>
    <div class="lt-rel">{"".join(f'<a href="/labs/{x["slug"]}/">{x["short"]}</a>' for x in rel)} <a href="/labs/">All tests</a></div>

    <p class="lt-src" style="margin-top:28px">Sources: {src}. This page is for general education and is not medical advice. Tests are ordered only after a consultation with a licensed provider.</p>
    <p><a class="lt-back" href="/hormone-optimization/#labs">&larr; Back to lab panels</a></p>
  </div>
</section>'''
    schemas = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Hormone Optimization", "item": SITE + "/hormone-optimization/"},
            {"@type": "ListItem", "position": 3, "name": "Lab Test Guide", "item": SITE + "/labs/"},
            {"@type": "ListItem", "position": 4, "name": clean(t["short"]), "item": url}]},
        {"@context": "https://schema.org", "@type": "MedicalWebPage", "url": url, "name": clean(title), "description": clean(desc),
         "about": {"@type": "MedicalTest", "name": clean(t["name"])},
         "reviewedBy": {"@type": "Physician", "name": "Robin Arora, MD"},
         "publisher": {"@type": "MedicalBusiness", "name": "Serene Med Spa", "url": SITE + "/"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in t["faqs"]]},
    ]
    d = os.path.join("bundle", "site", "labs", t["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(title, desc, url, body, schemas)); n += 1

# index
cards = "".join(f'<a href="/labs/{t["slug"]}/"><b>{t["name"]}</b><span>{t["lead"]}</span></a>' for t in TESTS)
idx_url = SITE + "/labs/"
idx_title = f"Lab Test Guide | Hormone &amp; Wellness Labs | {CITY}"
idx_desc = f"Plain-language guides to every test in our Biote hormone and wellness lab panels, from CBC to thyroid, vitamin D and PSA. Serene Med Spa, {CITY}."
if len(clean(idx_desc)) > 158:
    idx_desc = f"Plain-language guides to every test in our Biote hormone and wellness lab panels. Serene Med Spa, {CITY}."
idx_body = f'''<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/hormone-optimization/">Hormone Optimization</a> &nbsp;&#8250;&nbsp; Lab Test Guide</div>
    <div class="svc-hero-txt" style="max-width:820px">
      <a class="lt-back" href="/hormone-optimization/#labs">&larr; Back to lab panels</a>
      <div class="eyebrow">Lab Test Guide &middot; {CITY}</div>
      <h1>Hormone &amp; Wellness Lab Test Guide</h1>
      <p style="font-size:1.15rem;font-weight:500;color:var(--ink)">What each test in our Biote lab panels measures and why it matters, explained in plain language for patients across {AREA}.</p>
    </div>
  </div>
</section>
<section class="lt-body"><div class="wrap" style="max-width:1100px"><div class="lt-index">{cards}</div></div></section>'''
idx_schema = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Hormone Optimization", "item": SITE + "/hormone-optimization/"},
    {"@type": "ListItem", "position": 3, "name": "Lab Test Guide", "item": idx_url}]}]
open(os.path.join("bundle", "site", "labs", "index.html"), "w", encoding="utf-8").write(page(idx_title, idx_desc, idx_url, idx_body, idx_schema))
print("build_labs: wrote", n, "test pages + index")
