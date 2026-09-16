# -*- coding: utf-8 -*-
# home_merz.py — idempotent: Merz Aesthetics ELITE+ provider status on the homepage
# (hero chip + partner row; replaces the older Bronze Preferred badge there). Identical in both repos.
import sys, os
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "index.html")
s = open(f, encoding="utf-8").read(); o = s
IMG = "/img/badges/merz-elite-plus.png"
T = "Merz Aesthetics ELITE+ Provider"
HERO = ('<a class="hero-merz" href="/xperience-rewards/" title="%s">'
        '<img src="%s" alt="%s" width="64" height="64">'
        '<span><b>Merz Aesthetics ELITE+ Provider</b><small>Top-tier status &middot; Xeomin, Radiesse &amp; Ultherapy</small></span></a>'
        '<style>.hero-merz{display:inline-flex;align-items:center;gap:14px;margin:12px 0 0 10px;padding:8px 18px 8px 8px;background:rgba(255,255,255,.85);border:1px solid rgba(31,42,92,.15);border-radius:999px;text-decoration:none;box-shadow:0 8px 24px rgba(31,42,92,.08);vertical-align:middle}'
        '.hero-merz img{width:56px;height:56px;display:block}.hero-merz b{display:block;color:var(--ink);font-size:1.02rem}'
        '.hero-merz small{display:block;color:var(--ink);opacity:.85;font-size:.9rem;font-weight:500}'
        '@media(max-width:600px){.hero-merz{margin-left:0}}</style>') % (T, IMG, T)
if 'class="hero-merz"' not in s:
    i = s.find('<a class="hero-obagi"')
    if i == -1:
        i = s.find('<a class="hero-biote"')
    if i != -1:
        j = s.find('</style>', i) + len('</style>')
        s = s[:j] + "\n    " + HERO + s[j:]
NEW = ('<a href="/xperience-rewards/" title="%s"><img src="%s" alt="%s" class="badge-round" loading="lazy" width="260" height="260"></a>' % (T, IMG, T))
pi = s.find('<div class="partners'); pe = s.find('</div>', pi) if pi != -1 else -1
if pi != -1 and IMG not in s[pi:pe]:
    a = s.find('<span title="Merz Aesthetics Bronze Preferred Partner">', pi)
    if a != -1 and a < pe:
        b = s.find('</span>', a) + len('</span>')
        s = s[:a] + NEW + s[b:]
    else:
        s = s[:pe] + "  " + NEW + "\n    " + s[pe:]
if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("home_merz:", "updated" if s != o else "already present")
