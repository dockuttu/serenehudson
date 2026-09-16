# -*- coding: utf-8 -*-
# easypay_inject.py — idempotent post-build pass (identical in both repos):
#   * replaces the old "flexible financing" band with the Cherry + CareCredit Easy Pay band,
#     or adds the band just above the consultation form on pages that don't have one
#   * adds "Easy Pay" to the top nav (after Pricing) and "Easy Pay Financing" to the footer
import glob, re, sys, os
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
ns = {}
exec(open("easypay.py", encoding="utf-8").read(), ns)
BAND = ns["ep_band"]()
SKIP = {"thank-you", "404"}
OLD = re.compile(r'<div class="finance"><div class="wrap reveal">.*?</div></div>', re.S)
OLD_BAND = re.compile(r'<section class="ep-band".*?</section>', re.S)
NAV_PRICING = re.compile(r'(<li><a href="/pricing/">[^<]*</a></li>)')
counts = {"band": 0, "nav": 0, "footer": 0}
for f in glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True):
    rel = os.path.relpath(f, SITE)
    top = rel.split(os.sep)[0].replace(".html", "")
    s = open(f, encoding="utf-8").read()
    o = s
    # nav link (first Pricing item = header nav)
    head_end = s.find("</header>")
    if head_end != -1 and 'href="/easy-pay/">Easy Pay</a>' not in s[:head_end]:
        m = NAV_PRICING.search(s, 0, head_end)
        if m:
            s = s[:m.end()] + '<li><a href="/easy-pay/">Easy Pay</a></li>' + s[m.end():]
            counts["nav"] += 1
    # footer link
    fi = s.find("<footer")
    if fi != -1 and 'href="/easy-pay/"' not in s[fi:]:
        k = -1
        for anchor in ('Book Now</a></li>', 'Book Online</a></li>'):
            k = s.find(anchor, fi)
            if k != -1:
                k += len(anchor)
                break
        if k != -1:
            s = s[:k] + '\n          <li><a href="/easy-pay/">Easy Pay Financing</a></li>' + s[k:]
            counts["footer"] += 1
    # band
    if top not in SKIP and 'data-ep-page="1"' not in s:
        if OLD_BAND.search(s):
            s = OLD_BAND.sub(lambda _: BAND, s, count=1)          # refresh (links may have changed)
        elif OLD.search(s):
            s = OLD.sub(lambda _: BAND, s, count=1)
        else:
            i = s.find('<section class="consult"')
            if i == -1:
                i = s.find("<footer")
            if i != -1:
                s = s[:i] + BAND + "\n\n" + s[i:]
        s = OLD.sub("", s)   # drop any leftover old bands
    if s != o:
        open(f, "w", encoding="utf-8").write(s)
        if "ep-band" in s: counts["band"] += 1
print("easypay_inject: %(band)d pages with band, nav +%(nav)d, footer +%(footer)d" % counts)
