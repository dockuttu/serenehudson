# -*- coding: utf-8 -*-
# Build guard: every service in the nav (CATEGORIES) must have a built page, every
# built page should be reachable from the nav, and pages with a Mangomint deep link
# must actually contain it. Runs last in build.sh and fails the build loudly.
import os, sys, glob, re
exec(open("common.py").read())
HIDE = {"peptide-therapy", "peptides", "body-contouring"}
try:
    from bv_localize import BV_SKIP; HIDE |= BV_SKIP
except ImportError:
    pass
SITE = "bundle/site"
errors, warnings = [], []

# 1. nav slug -> page exists
for slug in ALL_SLUGS:
    if slug in HIDE: continue
    f = os.path.join(SITE, slug, "index.html")
    if not os.path.exists(f):
        errors.append("nav links to /%s/ but no page was built" % slug); continue
    html = open(f, encoding="utf-8", errors="ignore").read()
    if slug in BOOK_MAP and BOOK_MAP[slug] not in html:
        errors.append("/%s/ is missing its Mangomint deep link %s" % (slug, BOOK_MAP[slug]))

# 2. page data slug -> in nav (so new pages don't get orphaned)
defined = set()
for f in sorted(glob.glob("pages_data*.py")):
    defined |= set(re.findall(r'"slug"\s*:\s*"([a-z0-9-]+)"', open(f, encoding="utf-8").read()))
for slug in sorted(defined - set(ALL_SLUGS) - HIDE):
    warnings.append("page /%s/ is built but not listed in CATEGORIES (not in nav/footer)" % slug)

for w in warnings: print("WARNING:", w)
for e in errors: print("ERROR:", e)
built = len(glob.glob(os.path.join(SITE, "*", "index.html")))
print("check_pages: %d nav services, %d pages built, %d error(s), %d warning(s)" % (len([s for s in ALL_SLUGS if s not in HIDE]), built, len(errors), len(warnings)))
sys.exit(1 if errors else 0)
