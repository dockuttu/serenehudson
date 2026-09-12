# -*- coding: utf-8 -*-
# tech_logos.py — Alma device logos: "Our technology" strip (home + service pages) and per-page "Powered by" badge.
# Usage: exec(open("tech_logos.py").read()) in common.py / gen_pages.py. Logos live in /img/logos/*-dark.png.
LOGO_H = {"alma":34, "harmony-bio-boost":58, "alma-hybrid":30, "soprano-ice-platinum":44, "opus-plasma":38, "alma-ted":32, "alma-duo":50, "botox-cosmetic":58, "juvederm":26, "skinvive":24, "kybella":40, "diamondglow":22, "alle":44, "app-platinum":76}
LOGO_ALT = {"alma":"Alma", "harmony-bio-boost":"Alma Harmony Bio-Boost", "alma-hybrid":"Alma Hybrid", "soprano-ice-platinum":"Alma Soprano ICE Platinum",
            "opus-plasma":"Opus Plasma", "alma-ted":"Alma TED", "alma-duo":"Alma Duo", "botox-cosmetic":"BOTOX Cosmetic (onabotulinumtoxinA) injection", "juvederm":"Juvéderm Collection of Fillers", "skinvive":"SKINVIVE by Juvéderm", "kybella":"KYBELLA (deoxycholic acid) injection", "diamondglow":"DiamondGlow", "alle":"Allē rewards", "app-platinum":"Allergan Partner Privileges — Platinum Partner 2026"}
LOGO_PAGE = {"harmony-bio-boost":"/harmony-bio-boost/", "alma-hybrid":"/alma-hybrid/", "soprano-ice-platinum":"/laser-hair-removal/",
             "opus-plasma":"/opus-plasma/", "alma-ted":"/alma-ted/", "alma-duo":"/alma-duo/", "botox-cosmetic":"/botox/", "juvederm":"/fillers/", "skinvive":"/skinvive/", "kybella":"/kybella/", "diamondglow":"/diamondglow/", "alle":"https://alle.com/"}

LOGO_DIM = {"alma":(1400,338), "harmony-bio-boost":(1092,740), "alma-hybrid":(1400,218), "soprano-ice-platinum":(1400,428),
            "opus-plasma":(1206,324), "alma-ted":(1400,269), "alma-duo":(592,283), "botox-cosmetic":(1200,578), "juvederm":(1400,146), "skinvive":(1400,121), "kybella":(1400,393), "diamondglow":(1400,118), "alle":(1400,666), "app-platinum":(230,442)}  # intrinsic px of *-dark.png

LOGO_SRC = {"app-platinum":"/img/badges/allergan-app-platinum-2026.png"}
BADGE_LABEL = {"botox-cosmetic":"Allergan Platinum Partner", "juvederm":"Allergan Platinum Partner", "skinvive":"Allergan Platinum Partner", "kybella":"Allergan Platinum Partner", "diamondglow":"Allergan Platinum Partner"}

def _logo_img(key, h=None, lazy=True):
    h = h or LOGO_H[key]; W, H = LOGO_DIM[key]; w = int(round(W * h / float(H)))
    src = LOGO_SRC.get(key, "/img/logos/%s-dark.png" % key)
    return '<img src="%s" alt="%s" width="%d" height="%d"%s>' % (src, LOGO_ALT[key], w, h, ' loading="lazy"' if lazy else '')

def tech_strip(keys, label="Our Technology"):
    """Logo row for the home page / stats band. keys: list of logo keys present at this location (alma first)."""
    items = []
    for k in keys:
        img = _logo_img(k)
        items.append('<a href="%s" title="%s"%s>%s</a>' % (LOGO_PAGE[k], LOGO_ALT[k], ' target="_blank" rel="noopener"' if LOGO_PAGE[k].startswith("http") else "", img) if k in LOGO_PAGE else '<span title="%s">%s</span>' % (LOGO_ALT[k], img))
    return '''<div class="tech reveal">
      <div class="tech-label">%s</div>
      <div class="tech-row">%s</div>
    </div>''' % (label, "\n        ".join(items))

SEAL_IMG = '<img class="hero-seal" src="/img/badges/allergan-app-platinum-2026.png" alt="Allergan Partner Privileges — Platinum Partner 2026" width="230" height="442">'
def hero_seal(slug, device_map):
    """Platinum ribbon hung over the hero image on Allergan pages."""
    return SEAL_IMG if "app-platinum" in (device_map.get(slug) or []) else ""

def device_badge(slug, device_map):
    """'Powered by' badge under the hero copy. device_map: {slug: [logo keys]}"""
    keys = [k for k in (device_map.get(slug) or []) if k != "app-platinum"]
    if not keys: return ""
    imgs = []
    for k in keys:
        img = _logo_img(k, lazy=False)
        imgs.append(img if (k not in LOGO_PAGE or LOGO_PAGE[k] == "/%s/" % slug) else '<a href="%s" title="%s">%s</a>' % (LOGO_PAGE[k], LOGO_ALT[k], img))
    label = BADGE_LABEL.get(keys[0], "Powered by")
    return '<div class="device-badge"><span>%s</span>%s</div>' % (label, "".join(imgs))

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
.svc-hero-media .hero-seal{position:absolute;top:-10px;right:22px;height:200px;width:auto;filter:drop-shadow(0 10px 18px rgba(63,43,61,.22));z-index:2}
@media(max-width:560px){.svc-hero-media .hero-seal{height:120px;right:12px}.tech-row{gap:14px 26px}.tech-row img{max-height:30px}.device-badge{flex-wrap:wrap;gap:10px}.device-badge img{max-height:34px}}
'''
