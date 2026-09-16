# -*- coding: utf-8 -*-
# tattoo_pricing.py — idempotent post-build pass (identical in both repos):
#   adds the "Pricing & Size Guide" section, free-consult note and buy-5-get-6th-free offer
#   to /laser-tattoo-removal/, plus Service/OfferCatalog schema.
import os, sys, json, re
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "laser-tattoo-removal", "index.html")
if not os.path.exists(f):
    print("tattoo_pricing: page missing"); sys.exit(0)
s = open(f, encoding="utf-8").read()
o = s
m = re.search(r'<link rel="canonical" href="(https://([a-z]+)\.serenemedspas\.com)/', s)
ORIGIN, SUB = (m.group(1), m.group(2)) if m else ("https://hudson.serenemedspas.com", "hudson")
CITY = "Barboursville, WV" if SUB == "barboursville" else "Hudson, OH"
BOOK = "https://booking.mangomint.com/serenemedspa?serviceId=321"

# Everyday objects drawn to the SAME scale (1 in = S px) so sizes compare at a glance.
S = 26
def _quarter():
    d = round(0.955 * S)
    return (f'<svg width="{d+4}" height="{d+4}" viewBox="0 0 {d+4} {d+4}" aria-hidden="true">'
            f'<circle cx="{(d+4)/2}" cy="{(d+4)/2}" r="{d/2}" fill="#c9ccd3" stroke="#6b7280" stroke-width="1.5"/>'
            f'<circle cx="{(d+4)/2}" cy="{(d+4)/2}" r="{d/2-3}" fill="none" stroke="#9aa0aa" stroke-width="1"/>'
            f'<text x="{(d+4)/2}" y="{(d+4)/2+3}" font-size="8" text-anchor="middle" fill="#4b5563" font-weight="700">25&#162;</text></svg>')
def _photo():
    w = 2 * S
    return (f'<svg width="{w+4}" height="{w+4}" viewBox="0 0 {w+4} {w+4}" aria-hidden="true">'
            f'<rect x="2" y="2" width="{w}" height="{w}" rx="3" fill="#e8eef8" stroke="#1f2a5c" stroke-width="1.5"/>'
            f'<circle cx="{w/2+2}" cy="{w*0.42}" r="{w*0.16}" fill="#9fb0d0"/>'
            f'<path d="M{w*0.2+2} {w+2} Q{w/2+2} {w*0.52} {w*0.8+2} {w+2}Z" fill="#9fb0d0"/></svg>')
def _card():
    w, h = round(3.37 * S), round(2.125 * S)
    return (f'<svg width="{w+4}" height="{h+4}" viewBox="0 0 {w+4} {h+4}" aria-hidden="true">'
            f'<rect x="2" y="2" width="{w}" height="{h}" rx="6" fill="#3a4a8c" stroke="#1f2a5c" stroke-width="1.5"/>'
            f'<rect x="10" y="{h*0.36}" width="15" height="11" rx="2" fill="#e6c36a"/>'
            f'<rect x="10" y="{h*0.72}" width="{w*0.6}" height="4" rx="2" fill="#c7d0ea"/></svg>')
def _bill():
    w, h = round(6.14 * S), round(2.61 * S)
    return (f'<svg width="{w+4}" height="{h+4}" viewBox="0 0 {w+4} {h+4}" aria-hidden="true">'
            f'<rect x="2" y="2" width="{w}" height="{h}" rx="3" fill="#dfe9d6" stroke="#4f7a3a" stroke-width="1.5"/>'
            f'<rect x="7" y="7" width="{w-10}" height="{h-10}" rx="2" fill="none" stroke="#7fa36a" stroke-width="1"/>'
            f'<ellipse cx="{w/2+2}" cy="{h/2+2}" rx="{h*0.26}" ry="{h*0.32}" fill="#b9cfa9"/>'
            f'<text x="16" y="24" font-size="14" font-weight="800" fill="#4f7a3a">$1</text>'
            f'<text x="{w-12}" y="{h-8}" font-size="14" font-weight="800" fill="#4f7a3a" text-anchor="end">$1</text></svg>')

# (size, sq-in range, everyday comparison, per session, drawing)
SIZES = [
    ("Micro",  "Under 1 sq in",     "Fits under a <b>quarter</b> &mdash; tiny symbols, initials, small dots",               125, _quarter()),
    ("Small",  "1&ndash;4 sq in",   "Up to a <b>2&times;2&Prime; passport photo</b> &mdash; small script, a little heart or star", 150, _photo()),
    ("Medium", "5&ndash;9 sq in",   "About a <b>credit card</b> or business card, up to a 3&times;3&Prime; Post-it note",       250, _card()),
    ("Large",  "10&ndash;16 sq in", "Up to a <b>dollar bill</b> (about the size of a smartphone)",                        400, _bill()),
]
def card(n, rng, cmp_, p, svg):
    return (f'<div class="tp-card reveal"><div class="tp-vis">{svg}</div>'
            f'<h3>{n}</h3><div class="tp-rng">{rng}</div><p>{cmp_}</p>'
            f'<div class="tp-price">${p}<small> / session</small></div>'
            f'<div class="tp-pack">6-session package: <b>${p*5:,}</b><br><span>(6th session free &middot; save ${p})</span></div></div>')

