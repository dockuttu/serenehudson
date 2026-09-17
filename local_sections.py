# local_sections.py — post-build, idempotent. Adds a location-specific block ("<Service> at our <Town>
# office") to the top treatment pages so the Hudson and Barboursville versions of each page are not
# near-duplicates. Everything in the block comes from this site's own data: prices from the pricing
# page's Offer schema, address/parking/same-day notes and nearby-town drive times from cities_data.py,
# providers per office, and Journal articles tagged for this location. Same file in both repos.
import glob, json, os, re, sys, html as H
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
ns = {"BOOK": ""}
exec(open("cities_data.py", encoding="utf-8").read(), ns)
SITE, CITIES = ns["CITY_SITE"], ns["CITIES"]
LOC = SITE["loc_short"]                       # "Hudson" / "Barboursville"
STATE = "OH" if LOC == "Hudson" else "WV"
IS_H = LOC == "Hudson"
LOCKEY = "hudson" if IS_H else "barboursville"
PROVIDERS = ("Dr. Shweta Arora, MD and Dr. Robin Arora, MD" if IS_H else
             "Dr. Shweta Arora, MD, Dr. Robin Arora, MD and Stephanie Welker, FNP-BC")
AREA = ("Summit, Portage and northern Cuyahoga counties" if IS_H else
        "Cabell, Wayne and Putnam counties and the Tri-State (Ashland, KY and Ironton, OH)")

# ---- prices from this site's pricing page ----
offers = {}
try:
    ps = open(os.path.join(BASE, "pricing", "index.html"), encoding="utf-8").read()
    def walk(x):
        if isinstance(x, dict):
            if x.get("@type") == "Offer":
                n = (x.get("itemOffered") or {}).get("name"); p = x.get("price")
                if n and p: offers[n] = p
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    for m in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', ps, re.S):
        try: walk(json.loads(m))
        except Exception: pass
except FileNotFoundError:
    pass
def P(name): return offers.get(name)
def money(v): return "$" + (f"{int(float(v)):,}" if float(v) == int(float(v)) else v)

# ---- Journal articles, location-tagged ----
J = "https://blog.serenemedspas.com/"
ART = {
 "lip":   [("half-syringe-lip-filler-cost-hudson-oh", "Half-syringe lip filler: cost and results", None),
           ("full-syringe-lip-filler-cost-barboursville-wv", "Full-syringe lip filler: cost and what to expect", None),
           ("lip-filler-touch-up-uneven-volbella-hudson-oh-barboursville-wv", "When lip filler fades unevenly: small touch-ups", None),
           ("male-lip-filler-juvederm-volbella", "Male lip filler with Juv&eacute;derm Volbella", None)],
 "hormone": [("ultrasound-hormone-pellet-placement-hudson-oh-barboursville-wv", "How ultrasound guides hormone pellet placement", None),
           ("hormone-lab-testing-before-treatment-hudson-oh", "Test first, then treat: labs before hormone therapy", "hudson"),
           ("hormone-optimization-barboursville-wv", "Hormone optimization in Barboursville, WV", "barboursville"),
           ("wellness-blood-work-explained-barboursville-huntington-wv", "Wellness blood work, explained", "barboursville"),
           ("menopause-symptoms-relief-hudson-oh-barboursville-wv", "Menopause symptoms and relief", None)],
 "wl":    [("glp-1-weight-loss-muscle-loss-hudson-oh", "GLP-1 weight loss without losing muscle", "hudson"),
           ("medicare-glp-1-bridge-program-barboursville-huntington-wv", "The Medicare GLP-1 bridge program", "barboursville")],
 "iv":    [("iv-therapy-immune-support-fall", "IV therapy for fall immune support", None)],
}
def articles(key):
    out = []
    for slug, title, loc in ART.get(key, []):
        if loc and loc != LOCKEY: continue
        out.append('<li><a href="%s%s/?loc=%s">%s</a></li>' % (J, slug, LOCKEY, title))
    return out

