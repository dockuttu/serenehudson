# -*- coding: utf-8 -*-
# review_cta_inject.py — post-build, idempotent. Adds a Google review ask to the end of the
# aftercare block on every built page that has one.
#
# Why post-build rather than inside aftercare_html(): three of the highest-traffic pages
# (botox, fillers, morpheus8) are hand-built static HTML that never passes through
# common.aftercare_html, so a hook there silently missed exactly the pages that matter most.
# Injecting after the fact covers generated and static pages with one mechanism.
#
# The link comes from GOOGLE_REVIEW_URL in common.py (Google Business Profile > Ask for reviews).
import glob, os, re, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
CTA = ns["REVIEW_CTA"]
MARK = "serene-review-cta"
ANCHOR = '<p class="ac-note">'

n = skipped = 0
for f in sorted(glob.glob(os.path.join(BASE, "**", "index.html"), recursive=True)):
    html = open(f, encoding="utf-8").read()
    if 'id="aftercare"' not in html:
        continue
    if MARK in html:          # already injected on a previous run
        skipped += 1; continue
    if ANCHOR not in html:
        print("  WARNING: %s has aftercare but no ac-note anchor" % f); continue
    html = html.replace(ANCHOR, CTA + "\n    " + ANCHOR, 1)
    open(f, "w", encoding="utf-8").write(html)
    n += 1
print("review_cta_inject: added to %d page(s)%s" % (n, (", %d already had it" % skipped) if skipped else ""))
