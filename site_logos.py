# -*- coding: utf-8 -*-
# site_logos.py — idempotent: keep brand/device logos current on EVERY built page, including hand-built ones.
#   1. "Our Technology" logo strips (TECH_STRIP from common.py) replace any older strips.
#   2. InMode Morpheus8 Verified Provider badge in the partner-badge row; Merz ELITE+ (not the old Bronze) everywhere.
#   3. Hand-built treatment pages (morpheus8, botox, fillers...) get the "Powered by" badge + hero seal
#      from STATIC_LOGOS below, same as generated pages get from gen_pages.DEVICE_LOGOS.
# New logo? Add the file to bundle/site/img/logos/<key>-dark.png, register it in tech_logos.py,
# map it to pages in gen_pages.DEVICE_LOGOS / STATIC_LOGOS, and list it in common.TECH_STRIP.
import sys, os, re
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
TECH_STRIP, device_badge, hero_seal = ns["TECH_STRIP"], ns["device_badge"], ns["hero_seal"]
STATIC_LOGOS = {"morpheus8": ["morpheus8", "m8-verified"],
                "botox": ["botox-cosmetic", "app-platinum"], "fillers": ["juvederm", "app-platinum"]}
MERZ_NEW = ('<a href="/xperience-rewards/" title="Merz Aesthetics ELITE+ Provider"><img src="/img/badges/merz-elite-plus.png" '
            'alt="Merz Aesthetics ELITE+ Provider" class="badge-round" loading="lazy" width="260" height="260"></a>')
BRONZE_RE = re.compile(r'<span title="Merz Aesthetics Bronze Preferred Partner">.*?</span>', re.S)
INMODE_BADGE = ('<a href="/morpheus8/" title="InMode Morpheus8 Verified Provider"><img src="/img/badges/inmode-morpheus8-verified.png" '
                'alt="InMode Morpheus8 Verified Provider" class="badge-round" loading="lazy"></a>\n      ')
TECH_RE = re.compile(r'<div class="tech reveal">\s*<div class="tech-label">.*?</div>\s*<div class="tech-row">.*?</div>\s*</div>(?:\s*<div class="tech reveal">\s*<div class="tech-label">.*?</div>\s*<div class="tech-row">.*?</div>\s*</div>)*', re.S)
changed = 0
for root, dirs, files in os.walk(SITE):
    rel = os.path.relpath(root, SITE)
    is_lp = rel == "lp" or rel.startswith("lp" + os.sep)            # ads-only pages: wording fixes only, no logo strips
    for fn in files:
        if not fn.endswith(".html"): continue
        f = os.path.join(root, fn); s = open(f, encoding="utf-8").read(); o = s
        if not is_lp and 'class="tech reveal"' in s:
            s = TECH_RE.sub(lambda m: TECH_STRIP.strip(), s, count=1)
        pi = s.find('<div class="partners')
        if not is_lp and pi != -1 and "inmode-morpheus8-verified" not in s[pi:s.find("</div>", pi)]:
            k = s.find('<span title="Allergan Partner Privileges', pi)
            if k != -1 and k < s.find("</div>", pi):
                s = s[:k] + INMODE_BADGE + s[k:]
        if "merz-bronze-preferred" in s or "Bronze" in s:   # ELITE+ replaced Bronze (home_merz.py); keep every page in step
            s = BRONZE_RE.sub(MERZ_NEW, s)
            s = (s.replace("merz-bronze-preferred.png", "merz-elite-plus.png")
                  .replace("Merz Aesthetics Bronze Preferred Partner", "Merz Aesthetics ELITE+ Provider")
                  .replace("Merz Bronze Preferred Partner", "Merz Aesthetics ELITE+ Provider")
                  .replace("a Merz Bronze preferred practice", "a Merz Aesthetics ELITE+ provider"))
        slug = rel
        if slug.startswith("morpheus8-") and slug not in STATIC_LOGOS:  # city landing pages (e.g. morpheus8-akron-oh)
            STATIC_LOGOS[slug] = STATIC_LOGOS["morpheus8"]
        if not is_lp and slug in STATIC_LOGOS and fn == "index.html":
            seal, bd = hero_seal(slug, STATIC_LOGOS), device_badge(slug, STATIC_LOGOS)
            if seal and "hero-seal" not in s and '<div class="svc-hero-media">' in s:
                s = s.replace('<div class="svc-hero-media">', '<div class="svc-hero-media">' + seal, 1)
            if bd and "device-badge" not in s and '<div class="svc-hero-txt">' in s:
                i = s.index('<div class="svc-hero-txt">'); j = s.index("</p>", i) + 4
                s = s[:j] + "\n    " + bd + s[j:]
        if s != o:
            open(f, "w", encoding="utf-8").write(s); changed += 1
print("site_logos: %d page(s) updated" % changed)