# ---- page config: slug -> (display name, price sentence, article key, same-day?) ----
def price_line(slug):
    if slug == "botox" and P("Botox"): return f"Botox is {money(P('Botox'))} per unit at our {LOC} office, with Dysport, Xeomin and Daxxify also available."
    if slug == "fillers" and P("Dermal Fillers"): return f"Dermal filler starts at {money(P('Dermal Fillers'))} per syringe in {LOC}."
    if slug == "lip-filler" and P("Lip Filler - Full Syringe (1 mL)"):
        return f"In {LOC}, a full syringe (1 mL) is {money(P('Lip Filler - Full Syringe (1 mL)'))} and a half syringe (0.5 mL) is {money(P('Lip Filler - Half Syringe (0.5 mL)'))}."
    if slug == "laser-tattoo-removal" and P("Laser Tattoo Removal"): return f"Tattoo removal sessions in {LOC} start at {money(P('Laser Tattoo Removal'))} and are priced by tattoo size, with 6-session packages (6th session free)."
    if slug == "morpheus8" and P("Morpheus8 RF"): return f"Morpheus8 is {money(P('Morpheus8 RF'))} per session at our {LOC} office."
    if slug == "weight-loss" and P("Medical Weight Loss Visit"): return f"Medical weight loss visits in {LOC} start at {money(P('Medical Weight Loss Visit'))}."
    if slug == "hydrafacial" and P("HydraFacial"): return f"A HydraFacial is {money(P('HydraFacial'))} at our {LOC} office."
    if slug == "iv-therapy" and P("IV Vitamin Infusion"): return f"IV vitamin infusions in {LOC} start at {money(P('IV Vitamin Infusion'))}."
    if slug == "ultherapy" and P("Ultherapy PRIME"): return f"Ultherapy PRIME treatments in {LOC} start at {money(P('Ultherapy PRIME'))}."
    if slug == "laser-hair-removal" and P("Laser Hair Removal"): return f"Laser hair removal in {LOC} starts at {money(P('Laser Hair Removal'))} per session, with packages available."
    if slug == "microneedling" and P("Microneedling with PRP"): return f"Microneedling with PRP is {money(P('Microneedling with PRP'))} in {LOC}."
    if slug == "hormone-optimization": return f"Hormone care in {LOC} starts with lab work; panel and pellet pricing is listed on our pricing page."
    return f"Current {LOC} prices are listed on our pricing page."
PAGES = {
 "botox": ("Botox", None, True), "fillers": ("Dermal Fillers", "lip", True), "lip-filler": ("Lip Filler", "lip", True),
 "laser-tattoo-removal": ("Laser Tattoo Removal", None, True), "morpheus8": ("Morpheus8", None, False),
 "weight-loss": ("Medical Weight Loss", "wl", False), "hormone-optimization": ("Hormone Optimization", "hormone", False),
 "hydrafacial": ("HydraFacial", None, True), "iv-therapy": ("IV Therapy", "iv", False), "ultherapy": ("Ultherapy", None, False),
 "laser-hair-removal": ("Laser Hair Removal", None, True), "microneedling": ("Microneedling", None, False),
}
SHORT = {"botox": "Botox", "fillers": "dermal filler", "lip-filler": "lip filler", "laser-tattoo-removal": "tattoo removal",
         "morpheus8": "Morpheus8", "weight-loss": "medical weight loss", "hormone-optimization": "hormone care",
         "hydrafacial": "a HydraFacial", "iv-therapy": "an IV drip", "ultherapy": "Ultherapy",
         "laser-hair-removal": "laser hair removal", "microneedling": "microneedling"}
COPY_FIXES = [("Modern medications such as semaglutide-class options, prescribed when clinically appropriate.",
               "Modern GLP-1 medications, prescribed only when clinically appropriate.")]
