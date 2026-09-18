# -*- coding: utf-8 -*-
# build_aftercare.py — aftercare hub (/aftercare/) + one page per treatment (/aftercare/<slug>/).
#
# Why this exists: Mangomint post-care Flows can't carry clinical instructions in an SMS, and the
# Canva aftercare cards are flat images (no selectable text, unreadable on a phone, invisible to
# search). So each treatment gets a real text page, and the hub is a gallery of the Canva cards
# linking into them. Every Mangomint message can then carry ONE link: /aftercare/.
#
# Card images are optional. If bundle/img/aftercare-<slug>.jpg exists it is used as the gallery
# thumbnail and shown on the detail page; if not, the tile falls back to a typographic card and
# the page is still complete. Nothing breaks while the images are missing.
#
# Reads AFTERCARE_PAGES from aftercare_pages_data.py. Pure stdlib. Runs after gen_pages.py.
import html as _h
import json, os, re, sys

SITE = "bundle/site"
IMGDIR = "bundle/img"

ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
exec(open("cities_data.py", encoding="utf-8").read(), ns)
exec(open("aftercare_pages_data.py", encoding="utf-8").read(), ns)

NAV, FOOTER, BOOK, LOGO = ns["NAV"], ns["FOOTER"], ns["BOOK"], ns["LOGO"]
SCRIPTS, STICKY_BAR = ns["SCRIPTS"], ns["STICKY_BAR"]
CONSULT_SECTION = ns["CONSULT_SECTION"]
S = ns["CITY_SITE"]
PAGES = ns["AFTERCARE_PAGES"]

LOC = S["loc_short"]
BASE = S["base"]
PHONE, TEL = S["phone"], S["tel"]

# treatment -> menu group (hub page filter)
GROUPS = [
 ("Injectables", ["botox", "dermal-filler", "sculptra", "pdo-threads"]),
 ("Skin &amp; Laser", ["co2-laser", "morpheus8", "opus-plasma", "moxi", "bbl-hero",
                       "pico-resurfacing", "hydrafacial", "chemical-peel", "forma"]),
 ("Laser Removal", ["laser-hair-removal", "tattoo-removal", "laser-toenail-fungus", "waxing"]),
 ("Wellness &amp; Intimate Health", ["hormone-pellets", "alma-duo", "o-shot", "p-shot", "vtone"]),
 ("Hair, Lashes &amp; Brows", ["alma-ted", "brow-tint-lamination", "lash-lift-tint"]),
]

def plain(s):
    return _h.unescape(re.sub(r"<[^>]+>", "", s))

