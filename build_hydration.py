# -*- coding: utf-8 -*-
import os, json
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://hudson.serenemedspas.com"
URL=f"{SITE}/hydration-bar/"

# key, name, goal (button label), blurb (supportive, compliant)
DRIPS=[
 ("immune-armor","Serene Immune Armor","Immune &amp; seasonal support",
   "Hydration plus key vitamins and antioxidants, formulated to support your immune system and overall wellness."),
 ("myers","Myer&rsquo;s Cocktail","An all-around wellness classic",
   "The time-tested blend of B vitamins, vitamin C, magnesium, and calcium &mdash; popular for general wellness and an energy lift."),
 ("beauty-glow","Serene Beauty Glow","Glow &amp; skin support",
   "Glutathione, the body&rsquo;s &ldquo;master antioxidant,&rdquo; to support cellular health and a healthy, radiant glow."),
 ("recovery","Serene Recovery &amp; Performance Pro","Bounce back &amp; recover",
   "For post-workout, post-travel, or a tough week &mdash; when you want to rebound and feel like yourself again."),
 ("quench","Serene Quench+","Deep hydration",
   "Replenish and rehydrate when you&rsquo;re running on empty and just feel depleted."),
 ("reboot","Serene Reboot Relief","Reset when you&rsquo;re run-down",
   "A reset for those run-down, depleted days when you need to feel steady again."),
 ("brain-boost","Serene Brain Boost","Focus &amp; mental clarity",
   "Support mental clarity and focus when you need to be at your sharpest."),
 ("pms-ease","Serene PMS Ease","Cycle comfort",
   "Thoughtful support for cycle-related discomfort, tailored to how you&rsquo;re feeling."),
 ("get-up-go","Serene Get-Up-&amp;-Go","An energy pick-me-up",
   "A quick boost to get moving when your energy is running low."),
]

# JS data (decode a few entities for clean display via textContent)
def dec(s): return s.replace("&amp;","&").replace("&rsquo;","’").replace("&mdash;","—").replace("&ldquo;","“").replace("&rdquo;","”")
JS_DRIPS=[{"key":k,"name":dec(n),"goal":dec(g),"blurb":dec(b)} for (k,n,g,b) in DRIPS]

# goal buttons
buttons="\n".join(
  f'      <button type="button" class="hb-opt" data-key="{k}">{g}</button>'
  for (k,n,g,b) in DRIPS)

# reference menu cards
cards="\n".join(
  f'''      <div class="hb-card" id="drip-{k}">
        <h3>{n}</h3>
        <p>{b}</p>
        <span class="hb-price">$149</span>
      </div>''' for (k,n,g,b) in DRIPS)

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"IV Therapy","item":SITE+"/iv-therapy/"},
  {"@type":"ListItem","position":3,"name":"Serene Hydration Bar","item":URL}]}

catalog={"@context":"https://schema.org","@type":"OfferCatalog","name":"Serene Hydration Bar — IV Infusion Menu","url":URL,
  "itemListElement":[{"@type":"Offer","price":"149","priceCurrency":"USD",
    "itemOffered":{"@type":"Service","name":dec(n),"serviceType":"IV Nutrient Therapy",
      "provider":{"@type":"MedicalBusiness","name":"Serene Med Spa — Hudson"}}} for (k,n,g,b) in DRIPS]}

