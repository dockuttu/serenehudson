#!/usr/bin/env python3
"""build_ads_pages.py — Google-Ads-only landing pages with no prescription-drug names.

Ported from serenebarboursville for the Hudson site.
Google's "Restricted drug terms" policy scans the *destination page*. Every public
page on this site names Botox / Dysport / Xeomin / Juvederm etc. (mega menu, footer,
price-match ribbon, logo strip, reviews), so every ad pointing here gets limited.
Same idea as build_wl_ads.py: derive noindex copies under /lp/<slug>/ with those
names removed. Public pages are untouched (SEO keeps its full copy).

Run after gen_pages/build_static (build.sh does this). Stdlib only.
Usage: python3 build_ads_pages.py [bundle/site]
"""
import os, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"

# public page slug ("" = homepage)  ->  ads-only path
PAGES = {
    "laser-tattoo-removal": "lp/tattoo-removal",
    "laser-hair-removal":   "lp/laser-hair-removal",
    "morpheus8":            "lp/morpheus8",
    "ultherapy":            "lp/ultherapy",
    "fillers":              "lp/dermal-fillers",
    "lip-filler":           "lp/lip-filler",
    "hydrafacial":          "lp/hydrafacial",
    "":                     "lp/med-spa",
}

# pages whose own name is a drug brand: links to them are dropped from ads pages
DRUG_SLUGS = r"(?:longevity|botox|skinvive|kybella|sculptra|sculptra-bbl|kenalog|weight-loss|medical-weight-loss|hormone-optimization|mens-sexual-wellness|womens-sexual-wellness)"

DRUG = (r"botox(?:\s*cosmetic)?|\w*botulinumtoxin\s*-?\s*a?|dysport|xeomin|jeuveau|daxxify|letybo|"
        r"juv(?:e|é|&eacute;)derm(?:\s*(?:voluma|volbella|vollure|volux|ultra)(?:\s*xc)?)?|restylane(?:\s*\w+)?|"
        r"\brha\b|belotero|revanesse|radiesse|sculptra|skinvive|kybella|deoxycholic\s*acid|kenalog|triamcinolone|"
        r"semaglutide|tirzepatide|wegovy|zepbound|ozempic|mounjaro|liraglutide|saxenda|\bglp-?1\b|"
        r"testosterone|estradiol|bi(?:o|ö|&ouml;)te|latisse|tretinoin|retin-?a\b|renova|hydroquinone|lidocaine|"
        r"sildenafil|tadalafil|viagra|cialis|ketamine|phentermine")
DRUG_RX = re.compile(DRUG, re.I)

# ordered text replacements (applied to visible text + alt/title/content/placeholder)
REPL = [
    (r"Botox,\s*Dysport,\s*Xeomin\s*(?:&amp;|&|and)\s*Daxxify", "Wrinkle relaxers"),
    (r"Botox\s*(?:&amp;|&|and|/)\s*Dysport", "Wrinkle relaxers"),
    (r"botox(?:\s*cosmetic)?|dysport|xeomin|jeuveau|daxxify|letybo", "wrinkle relaxer"),
    (r"\(?\w*botulinumtoxin\s*-?\s*a?\)?", ""),
    (r"juv(?:e|é|&eacute;)derm(?:\s*(?:voluma|volbella|vollure|volux|ultra)(?:\s*xc)?)?|restylane(?:\s*(?:lyft|kysse|defyne|refyne|contour|silk|eyelight))?|\brha\b|belotero|revanesse", "hyaluronic filler"),
    (r"radiesse|sculptra", "collagen stimulator"),
    (r"skinvive", "skin booster"),
    (r"kybella|\(?deoxycholic\s*acid\)?", "chin-fat treatment"),
    (r"kenalog|triamcinolone", "scar-softening injection"),
    (r"semaglutide|tirzepatide|wegovy|zepbound|ozempic|mounjaro|liraglutide|saxenda|\bglp-?1\b", "physician-prescribed treatment"),
    (r"bi(?:o|ö|&ouml;)te", "hormone optimization"),
    (r"testosterone|estradiol", "hormone"),
    (r"latisse", "lash serum"),
    (r"retinoids/retin-?a\b", "retinoid creams"),
    (r"tretinoin|retin-?a\b|renova|hydroquinone", "prescription-strength skincare"),
    (r"lidocaine", "numbing"),
    (r"sildenafil|tadalafil|viagra|cialis|ketamine|phentermine", "treatment"),
]
REPL = [(re.compile(a, re.I), b) for a, b in REPL]

