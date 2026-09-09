# -*- coding: utf-8 -*-
import os, json, re
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
URL="https://hudson.serenemedspas.com/before-after/"

# category -> (service_link, [ (img, title, desc, link) ])
CATS = [
 ("Lip Filler", "/lip-filler/", [
   ("ba-lip-volbella.jpg", "Juv&eacute;derm Volbella &mdash; Male Lip Filler",
    "One syringe, 70/30 upper-to-lower, with symmetry corrected across all four quadrants and a softened Cupid&rsquo;s bow.",
    "https://blog.serenemedspas.com/male-lip-filler-juvederm-volbella/", "Read the case"),
   ("ba-lip.jpg", "Lip Filler &mdash; Natural Volume",
    "Subtle enhancement that adds fullness while keeping a natural lip shape.", "/lip-filler/", "See treatment"),
 ]),
 ("Dermal Filler", "/fillers/", [
   ("ba-cheek.jpg", "Cheek Filler &mdash; Midface Volume",
    "Restored cheek projection for a lifted, refreshed look.", "/cheek-filler/", "See treatment"),
 ]),
 ("Wrinkle Relaxer", "/botox/", [
   ("ba-forehead.jpg", "Botox &mdash; Forehead &amp; Frown Lines",
    "Smoothed dynamic lines for a rested, natural expression.", "/botox/", "See treatment"),
 ]),
 ("Morpheus8", "/morpheus8/", [
   ("m8-result.jpg", "Morpheus8 &mdash; Skin Tightening",
    "Radiofrequency microneedling to firm skin and refine texture.", "/morpheus8/", "See treatment"),
 ]),
]

def _slug(t): return "gal-"+re.sub(r'[^a-z0-9]+','-', re.sub(r'&[a-z]+;','',t).lower()).strip('-')

def _cards(items):
    out=[]
    for img,title,desc,link,cta in items:
        out.append(
          '<figure class="res reveal">'
          '<img loading="lazy" src="/img/%s" alt="%s before and after at Serene Med Spa Hudson">'
          '<figcaption><b>%s</b><span>%s</span>'
          '<a href="%s">%s &#8250;</a></figcaption></figure>' % (img, re.sub(r'&[a-z]+;','',title), title, desc, link, cta))
    return "".join(out)

cats_html="\n".join(
  '<div class="price-cat reveal" id="%s"><h3>%s</h3><div class="gal-grid">%s</div></div>'
  % (_slug(t), t, _cards(items)) for t,_,items in CATS)
jump_html='<div class="price-jump reveal">'+"".join('<a href="#%s">%s</a>'%(_slug(t),t) for t,_,_ in CATS)+'</div>'

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"https://hudson.serenemedspas.com/"},
 {"@type":"ListItem","position":2,"name":"Before & After Gallery","item":URL}]}
gallery_schema={"@context":"https://schema.org","@type":"MedicalWebPage","name":"Before & After Gallery — Serene Med Spa Hudson",
 "url":URL,"about":{"@type":"MedicalBusiness","name":"Serene Med Spa"},
 "image":["https://hudson.serenemedspas.com/img/%s"%items[0][0] for _,_,items in CATS]}

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Before &amp; After Gallery &mdash; Serene Med Spa, Hudson OH</title>
<meta name="description" content="Real before and after results from Serene Med Spa in Hudson, Ohio — lip filler, dermal filler, Botox, and Morpheus8, organized by treatment. Physician-led, patient photos shared with consent.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Before &amp; After Gallery &mdash; Serene Med Spa, Hudson OH">
<meta property="og:description" content="Real patient before &amp; after results by treatment &mdash; physician-led care in Hudson, Ohio.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="https://hudson.serenemedspas.com/img/ba-lip-volbella.jpg">
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
{json.dumps(gallery_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Real Results</strong> &mdash; browse our before &amp; after gallery by treatment. <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Before &amp; After</div>
    <div class="svc-hero-grid">
      <div class="svc-hero-txt">
        <div class="eyebrow">Real Patients, Real Results</div>
        <h1>Before &amp; After Gallery</h1>
        <p>Actual results from our Hudson patients, organized by treatment. Every photo is shared with consent &mdash; individual results vary, and your personalized plan is built at your consultation.</p>
        <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Consultation</a>
        <a class="btn btn-outline" href="/pricing/">View Pricing</a>
      </div>
      <div class="svc-hero-media"><img src="/img/ba-lip-volbella.jpg" alt="Before and after lip filler results at Serene Med Spa Hudson" width="1148" height="790"></div>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    {jump_html}
    <div class="price-cats">
{cats_html}
    </div>
    <p class="price-note">Individual results may vary and are not guaranteed. All photos are of our own patients and shared with their written consent. The best way to understand what&rsquo;s possible for you is a personalized consultation.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
os.makedirs("bundle/site/before-after", exist_ok=True)
open("bundle/site/before-after/index.html","w").write(HTML)
print("gallery page written:", len(HTML), "bytes;", len(CATS), "categories")
