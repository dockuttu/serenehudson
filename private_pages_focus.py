#!/usr/bin/env python3
"""private_pages_focus.py — Nov 10 2026 (Robin OK'd). The women's intimate-wellness pages (EmpowerRF, VTone, FormaV,
Morpheus8V) had an 86% bounce rate: on a phone the first screen was the November promo banner and an unrelated
Deal of the Day bar, with the page's own topic pushed below the fold. On these four pages only:
  1. hide the promo banner and the Deal of the Day bar,
  2. add one line under the headline: private complimentary consultation, the series price, no surgery / no hormones,
  3. point the phone 'Book Now' bar at the private Sexual Wellness Consultation (Mangomint service 325).
Identical file in both office repos; idempotent. Usage: python3 private_pages_focus.py bundle/site
"""
import os, re, sys

BOOK = "https://booking.mangomint.com/serenemedspa?serviceId=325"
PAGES = {   # slug -> the price part of the line under the headline (prices are the same at both offices)
    "empowerrf": "Series from $1,350",
    "vtone": "6 sessions for $1,500",
    "formav": "3 sessions for $1,350",
    "morpheus8v": "3 sessions for $2,100",
}
MARK = "data-private-focus"
STYLE = ('<style ' + MARK + '>.promo,#dotd-strip{display:none!important}'
         'p.hero-private{font-size:1.1rem!important;font-weight:700!important;color:#10322F!important;margin:8px 0 16px;line-height:1.5}</style>')

def fix(html, price):
    if MARK in html:
        return html, False
    # 1. hide the promo banner + Deal of the Day bar (their scripts un-hide them, so this must win: !important)
    html = html.replace("</head>", STYLE + "</head>", 1)
    # 2. one line under the headline's first paragraph
    line = ('<p class="hero-private">Private, complimentary consultation &middot; ' + price +
            ' &middot; No surgery, no hormones</p>')
    html, n = re.subn(r"(<h1[^>]*>.*?</h1>\s*<p>.*?</p>)", lambda m: m.group(1) + "\n        " + line, html, count=1, flags=re.S)
    if not n:
        print("  !! no headline paragraph found; line not added")
    # 3. phone 'Book Now' bar -> private consultation (drop data-loc-book so the shell script doesn't re-point it)
    html = re.sub(r'<a class="mbar-book" href="[^"]*" data-loc-book>', '<a class="mbar-book" href="' + BOOK + '">', html)
    return html, True

def main(site):
    for slug, price in PAGES.items():
        p = os.path.join(site, slug, "index.html")
        if not os.path.exists(p):
            print("private_pages_focus: missing", p); continue
        s = open(p, encoding="utf-8").read()
        s2, changed = fix(s, price)
        if changed:
            open(p, "w", encoding="utf-8").write(s2)
        print("private_pages_focus:", slug, "updated" if changed else "already done")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bundle/site")
