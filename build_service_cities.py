# -*- coding: utf-8 -*-
# build_service_cities.py — service + city landing pages ("Dermal Fillers in Akron, OH").
#
# Why these exist: Search Console (28 days to Sept 2026) shows the Hudson site already
# ranking ~30 for high-impression service+city queries with ZERO clicks. The existing
# /med-spa-<city>-oh/ pages target "med spa <city>", which almost nobody searches.
# These target what people actually type.
#
# Reads SC_PAGES from service_cities_data.py and reuses build_cities.py's TEMPLATE so the
# markup and styling stay identical to the city pages. Pure stdlib. Runs after
# build_cities.py in build.sh. Also injects a "nearby" link block into the parent service
# pages so the new pages are internally linked (idempotent).
import json, os, re, sys, html as _h

SITE = "bundle/site"

ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
exec(open("cities_data.py", encoding="utf-8").read(), ns)
exec(open("service_cities_data.py", encoding="utf-8").read(), ns)

NAV, FOOTER, BOOK, LOGO = ns["NAV"], ns["FOOTER"], ns["BOOK"], ns["LOGO"]
STATS_BRANDS, REVIEWS_SECTION = ns["STATS_BRANDS"], ns["REVIEWS_SECTION"]
FINANCE_BAND, STICKY_BAR, SCRIPTS = ns["FINANCE_BAND"], ns["STICKY_BAR"], ns["SCRIPTS"]
CONSULT_SECTION, areas_section = ns["CONSULT_SECTION"], ns["areas_section"]
S, SC_PAGES = ns["CITY_SITE"], ns["SC_PAGES"]

# --- reuse the city template, retargeted from "city" to "service in city" ---
_cb = {}
exec(open("build_cities.py", encoding="utf-8").read().split('if __name__')[0], _cb)
TEMPLATE = _cb["TEMPLATE"]
_steps, _faq_vis, _plain = _cb["_steps"], _cb["_faq_vis"], _cb["_plain"]

def _swap(t, old, new):
    if old not in t:
        raise SystemExit("build_service_cities: template drifted, cannot find:\n  %s" % old[:90])
    return t.replace(old, new)

TEMPLATE = _swap(TEMPLATE,
    '<a href="/#areas">Areas We Serve</a> &nbsp;&#8250;&nbsp; {city}',
    '<a href="{service_url}">{service}</a> &nbsp;&#8250;&nbsp; {city}')
TEMPLATE = _swap(TEMPLATE,
    '<div class="eyebrow">Most Requested</div>\n      <h2>Popular treatments for {city} patients</h2>',
    '<div class="eyebrow">Pricing</div>\n      <h2>{service} pricing for {city} patients</h2>')
TEMPLATE = _swap(TEMPLATE,
    '<p style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="/pricing/">See the full price list</a>',
    '<p style="font-size:17px;font-weight:500;color:#222;max-width:760px;margin:22px auto 0;text-align:center">Prices are published and identical for every patient. A consultation is always free.</p>\n    <p style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="/pricing/">See the full price list</a>')

def price_cards(rows):
    out = []
    for label, price in rows:
        out.append('      <div class="card reveal"><div class="ico">&#10022;</div>'
                   '<h3 style="font-size:20px">%s</h3>'
                   '<p style="font-size:30px;font-weight:800;color:#0f2f26;margin:8px 0 0">%s</p></div>' % (label, price))
    return "\n".join(out)

def related_block(p):
    links = " &nbsp;&middot;&nbsp; ".join(
        '<a href="%s" style="font-weight:700;color:#1f5c4a">%s</a>' % (u, t) for u, t in p["related"])
    return ('<p style="font-size:18px;font-weight:600;color:#1a1a1a;margin-top:26px">'
            'Related: %s</p>' % links)

