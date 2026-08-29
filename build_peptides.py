# -*- coding: utf-8 -*-
import os, json
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://hudson.serenemedspas.com"
URL=f"{SITE}/peptides/"

# Curated OFFER (clean-footing) peptides only. group, name, benefit (supportive/compliant), price
GROUPS=[
 ("Growth Hormone &amp; Anti-Aging",[
   ("Sermorelin","Supports your body&rsquo;s own growth hormone for energy, recovery &amp; healthy aging.","$150/mo"),
   ("Ipamorelin","A gentle GH secretagogue to support recovery, sleep &amp; vitality.","$165/mo"),
   ("CJC-1295 + Ipamorelin","Our flagship anti-aging pairing &mdash; supports GH, recovery &amp; body composition.","$225/mo"),
   ("Tesamorelin","Supports metabolism and healthy body composition.","$250/mo"),
 ]),
 ("Sexual Wellness",[
   ("PT-141 (Bremelanotide)","Supports libido and sexual wellness for women and men.","$150/vial"),
 ]),
 ("Skin &amp; Aesthetic",[
   ("GHK-Cu (Copper Peptide)","Supports skin firmness, a healthy glow, and hair.","$150/mo"),
 ]),
 ("Cellular &amp; Immune Wellness",[
   ("NAD+","Cellular energy and anti-aging support.","$250/vial"),
   ("Glutathione","The body&rsquo;s master antioxidant &mdash; for glow and cellular defense.","$50 IV add-on"),
   ("Thymosin Alpha-1","Supports immune resilience and overall wellness.","$200/mo"),
 ]),
 ("Focus &amp; Mood",[
   ("Semax","Supports focus, mental clarity, and mood.","$140/mo"),
   ("Selank","Supports calm, focus, and mood balance.","$140/mo"),
 ]),
]

def group_html(title, items):
    cards="\n".join(f'''        <div class="pep-card">
          <div class="pep-top"><h3>{n}</h3><span class="pep-price">{p}</span></div>
          <p>{b}</p>
        </div>''' for (n,b,p) in items)
    return f'''      <div class="pep-group">
        <h2 class="pep-h">{title}</h2>
        <div class="pep-grid">
{cards}
        </div>
      </div>'''

body="\n".join(group_html(t,i) for t,i in GROUPS)

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"IV Therapy","item":SITE+"/iv-therapy/"},
  {"@type":"ListItem","position":3,"name":"Peptide Menu","item":URL}]}
page_schema={"@context":"https://schema.org","@type":"MedicalWebPage","name":"Peptide Therapy Menu","url":URL,
  "about":{"@type":"MedicalTherapy","name":"Peptide Therapy"},"lastReviewed":"2026-08-27","audience":{"@type":"Patient"}}

HEAD_FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Peptide Therapy Menu | Serene Med Spa, Hudson OH</title>
<meta name="description" content="Physician-led peptide therapy in Hudson, OH &mdash; Sermorelin, CJC-1295 + Ipamorelin, PT-141, GHK-Cu, NAD+ &amp; more. Offered after consultation. See the menu.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="noindex, nofollow">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Peptide Therapy Menu | Serene Med Spa">
<meta property="og:description" content="Physician-led peptide therapy in Hudson, OH. Offered after consultation.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/img/inject-hero.jpg">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(page_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Physician-Led Peptide Therapy</strong> &mdash; personalized wellness, offered after consultation. <a href="{BOOK}" target="_blank" rel="noopener">Book a consult</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/peptide-therapy/">Peptide Therapy</a> &nbsp;&#8250;&nbsp; Menu</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <div class="eyebrow">Physician-Led Peptide Therapy</div>
      <h1>Peptide Therapy Menu</h1>
      <p>Targeted peptides to support energy, recovery, skin, immunity, and healthy aging &mdash; personalized and physician-supervised. Every plan starts with a consultation to find the right fit for you.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
{body}
    <p class="pep-fine">Peptide therapy is offered after a physician consultation to appropriate candidates (18+) and is intended to support general wellness &mdash; it is not intended to diagnose, treat, cure, or prevent any disease. Availability is at our medical team&rsquo;s discretion. Additional peptides may be available; ask during your consultation. See full <a href="/pricing/">pricing</a>.</p>
    <div class="pep-cta">
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Peptide Consultation</a>
    </div>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''

os.makedirs("bundle/site/peptides",exist_ok=True)
open("bundle/site/peptides/index.html","w").write(HTML)
print("peptides page written:", len(HTML), "bytes")