page_schema={"@context":"https://schema.org","@type":"MedicalWebPage","name":"The Serene Hydration Bar","url":URL,
  "description":"An interactive tool to match a physician-supervised IV wellness drip to your goals at Serene Med Spa in Hudson, OH.",
  "about":{"@type":"MedicalTherapy","name":"IV Nutrient Therapy"},
  "lastReviewed":"2026-08-24","audience":{"@type":"Patient"}}

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
<title>The Serene Hydration Bar &mdash; Find Your IV Drip | Hudson, OH</title>
<meta name="description" content="Not sure which IV drip is right for you? The Serene Hydration Bar matches a physician-supervised wellness drip to your goals &mdash; every infusion $149, Hudson, OH.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio"><meta name="geo.position" content="41.2401;-81.4409"><meta name="ICBM" content="41.2401, -81.4409">
<meta property="og:type" content="website">
<meta property="og:title" content="The Serene Hydration Bar &mdash; Find Your IV Drip">
<meta property="og:description" content="Match a physician-supervised wellness drip to your goals. Every infusion $149 in Hudson, Ohio.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/img/iv-therapy-blog.jpg">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(page_schema)}
</script>
<script type="application/ld+json">
{json.dumps(catalog)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>The Serene Hydration Bar</strong> &mdash; find the drip that fits your goals. Every infusion $149. <a href="{BOOK}" target="_blank" rel="noopener">Book now</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/iv-therapy/">IV Therapy</a> &nbsp;&#8250;&nbsp; Hydration Bar</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <div class="eyebrow">Find Your Drip</div>
      <h1>The Serene Hydration Bar</h1>
      <p>Not sure which IV infusion is the best match for you? Tell us how you want to feel, and we&rsquo;ll point you to a drip that fits your goals. Every infusion is <strong>$149</strong> and personalized by our physician-supervised team.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="hb-tool">
      <p class="hb-q">How do you want to feel today?</p>
      <div class="hb-opts">
{buttons}
      </div>
      <div class="hb-result" id="hb-result" hidden>
        <div class="hb-result-inner">
          <span class="hb-tag">Your match</span>
          <h2 id="hb-name"></h2>
          <p id="hb-blurb"></p>
          <span class="hb-price hb-price-lg">$149</span>
          <div class="hb-actions">
            <a class="btn" id="hb-book" href="{BOOK}" target="_blank" rel="noopener">Book This Drip</a>
            <a class="btn btn-outline" href="#hb-menu">See Full Menu</a>
          </div>
          <p class="hb-note">Not sure? Our team will help you choose at your visit &mdash; <a href="{BOOK}" target="_blank" rel="noopener">book a quick consult</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="hb-menu">
  <div class="wrap">
    <div class="hb-menu-head">
      <div class="eyebrow">Every Drip $149</div>
      <h2>The Full Menu</h2>
      <p>All of our infusions are physician-supervised and delivered in a calm, comfortable setting in Hudson.</p>
    </div>
    <div class="hb-grid">
{cards}
    </div>
    <p class="hb-links">See every treatment on our <a href="/pricing/">full pricing menu</a>, learn more <a href="/iv-therapy/">about IV therapy</a>, or read <a href="/blog/iv-therapy-immune-support-fall/">how IV therapy supports your wellness</a>.</p>
    <p class="hb-disclaimer">IV therapy is intended to support general wellness and hydration and is not intended to diagnose, treat, cure, or prevent any disease. Our medical team will review your suitability at your visit.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}

<script>
(function(){{
  var DRIPS={json.dumps(JS_DRIPS)};
  var byKey={{}}; DRIPS.forEach(function(d){{byKey[d.key]=d;}});
  var res=document.getElementById('hb-result');
  var nm=document.getElementById('hb-name'), bl=document.getElementById('hb-blurb');
  var opts=document.querySelectorAll('.hb-opt');
  opts.forEach(function(btn){{
    btn.addEventListener('click',function(){{
      opts.forEach(function(b){{b.classList.remove('is-active');}});
      btn.classList.add('is-active');
      var d=byKey[btn.getAttribute('data-key')]; if(!d) return;
      nm.textContent=d.name; bl.textContent=d.blurb;
      res.hidden=false;
      res.scrollIntoView({{behavior:'smooth',block:'center'}});
    }});
  }});
}})();
</script>
</body>
</html>
'''

os.makedirs("bundle/site/hydration-bar",exist_ok=True)
open("bundle/site/hydration-bar/index.html","w").write(HTML)
print("hydration-bar written:", len(HTML), "bytes;", len(DRIPS), "drips")
