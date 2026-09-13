#!/usr/bin/env python3
"""inject_meta_pixel.py — add the Meta (Facebook) pixel to every HTML page in
bundle/site/. Idempotent: pages already carrying the marker are skipped.
Run after inject_gtag.py (see build.sh).

Events:
  PageView  — every page
  Lead      — whenever the site fires gtag('event','generate_lead') (Zoho consult
              form, New-Client popup) — we watch dataLayer pushes so the forms
              need no changes; also fired on /thank-you/ as a fallback
  Schedule  — click on any booking.mangomint.com link
  Contact   — click on any tel: link
No personal data is sent; standard pixel only.
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
PIXEL_ID = "475660982946848"
MARK = "<!-- meta-pixel -->"
TAG = """<!-- meta-pixel -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','%(id)s');fbq('track','PageView');
(function(){var dl=window.dataLayer=window.dataLayer||[];var op=dl.push.bind(dl);dl.push=function(){try{var a=arguments[0];if(a&&a[0]==='event'&&a[1]==='generate_lead'){fbq('track','Lead');}}catch(e){}return op.apply(null,arguments);};
if(/^\\/thank-you\\/?$/.test(location.pathname)){fbq('track','Lead');}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('booking.mangomint.com')>-1){fbq('track','Schedule');}else if(h.indexOf('tel:')===0){fbq('track','Contact');}},true);})();
</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=%(id)s&ev=PageView&noscript=1"></noscript>
""" % {"id": PIXEL_ID}

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
print(f"inject_meta_pixel: tagged {n} pages, {skipped} already tagged")
