# -*- coding: utf-8 -*-
# home_obagi.py — idempotent: Obagi "authorized provider" logo on the homepage (hero chip + partner row)
# and an Obagi skincare band with best sellers. Identical in both repos.
import os, sys, json
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "index.html")
s = open(f, encoding="utf-8").read()
o = s
ns = {}
exec(open("shop_obagi_data.py", encoding="utf-8").read(), ns)
BY = ns["BY_SLUG"]
LOGO = "/img/obagi/obagi-medical-logo.webp"

HERO = ('<a class="hero-obagi" href="/obagi/" title="Authorized Obagi Medical Provider">'
        '<img src="%s" alt="Obagi Medical" width="89" height="38">'
        '<span><b>Authorized Obagi Provider</b><small>Our medical-grade skincare line</small></span></a>'
        '<style>.hero-obagi{display:inline-flex;align-items:center;gap:14px;margin:12px 0 0 10px;padding:10px 18px 10px 14px;background:rgba(255,255,255,.85);border:1px solid rgba(31,42,92,.15);border-radius:999px;text-decoration:none;box-shadow:0 8px 24px rgba(31,42,92,.08);vertical-align:middle}'
        '.hero-obagi img{height:38px;width:auto;display:block}.hero-obagi b{display:block;color:#1f2a5c;font-size:1.02rem}'
        '.hero-obagi small{display:block;color:var(--ink);opacity:.85;font-size:.9rem;font-weight:500}'
        '@media(max-width:600px){.hero-obagi{margin-left:0}}</style>') % LOGO
if 'class="hero-obagi"' not in s:
    i = s.find('<a class="hero-biote"')
    if i != -1:
        j = s.find('</style>', i) + len('</style>')
        s = s[:j] + "\n    " + HERO + s[j:]

pi = s.find('<div class="partners')
pe = s.find('</div>', pi) if pi != -1 else -1
if pi != -1 and LOGO not in s[pi:pe]:
    k = s.find('<a href="/hormone-optimization/" title="Biote', pi)
    if k == -1 or k > pe:
        k = pe
    s = s[:k] + ('<a href="/obagi/" title="Authorized Obagi Medical Provider"><img src="%s" alt="Authorized Obagi Medical Provider" style="height:46px;width:auto" loading="lazy"></a>\n      ' % LOGO) + s[k:]

feat = ["professional-c-serum-20", "nu-derm-fx-system-normal-oily", "elastiderm-firming-eye-cream", "hydrate-luxe"]
def mini(p):
    price = ("$%d" % p["price"])
    return (f'<a class="hob-item" href="/shop/{p["slug"]}/"><img loading="lazy" src="/img/obagi/{p["img"]}-400.webp" alt="" width="400" height="400">'
            f'<b>{p["name"]}</b><span>{p["size"]} &middot; {price}</span></a>')
BAND = f'''<section class="hob" id="obagi" aria-label="Obagi Medical skincare">
  <div class="wrap reveal">
    <div class="hob-grid">
      <div class="hob-txt">
        <img src="{LOGO}" alt="Obagi Medical" width="140" height="60" style="height:60px;width:auto">
        <div class="eyebrow" style="margin-top:12px">Authorized Obagi Medical Provider</div>
        <h2>Our Skincare Line: Obagi Medical</h2>
        <p>Medical-grade skincare chosen by our physicians to protect and extend your results. Reserve Obagi online, then pay and pick up at your visit.</p>
        <p><a class="btn" href="/shop/">Shop Obagi</a> &nbsp; <a class="btn btn-outline" href="/obagi/">Why Obagi</a></p>
      </div>
      <div class="hob-items">{"".join(mini(BY[x]) for x in feat)}</div>
    </div>
  </div>
  <style>
  .hob{{padding:64px 0;background:#f3f5fb}}
  .hob-grid{{display:grid;grid-template-columns:1fr 1.3fr;gap:36px;align-items:center}}
  .hob-txt h2{{margin:6px 0 10px}}
  .hob-txt p{{font-size:1.12rem;line-height:1.7;color:var(--ink);font-weight:500}}
  .hob-items{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}}
  .hob-item{{background:#fff;border-radius:16px;overflow:hidden;text-decoration:none;border:1px solid rgba(31,42,92,.12);display:block}}
  .hob-item img{{width:100%;height:auto;display:block;background:#ededed}}
  .hob-item b{{display:block;padding:10px 12px 0;color:var(--ink);font-size:1rem;line-height:1.3}}
  .hob-item span{{display:block;padding:2px 12px 12px;color:#1f2a5c;font-weight:600;font-size:.95rem}}
  @media(min-width:1000px){{.hob-items{{grid-template-columns:repeat(4,1fr)}}}}
  @media(max-width:800px){{.hob-grid{{grid-template-columns:1fr}}}}
  </style>
</section>

'''
if 'class="hob"' not in s:
    k = s.find('<section class="about" id="about">')
    if k != -1:
        s = s[:k] + BAND + s[k:]

if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("home_obagi:", "updated" if s != o else "already present")
