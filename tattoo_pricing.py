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

# (size, sq-in range, everyday comparison, per session, box edge px for the visual)
SIZES = [
    ("Micro",  "Under 1 sq in",  "About the size of a fingernail",            125, 22),
    ("Small",  "1&ndash;4 sq in",  "Postage stamp to business card",            150, 40),
    ("Medium", "5&ndash;9 sq in",  "Post-it note to the palm of your hand",     250, 58),
    ("Large",  "10&ndash;16 sq in", "About the size of an iPhone",              400, 76),
]
def card(n, rng, cmp_, p, px):
    return (f'<div class="tp-card reveal"><div class="tp-vis"><span style="width:{px}px;height:{px}px"></span></div>'
            f'<h3>{n}</h3><div class="tp-rng">{rng}</div><p>{cmp_}</p>'
            f'<div class="tp-price">${p}<small> / session</small></div>'
            f'<div class="tp-pack">6-session package: <b>${p*5:,}</b><br><span>(6th session free &middot; save ${p})</span></div></div>')

SECTION = f'''<section class="tp" id="tattoo-pricing" aria-label="Laser tattoo removal pricing and size guide">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Pricing &amp; Size Guide</div>
      <h2>Laser Tattoo Removal Pricing in {CITY}</h2>
      <p>Tattoo removal is priced <b>per session</b>, based on the size of the tattoo. Measure the rectangle that fits around your whole design &mdash; or just come in: <b>your consultation is always free</b>, and we&rsquo;ll confirm the size and price on the spot.</p>
    </div>
    <div class="tp-grid">{"".join(card(*z) for z in SIZES)}</div>
    <p class="tp-note reveal"><b>Larger than 16 sq in?</b> Sleeves, back pieces and other large tattoos are priced individually at your free consultation.</p>
    <div class="tp-offer reveal">
      <div><div class="tp-badge">Package Offer</div>
      <h3>Buy 5 sessions, get the 6th session free</h3>
      <p>Pay for 5 sessions and your 6th session is free of charge. Package sessions are for the <b>same tattoo</b>.</p></div>
      <div class="tp-cta"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Free Consultation</a><a class="btn btn-outline" href="/pricing/#cat-laser-skin">See All Pricing</a></div>
    </div>
  </div>
  <style>
  .tp{{padding:72px 0;background:#f3f5fb}}
  .tp .section-head p{{font-size:1.15rem;line-height:1.7;color:var(--ink);font-weight:500;max-width:780px;margin:10px auto 0}}
  .tp-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:28px}}
  .tp-card{{background:#fff;border:1px solid rgba(31,42,92,.14);border-radius:18px;padding:22px 20px;text-align:center;box-shadow:0 8px 24px rgba(31,42,92,.06)}}
  .tp-vis{{height:84px;display:flex;align-items:center;justify-content:center}}
  .tp-vis span{{display:block;border:2px dashed #1f2a5c;border-radius:6px;background:rgba(31,42,92,.06)}}
  .tp-card h3{{margin:6px 0 2px;font-size:1.45rem;color:#1f2a5c;font-weight:700}}
  .tp-rng{{font-weight:700;color:var(--ink);font-size:1.08rem}}
  .tp-card p{{margin:6px 0 12px;color:var(--ink);font-size:1.02rem;font-weight:500;line-height:1.45}}
  .tp-price{{font-size:2rem;font-weight:800;color:#1f2a5c}}
  .tp-price small{{font-size:1rem;font-weight:600}}
  .tp-pack{{margin-top:10px;padding-top:10px;border-top:1px solid rgba(31,42,92,.12);color:var(--ink);font-size:1rem;font-weight:500}}
  .tp-pack b{{color:#1f2a5c;font-size:1.1rem}}
  .tp-pack span{{font-size:.92rem;font-weight:600}}
  .tp-note{{text-align:center;margin:22px auto 0;font-size:1.1rem;color:var(--ink);font-weight:500}}
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
for n, rng, _, p, _ in SIZES:
    r = rng.replace("&ndash;", "-")
    offers.append({"@type": "Offer", "name": f"Laser Tattoo Removal - {n} ({r}), per session", "price": str(p), "priceCurrency": "USD"})
    offers.append({"@type": "Offer", "name": f"Laser Tattoo Removal - {n}, 6-session package (buy 5, 6th free, same tattoo)", "price": str(p * 5), "priceCurrency": "USD"})
offers.append({"@type": "Offer", "name": "Laser Tattoo Removal Consultation", "price": "0", "priceCurrency": "USD"})
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