steps = dict(SITE.get("steps", []))
park = next((v for k, v in SITE.get("steps", []) if "park" in k.lower() or "exit" in k.lower()), "")
MARK_S, MARK_E = "<!-- local-block:start -->", "<!-- local-block:end -->"
CSS = ("<style>.local-block{background:#fff}.local-block .lb-grid{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;max-width:1040px;margin:0 auto}"
       ".local-block p,.local-block li{font-size:1.08rem;line-height:1.65;color:#2b2230;font-weight:500}.local-block h3{font-size:1.35rem;margin:0 0 10px}"
       ".local-block .lb-card{background:var(--blush,#fbf1f4);border-radius:18px;padding:22px 24px}.local-block ul{margin:0 0 0 18px;padding:0}"
       ".local-block li{margin:0 0 6px}.local-block a{color:var(--rose,#c94f74);font-weight:600}.local-block .lb-faq p{margin:0 0 12px}"
       "@media(max-width:820px){.local-block .lb-grid{grid-template-columns:1fr}}</style>")

def block(slug, name, akey, same_day):
    city_items = "".join('<li><a href="/%s/">%s</a> &mdash; %s</li>' % (c["slug"], c["city"], c.get("drive", "")) for c in CITIES)
    arts = articles(akey)
    arts_html = ('<h3>From the Serene Journal</h3><ul>%s</ul>' % "".join(arts)) if arts else ""
    gallery = ' See real results in our <a href="/before-after/">before &amp; after gallery</a>.' if slug in ("botox", "fillers", "lip-filler", "morpheus8") else ""
    sh = SHORT.get(slug, name)
    sd = (f" If you&rsquo;re a good candidate, {sh} can often be done the same day as your consultation." if same_day else
          f" Every {name.lower() if name not in ('Morpheus8', 'Ultherapy') else name} plan starts with a complimentary, no-commitment consultation.")
    pl = price_line(slug)
    faq = (f'<p><strong>What does {name.lower() if name not in ("Botox", "Morpheus8", "HydraFacial", "Ultherapy") else name} cost in {LOC}, {STATE}?</strong><br>{pl} <a href="/pricing/">See full {LOC} pricing</a>.</p>'
           f'<p><strong>Who performs {name} at Serene {LOC}?</strong><br>{PROVIDERS}.</p>'
           f'<p><strong>Where is the {LOC} office?</strong><br>{SITE["addr1"]}, {SITE["addr2"]}. Call <a href="{SITE["tel"]}">{SITE["phone"]}</a>. Open {H.unescape(SITE["hours"]).replace("<br>", "; ")}.</p>')
    return (MARK_S + CSS +
      f'<section class="local-block" id="{LOC.lower()}-{slug}"><div class="wrap">'
      f'<div class="section-head"><div class="eyebrow">Serene Med Spa &mdash; {LOC}, {STATE}</div><h2>{name} at our {LOC} office</h2></div>'
      f'<div class="lb-grid"><div>'
      f'<p>{name} at Serene {LOC} is performed or supervised by {PROVIDERS}.{sd}{gallery}</p>'
      f'<p>{park}</p>'
      f'<p>We see patients from across {AREA}. Coming from nearby?</p><ul>{city_items}</ul>'
      f'</div><div class="lb-card lb-faq"><h3>{name} in {LOC}: quick answers</h3>{faq}{arts_html}</div></div>'
      f'</div></section>' + MARK_E + "\n")

n = 0
for slug, (name, akey, same_day) in PAGES.items():
    p = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(p): continue
    s = open(p, encoding="utf-8").read()
    s = re.sub(re.escape(MARK_S) + r".*?" + re.escape(MARK_E) + r"\n?", "", s, flags=re.S)
    i = s.find('<section id="faq"')
    if i < 0: continue
    s = s[:i] + block(slug, name, akey, same_day) + "\n" + s[i:]
    for a, b in COPY_FIXES: s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s); n += 1
print("local_sections: %s block added to %d page(s)" % (LOC, n))
