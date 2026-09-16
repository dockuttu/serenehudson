# -*- coding: utf-8 -*-
# shop_inject.py — idempotent post-build pass (identical in both repos):
#   * loads /shop.js (cart button + cart count) on every page
#   * makes sure the header nav has a "Shop" link and the footer has "Shop Obagi Skincare"
import glob, os, re, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
try:
    V = open(".shopjs_version").read().strip()
except OSError:
    V = "1"
TAG = '<script src="/shop.js?v=%s" defer></script>' % V
OLD = re.compile(r'<script src="/shop\.js\?v=[^"]*" defer></script>')
SKIP_DIRS = ("/lp/", "/medical-weight-loss/")
c = {"js": 0, "nav": 0, "foot": 0}
for f in glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True):
    if any(s in f.replace(os.sep, "/") for s in SKIP_DIRS):
        continue
    s = open(f, encoding="utf-8").read()
    o = s
    if TAG not in s:
        if OLD.search(s):
            s = OLD.sub(TAG, s)
        elif "</body>" in s:
            s = s.replace("</body>", TAG + "\n</body>", 1)
        c["js"] += s != o
    he = s.find("</header>")
    if he != -1 and 'href="/shop/"' not in s[:he]:
        for anchor in ('<li><a href="/easy-pay/">Easy Pay</a></li>', '<li><a href="/pricing/">Pricing</a></li>'):
            k = s.find(anchor, 0, he)
            if k != -1:
                k += len(anchor)
                s = s[:k] + '<li><a href="/shop/">Shop</a></li>' + s[k:]
                c["nav"] += 1
                break
    fi = s.find("<footer")
    if fi != -1 and "Shop Obagi Skincare" not in s[fi:]:
        k = s.find("Easy Pay Financing</a></li>", fi)
        if k != -1:
            k += len("Easy Pay Financing</a></li>")
            s = s[:k] + '\n          <li><a href="/shop/">Shop Obagi Skincare</a></li>' + s[k:]
            c["foot"] += 1
    if s != o:
        open(f, "w", encoding="utf-8").write(s)
print("shop_inject:", c)