def img_for(slug):
    for ext in (".jpg", ".webp", ".png"):
        if os.path.exists(os.path.join(IMGDIR, "aftercare-" + slug + ext)):
            return "/img/aftercare-" + slug + ext
    return None

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
{geo}
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>
.ac-wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
.ac-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:22px;margin:26px 0 8px}}
.ac-card{{display:block;text-decoration:none;border:1px solid #cfe0d8;border-radius:14px;overflow:hidden;background:#fff;transition:box-shadow .18s,transform .18s}}
.ac-card:hover{{box-shadow:0 10px 26px rgba(15,47,38,.13);transform:translateY(-2px)}}
.ac-card img{{display:block;width:100%;height:auto;background:#f3f7f5}}
.ac-card .ac-fallback{{aspect-ratio:480/672;display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;background:linear-gradient(160deg,#f3f7f5,#e6efe9)}}
.ac-card .ac-fallback span{{font-size:21px;font-weight:800;color:#0f2f26;line-height:1.3}}
.ac-card .ac-label{{padding:13px 15px;font-size:17px;font-weight:700;color:#0f2f26}}
.ac-groupnav{{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:24px 0 6px}}
.ac-groupnav a{{padding:9px 17px;border-radius:999px;border:1px solid #cfe0d8;background:#fff;color:#0f2f26;font-weight:700;font-size:16px;text-decoration:none}}
.ac-groupnav a:hover{{background:#f3f7f5}}
.ac-sec{{margin:40px 0 0}}
.ac-sec h2{{font-size:30px;font-weight:800;color:#0f2f26;margin:0 0 4px}}
.ac-cols{{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));gap:24px;margin:26px 0}}
.ac-col h3{{font-size:19px;font-weight:800;color:#0f2f26;margin:0 0 10px;padding-bottom:8px;border-bottom:2px solid #c8a96a}}
.ac-col ul{{margin:0;padding-left:20px}}
.ac-col li{{font-size:17.5px;font-weight:500;color:#1a1a1a;line-height:1.62;margin-bottom:8px}}
.ac-note{{margin:6px 0 24px;padding:17px 19px;border-radius:12px;background:#f3f7f5;border:1px solid #cfe0d8;font-size:17.5px;font-weight:600;color:#12352b}}
.ac-strip{{margin:26px 0;padding:20px 22px;border-radius:13px;background:#f3f7f5;border:1px solid #cfe0d8}}
.ac-strip.alert{{background:#fdf4f2;border-color:#e8c9c0}}
.ac-strip h3{{margin:0 0 10px;font-size:18px;font-weight:800;color:#0f2f26}}
.ac-strip.alert h3{{color:#8c3a24}}
.ac-tags{{display:flex;flex-wrap:wrap;gap:9px}}
.ac-tags span{{background:#fff;border:1px solid #cfe0d8;border-radius:999px;padding:7px 14px;font-size:16px;font-weight:600;color:#1a1a1a}}
.ac-strip.alert .ac-tags span{{border-color:#e8c9c0}}
.ac-cta{{margin:34px 0 10px;padding:26px 22px;border-radius:14px;background:#f3f7f5;border:1px solid #cfe0d8;text-align:center}}
.ac-hero-img{{max-width:430px;width:100%;border-radius:14px;border:1px solid #cfe0d8;display:block;margin:0 auto 6px}}
@media(max-width:640px){{.ac-grid{{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:15px}}}}
</style>
{schema}
</head>
<body>
{promo}
{nav}
'''

TAIL = '''
{consult}
{footer}
{sticky}
{scripts}
</body>
</html>
'''

def card(p):
    src = img_for(p["slug"])
    # With a card image the name goes in the label row underneath; without one the typographic
    # tile already carries the name, so repeating it below just reads as a duplicate.
    if src:
        inner = ('<img loading="lazy" src="%s" alt="%s aftercare instructions" width="480" height="672">'
                 % (src, plain(p["name"])))
        label = '<div class="ac-label">%s</div>' % p["name"]
    else:
        inner = '<div class="ac-fallback"><span>%s</span></div>' % p["name"]
        label = ""
    return '<a class="ac-card reveal" href="/aftercare/%s/">%s%s</a>' % (p["slug"], inner, label)

def build_hub():
    url = BASE + "/aftercare/"
    title = "Aftercare Instructions | Serene Med Spa %s" % LOC
    desc = ("Post-care instructions for every treatment at Serene Med Spa &mdash; Botox, filler, lasers, "
            "Morpheus8, peels and more. Find your treatment and follow the steps for the best results.")
    by_slug = {p["slug"]: p for p in PAGES}
    seen, sections, nav = set(), [], []
    for gname, slugs in GROUPS:
        items = [by_slug[s] for s in slugs if s in by_slug]
        seen.update(s for s in slugs if s in by_slug)
        if not items: continue
        gid = re.sub(r"[^a-z0-9]+", "-", plain(gname).lower()).strip("-")
        nav.append('<a href="#%s">%s</a>' % (gid, gname))
        sections.append('<section class="ac-sec" id="%s"><div class="ac-wrap">'
                        '<h2>%s</h2><div class="ac-grid">%s</div></div></section>'
                        % (gid, gname, "".join(card(p) for p in items)))
    leftover = [p for p in PAGES if p["slug"] not in seen]
    if leftover:
        sections.append('<section class="ac-sec" id="more"><div class="ac-wrap"><h2>More Treatments</h2>'
                        '<div class="ac-grid">%s</div></div></section>' % "".join(card(p) for p in leftover))
    schema = {"@context": "https://schema.org", "@type": "CollectionPage",
              "name": plain(title), "url": url,
              "hasPart": [{"@type": "MedicalWebPage", "name": plain(p["title"]),
                           "url": BASE + "/aftercare/" + p["slug"] + "/"} for p in PAGES]}
    head = HEAD.format(title=plain(title), desc=plain(desc), url=url, geo=S["geo_meta"], ogimg=LOG_OG,
                       schema='<script type="application/ld+json">%s</script>' % json.dumps(schema, ensure_ascii=False),
                       promo=S.get("promo", ""), nav=NAV)
    body = '''
<section class="svc-hero"><div class="wrap" style="text-align:center">
  <div class="eyebrow" style="justify-content:center">After Your Visit</div>
  <h1>Aftercare Instructions</h1>
  <p style="max-width:720px;margin:0 auto;font-size:19.5px;font-weight:500;color:#1a1a1a">
    Find your treatment below for exactly what to do &mdash; and what to avoid &mdash; while you heal.
    Always follow the specific instructions your provider gave you.</p>
  <div class="ac-groupnav">%s</div>
</div></section>
%s
<section><div class="ac-wrap"><div class="ac-cta">
  <p style="font-size:23px;font-weight:800;color:#0f2f26;margin:0 0 8px">Not sure, or something doesn&rsquo;t look right?</p>
  <p style="font-size:18px;font-weight:500;color:#1a1a1a;margin:0 0 16px">Call us &mdash; we would always rather hear from you.</p>
  <p style="margin:0"><a href="%s" style="display:inline-block;padding:13px 28px;border-radius:999px;background:#1f5c4a;color:#fff;font-weight:700;font-size:18px;text-decoration:none">Call %s</a></p>
</div></div></section>
''' % ("".join(nav), "".join(sections), TEL, PHONE)
    tail = TAIL.format(consult=CONSULT_SECTION, footer=FOOTER, sticky=STICKY_BAR, scripts=SCRIPTS)
    return head + body + tail

def build_page(p):
    slug = p["slug"]
    url = BASE + "/aftercare/" + slug + "/"
    for cand in ("%s | Serene Med Spa %s" % (plain(p["title"]), LOC),
                 "%s | Serene %s" % (plain(p["title"]), LOC),
                 plain(p["title"])):
        title = cand
        if len(title) <= 60:
            break
    desc = plain(p["tagline"])[:150]
    src = img_for(slug)
    cols = "".join('<div class="ac-col reveal"><h3>%s</h3><ul>%s</ul></div>'
                   % (h, "".join("<li>%s</li>" % b for b in items))
                   for h, items in p["blocks"])
    note = '<div class="ac-note">%s</div>' % p["note"] if p.get("note") else ""
    normal = ('<div class="ac-strip reveal"><h3>What is normal</h3><div class="ac-tags">%s</div></div>'
              % "".join("<span>%s</span>" % x for x in p["normal"]))
    urgent = ('<div class="ac-strip alert reveal"><h3>&#9888; Call your provider if you experience</h3>'
              '<div class="ac-tags">%s</div></div>' % "".join("<span>%s</span>" % x for x in p["urgent"]))
    related = "".join('<a href="/%s/" style="font-weight:700;color:#1f5c4a">%s</a> &nbsp;&middot;&nbsp; ' % (s, s.replace("-", " ").title())
                      for s in p["services"] if os.path.exists(os.path.join(SITE, s, "index.html")))
    schema = {"@context": "https://schema.org", "@type": "MedicalWebPage",
              "name": plain(p["title"]), "url": url, "description": desc,
              "about": {"@type": "MedicalProcedure", "name": plain(p["name"])},
              "publisher": {"@type": "MedicalBusiness", "name": S["biz_name"], "telephone": S["tel_e164"]}}
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Aftercare", "item": BASE + "/aftercare/"},
        {"@type": "ListItem", "position": 3, "name": plain(p["name"]), "item": url}]}
    head = HEAD.format(title=title, desc=desc, url=url, geo=S["geo_meta"], ogimg=(BASE + src) if src else LOG_OG,
                       schema='<script type="application/ld+json">%s</script>\n<script type="application/ld+json">%s</script>'
                              % (json.dumps(schema, ensure_ascii=False), json.dumps(crumb, ensure_ascii=False)),
                       promo=S.get("promo", ""), nav=NAV)
    hero_img = ('<img class="ac-hero-img" src="%s" alt="%s aftercare card" width="480" height="672">' % (src, plain(p["name"]))) if src else ""
    body = '''
<section class="svc-hero"><div class="wrap">
  <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/aftercare/">Aftercare</a> &nbsp;&#8250;&nbsp; %s</div>
  <div style="text-align:center">
    <div class="eyebrow" style="justify-content:center">After Your Visit</div>
    <h1>%s</h1>
    <p style="max-width:720px;margin:0 auto;font-size:19.5px;font-weight:500;color:#1a1a1a">%s</p>
  </div>
</div></section>

<section><div class="ac-wrap">
  <div class="ac-cols">%s</div>
  %s
  %s
  %s
  <p style="font-size:17.5px;font-weight:600;color:#12352b;margin:22px 0 0"><strong>Results:</strong> %s</p>
  <p style="font-size:16px;font-weight:500;color:#333;margin:14px 0 0">%s</p>
  <p style="font-size:16px;color:#333;margin:18px 0 0">General guidance from Serene Med Spa &mdash; always follow the specific instructions your provider gives you.
     Questions? Call <a href="%s" style="font-weight:700;color:#1f5c4a">%s</a>.</p>
  <div class="ac-cta">
    <p style="font-size:22px;font-weight:800;color:#0f2f26;margin:0 0 8px">Something doesn&rsquo;t look right?</p>
    <p style="font-size:18px;font-weight:500;color:#1a1a1a;margin:0 0 16px">Call us &mdash; we would always rather hear from you.</p>
    <p style="margin:0 0 12px"><a href="%s" style="display:inline-block;padding:13px 28px;border-radius:999px;background:#1f5c4a;color:#fff;font-weight:700;font-size:18px;text-decoration:none">Call %s</a></p>
    <p style="margin:0"><a href="/aftercare/" style="font-weight:700;color:#1f5c4a">&#8592; All aftercare instructions</a></p>
  </div>
  %s
</div></section>
''' % (p["name"], p["title"], p["tagline"], cols, note, normal, urgent, p["outlook"],
       hero_img, TEL, PHONE, TEL, PHONE,
       ('<p style="font-size:17px;font-weight:600;margin-top:20px">Treatment pages: %s</p>' % related.rstrip(" &nbsp;&middot;&nbsp; ")) if related else "")
    tail = TAIL.format(consult=CONSULT_SECTION, footer=FOOTER, sticky=STICKY_BAR, scripts=SCRIPTS)
    return head + body + tail

LOG_OG = LOGO

if __name__ == "__main__":
    d = os.path.join(SITE, "aftercare")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build_hub())
    n = 0
    seen = set()
    for p in PAGES:
        if p["slug"] in seen:
            raise SystemExit("build_aftercare: duplicate slug %s" % p["slug"])
        seen.add(p["slug"])
        pd = os.path.join(d, p["slug"])
        os.makedirs(pd, exist_ok=True)
        open(os.path.join(pd, "index.html"), "w", encoding="utf-8").write(build_page(p))
        n += 1
    have = sum(1 for p in PAGES if img_for(p["slug"]))
    print("build_aftercare: hub + %d treatment pages (%d/%d card images present)" % (n, have, len(PAGES)))
