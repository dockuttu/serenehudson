#!/usr/bin/env python3
"""lp_resanitize.py <site-dir> — run AFTER v2_merge.py.

v2_merge swaps in the main site's shell (mega menu "Botox & Wrinkle Relaxers", footer
"Botox & Dysport", promo ribbon "prepaid Botox & filler savings"), which put drug names
back on the ads-only /lp/* pages and got every Google Ad flagged "Restricted drug terms"
(found Oct 6, 2026). This re-applies build_ads_pages.sanitize() to the finished /lp/ pages.
Stdlib only.
"""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
sys.argv = [sys.argv[0], SITE]          # build_ads_pages reads argv at import; keep it harmless
import build_ads_pages as BAP           # noqa: E402  (import only; its __main__ block does not run)

bad = []
for f in sorted(glob.glob(os.path.join(SITE, "lp", "*", "index.html"))):
    s = open(f, encoding="utf-8").read()
    t = BAP.sanitize(s)
    # "prepaid Botox & filler" -> keep the generic term lowercase mid-sentence
    t = re.sub(r"\b(prepaid|plus|with|and|or|of|for|your)\s+Wrinkle relaxer", r"\1 wrinkle relaxer", t)
    if t != s:
        open(f, "w", encoding="utf-8").write(t)
    left = sorted(set(x.lower() for x in BAP.DRUG_RX.findall(re.sub(r'(?:src|href|id|class)="[^"]*"', "", t))))
    print("lp_resanitize: %s  residual drug terms: %s" % (os.path.relpath(f, SITE), left or "none"))
    if left and "wrinkle-relaxer" not in f:
        bad.append(f)
sys.exit(1 if bad else 0)