SECTION = f'''<section class="tp" id="tattoo-pricing" aria-label="Laser tattoo removal pricing and size guide">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Pricing &amp; Size Guide</div>
      <h2>Laser Tattoo Removal Pricing in {CITY}</h2>
      <p>Tattoo removal is priced <b>per session</b>, based on the size of the tattoo. Not sure of your size? Compare it to something in your wallet &mdash; or just come in: <b>your consultation is complimentary, with no commitment</b>, and we&rsquo;ll confirm the size and price on the spot.</p>
    </div>
    <div class="tp-grid">{"".join(card(*z) for z in SIZES)}</div>
    <p class="tp-note reveal">Objects shown to scale. <b>Quick check:</b> lay a dollar bill over your tattoo &mdash; if the whole design fits underneath, it&rsquo;s Large or smaller.</p>
    <p class="tp-note reveal"><b>Bigger than a dollar bill?</b> Sleeves, back pieces and other large tattoos are priced individually at your complimentary, no-commitment consultation.</p>
    <div class="tp-offer reveal">
      <div><div class="tp-badge">Package Offer</div>
      <h3>Buy 5 sessions, get the 6th session free</h3>
      <p>Pay for 5 sessions and your 6th session is free of charge. Package sessions are for the <b>same tattoo</b>.</p></div>
      <div class="tp-cta"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Complimentary Consultation</a><a class="btn btn-outline" href="/pricing/#cat-laser-skin">See All Pricing</a></div>
    </div>
  </div>
  <style>
  .tp{{padding:72px 0;background:#f3f5fb}}
  .tp .section-head p{{font-size:1.15rem;line-height:1.7;color:var(--ink);font-weight:500;max-width:780px;margin:10px auto 0}}
  .tp-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:28px}}
  .tp-card{{background:#fff;border:1px solid rgba(31,42,92,.14);border-radius:18px;padding:22px 20px;text-align:center;box-shadow:0 8px 24px rgba(31,42,92,.06)}}
  .tp-vis{{height:80px;display:flex;align-items:center;justify-content:center}}
  .tp-vis svg{{max-width:100%;height:auto}}
  .tp-card h3{{margin:6px 0 2px;font-size:1.45rem;color:#1f2a5c;font-weight:700}}
  .tp-rng{{font-weight:700;color:var(--ink);font-size:1.08rem}}
  .tp-card p{{margin:6px 0 12px;color:var(--ink);font-size:1.02rem;font-weight:500;line-height:1.45}}
  .tp-price{{font-size:2rem;font-weight:800;color:#1f2a5c}}
  .tp-price small{{font-size:1rem;font-weight:600}}
  .tp-pack{{margin-top:10px;padding-top:10px;border-top:1px solid rgba(31,42,92,.12);color:var(--ink);font-size:1rem;font-weight:500}}
  .tp-pack b{{color:#1f2a5c;font-size:1.1rem}}
  .tp-pack span{{font-size:.92rem;font-weight:600}}
  .tp-note{{text-align:center;margin:14px auto 0;font-size:1.1rem;color:var(--ink);font-weight:500}}
  .tp-offer{{margin-top:26px;display:flex;gap:24px;align-items:center;justify-content:space-between;background:#1f2a5c;color:#fff;border-radius:20px;padding:26px 30px}}
  .tp-offer h3{{color:#fff;margin:6px 0;font-size:1.5rem}}
  .tp-offer p{{color:#fff;margin:0;font-size:1.08rem;font-weight:500}}
  .tp-badge{{display:inline-block;background:#fff;color:#1f2a5c;font-weight:700;font-size:.85rem;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:4px 12px}}
  .tp-cta{{display:flex;gap:10px;flex-wrap:wrap}}
  .tp-offer .btn-outline{{color:#fff;border-color:#fff}}
  @media(max-width:1000px){{.tp-grid{{grid-template-columns:repeat(2,1fr)}}}}
  @media(max-width:700px){{.tp-offer{{flex-direction:column;align-items:flex-start}}}}
  @media(max-width:520px){{.tp-grid{{grid-template-columns:1fr}}}}
  </style>
</section>
'''
if 'id="tattoo-pricing"' not in s:
    k = s.find('<section id="faq">')
    if k != -1:
        s = s[:k] + SECTION + s[k:]

offers = []
for n, rng, _, p, _ in SIZES:  # noqa
    r = rng.replace("&ndash;", "-")
    offers.append({"@type": "Offer", "name": f"Laser Tattoo Removal - {n} ({r}), per session", "price": str(p), "priceCurrency": "USD"})
    offers.append({"@type": "Offer", "name": f"Laser Tattoo Removal - {n}, 6-session package (buy 5, 6th free, same tattoo)", "price": str(p * 5), "priceCurrency": "USD"})
offers.append({"@type": "Offer", "name": "Laser Tattoo Removal Consultation (complimentary, no commitment)", "price": "0", "priceCurrency": "USD"})
SCHEMA = {"@context": "https://schema.org", "@type": "Service", "name": f"Laser Tattoo Removal in {CITY}",
          "serviceType": "Laser Tattoo Removal", "url": ORIGIN + "/laser-tattoo-removal/",
          "provider": {"@type": "MedicalBusiness", "name": "Serene Med Spa", "url": ORIGIN + "/"},
          "areaServed": CITY,
          "offers": {"@type": "AggregateOffer", "lowPrice": "0", "highPrice": "2000", "priceCurrency": "USD", "offerCount": str(len(offers))},
          "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Laser Tattoo Removal Pricing", "itemListElement": offers}}
if 'id="tattoo-offers-ld"' not in s:
    tag = '<script type="application/ld+json" id="tattoo-offers-ld">%s</script>\n' % json.dumps(SCHEMA, ensure_ascii=False)
    s = s.replace("</head>", tag + "</head>", 1)

if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("tattoo_pricing:", "updated" if s != o else "already present", CITY)
