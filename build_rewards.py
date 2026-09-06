# -*- coding: utf-8 -*-
# build_rewards.py — /xperience-rewards/ : Merz Aesthetics Xperience+ loyalty page (Hudson)
import os, json
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION, STICKY_BAR
SITE="https://hudson.serenemedspas.com"
URL=f"{SITE}/xperience-rewards/"
XP="https://www.xperiencemerz.com/"

FAQ=[
 ("Is Xperience+ free to join?","Yes. Xperience+ is Merz Aesthetics&rsquo; free patient loyalty program. Join online in about two minutes and you start earning at your very next eligible treatment at Serene."),
 ("Which treatments earn points?","Xeomin (100 points per treatment), Radiesse and Belotero Balance (200 points per syringe), Ultherapy PRIME (1 point per treatment line), and Neocutis skincare (40&ndash;290 points per product). Points post to your Xperience+ account after your visit."),
 ("What are points worth?","Every 100 points equals $10 in savings on future Merz Aesthetics treatments or Neocutis products. Xperience+ also gives an instant $50 discount on applicable Xeomin treatments."),
 ("How do I redeem at Serene?","Tell us at check-in that you&rsquo;re an Xperience+ member. We&rsquo;ll log your treatment so your points post, and apply any rewards you&rsquo;ve chosen to redeem at checkout."),
 ("Can I use points at both Serene locations?","Yes. Xperience+ is tied to you, not the clinic, so points earned in Hudson can be used at our Barboursville, WV location and vice versa."),
 ("Do points expire?","Point expiration and limits (for example, up to 20 filler syringes per year and 1,500 Ultherapy lines per treatment) are set by Merz Aesthetics. The current terms are always at xperiencemerz.com."),
]
faq_html='<div class="faq-list">'+"".join(f'<div class="faq reveal"><button>{q}<span class="plus">+</span></button><div class="ans"><p>{a}</p></div></div>' for q,a in FAQ)+'</div>'
faq_schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q.replace("&rsquo;","'").replace("&ndash;","–"),"acceptedAnswer":{"@type":"Answer","text":a.replace("&rsquo;","'").replace("&ndash;","–")}} for q,a in FAQ]}
crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"Xperience+ Rewards","item":URL}]}

HEAD_FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Xperience+ Rewards | Merz Points at Serene Med Spa Hudson</title>
<meta name="description" content="Earn Xperience+ points on Xeomin, Radiesse, Belotero &amp; Ultherapy PRIME at Serene Med Spa in Hudson, OH — a Merz Aesthetics Bronze Preferred Partner. Every 100 points = $10 off.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Xperience+ Rewards at Serene Med Spa Hudson">
<meta property="og:description" content="Earn points on Xeomin, Radiesse, Belotero &amp; Ultherapy PRIME. Every 100 points = $10 off.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/img/badges/xperience-plus.png">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(faq_schema)}
</script>
</head>
<body>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Xperience+ Rewards</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <img src="/img/badges/xperience-plus.png" alt="Xperience+ Rewards Program by Merz Aesthetics" class="xp-hero-badge">
      <div class="eyebrow">Merz Aesthetics Loyalty &middot; Hudson, OH</div>
      <h1>Xperience+ Rewards</h1>
      <p>Get rewarded for the treatments you already love. Earn points on <strong>Xeomin, Radiesse, Belotero and Ultherapy PRIME</strong> at Serene &mdash; and turn them into savings on your next visit.</p>
      <a class="btn" href="{XP}" target="_blank" rel="noopener">Join Xperience+ (free)</a>
      <a class="btn btn-outline" href="{BOOK}" target="_blank" rel="noopener">Book a Treatment</a>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Earn</div><h2>Points on every Merz treatment</h2><p>Every 100 points is $10 toward future Merz Aesthetics treatments or Neocutis skincare.</p></div>
    <div class="xp-earn">
      <div class="hc-offer reveal"><b>100</b><h3>Xeomin</h3><p>points per treatment, plus an instant <strong>$50</strong> discount on applicable Xeomin treatments.</p></div>
      <div class="hc-offer reveal"><b>200</b><h3>Radiesse</h3><p>points per syringe of Radiesse or Radiesse(+).</p></div>
      <div class="hc-offer reveal"><b>200</b><h3>Belotero</h3><p>points per syringe of Belotero Balance or Belotero Balance(+).</p></div>
      <div class="hc-offer reveal"><b>1 / line</b><h3>Ultherapy PRIME</h3><p>one point per treatment line &mdash; a full face &amp; neck can be well over 1,000 lines.</p></div>
    </div>
    <p class="xp-fine">Bonus points: 10 for joining, 50 on your birthday, and 50 for staying loyal to the same provider. Neocutis skincare earns 40&ndash;290 points per product.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">How it works</div><h2>Three steps to savings</h2></div>
    <div class="hc-offers">
      <div class="hc-offer reveal"><h3>1. Join free</h3><p>Sign up at <a href="{XP}" target="_blank" rel="noopener">xperiencemerz.com</a> before your visit. It takes about two minutes and you get 10 points just for enrolling.</p></div>
      <div class="hc-offer reveal"><h3>2. Tell us at check-in</h3><p>Let our front desk know you&rsquo;re an Xperience+ member. We log every eligible Xeomin, Radiesse, Belotero and Ultherapy PRIME treatment so your points post.</p></div>
      <div class="hc-offer reveal"><h3>3. Redeem at checkout</h3><p>Choose a reward in your Xperience+ account and apply it to your next Merz treatment or Neocutis product at Serene.</p></div>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="ult-cred reveal">
      <img src="/img/badges/merz-bronze-preferred.png" alt="Merz Aesthetics Bronze Preferred Partner" class="badge-round">
      <img src="/img/badges/ultherapy-prime.png" alt="Ultherapy PRIME" class="badge-wide">
      <p>Serene Med Spa is a <strong>Merz Aesthetics Bronze Preferred Partner</strong> and an authorized <strong><a href="/ultherapy/">Ultherapy PRIME</a></strong> provider in Hudson, Ohio.</p>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Questions</div><h2>Xperience+ FAQ</h2></div>
    {faq_html}
    <p class="xp-fine">Xperience+&trade; is a loyalty program operated by Merz Aesthetics, not by Serene Med Spa. Point values, eligible products, limits and expiration are set by Merz and may change; the current program terms are at <a href="{XP}" target="_blank" rel="noopener">xperiencemerz.com</a>. Xeomin&reg;, Radiesse&reg;, Belotero&reg;, Ultherapy&reg; and Neocutis&reg; are trademarks of Merz Aesthetics.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}
{STICKY_BAR}
{SCRIPTS}
</body>
</html>'''

os.makedirs("bundle/site/xperience-rewards",exist_ok=True)
open("bundle/site/xperience-rewards/index.html","w",encoding="utf-8").write(HTML)
print("wrote bundle/site/xperience-rewards/index.html")
