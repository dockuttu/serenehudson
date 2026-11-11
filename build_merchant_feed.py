# -*- coding: utf-8 -*-
# build_merchant_feed.py — Google Merchant Center files for the Obagi "reserve online, pay & pick up in store" shop.
# Writes (Hudson site only; one set of files covers both offices):
#   bundle/site/merchant/obagi-products.xml        primary product source (in-store products)
#   bundle/site/merchant/obagi-local-inventory.tsv local inventory source (stock + price at each office)
# Merchant Center fetches both URLs on a schedule. Prices, names and images come from shop_obagi_data.py,
# so a price change in that file reaches Google on the next fetch.
import os, re, html as _h
from xml.sax.saxutils import escape as xesc

ns = {}
exec(open("shop_obagi_data.py", encoding="utf-8").read(), ns)
PRODUCTS = [p for p in ns["PRODUCTS"] if not p["rx"] and p.get("price")]

HUDSON_SITE = "https://hudson.serenemedspas.com"
# Store codes must match the store code on each Google Business Profile listing.
STORES = {"serene-hudson": "Hudson, OH", "serene-barboursville": "Barboursville, WV"}
OUT = os.path.join("bundle", "site", "merchant")
os.makedirs(OUT, exist_ok=True)

def clean(s):
    s = _h.unescape(re.sub(r"<[^>]+>", "", s or ""))
    return re.sub(r"[®™]", "", s).replace("  ", " ").strip()

def pid(p):  # same IDs Google already uses for these products
    return "obagi-" + p["slug"]

def img(p):
    return "%s/img/obagi/%s.webp" % (HUDSON_SITE, p["img"]) if p["img"] else ""

items = []
for p in PRODUCTS:
    url = "%s/shop/%s/" % (HUDSON_SITE, p["slug"])
    title = clean(p["name"])
    if p.get("size") and p["size"].lower() not in title.lower():
        title = "%s, %s" % (title, p["size"])
    desc = clean(p["blurb"]) + " Reserve online and pay when you pick it up at Serene Med Spa in Hudson, OH or Barboursville, WV."
    f = [
        ("g:id", pid(p)),
        ("g:title", title[:150]),
        ("g:description", desc[:5000]),
        ("g:link", url),
        ("g:link_template", url + "?store={store_code}"),
        ("g:image_link", img(p)),
        ("g:brand", "Obagi"),
        ("g:condition", "new"),
        ("g:price", "%.2f USD" % float(p["price"])),
        ("g:availability", "in_stock"),
        ("g:google_product_category", "567"),  # Health & Beauty > Personal Care > Cosmetics > Skin Care
        ("g:product_type", "Skin Care > Obagi > " + clean(dict((k, n) for k, n, d in ns["COLLECTIONS"])[p["collection"]])),
        ("g:size", p.get("size") or ""),
        ("g:pickup_method", "reserve"),
        ("g:pickup_sla", "next_day"),
    ]
    items.append("<item>\n" + "\n".join("  <%s>%s</%s>" % (k, xesc(v), k) for k, v in f if v) + "\n</item>")

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n<channel>\n'
       '<title>Serene Med Spa - Obagi (reserve online, pick up in store)</title>\n'
       '<link>%s/shop/</link>\n<description>Obagi products available for in-store pickup at Serene Med Spa Hudson, OH and Barboursville, WV.</description>\n'
       % HUDSON_SITE + "\n".join(items) + "\n</channel>\n</rss>\n")
open(os.path.join(OUT, "obagi-products.xml"), "w", encoding="utf-8").write(xml)

rows = ["store_code\tid\tavailability\tprice\tpickup_method\tpickup_sla"]
for code in STORES:
    for p in PRODUCTS:
        rows.append("\t".join([code, pid(p), "in_stock", "%.2f USD" % float(p["price"]), "reserve", "next_day"]))
open(os.path.join(OUT, "obagi-local-inventory.tsv"), "w", encoding="utf-8").write("\n".join(rows) + "\n")

print("merchant feed: %d products, %d store rows" % (len(PRODUCTS), len(rows) - 1))
