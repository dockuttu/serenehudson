# -*- coding: utf-8 -*-
# build_cities.py — nearby-city landing pages ("Med spa near Akron, OH" etc.).
# Reads CITY_SITE + CITIES from cities_data.py and the shared components from
# common.py. Pure stdlib. Runs after gen_pages.py in build.sh.
import json, os, html as _h
exec(open("common.py").read())          # NAV, FOOTER, BOOK, STATS_BRANDS, REVIEWS_SECTION, FINANCE_BAND, STICKY_BAR, SCRIPTS, CONSULT_SECTION, areas_section, LOGO
exec(open("cities_data.py").read())     # CITY_SITE, CITIES, TREATMENTS
SITE = "bundle/site"

def _cards(items):
    out=[]
    for slug,name,price,blurb in items:
        out.append('      <a class="card reveal" href="/%s/" style="display:block;text-decoration:none"><div class="ico">&#10022;</div><h3>%s</h3><p>%s</p><p style="margin-top:12px;color:var(--plum);font-weight:600">%s &nbsp;<span style="color:var(--rose-deep);font-weight:500">Learn more &#8594;</span></p></a>' % (slug,name,blurb,price))
    return "\n".join(out)

def _steps(steps):
    return "\n".join('      <div class="step reveal"><div class="num"></div><div><h3>%s</h3><p>%s</p></div></div>' % (h,p) for h,p in steps)

def _faq_vis(faqs):
    return "\n".join('      <div class="faq reveal"><button>%s<span class="plus">+</span></button><div class="ans"><p>%s</p></div></div>' % (q,a) for q,a in faqs)

def _plain(s):  # schema text: strip entities/tags
    import re; return _h.unescape(re.sub(r"<[^>]+>","",s))

def _faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":_plain(q),"acceptedAnswer":{"@type":"Answer","text":_plain(a)}} for q,a in faqs]}

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
{geo}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{logo}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{biz}
</script>
<script type="application/ld+json">
{crumb}
</script>
<script type="application/ld+json">
{faq}
</script>
</head>
<body>

{promo}

{nav}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/#areas">Areas We Serve</a> &nbsp;&#8250;&nbsp; {city}</div>
    <div class="svc-hero-grid">
      <div class="svc-hero-txt">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{h1}</h1>
        <p>{hero}</p>
        <a class="btn" href="{book}" target="_blank" rel="noopener">Book a Free Consultation</a>
        <a class="btn btn-outline" href="{tel}">Call {phone}</a>
      </div>
      <div class="svc-hero-media"><img src="/img/{hero_img}" alt="Serene Med Spa {loc_short} lobby &mdash; serving {city}" width="1800" height="1200"></div>
    </div>
  </div>
</section>

<div class="trust">
  <div class="wrap">
    <div class="item"><b>&#10022;</b> {drive} from {city}</div>
    <div class="item"><b>&#10022;</b> Board-certified physicians</div>
    <div class="item"><b>&#10022;</b> Published pricing, no surprises</div>
    <div class="item"><b>&#10022;</b> Free consultations</div>
  </div>
</div>

{stats}

<section>
  <div class="wrap prose reveal">
    <h2>{introh2}</h2>
    <p class="lead">{introlead}</p>
    {intro}
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Most Requested</div>
      <h2>Popular treatments for {city} patients</h2>
    </div>
    <div class="grid">
{cards}
    </div>
    <p style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="/pricing/">See the full price list</a> &nbsp; <a class="btn" href="/#services">All {ntreat}+ treatments</a></p>
  </div>
</section>

<section>
  <div class="wrap loc-grid">
    <div class="loc-info reveal">
      <div class="eyebrow">Getting Here</div>
      <h2 style="font-size:clamp(2rem,4vw,2.8rem);margin-bottom:18px">From {city} to Serene Med Spa</h2>
      {directions}
      <div style="margin-top:22px"><a class="btn" href="https://www.google.com/maps/dir/?api=1&origin={origin}&destination={dest}" target="_blank" rel="noopener">Open directions in Google Maps</a></div>
    </div>
    <iframe class="map reveal" loading="lazy" title="Map from {city} to Serene Med Spa {loc_short}" src="https://www.google.com/maps?q={dest_q}&output=embed"></iframe>
  </div>
</section>

<section class="tint-mint">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Your First Visit</div><h2>What to expect when you drive in from {city}</h2></div>
    <div class="steps">
{steps}
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Good to Know</div><h2>{city} patients ask us</h2></div>
    <div class="faq-list">
{faqvis}
    </div>
  </div>
