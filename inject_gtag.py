#!/usr/bin/env python3
"""inject_gtag.py — add the Google Ads tag (AW-788907512) + booking/call click
conversion events to every HTML page in bundle/site/. Idempotent: pages that
already carry the marker are skipped. Run after all builders (see build.sh).

Conversion "Booking click" (Google Ads › Goals) fires when a visitor clicks any
link to booking.mangomint.com. tel: clicks send a plain 'call_click' event so we
can add a call conversion later without touching the site again.
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
MARK = "<!-- gads-tag -->"
TAG = """<!-- gads-tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-788907512"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());gtag('config','AW-788907512');
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('booking.mangomint.com')>-1){gtag('event','conversion',{'send_to':'AW-788907512/lQdCCL31zvUcEPiLl_gC'});}
else if(h.indexOf('tel:')===0){gtag('event','call_click',{'send_to':'AW-788907512'});}},true);
</script>
"""

n = 0; skipped = 0
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".html"):
            continue
        p = os.path.join(dp, f)
        s = open(p, encoding="utf-8").read()
        if MARK in s:
            skipped += 1; continue
        m = re.search(r"<head[^>]*>", s, re.I)
        if not m:
            continue
        s = s[:m.end()] + "\n" + TAG + s[m.end():]
        open(p, "w", encoding="utf-8").write(s)
        n += 1
print(f"inject_gtag: tagged {n} pages, {skipped} already tagged")
