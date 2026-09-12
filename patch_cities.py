# patch_cities.py — wire nearby-city pages into a site repo (run from the repo root).
# - common.py: CITY_LINKS, AREA_TOWNS additions, areas_section() links + id="areas", footer "Areas we serve" line
# - styles.css: .area-tags a + .foot-areas
# - build.sh: run build_cities.py after gen_pages.py
# - home page: link the area tags (Hudson: bundle/site/index.html; BV: templates/home.html)
import re, sys, os
site = sys.argv[1]  # hudson | bv
if site == "hudson":
    CITY_LINKS = [("Akron","/med-spa-akron-oh/"),("Stow","/med-spa-stow-oh/"),("Cuyahoga Falls","/med-spa-cuyahoga-falls-oh/"),("Twinsburg","/med-spa-twinsburg-oh/"),("Solon","/med-spa-solon-oh/"),("Aurora","/med-spa-aurora-oh/")]
    add_towns = ["Akron","Solon"]
    home = "bundle/site/index.html"
else:
    CITY_LINKS = [("Huntington","/med-spa-huntington-wv/"),("Ashland, KY","/med-spa-ashland-ky/"),("Ironton, OH","/med-spa-ironton-oh/"),("Charleston","/med-spa-charleston-wv/")]
    add_towns = ["Charleston"]
    home = "templates/home.html"

def rw(p, fn):
    s = open(p, encoding="utf-8").read(); n = fn(s)
    if n != s: open(p, "w", encoding="utf-8").write(n); print("patched", p)
    else: print("unchanged", p)

# ---- common.py
def patch_common(s):
    if "CITY_LINKS" in s: return s
    # AREA_TOWNS additions
    m = re.search(r'AREA_TOWNS = \[(.*?)\]', s)
    towns = m.group(1)
    for t in add_towns:
        if '"%s"' % t not in towns: towns = towns + ', "%s"' % t
    s = s[:m.start(1)] + towns + s[m.end(1):]
    links = "CITY_LINKS = {%s}\n" % ", ".join('"%s":"%s"' % kv for kv in CITY_LINKS)
    s = s.replace("AREA_SERVED = (", links + "def _area_tag(t):\n    return ('<a href=\"%s\">%s</a>' % (CITY_LINKS[t], t)) if t in CITY_LINKS else ('<span>%s</span>' % t)\nAREA_SERVED = (", 1)
    s = s.replace("tags = \"\".join('<span>%s</span>' % t for t in AREA_TOWNS)", "tags = \"\".join(_area_tag(t) for t in AREA_TOWNS)")
    s = s.replace("return '''<section class=\"areas\">", "return '''<section class=\"areas\" id=\"areas\">", 1)
    # footer areas line
    foot = '    <div class="foot-areas">Areas we serve: %s</div>\n    <div class="foot-bottom">' % " &middot; ".join('<a href="%s">%s</a>' % (u, n) for n, u in CITY_LINKS)
    s = s.replace('    <div class="foot-bottom">', foot, 1)
    return s
rw("common.py", patch_common)

# ---- styles.css
def patch_css(s):
    if ".foot-areas" in s: return s
    return s + "\n.area-tags a{background:#fff;border:1px solid var(--blush-deep);color:var(--plum);border-radius:30px;padding:8px 18px;font-size:.82rem;letter-spacing:.02em;text-decoration:none;font-weight:500;transition:.2s}.area-tags a:hover{background:var(--plum);color:#fff;border-color:var(--plum)}\n.foot-areas{font-size:.82rem;color:rgba(255,255,255,.7);padding:18px 0 4px;text-align:center}.foot-areas a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35)}.foot-areas a:hover{border-color:#fff}\n"
rw("bundle/site/styles.css", patch_css)

# ---- build.sh
def patch_build(s):
    if "build_cities" in s: return s
    return s.replace("python3 gen_pages.py\n", "python3 gen_pages.py\npython3 build_cities.py\n", 1)
rw("build.sh", patch_build)

# ---- home page area tags
def patch_home(s):
    if 'class="areas" id="areas"' in s and "med-spa-" in s: return s
    s = s.replace('<section class="areas">', '<section class="areas" id="areas">', 1)
    m = re.search(r'<div class="area-tags">(.*?)</div>', s, re.S)
    if not m: print("!! no area-tags on home"); return s
    inner = m.group(1)
    for name, url in CITY_LINKS:
        span = "<span>%s</span>" % name
        link = '<a href="%s">%s</a>' % (url, name)
        if span in inner: inner = inner.replace(span, link)
        elif link not in inner: inner = inner + link
    return s[:m.start(1)] + inner + s[m.end(1):]
rw(home, patch_home)
