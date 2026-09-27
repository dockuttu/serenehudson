# -*- coding: utf-8 -*-
# tech_logos.py — device & brand logos (Alma, Allergan, InMode, Biote, Obagi, SKNLAB): "Our technology" strip (home + service pages) and per-page "Powered by" badge.
# Usage: exec(open("tech_logos.py").read()) in common.py / gen_pages.py. Logos live in /img/logos/*-dark.png.
LOGO_H = {"alma":34, "harmony-bio-boost":58, "alma-hybrid":30, "soprano-ice-platinum":44, "opus-plasma":38, "alma-ted":32, "alma-duo":50, "botox-cosmetic":58, "juvederm":26, "skinvive":24, "kybella":40, "diamondglow":22, "alle":44, "app-platinum":76, "morpheus8":22, "morpheus8v":22, "formav":30, "empowerrf":56, "biote":38, "obagi":40, "m8-verified":76, "evolvex":58, "ignite":58, "optimasmax":50, "lumecca-peak":30, "fusion":20, "bodytite":28, "facetite":28, "accutite":28, "quantumrf":22, "quantumrf10":22, "morpheus8-burst":22, "morpheus8-burst-deep":22, "evolvex-ttt":14}
LOGO_ALT = {"alma":"Alma", "harmony-bio-boost":"Alma Harmony Bio-Boost", "alma-hybrid":"Alma Hybrid", "soprano-ice-platinum":"Alma Soprano ICE Platinum",
            "opus-plasma":"Opus Plasma", "alma-ted":"Alma TED", "alma-duo":"Alma Duo", "botox-cosmetic":"BOTOX Cosmetic (onabotulinumtoxinA) injection", "juvederm":"Juvéderm Collection of Fillers", "skinvive":"SKINVIVE by Juvéderm", "kybella":"KYBELLA (deoxycholic acid) injection", "diamondglow":"DiamondGlow", "alle":"Allē rewards", "app-platinum":"Allergan Partner Privileges — Platinum Partner 2026", "morpheus8":"Morpheus8 by InMode", "morpheus8v":"Morpheus8V by InMode", "formav":"FormaV by InMode", "empowerrf":"EmpowerRF by InMode", "biote":"Biote hormone optimization", "obagi":"Obagi Medical", "m8-verified":"InMode Morpheus8 Verified Provider", "evolvex":"EvolveX by InMode", "ignite":"IgniteRF by InMode", "optimasmax":"OptimasMAX by InMode", "lumecca-peak":"Lumecca Peak IPL by InMode", "fusion":"Fusion Light and Fusion Dark hair removal by InMode", "bodytite":"BodyTite by InMode", "facetite":"FaceTite by InMode", "accutite":"AccuTite by InMode", "quantumrf":"QuantumRF 25 by InMode", "quantumrf10":"QuantumRF 10 by InMode", "morpheus8-burst":"Morpheus8 Burst by InMode", "morpheus8-burst-deep":"Morpheus8 Burst Deep by InMode", "evolvex-ttt":"EvolveX Tite, Tone and Transform"}
LOGO_PAGE = {"harmony-bio-boost":"/harmony-bio-boost/", "alma-hybrid":"/alma-hybrid/", "soprano-ice-platinum":"/laser-hair-removal/",
             "opus-plasma":"/opus-plasma/", "alma-ted":"/alma-ted/", "alma-duo":"/alma-duo/", "botox-cosmetic":"/botox/", "juvederm":"/fillers/", "skinvive":"/skinvive/", "kybella":"/kybella/", "diamondglow":"/diamondglow/", "alle":"https://alle.com/", "morpheus8":"/morpheus8/", "morpheus8v":"/morpheus8v/", "formav":"/formav/", "empowerrf":"/empowerrf/", "biote":"/hormone-optimization/", "obagi":"/obagi/", "evolvex":"/evolve-x/", "ignite":"/bodytite/", "optimasmax":"/lumecca/", "lumecca-peak":"/lumecca/", "fusion":"/laser-hair-removal/", "bodytite":"/bodytite/", "facetite":"/facetite/", "accutite":"/accutite/", "quantumrf":"/quantumrf/", "quantumrf10":"/quantumrf/", "morpheus8-burst":"/morpheus8/", "morpheus8-burst-deep":"/morpheus8/", "evolvex-ttt":"/evolve-x/"}

LOGO_DIM = {"alma":(1400,338), "harmony-bio-boost":(1092,740), "alma-hybrid":(1400,218), "soprano-ice-platinum":(1400,428),
            "opus-plasma":(1206,324), "alma-ted":(1400,269), "alma-duo":(592,283), "botox-cosmetic":(1200,578), "juvederm":(1400,146), "skinvive":(1400,121), "kybella":(1400,393), "diamondglow":(1400,118), "alle":(1400,666), "app-platinum":(230,442), "morpheus8":(1400,146), "morpheus8v":(1400,133), "formav":(1152,181), "empowerrf":(1022,565), "biote":(1007,434), "obagi":(600,256), "m8-verified":(435,440), "evolvex":(742,564), "ignite":(1400,1048), "optimasmax":(1400,568), "lumecca-peak":(1400,300), "fusion":(1400,141), "bodytite":(1119,207), "facetite":(1055,200), "accutite":(1138,207), "quantumrf":(1400,151), "quantumrf10":(1400,151), "morpheus8-burst":(1400,163), "morpheus8-burst-deep":(1400,161), "evolvex-ttt":(1400,77)}  # intrinsic px of *-dark.png

LOGO_SRC = {"app-platinum":"/img/badges/allergan-app-platinum-2026.png", "m8-verified":"/img/badges/inmode-morpheus8-verified.png"}
BADGE_LABEL = {"botox-cosmetic":"Allergan Platinum Partner", "juvederm":"Allergan Platinum Partner", "skinvive":"Allergan Platinum Partner", "kybella":"Allergan Platinum Partner", "diamondglow":"Allergan Platinum Partner", "biote":"Hormone optimization with", "obagi":"Medical-grade skincare by"}

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
SEALS = {"app-platinum": SEAL_IMG,
         "m8-verified": '<img class="hero-seal hex" src="/img/badges/inmode-morpheus8-verified.png" alt="InMode Morpheus8 Verified Provider" width="435" height="440">'}
def hero_seal(slug, device_map):
    """Seal hung over the hero image: Allergan Platinum ribbon or InMode Morpheus8 Verified Provider hexagon."""
    for k in (device_map.get(slug) or []):
        if k in SEALS: return SEALS[k]
    return ""

def device_badge(slug, device_map):
    """'Powered by' badge under the hero copy. device_map: {slug: [logo keys]}"""
    keys = [k for k in (device_map.get(slug) or []) if k not in SEALS]
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
.svc-hero-media .hero-seal.hex{top:14px;height:150px;box-shadow:none;border-radius:0;object-fit:contain}
@media(max-width:560px){.svc-hero-media .hero-seal{height:120px;right:12px}.svc-hero-media .hero-seal.hex{height:92px;top:10px}.tech-row{gap:14px 26px}.tech-row img{max-height:30px}.device-badge{flex-wrap:wrap;gap:10px}.device-badge img{max-height:34px}}
'''