</section>

{reviews}

{areas}

<section class="location" id="location">
  <div class="wrap loc-grid">
    <div class="loc-info reveal">
      <div class="eyebrow" style="-webkit-text-fill-color:initial;color:var(--gold);background:none">Visit Us</div>
      <h2 style="font-size:clamp(2.1rem,4.4vw,3rem);margin-bottom:20px">Serene Med Spa &mdash; {loc_short}</h2>
      <div class="row"><strong>Address</strong><span>{addr1}<br>{addr2}</span></div>
      <div class="row"><strong>Call</strong><span><a href="{tel}">{phone}</a></span></div>
      <div class="row"><strong>Hours</strong><span>{hours}</span></div>
      <div style="margin-top:28px"><a class="btn" href="{book}" target="_blank" rel="noopener">Book Online</a></div>
    </div>
    <iframe class="map reveal" loading="lazy" title="Map to Serene Med Spa {loc_short}" src="https://www.google.com/maps?q={dest_q}&output=embed"></iframe>
  </div>
</section>

{finance}

<section class="cta">
  <div class="wrap reveal">
    <h2>Worth the drive from {city}</h2>
    <p>Physician injectors, real prices, and a team that remembers your name. Book a free consultation and see why {city} patients make Serene their med spa.</p>
    <a class="btn" href="{book}" target="_blank" rel="noopener">Book Your Visit</a>
  </div>
</section>

{consult}

{footer}

{sticky}

{scripts}
</body>
</html>
'''

def build_city(c):
    S = CITY_SITE
    url = S["base"] + "/" + c["slug"] + "/"
    title = c.get("title") or "Med Spa Near %s | Serene Med Spa %s" % (c["city"], S["loc_short"])
    desc = c["desc"]
    biz = {"@context":"https://schema.org","@type":"MedicalBusiness","name":S["biz_name"],"url":url,
           "telephone":S["tel_e164"],"image":S["base"]+"/img/"+S["hero_img"],
           "address":S["address"],"geo":S["geo"],"priceRange":"$$",
           "areaServed":[{"@type":"City","name":c["city_state"]}] + [{"@type":"City","name":n} for n in c.get("also",[])],
           "hasMap":"https://www.google.com/maps?q="+S["dest_q"],
           "openingHoursSpecification":S["hours_spec"],
           "parentOrganization":{"@type":"Organization","name":"Serene Med Spa","url":"https://serenemedspas.com/"}}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":S["base"]+"/"},
        {"@type":"ListItem","position":2,"name":"Areas We Serve","item":S["base"]+"/#areas"},
        {"@type":"ListItem","position":3,"name":c["city"],"item":url}]}
    cards = _cards([t for t in TREATMENTS if t[0] in c["treatments"]] if c.get("treatments") else TREATMENTS[:6])
    return TEMPLATE.format(
        title=title, desc=desc, url=url, geo=S["geo_meta"], logo=LOGO, biz=json.dumps(biz,ensure_ascii=False),
        crumb=json.dumps(crumb,ensure_ascii=False), faq=json.dumps(_faq_schema(c["faqs"]),ensure_ascii=False),
        promo=S.get("promo",""), nav=NAV, city=c["city"], eyebrow=c.get("eyebrow","Serving %s" % c["city_state"]),
        h1=c["h1"], hero=c["hero"], book=BOOK, tel=S["tel"], phone=S["phone"], hero_img=S["hero_img"], loc_short=S["loc_short"],
        drive=c["drive"], stats=STATS_BRANDS, introh2=c["introh2"], introlead=c["introlead"], intro=c["intro"],
        cards=cards, ntreat=S["ntreat"], directions=c["directions"], origin=c["origin_q"], dest=S["dest_q"], dest_q=S["dest_q"],
        steps=_steps(c.get("steps") or S["steps"]), faqvis=_faq_vis(c["faqs"]), reviews=REVIEWS_SECTION,
        areas=areas_section(c.get("area_kw","physician-led aesthetic care")), addr1=S["addr1"], addr2=S["addr2"], hours=S["hours"],
        finance=FINANCE_BAND, consult=CONSULT_SECTION, footer=FOOTER, sticky=STICKY_BAR, scripts=SCRIPTS)

if __name__ == "__main__":
    n=0
    for c in CITIES:
        d=os.path.join(SITE,c["slug"]); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(build_city(c)); n+=1
    print("build_cities: wrote %d city pages" % n)
