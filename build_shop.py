# -*- coding: utf-8 -*-
import os, json
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://hudson.serenemedspas.com"
URL=f"{SITE}/shop/"

# Placeholder link target until Mangomint package links are provided.
# Swap each item's "link" for its Mangomint package purchase URL at launch.
PH=BOOK

# name, slug, image, regular, prepaid(-20%), redeems-for, purchase link
ITEMS=[
 ("HydraFacial","hydrafacial","/img/hydrafacial.jpg",150,120,"1 HydraFacial",PH),
 ("Botox &mdash; 20 Units","botox","/img/botox-inject.jpg",220,198,"20 units of Botox",PH),
 ("Morpheus8 RF","morpheus8","/img/morpheus8.jpg",800,640,"1 Morpheus8 (per treatment)",PH),
 ("Laser Facial","laser-facial","/img/laser.jpg",400,320,"1 Laser Facial",PH),
 ("DiamondGlow","diamondglow","/img/facial-2.jpg",150,120,"1 DiamondGlow facial",PH),
 ("Microneedling with PRP","microneedling-prp","/img/facial-3.jpg",500,400,"1 Microneedling + PRP",PH),
 ("VI Chemical Peel","vi-peel","/img/facial-4.jpg",250,200,"1 VI Peel",PH),
 ("Serene IV Infusion","iv-infusion","/img/iv-therapy-blog.jpg",149,119,"1 IV drip of your choice",PH),
]

def card(name,slug,img,reg,pre,red,link):
    pct=round((1-pre/reg)*100)
    return f'''      <div class="shop-card reveal">
        <div class="shop-thumb"><img loading="lazy" src="{img}" alt="{name} at Serene Med Spa, Hudson OH"><span class="shop-badge">{pct}% OFF</span></div>
        <div class="shop-txt">
          <h3>{name}</h3>
          <div class="shop-price"><span class="shop-reg">${reg}</span><span class="shop-now">${pre}</span></div>
          <p class="shop-red">Redeems for {red}</p>
          <a class="btn shop-buy" href="{link}" target="_blank" rel="noopener">Book Now</a>
        </div>
      </div>'''

cards="\n".join(card(*it) for it in ITEMS)

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"Shop","item":URL}]}
offer_catalog={"@context":"https://schema.org","@type":"OfferCatalog","name":"Serene Med Spa — Prepay & Save Shop","url":URL,
  "itemListElement":[{"@type":"Offer","price":str(pre),"priceCurrency":"USD",
    "itemOffered":{"@type":"Service","name":name,"provider":{"@type":"MedicalBusiness","name":"Serene Med Spa — Hudson"}}}
    for (name,slug,img,reg,pre,red,link) in ITEMS]}

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
<title>Shop &mdash; Prepay &amp; Save up to 20% | Serene Med Spa, Hudson OH</title>
<meta name="description" content="Prepay select treatments online and save up to 20% at Serene Med Spa in Hudson, OH. Buy in advance, redeem at your appointment &mdash; HydraFacial, Morpheus8, laser &amp; more.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Shop &mdash; Prepay &amp; Save up to 20% | Serene Med Spa">
<meta property="og:description" content="Prepay select treatments online and save up to 20%. Redeem at your visit in Hudson, OH.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/img/hydrafacial.jpg">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(offer_catalog)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Prepay &amp; Save up to 20%</strong> &mdash; buy your treatment in advance, redeem at your visit. <a href="{BOOK}" target="_blank" rel="noopener">Book now</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Shop</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <div class="eyebrow">The Serene Shop</div>
      <h1>Prepay &amp; Save up to 20%</h1>
      <p>Buy select treatments in advance and save &mdash; then redeem your prepaid visit whenever you&rsquo;re ready. Physician-led care in Hudson, Ohio.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="shop-steps">
      <div><span>1</span><p>Choose a treatment and <strong>prepay online</strong> at up to 20% off.</p></div>
      <div><span>2</span><p>We hold your <strong>prepaid credit</strong> on your account.</p></div>
      <div><span>3</span><p><strong>Redeem it at your appointment</strong> &mdash; book anytime.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="shop-notice">&#128274; <strong>Lock in your best prepaid rate today.</strong> Online prepay checkout is launching shortly &mdash; for now, call <a href="tel:+13304605915">(330) 460-5915</a> or ask at your visit to prepay and save, or book any treatment below.</p>
    <div class="shop-grid">
{cards}
    </div>
    <p class="shop-fine">Prepaid treatments are redeemed at your appointment and are valid for 12 months from purchase. Have questions? <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> or call <a href="tel:+13304605915">(330) 460-5915</a>.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''

os.makedirs("bundle/site/shop",exist_ok=True)
open("bundle/site/shop/index.html","w").write(HTML)
print("shop written:", len(HTML), "bytes;", len(ITEMS), "items")
