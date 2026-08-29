# -*- coding: utf-8 -*-
import os, json
exec(open("/home/claude/hudson-site/common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://hudson.serenemedspas.com"
URL=f"{SITE}/house-calls/"

# Covered ZIP codes within ~20 miles of the Hudson spa (50 W Streetsboro St, 44236).
# Editable seed list — trim/add after review. ZIP -> town label shown to the client.
COVERED={
 "44236":"Hudson","44224":"Stow / Silver Lake","44221":"Cuyahoga Falls","44223":"Cuyahoga Falls",
 "44262":"Munroe Falls","44278":"Tallmadge","44240":"Kent","44242":"Kent","44241":"Streetsboro",
 "44202":"Aurora","44087":"Twinsburg","44056":"Macedonia","44067":"Northfield / Sagamore Hills",
 "44264":"Peninsula","44286":"Richfield","44333":"Fairlawn / Bath","44313":"Akron (Northwest)",
 "44310":"Akron (North)","44303":"Akron (Northwest)","44305":"Akron (East)","44139":"Solon",
 "44146":"Bedford","44147":"Broadview Heights","44141":"Brecksville","44022":"Chagrin Falls",
 "44023":"Chagrin Falls / Bainbridge","44122":"Beachwood","44124":"Pepper Pike","44266":"Ravenna",
 "44260":"Mogadore",
}

crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"House Calls","item":URL}]}
svc_schema={"@context":"https://schema.org","@type":"Service","name":"Serene at Home — Mobile Aesthetics & IV",
  "serviceType":"Mobile medical spa house calls","url":URL,
  "areaServed":{"@type":"GeoCircle","geoMidpoint":{"@type":"GeoCoordinates","latitude":41.2401,"longitude":-81.4409},"geoRadius":"32187"},
  "provider":{"@type":"MedicalBusiness","name":"Serene Med Spa — Hudson","telephone":"+1-330-460-5915",
    "address":{"@type":"PostalAddress","streetAddress":"50 W Streetsboro St, Suite 2","addressLocality":"Hudson","addressRegion":"OH","postalCode":"44236","addressCountry":"US"}}}

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
<title>Serene at Home &mdash; House Calls &amp; Botox Parties | Hudson, OH</title>
<meta name="description" content="Serene comes to you. Botox parties and mobile IV therapy at home, physician-led, transportation included within 20 miles of Hudson, OH. Prepaid. Check your ZIP.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Serene at Home &mdash; House Calls &amp; Botox Parties">
<meta property="og:description" content="Botox parties &amp; mobile IV therapy at home, physician-led, within 20 miles of Hudson, OH.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/img/inject-hero.jpg">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(svc_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Serene at Home</strong> &mdash; Botox parties &amp; mobile IV, we come to you. Within 20 miles &middot; prepaid. <a href="{BOOK}" target="_blank" rel="noopener">Book now</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; House Calls</div>
    <div class="svc-hero-txt" style="max-width:760px">
      <div class="eyebrow">Serene at Home</div>
      <h1>House Calls &amp; Botox Parties</h1>
      <p>Gather your group or treat yourself &mdash; our physician-led team brings Serene to your door. <strong>Transportation included within 20 miles</strong> of our Hudson spa. Prepaid.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="hc-offers">
      <div class="hc-offer">
        <h3>Botox Parties</h3>
        <p>Host your friends and <strong>prepay 100 units of Botox</strong> &mdash; we handle the rest. A physician consults each guest before treatment. From <strong>$1,100</strong> (100 units).</p>
      </div>
      <div class="hc-offer">
        <h3>Mobile IV Therapy</h3>
        <p>Our wellness &amp; recovery drips, delivered in the comfort of your home. <strong>$299 per treatment</strong>, physician-supervised.</p>
      </div>
      <div class="hc-offer">
        <h3>Included &amp; Simple</h3>
        <p><strong>Transportation is included</strong> within 20 miles of Hudson, and all visits are <strong>prepaid</strong> to reserve your date. Must be 18+.</p>
      </div>
    </div>
  </div>
</section>

<section id="hc-check">
  <div class="wrap">
    <div class="hc-checker">
      <div class="eyebrow">Do We Come To You?</div>
      <h2>Check your ZIP code</h2>
      <p>Enter your ZIP to see if you&rsquo;re inside our 20-mile house-call zone.</p>
      <form class="hc-form" onsubmit="return false;">
        <input id="hc-zip" type="text" inputmode="numeric" maxlength="5" pattern="[0-9]*" placeholder="e.g. 44236" aria-label="ZIP code">
        <button class="btn" id="hc-go" type="submit">Check</button>
      </form>
      <div class="hc-result" id="hc-result" hidden></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="hc-fine">Serene at Home is physician-led. Every guest receives a consultation before any treatment, and services are provided at our medical team&rsquo;s discretion for appropriate candidates (18+). Questions? <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> or call <a href="tel:+13304605915">(330) 460-5915</a>.</p>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}

<script>
(function(){{
  var COVERED={json.dumps(COVERED)};
  var f=document.getElementById('hc-go'), zip=document.getElementById('hc-zip'), res=document.getElementById('hc-result');
  function check(){{
    var z=(zip.value||'').replace(/[^0-9]/g,'').slice(0,5);
    if(z.length!==5){{ res.hidden=false; res.className='hc-result hc-warn'; res.innerHTML='Please enter a 5-digit ZIP code.'; return; }}
    if(COVERED[z]){{
      res.hidden=false; res.className='hc-result hc-yes';
      res.innerHTML='&#10003; Great news &mdash; we come to <strong>'+COVERED[z]+'</strong>! Transportation is included. <a href="{BOOK}" target="_blank" rel="noopener">Reserve your visit &rsaquo;</a>';
    }} else {{
      res.hidden=false; res.className='hc-result hc-no';
      res.innerHTML='You&rsquo;re just outside our 20-mile zone &mdash; but call us, we may still be able to come to you. <a href="tel:+13304605915">(330) 460-5915</a>';
    }}
  }}
  f.addEventListener('click',check);
  zip.addEventListener('keydown',function(e){{ if(e.key==='Enter'){{ e.preventDefault(); check(); }} }});
}})();
</script>
</body>
</html>
'''

os.makedirs("/home/claude/hudson-site/bundle/site/house-calls",exist_ok=True)
open("/home/claude/hudson-site/bundle/site/house-calls/index.html","w").write(HTML)
print("house-calls written:", len(HTML), "bytes;", len(COVERED), "covered ZIPs")