def fix_text(t):
    for rx, b in REPL:
        def sub(m, b=b):
            s = m.group(0)
            return b[:1].upper() + b[1:] if (b and s[:1].isupper()) else b
        t = rx.sub(sub, t)
    t = re.sub(r"hyaluronic filler(\s*(?:,|&amp;|&|and|/)\s*hyaluronic filler)+", "hyaluronic fillers", t, flags=re.I)
    t = re.sub(r"wrinkle relaxer(\s*(?:,|&amp;|&|and|/)\s*wrinkle relaxer)+", "wrinkle relaxers", t, flags=re.I)
    return t

ATTR = re.compile(r'(\b(?:alt|title|content|placeholder|aria-label)=")([^"]*)(")', re.I)

def sanitize(html):
    # 1. drop links to drug-named pages and any link/figure whose markup names a drug
    html = re.sub(r'<a\b[^>]*href="(?:https?://[^"/]+)?/' + DRUG_SLUGS + r'/[^"]*"[^>]*>.*?</a>', "", html, flags=re.S | re.I)
    html = re.sub(r'<a\b(?=[^>]*(?:' + DRUG + r'))[^>]*>.*?</a>', "", html, flags=re.S | re.I)
    # 2. drop images whose file name / alt names a drug (logo strip, injectable photos)
    html = re.sub(r'<img\b[^>]*(?:src|alt)="[^"]*(?:' + DRUG + r'|botox-inject|filler-inject)[^"]*"[^>]*>', "", html, flags=re.I)
    # 3. rewrite remaining text (outside tags) and descriptive attributes
    parts = re.split(r"(<[^>]+>)", html)
    out = []
    for p in parts:
        if p.startswith("<"):
            out.append(ATTR.sub(lambda m: m.group(1) + fix_text(m.group(2)) + m.group(3), p))
        else:
            out.append(fix_text(p))
    return "".join(out)

def build(src_slug, dst_path):
    src = os.path.join(SITE, src_slug, "index.html") if src_slug else os.path.join(SITE, "index.html")
    if not os.path.exists(src):
        print("build_ads_pages: skip (missing)", src); return None
    s = open(src, encoding="utf-8").read()
    m = re.search(r'<link rel="canonical" href="(https://[^/"]+)/', s)
    host = m.group(1) if m else "https://hudson.serenemedspas.com"
    s = sanitize(s)
    old = host + "/" + (src_slug + "/" if src_slug else "")
    new = host + "/" + dst_path + "/"
    s = re.sub(r'(<link rel="canonical" href=")' + re.escape(old) + '"', r"\g<1>" + new + '"', s)
    s = re.sub(r'(<meta property="og:url" content=")' + re.escape(old) + '"', r"\g<1>" + new + '"', s)
    s = re.sub(r'<meta name="robots"[^>]*>\s*', "", s)
    s = s.replace("</title>", '</title>\n<meta name="robots" content="noindex,follow">', 1)
    dst = os.path.join(SITE, dst_path, "index.html")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(s)
    left = sorted(set(x.lower() for x in DRUG_RX.findall(re.sub(r'(?:src|href)="[^"]*"', "", s))))
    print("build_ads_pages: /%s/ <- /%s  residual drug terms: %s" % (dst_path, src_slug, left or "none"))
    return left

if __name__ == "__main__":
    bad = [p for p, sl in PAGES.items() if build(p, sl)]
    sys.exit(1 if bad else 0)
