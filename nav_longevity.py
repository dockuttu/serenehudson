# nav_longevity.py — idempotent: add "Longevity & NAD+" to the Wellness column of the
# Treatments mega-menu on every built page (static hand-built pages carry their own nav copy).
import glob, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
LINK = '<a href="/longevity/">Longevity &amp; NAD+</a>'
n = 0
for f in glob.glob(SITE + "/**/*.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    if 'href="/longevity/">Longevity' in s or '<h5>Wellness</h5>' not in s: continue
    i = s.index('<h5>Wellness</h5>')
    anchor = '<a href="/iv-therapy/">IV Therapy</a>'
    j = s.find(anchor, i)
    if j == -1 or j - i > 400:
        s = s[:i+len('<h5>Wellness</h5>')] + LINK + s[i+len('<h5>Wellness</h5>'):]
    else:
        s = s[:j+len(anchor)] + LINK + s[j+len(anchor):]
    open(f, "w", encoding="utf-8").write(s); n += 1
print("nav_longevity: added to", n, "page(s)")
