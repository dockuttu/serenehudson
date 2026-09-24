# -*- coding: utf-8 -*-
"""pricing_links.py — maps price-list rows to the treatment page that explains them (identical file in both office repos).

build_pricing.row()/rowaka()/sub() call link_for(name) and wrap the name in a link when one is found.
RULES are (regex, [candidate slugs in preference order]); the first candidate that exists under bundle/site wins.
"kind" in the report: exact = dedicated page, parent = covered by a broader page (candidate for its own page), none = no page.
Run `python3 pricing_links.py bundle/site` to print the coverage report used to decide which pages to build next.
"""
import os, re, sys, html

RULES = [
    # injectables
    (r"^lip filler|^lip flip", ["lip-filler"]),
    (r"^cheek filler", ["cheek-filler"]),
    (r"^under-eye filler", ["under-eye-filler"]),
    (r"^under-eye pr[pf]", ["under-eye-prp"]),
    (r"^jawline filler", ["jawline-filler"]),
    (r"^chin filler", ["chin-filler"]),
    (r"^hand filler", ["hand-filler", "fillers"]),
    (r"^radiesse", ["radiesse", "fillers"]),
    (r"^filler reversal|hyaluronidase", ["filler-dissolver", "fillers"]),
    (r"^3 juv", ["fillers"]),
    (r"^hyperhidrosis", ["hyperhidrosis-treatment", "botox"]),
    (r"^teeth grinding|masseter", ["masseter-botox", "botox"]),
    (r"^baby botox", ["baby-botox", "botox"]),
    (r"shoulder slimming|^trap", ["shoulder-slimming-botox", "botox"]),
    (r"^botox|^xeomin|^dysport|^daxxify", ["botox"]),
    (r"^sculptra bbl", ["sculptra-bbl"]),
    (r"^sculptra", ["sculptra"]),
    (r"^skinvive", ["skinvive"]),
    (r"^kybella", ["kybella"]),
    (r"^kenalog", ["kenalog", "acne-treatment"]),
    (r"^pdo ", ["thread-lift"]),
    (r"spider vein", ["spider-veins"]),
    # wellness
    (r"^medical weight loss", ["weight-loss", "medical-weight-loss"]),
    (r"^bi.te.*(female|women)", ["hormone-therapy-women", "hormone-optimization"]),
    (r"^bi.te.*(male|men)|^gonadorelin|^testosterone", ["testosterone-therapy-men", "hormone-optimization"]),
    (r"^bi.te", ["hormone-optimization"]),
    (r"^vitamin b12|^lipo-b|^amino blend|^lipo shot|^lipo pack|^glutathione (shot|injection)|^niagen. injection|^nad\+ injection|^nad\+$", ["vitamin-injections", "iv-therapy"]),
    (r"^iv vitamin|^glutathione|^tri-immune|^coq10|^vitamin d3|^biotin|^anti-nausea|^serene (quench|recovery|immune|beauty|reboot|brain|pms|get-up)|^myer|^glow drip|^longevity drip|^nad\+ iv|^niagen. iv", ["iv-drip-menu", "iv-therapy", "hydration-bar"]),
    (r"^sermorelin|^nad\+ & sermorelin", ["sermorelin", "longevity"]),
    (r"^low-dose naltrexone|^ldn", ["low-dose-naltrexone", "longevity"]),
    (r"^longevity", ["longevity", "peptides"]),
    (r"^bpc-157|^tb-500|^wolverine|^cjc-1295|^tesamorelin|^ghk-cu|^pt-141|^ipamorelin|^thymosin|^semax|^selank", ["longevity", "peptides"]),  # /peptides/ stays unlinked until LegitScript clears
    # skin & laser
    (r"^morpheus8|^morpheusv", ["morpheus8"]),
    (r"^laser facial", ["laser-facial"]),
    (r"^laser nail fungus", ["laser-nail-fungus"]),
    (r"^depigmentation", ["hyperpigmentation"]),
    (r"^acne", ["acne-treatment", "chemical-peels"]),
    (r"chemical peel", ["chemical-peels"]),
    (r"^sciton bbl", ["photofacial"]),
    (r"^alma hybrid", ["alma-hybrid", "laser-skin"]),
    (r"^sciton moxi|^moxi", ["sciton-moxi", "laser-skin"]),
    (r"^deka co", ["deka-co2-laser", "laser-skin"]),
    (r"^coolpeel", ["coolpeel", "laser-skin"]),
    (r"^pico fractional|^clear lift", ["pico-fractional-resurfacing", "laser-skin"]),
    (r"^opus plasma", ["opus-plasma"]),
    (r"^full face|^lower face|^neck / under-chin|^brow lift|^d.collet", ["ultherapy"]),   # Ultherapy area rows
    (r"^prp hair", ["prp-hair-restoration"]),
    (r"^alma ted", ["alma-ted"]),
    (r"^hydrafacial", ["hydrafacial"]),
    (r"^sknlab", ["sknlab"]),
    (r"^diamondglow", ["diamondglow"]),
    (r"^microdermabrasion|^facials", ["medical-facials"]),
    (r"^microneedling", ["microneedling"]),
    # body & intimate
    (r"^evolvex", ["evolve-x"]),
    (r"^emsculpt", ["emsculpt-neo"]),
    (r"^v-renew", ["v-renew", "womens-sexual-wellness"]),
    (r"^vtone", ["vtone", "womens-sexual-wellness"]),
    (r"^formav", ["formav", "womens-sexual-wellness"]),
    (r"^alma duo", ["alma-duo", "mens-sexual-wellness"]),
    (r"^p-renew", ["p-renew", "mens-sexual-wellness"]),
    (r"^grow girth", ["grow-girth", "mens-sexual-wellness"]),
    # group headers (sub())
    (r"^ultherapy prime", ["ultherapy"]),
    (r"^laser hair removal", ["laser-hair-removal"]),
    (r"^laser tattoo removal", ["laser-tattoo-removal"]),
    (r"^facials$", ["medical-facials"]),
    (r"^dermal fillers", ["fillers"]),
    (r"^neurotoxins", ["botox"]),
    (r"^collagen & biostimulators", ["sculptra"]),
    (r"^vitamin & lipo shots", ["vitamin-injections"]),
    (r"^monthly programs", ["longevity"]),
    (r"^add-on injections", ["iv-drip-menu"]),
    (r"^hair restoration", ["prp-hair-restoration"]),
    (r"^body treatments", ["evolve-x", "body-contouring"]),
    (r"^female wellness", ["womens-sexual-wellness"]),
    (r"^male wellness", ["mens-sexual-wellness"]),
]
# rows that resolve to one of these are "covered by a parent page" — a dedicated page is a candidate
PARENT_SLUGS = {"fillers", "botox", "laser-skin", "iv-therapy", "hydration-bar", "longevity", "peptides", "medical-facials", "chemical-peels", "mens-sexual-wellness", "womens-sexual-wellness", "hormone-optimization"}

