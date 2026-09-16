# -*- coding: utf-8 -*-
# home_badges.py — idempotent: Biote Certified Provider badge in the homepage hero + partner row.
import sys, os
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "index.html")
s = open(f, encoding="utf-8").read()
o = s
IMG = "/img/badges/biote-certified-provider.webp"
HERO = ('<a class="hero-biote" href="/hormone-optimization/" title="Biote Certified Provider">'
        '<img src="%s" alt="Biote Certified Provider" width="84" height="84">'
        '<span><b>Biote Certified Provider</b><small>Physician-led hormone optimization &amp; wellness labs</small></span></a>'
        '<style>.hero-biote{display:inline-flex;align-items:center;gap:14px;margin-top:22px;padding:10px 18px 10px 10px;background:rgba(255,255,255,.85);border:1px solid rgba(63,43,61,.12);border-radius:999px;text-decoration:none;box-shadow:0 8px 24px rgba(63,43,61,.08)}'
        '.hero-biote img{width:64px;height:64px;display:block}.hero-biote b{display:block;color:var(--ink);font-size:1.02rem}'
        '.hero-biote small{display:block;color:var(--ink);opacity:.8;font-size:.9rem;font-weight:500}</style>') % IMG
if 'class="hero-biote"' not in s:
    i = s.find('<div class="hero-chips">')
    if i != -1:
        j = s.find('</div>', i) + len('</div>')
        s = s[:j] + "\n    " + HERO + s[j:]
pi = s.find('<div class="partners')
pe = s.find('</div>', pi) if pi != -1 else -1
if pi != -1 and IMG not in s[pi:pe]:
    k = s.find('<span title="Allergan Partner Privileges', pi)
    if k != -1 and k < pe:
        s = s[:k] + ('<a href="/hormone-optimization/" title="Biote Certified Provider"><img src="%s" alt="Biote Certified Provider" class="badge-round" loading="lazy"></a>\n      ' % IMG) + s[k:]
if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("home_badges:", "updated" if s != o else "already present")
