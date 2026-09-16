# -*- coding: utf-8 -*-
# build_easypay.py — /easy-pay/ : Cherry + CareCredit financing page. Identical in both site repos.
import json, os
ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
exec(open("easypay.py", encoding="utf-8").read(), ns)
NAV, FOOTER, SCRIPTS, BOOK = ns["NAV"], ns["FOOTER"], ns["SCRIPTS"], ns["BOOK"]
CONSULT, STICKY = ns["CONSULT_SECTION"], ns.get("STICKY_BAR", "")
CHERRY_URL, CARECREDIT_URL, cc_logo = ns["CHERRY_URL"], ns["CARECREDIT_URL"], ns["_cc_logo"]

if "barboursville" in os.path.basename(os.getcwd()).lower():
    SITE, CITY, REGION, PHONE, TEL = "https://barboursville.serenemedspas.com", "Barboursville, WV", "US-WV", "(304) 520-0461", "tel:+13045200461"
    AREA = "Barboursville, Huntington and the Tri-State"
else:
    SITE, CITY, REGION, PHONE, TEL = "https://hudson.serenemedspas.com", "Hudson, OH", "US-OH", "(330) 460-5915", "tel:+13304605915"
    AREA = "Hudson, Akron and Northeast Ohio"
URL = SITE + "/easy-pay/"

FAQ = [
 ("Will applying hurt my credit score?", "Applying with Cherry has no impact on your credit score. CareCredit lets you check whether you prequalify first; its full application terms are explained on the CareCredit site before you submit."),
 ("Is 0% APR really available?", "Yes, for qualified patients. Both Cherry and CareCredit offer promotional plans. Your rate, term and monthly payment depend on the lender&rsquo;s approval, and you&rsquo;ll see the terms before you accept."),
 ("What can I finance at Serene?", "Most treatments and packages, including injectables, laser and skin treatments, body contouring and wellness programs. Our team will confirm your options at checkout."),
 ("How fast is the decision?", "Most people get a decision within minutes. You can apply from your phone before your visit or at the front desk."),
 ("What does &ldquo;deferred interest&rdquo; mean with CareCredit?", "On a deferred interest promotion, no interest is charged if you pay the full promotional balance by the end of the promo period. If you don&rsquo;t, interest is charged from the original purchase date. Paying on schedule avoids that."),
 ("Is Serene the lender?", "No. Serene Med Spa is not a lender. Cherry plans are provided by Cherry Technologies Inc. and its lending partners, and CareCredit is issued by Synchrony Bank."),
]
def clean(s):
    return (s.replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&amp;", "&"))
faq_html = '<div class="faq-list">' + "".join(
    f'<div class="faq reveal"><button>{q}<span class="plus">+</span></button><div class="ans"><p>{a}</p></div></div>' for q, a in FAQ) + '</div>'
faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in FAQ]}
crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Easy Pay Financing", "item": URL}]}

HEAD_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

TITLE = f"Easy Pay Financing | Cherry &amp; CareCredit | {CITY}"
DESC = f"Pay over time for treatments at Serene Med Spa in {CITY}. Monthly plans through Cherry and CareCredit, with 0% APR options for qualified patients."

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="{REGION}"><meta name="geo.placename" content="{CITY}">
<meta property="og:type" content="website">
<meta property="og:title" content="Easy Pay Financing at Serene Med Spa {CITY}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(faq_schema)}
</script>
</head>
<body data-ep-page="1">

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Easy Pay</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <div class="eyebrow">Easy Pay &middot; {CITY}</div>
      <h1>Easy Pay Financing</h1>
      <p style="font-size:1.15rem;font-weight:500;color:var(--ink)">Get the treatment you want now and pay over time. Serene Med Spa offers monthly payment plans through <strong>Cherry</strong> and <strong>CareCredit</strong>, with 0% APR options for qualified patients across {AREA}.</p>
      <a class="btn" href="{CHERRY_URL}" target="_blank" rel="noopener">See your options with Cherry</a>
      <a class="btn btn-outline" href="{CARECREDIT_URL}" target="_blank" rel="noopener">Apply for CareCredit</a>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Two ways to pay over time</div><h2>Choose the plan that fits you</h2></div>
    <div class="ep-cards">
      <div class="ep-card reveal">
        <img src="/img/logos/cherry.svg" alt="Cherry" class="ep-logo" loading="lazy">
        <h3>Monthly plans with Cherry</h3>
        <ul>
          <li>0% APR plans available for qualified patients</li>
          <li>No impact to your credit score to apply</li>
          <li>Apply from your phone in minutes</li>
          <li>Pay over time for your treatment at Serene</li>
        </ul>
        <a class="btn" href="{CHERRY_URL}" target="_blank" rel="noopener">See your options</a>
      </div>
      <div class="ep-card reveal">
        {cc_logo()}
        <h3>CareCredit health &amp; wellness card</h3>
        <ul>
          <li>Promotional financing options on qualifying purchases</li>
          <li>No annual fee</li>
          <li>Use it again for future visits and at other CareCredit locations</li>
          <li>Check whether you prequalify before you apply</li>
        </ul>
        <a class="btn" href="{CARECREDIT_URL}" target="_blank" rel="noopener">Apply for CareCredit</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">How it works</div><h2>Three simple steps</h2></div>
    <div class="hc-offers">
      <div class="hc-offer reveal"><h3>1. Plan your treatment</h3><p>Book a free consultation. Your provider builds a plan and gives you the exact price.</p></div>
      <div class="hc-offer reveal"><h3>2. Apply in minutes</h3><p>Choose Cherry or CareCredit and apply on your phone, before your visit or at our front desk. Most decisions come back in minutes.</p></div>
      <div class="hc-offer reveal"><h3>3. Treat now, pay monthly</h3><p>Get your treatment on your schedule and pay it off in monthly installments.</p></div>
    </div>
    <p style="text-align:center;margin-top:22px"><a class="btn btn-outline" href="{BOOK}" target="_blank" rel="noopener">Book a Free Consultation</a> &nbsp; <a class="btn btn-outline" href="/pricing/">See Our Pricing</a></p>
  </div>
</section>

<section id="faq" class="tint-blush">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Questions</div><h2>Easy Pay FAQ</h2></div>
    {faq_html}
    <p class="ep-fine">Serene Med Spa is not a lender. Payment options through Cherry Technologies Inc. are issued by its financing partners; 0% APR and other promotional rates are subject to eligibility. CareCredit is a credit card issued by Synchrony Bank; subject to credit approval, minimum monthly payments required. Questions? Call <a href="{TEL}">{PHONE}</a>.</p>
  </div>
</section>

{CONSULT}

{FOOTER}
{STICKY}
{SCRIPTS}
</body>
</html>'''

os.makedirs("bundle/site/easy-pay", exist_ok=True)
open("bundle/site/easy-pay/index.html", "w", encoding="utf-8").write(HTML)
print("wrote bundle/site/easy-pay/index.html")

# keep the Easy Pay styles in styles.css (between markers; runs before cachebust)
_css_path = "bundle/site/styles.css"
_css = open(_css_path, encoding="utf-8").read()
_start, _end = "/* ---- Easy Pay (Cherry + CareCredit) ---- */", "/* ---- /Easy Pay ---- */"
if _start in _css:
    _css = _css[:_css.index(_start)].rstrip() + "\n" + _css[_css.index(_end) + len(_end):].lstrip("\n")
_css = _css.rstrip() + "\n" + ns["EP_CSS"].strip() + "\n"
open(_css_path, "w", encoding="utf-8").write(_css)
print("easy pay styles synced into styles.css")