def _clean(name):
    return re.sub(r"<[^>]+>", "", html.unescape(name)).strip().lower()

def resolve(name, site="bundle/site"):
    n = _clean(name)
    for rx, slugs in RULES:
        if re.search(rx, n):
            for s in slugs:
                if os.path.isfile(os.path.join(site, s, "index.html")):
                    return s, ("parent" if s in PARENT_SLUGS else "exact")
            return slugs[0], ("parent" if slugs[0] in PARENT_SLUGS else "exact")  # not built yet (built later in build.sh) — link anyway
    return None, "none"

def link_for(name, site="bundle/site"):
    slug, _ = resolve(name, site)
    return f"/{slug}/" if slug else None

def linked(name, site="bundle/site"):
    href = link_for(name, site)
    return f'<a href="{href}" class="price-link">{name}</a>' if href else name

def report(site="bundle/site", names=()):
    rows = [(n, *resolve(n, site)) for n in names]
    exact = [r for r in rows if r[2] == "exact"]; parent = [r for r in rows if r[2] == "parent"]; none = [r for r in rows if r[2] not in ("exact", "parent")]
    print(f"{len(rows)} price rows: {len(exact)} link to a dedicated page, {len(parent)} covered by a parent page, {len(none)} with no page\n")
    print("COVERED BY A PARENT PAGE (candidates for a dedicated page):")
    by = {}
    for n, s, k in parent: by.setdefault(s, []).append(_clean(n))
    for s, ns in sorted(by.items()): print(f"  /{s}/  <-  " + "; ".join(ns))
    print("\nNO PAGE:")
    for n, s, k in none: print(f"  {_clean(n)}  ({k})")

if __name__ == "__main__":
    site = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
    src = open("build_pricing.py", encoding="utf-8").read()
    names = re.findall(r'\b(?:row|rowaka|sub)\("([^"]+)"', src)
    report(site, names)
