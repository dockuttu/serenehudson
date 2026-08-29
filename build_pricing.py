# -*- coding: utf-8 -*-
import os, json
exec(open("/home/claude/hudson-site/common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
URL="https://hudson.serenemedspas.com/pricing/"

def row(name, val, unit=""):
    u = ' <span class="unit">%s</span>' % unit if unit else ""
    if val is None:  # free
        val_html = '<span class="price-free">Free</span>'
    else:
        val_html = val + u
    return '<div class="price-row"><span class="price-name">%s</span><span class="price-lead"></span><span class="price-val">%s</span></div>' % (name, val_html)

def sub(t): return '<div class="sub">%s</div>' % t

def rowaka(name, aka, val, unit=""):
    u = ' <span class="unit">%s</span>' % unit if unit else ""
    nm = '%s<span style="display:block;font-size:.76rem;color:var(--muted);font-weight:400;margin-top:2px">also known as the %s</span>' % (name, aka)
    return '<div class="price-row"><span class="price-name">%s</span><span class="price-lead"></span><span class="price-val">%s%s</span></div>' % (nm, val, u)

# ---- categories: (title, inner_html) ----
CATS=[]

CATS.append(("Injectables", sub("Dermal Fillers &mdash; Juv&eacute;derm") +
  row("Lip Filler","$500","/syringe")+row("Mini Pout","$300")+row("Cheek Filler","$500","/syringe")+
  row("Under-Eye Filler","$500","/syringe")+row("Jawline Filler","$500","/syringe")+row("Hand Filler","$500","/syringe")+
  row("Radiesse","$500","/syringe")+row("3 Juv&eacute;derm Fillers","$1,400")+
  sub("Neurotoxins")+
  row("Botox","$11","/unit")+row("Xeomin","$11","/unit")+row("Dysport","$3.99","/unit")+row("Daxxify","$11","/unit")+
  row("Shoulder Slimming Botox","$11","/unit")+row("Baby Botox","$220","/ 20 units")+
  sub("Collagen &amp; Biostimulators")+
  row("Sculptra","$750","/vial")+row("Skinvive","$400","/syringe")+row("Under-Eye PRP","$400")+row("Under-Eye PRF","$600")+
  row("Kybella Fat Dissolver","$600","/vial")+row("Filler Reversal","$150+")))

CATS.append(("Weight Loss &amp; Wellness",
  row("Medical Weight Loss Visit","$149","/month")+
  row("Bi&ouml;te Hormone Therapy &mdash; Female","$450")+row("Bi&ouml;te Hormone Therapy &mdash; Male","$650")+
  row("NAD+","$250","/vial")+row("IV Vitamin Infusions","$149")+
  row("Hyperhidrosis Treatment","$400")+row("Morpheus8 Hyperhidrosis","$600")+
  row("Teeth Grinding Treatment","$360+")+
  '<div class="price-row" style="border:0"><span class="price-name" style="font-size:.8rem;color:var(--muted)">Wegovy&reg; or Zepbound&reg; prescribed to your pharmacy when appropriate &mdash; medication billed separately. The visit fee covers your medical consultation.</span><span class="price-lead"></span><span class="price-val"></span></div>'))

CATS.append(("Laser &amp; Skin",
  row("Laser Facial","$400")+row("Laser Nail Fungus","$150+")+row("Depigmentation Treatment","$200+")+
  row("VI Chemical Peels","$250+")+row("PDO Thread Face Lift","$500+")+row("Sciton BBL Heroic","$400")+
  row("Sciton Moxi","$500")+row("CoolPeel","$400")+row("Deka CO&sup2; Laser","$800")+row("Opus Plasma","$400")+
  '<div class="sub">Laser Hair Removal &mdash; per session / package of 6 (save 10%)</div>'+
  '''<table class="lhr-table"><thead><tr><th>Area</th><th>Per session</th><th>Package of 6</th></tr></thead><tbody>
  <tr><td>Upper Lip</td><td>$60</td><td>$325</td></tr>
  <tr><td>Chin</td><td>$60</td><td>$325</td></tr>
  <tr><td>Lip &amp; Chin</td><td>$80</td><td>$430</td></tr>
  <tr><td>Under Arms</td><td>$90</td><td>$485</td></tr>
  <tr><td>Face</td><td>$115</td><td>$620</td></tr>
  <tr><td>Forearms</td><td>$115</td><td>$620</td></tr>
  <tr><td>Back / Front of Neck</td><td>$115</td><td>$620</td></tr>
  <tr><td>Bikini</td><td>$145</td><td>$785</td></tr>
  <tr><td>Full Arms</td><td>$175</td><td>$945</td></tr>
  <tr><td>Brazilian Bikini</td><td>$175</td><td>$945</td></tr>
  <tr><td>Half Legs (lower or upper)</td><td>$175</td><td>$945</td></tr>
  <tr><td>Back</td><td>$205</td><td>$1,105</td></tr>
  <tr><td>Full Legs</td><td>$235</td><td>$1,270</td></tr>
  </tbody></table>'''))

CATS.append(("Acne Clinic",
  row("Acne Consultation (new &amp; follow-up)",None)+row("Acne Peel","$100")+row("Acne Back Peel","$150")))

CATS.append(("Hair, Face &amp; Body", sub("Hair Restoration")+
  row("PRP Hair Restoration","$800","/tx")+row("Alma TED","$850","/tx")+
  sub("Facials")+row("HydraFacial","$150")+row("DiamondGlow","$150")+row("Facials &amp; Dermaplaning","$100+")+
  sub("Body Treatments")+row("Microneedling","$200")+row("Microneedling with PRP","$500")+
  row("Morpheus8 RF","$800","/tx")+row("Morpheus8 RF &mdash; Series of 3","$2,100")+
  row("Spider Vein","$300+","/session")+row("Sculptra BBL","$6,000")+row("EvolveX Body Contouring","$250","/tx")+
  row("EMSCULPT Neo","$750","/tx")))

CATS.append(("Sexual Wellness", sub("Female Wellness")+
  rowaka("V-Renew PRP","O-Shot&reg;","$800")+row("VTone (Muscle Strengthening)","$350","/tx")+
  row("MorpheusV (Remodeling)","$800")+row("FormaV (Tightening)","$500")+
  sub("Male Wellness")+rowaka("P-Renew PRP","P-Shot&reg;","$1,200")+row("Alma Duo","$500","/tx")+row("Grow Girth","$800","/syringe")))

_HIDDEN_PEPTIDES = (("Peptide Therapy", sub("Priced monthly unless noted")+
  row("BPC-157","$150","/mo")+row("TB-500","$200","/mo")+row("Wolverine Stack (BPC-157 + TB-500)","$450","/mo")+
  row("CJC-1295 + Ipamorelin","$225","/mo")+row("Sermorelin","$150","/mo")+row("Tesamorelin","$250","/mo")+
  row("GHK-Cu (Copper Peptide)","$150","/mo")+row("PT-141 / Bremelanotide","$150","/vial")+
  row("Ipamorelin","$165","/mo")+row("Thymosin Alpha-1","$200","/mo")+row("Semax","$140","/mo")+row("Selank","$140","/mo")+
  row("NAD+","$250","/vial")+row("Glutathione","$50","IV add-on")+
  '<div class="price-row" style="border:0"><span class="price-name" style="font-size:.8rem;color:var(--muted)">Semaglutide &amp; Tirzepatide priced under Weight Loss &amp; Wellness.</span><span class="price-lead"></span><span class="price-val"></span></div>'))

CATS.append(("IV Infusions", sub("$149 each")+
  row("Serene Quench+","$149")+row("Serene Recovery &amp; Performance Pro","$149")+row("Serene Immune Armor","$149")+
  row("Myer&rsquo;s Cocktail","$149")+
  row("Serene Beauty Glow","$149")+row("Serene Reboot Relief","$149")+row("Serene Brain Boost","$149")+
  row("Serene PMS Ease","$149")+row("Serene Get-Up-&amp;-Go","$149")))

import re as _re
def _slug(t): return "cat-"+_re.sub(r'[^a-z0-9]+','-', _re.sub(r'&[a-z]+;','',t).lower()).strip('-')
cats_html="\n".join('<div class="price-cat reveal" id="%s"><h3>%s</h3>%s</div>'%(_slug(t),t,inner) for t,inner in CATS)
jump_html='<div class="price-jump reveal">'+"".join('<a href="#%s">%s</a>'%(_slug(t),t) for t,_ in CATS)+'</div>'

# Offer schema (headline priced services)
OFFERS=[("Botox",11),("Dermal Fillers",500),("Lip Filler",500),("Sculptra",700),("Kybella",600),
 ("Morpheus8 RF",800),("HydraFacial",199),("DiamondGlow",175),("Microneedling with PRP",675),
 ("Laser Hair Removal",60),("EMSCULPT Neo",750),("IV Vitamin Infusion",149),
 ("Medical Weight Loss Visit",149),("PRP Hair Restoration",800)]
offer_schema={"@context":"https://schema.org","@type":"OfferCatalog","name":"Serene Med Spa Hudson — Menu & Pricing","url":URL,
 "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n},"price":str(p),"priceCurrency":"USD"} for n,p in OFFERS]}

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"https://hudson.serenemedspas.com/"},
 {"@type":"ListItem","position":2,"name":"Pricing","item":URL}]}

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pricing &amp; Menu | Serene Med Spa, Hudson OH</title>
<meta name="description" content="Serene Med Spa Hudson pricing: Botox from $11/unit, dermal fillers, Morpheus8, laser, HydraFacial, weight loss, IV infusions &amp; more. Physician-led care in Hudson, OH.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Menu &amp; Pricing &mdash; Serene Med Spa, Hudson OH">
<meta property="og:description" content="Physician-led med spa pricing in Hudson, Ohio &mdash; injectables, laser, body, wellness &amp; more.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(offer_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Menu &amp; Pricing</strong> &mdash; ask about current specials, memberships &amp; package savings. <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Pricing</div>
    <div class="svc-hero-grid">
      <div class="svc-hero-txt">
        <div class="eyebrow">Transparent, Physician-Led</div>
        <h1>Menu &amp; Pricing</h1>
        <p>Our full treatment menu at the Hudson location. Prices are a starting point &mdash; your exact plan and final pricing are confirmed during your consultation. Package &amp; membership savings available.</p>
        <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Consultation</a>
        <a class="btn btn-outline" href="tel:+13304605915">Call (330) 460-5915</a>
      </div>
      <div class="svc-hero-media"><img src="/img/facial-2.jpg" alt="Serene Med Spa treatment menu &amp; pricing, Hudson Ohio" width="800" height="800"></div>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    {jump_html}
    <div class="price-cats">
{cats_html}
    </div>
    <p class="price-note">Prices shown are starting points and may vary based on your individual treatment plan, product amount, and areas treated. Final pricing is confirmed at your consultation. Package, membership, and financing options are available &mdash; ask our team for details. Pricing subject to change.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
os.makedirs("/home/claude/hudson-site/bundle/site/pricing", exist_ok=True)
open("/home/claude/hudson-site/bundle/site/pricing/index.html","w").write(HTML)
print("pricing page written:", len(HTML), "bytes;", len(CATS), "categories")
