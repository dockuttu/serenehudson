# -*- coding: utf-8 -*-
# tech_logos.py — Alma device logos: "Our technology" strip (home + service pages) and per-page "Powered by" badge.
# Usage: exec(open("tech_logos.py").read()) in common.py / gen_pages.py. Logos live in /img/logos/*-dark.png.
LOGO_H = {"alma":34, "harmony-bio-boost":58, "alma-hybrid":30, "soprano-ice-platinum":44, "opus-plasma":38, "alma-ted":32, "alma-duo":50}
LOGO_ALT = {"alma":"Alma", "harmony-bio-boost":"Alma Harmony Bio-Boost", "alma-hybrid":"Alma Hybrid", "soprano-ice-platinum":"Alma Soprano ICE Platinum",
            "opus-plasma":"Opus Plasma", "alma-ted":"Alma TED", "alma-duo":"Alma Duo"}
LOGO_PAGE = {"harmony-bio-boost":"/harmony-bio-boost/", "alma-hybrid":"/alma-hybrid/", "soprano-ice-platinum":"/laser-hair-removal/",
             "opus-plasma":"/opus-plasma/", "alma-ted":"/alma-ted/", "alma-duo":"/alma-duo/"}

LOGO_DIM = {"alma":(1400,338), "harmony-bio-boost":(1092,740), "alma-hybrid":(1400,218), "soprano-ice-platinum":(1400,428),
            "opus-plasma":(1206,324), "alma-ted":(1400,269), "alma-duo":(592,283)}  # intrinsic px of *-dark.png

def _logo_img(key, h=None, lazy=True):
    h = h or LOGO_H[key]; W, H = LOGO_DIM[key]; w = int(round(W * h / float(H)))
    return '<img src="/img/logos/%s-dark.png" alt="%s" width="%d" height="%d"%s>' % (key, LOGO_ALT[key], w, h, ' loading="lazy"' if lazy else '')

def tech_strip(keys):
    """Logo row for the home page / stats band. keys: list of logo keys present at this location (alma first)."""
    items = []
    for k in keys:
        img = _logo_img(k)
        items.append('<a href="%s" title="%s">%s</a>' % (LOGO_PAGE[k], LOGO_ALT[k], img) if k in LOGO_PAGE else '<span title="%s">%s</span>' % (LOGO_ALT[k], img))
    return '''<div class="tech reveal">
      <div class="tech-label">Our Technology</div>
      <div class="tech-row">%s</div>
    </div>''' % "\n        ".join(items)

def device_badge(slug, device_map):
    """'Powered by' badge under the hero copy. device_map: {slug: [logo keys]}"""
    keys = device_map.get(slug)
    if not keys: return ""
    imgs = []
    for k in keys:
        img = _logo_img(k, lazy=False)
        imgs.append(img if LOGO_PAGE.get(k) == "/%s/" % slug else '<a href="%s" title="%s">%s</a>' % (LOGO_PAGE.get(k, "#"), LOGO_ALT[k], img))
    return '<div class="device-badge"><span>Powered by</span>%s</div>' % "".join(imgs)

TECH_CSS = '''
/* Alma technology logos */
.tech{margin-top:30px;padding-top:26px;border-top:1px solid var(--blush-deep);text-align:center}
.tech-label{font-family:'Jost',sans-serif;font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:16px}
.tech-row{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:18px 44px;max-width:860px;margin:0 auto}
.tech-row img{width:auto;display:block;opacity:.88;transition:opacity .3s}
.tech-row a:hover img{opacity:1}
.device-badge{display:flex;width:fit-content;align-items:center;gap:14px;margin:-6px 0 24px;padding:10px 16px;border:1px solid var(--blush-deep);border-radius:999px;background:#fff}
.device-badge span{font-family:'Jost',sans-serif;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.device-badge img{width:auto;display:block}
.device-badge a{display:block}
@media(max-width:560px){.tech-row{gap:14px 26px}.tech-row img{max-height:30px}.device-badge{flex-wrap:wrap;gap:10px}.device-badge img{max-height:34px}}
'''