def build_page(p):
    url = S["base"] + "/" + p["slug"] + "/"
    svc_plain = _plain(p["service"])
    biz = {"@context":"https://schema.org","@type":"MedicalBusiness","name":S["biz_name"],"url":url,
           "telephone":S["tel_e164"],"image":S["base"]+"/img/"+S["hero_img"],
           "address":S["address"],"geo":S["geo"],"priceRange":"$$",
           "areaServed":[{"@type":"City","name":p["city_state"]}] + [{"@type":"City","name":n} for n in p.get("also",[])],
           "hasMap":"https://www.google.com/maps?q="+S["dest_q"],
           "openingHoursSpecification":S["hours_spec"],
           "makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":_plain(l)},"priceCurrency":"USD",
                          "description":_plain(v)} for l, v in p["price_rows"]],
           "parentOrganization":{"@type":"Organization","name":"Serene Med Spa","url":"https://serenemedspas.com/"}}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":S["base"]+"/"},
        {"@type":"ListItem","position":2,"name":svc_plain,"item":S["base"]+p["service_url"]},
        {"@type":"ListItem","position":3,"name":"%s in %s" % (svc_plain, p["city"]),"item":url}]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":_plain(q),"acceptedAnswer":{"@type":"Answer","text":_plain(a)}} for q, a in p["faqs"]]}
    return TEMPLATE.format(
        title=p["title"], desc=p["desc"], url=url, geo=S["geo_meta"], logo=LOGO,
        biz=json.dumps(biz, ensure_ascii=False), crumb=json.dumps(crumb, ensure_ascii=False),
        faq=json.dumps(faq, ensure_ascii=False),
        promo=S.get("promo",""), nav=NAV, city=p["city"], eyebrow=p["eyebrow"],
        service=p["service"], service_url=p["service_url"],
        h1=p["h1"], hero=p["hero"], book=BOOK, tel=S["tel"], phone=S["phone"],
        hero_img=S["hero_img"], loc_short=S["loc_short"], drive=p["drive"], stats=STATS_BRANDS,
        introh2=p["introh2"], introlead=p["introlead"], intro=p["intro"] + related_block(p),
        cards=price_cards(p["price_rows"]), ntreat=S["ntreat"],
        directions=p["directions"], origin=p["origin_q"], dest=S["dest_q"], dest_q=S["dest_q"],
        steps=_steps(p.get("steps") or S["steps"]), faqvis=_faq_vis(p["faqs"]),
        reviews=REVIEWS_SECTION, areas=areas_section(_plain(p["service"]).lower()),
        addr1=S["addr1"], addr2=S["addr2"], hours=S["hours"],
        finance=FINANCE_BAND, consult=CONSULT_SECTION, footer=FOOTER,
        sticky=STICKY_BAR, scripts=SCRIPTS)

MARK = "<!-- service-city-links -->"

def inject_parent_links():
    """Link each parent service page to its service+city pages. Idempotent."""
    by_parent = {}
    for p in SC_PAGES:
        by_parent.setdefault(p["service_url"], []).append(p)
    n = 0
    for parent, pages in by_parent.items():
        f = os.path.join(SITE, parent.strip("/"), "index.html")
        if not os.path.exists(f):
            print("  WARNING: parent page %s not built, skipping link block" % parent); continue
        html = open(f, encoding="utf-8").read()
        html = re.sub(re.escape(MARK) + r".*?" + re.escape(MARK), "", html, flags=re.S)  # drop old block
        links = "".join(
            '<a class="card reveal" href="/%s/" style="display:block;text-decoration:none">'
            '<div class="ico">&#10022;</div><h3>%s in %s</h3>'
            '<p style="font-size:17px;font-weight:500;color:#1a1a1a">%s</p>'
            '<p style="margin-top:10px;color:var(--plum);font-weight:700">Learn more &#8594;</p></a>'
            % (p["slug"], p["service"], p["city"], p["drive"]) for p in pages)
        block = (MARK + '<section class="tint-blush"><div class="wrap">'
                 '<div class="section-head reveal"><div class="eyebrow">Nearby</div>'
                 '<h2>Serving patients from across Northeast Ohio</h2></div>'
                 '<div class="grid">%s</div></div></section>' % links + MARK)
        anchor = '<section class="cta"'
        if anchor not in html:
            print("  WARNING: no CTA anchor in %s, skipping" % parent); continue
        html = html.replace(anchor, block + anchor, 1)
        open(f, "w", encoding="utf-8").write(html)
        n += 1
    return n

if __name__ == "__main__":
    seen = set()
    for p in SC_PAGES:
        if p["slug"] in seen:
            raise SystemExit("build_service_cities: duplicate slug %s" % p["slug"])
        seen.add(p["slug"])
        d = os.path.join(SITE, p["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build_page(p))
    n = inject_parent_links()
    print("build_service_cities: wrote %d service+city pages, linked from %d parent pages" % (len(SC_PAGES), n))
