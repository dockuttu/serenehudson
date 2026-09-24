# -*- coding: utf-8 -*-
"""v2_merge.py <site-dir> — FINAL build pass for the Hudson site.

Phase 2 of folding the location sites into serenemedspas.com (Sep 2026):
  * every root-relative URL (/botox/, /img/x.jpg, /shop.js …) becomes /hudson/…
  * https://hudson.serenemedspas.com/… becomes https://serenemedspas.com/hudson/…
    (canonicals, og:url, JSON-LD, sitemap.xml)
  * the Hudson header/promo/footer/mobile bar are swapped for the main site's v2 shell
    (site_lib.NAV / FOOTER from the serenemain repo) and a small v2.css + v2-shell.js are written
    so the pages pick up the v2 design tokens (Poppins / Noto Serif Display, forest green + lavender).

The built tree is then served by the MAIN nginx container at serenemedspas.com/hudson/
(bind mount of /root/hudson, `location /hudson/ { alias … }`), and the
hudson. subdomain only 301s (bundle/nginx.conf).

The serenemain checkout is found via $SERENEMAIN_SRC, else /root/serenemain-src (VPS),
else ../serenemain (Mac).
"""
import os, re, sys, hashlib, glob, json

SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
PREFIX = "/hudson"
OLD_HOST = "https://hudson.serenemedspas.com"
NEW_HOST = "https://serenemedspas.com" + PREFIX
HERE = os.path.dirname(os.path.abspath(__file__))

def find_main():
    cands = [os.environ.get("SERENEMAIN_SRC"), "/root/serenemain-src", os.path.join(os.path.dirname(HERE), "serenemain"),
             "/Volumes/Extreme SSD/serenemain"]
    for c in cands:
        if c and os.path.isfile(os.path.join(c, "site_lib.py")): return c
    sys.exit("v2_merge: serenemain repo not found (set SERENEMAIN_SRC)")

MAIN = find_main()
sys.path.insert(0, MAIN)
import site_lib as SL  # noqa: E402

# ------------------------------------------------------------------ URL prefixing
def pre(u):
    if not u.startswith("/") or u.startswith("//") or u == PREFIX or u.startswith(PREFIX + "/"): return u
    return PREFIX + u

ATTR_RX = re.compile(r'\b(href|src|action|poster|data-src|data-bg|data-href)=(["\'])(/[^"\']*)\2')
SRCSET_RX = re.compile(r'\b(srcset|data-srcset)=(["\'])([^"\']*)\2')
CSSURL_RX = re.compile(r'url\((["\']?)(/[^)"\']+)\1\)')
QUOTED_RX = re.compile(r'''(["'])(/[a-z0-9][^"'\s]*)\1''')
SCRIPT_RX = re.compile(r'(<script(?![^>]*\bsrc=)[^>]*>)(.*?)(</script>)', re.S)
STYLE_RX = re.compile(r'(<style[^>]*>)(.*?)(</style>)', re.S)

def prefix_srcset(v):
    parts = []
    for item in v.split(","):
        item = item.strip()
        if not item: continue
        bits = item.split()
        bits[0] = pre(bits[0])
        parts.append(" ".join(bits))
    return ", ".join(parts)

def prefix_html(s):
    s = ATTR_RX.sub(lambda m: f'{m.group(1)}={m.group(2)}{pre(m.group(3))}{m.group(2)}', s)
    s = SRCSET_RX.sub(lambda m: f'{m.group(1)}={m.group(2)}{prefix_srcset(m.group(3))}{m.group(2)}', s)
    s = CSSURL_RX.sub(lambda m: f'url({m.group(1)}{pre(m.group(2))}{m.group(1)})', s)
    s = SCRIPT_RX.sub(lambda m: m.group(1) + QUOTED_RX.sub(lambda q: f'{q.group(1)}{pre(q.group(2))}{q.group(1)}', m.group(2)) + m.group(3), s)
    s = s.replace(OLD_HOST + "/", NEW_HOST + "/").replace(OLD_HOST, NEW_HOST)
    return s

def prefix_js(s):
    s = QUOTED_RX.sub(lambda q: f'{q.group(1)}{pre(q.group(2))}{q.group(1)}', s)
    return s.replace(OLD_HOST, NEW_HOST)

def prefix_css(s):
    s = CSSURL_RX.sub(lambda m: f'url({m.group(1)}{pre(m.group(2))}{m.group(1)})', s)
    s = s.replace("'Jost'", "'Poppins'").replace("'Cormorant Garamond'", "'Noto Serif Display'")
    return s

# ------------------------------------------------------------------ v2 shell assets
def slice_css(css, start_marker, end_marker):
    a = css.index(start_marker); b = css.index(end_marker, a)
    return css[a:b]


GALLERY_CSS = """
/* Inside our Hudson office — photo mosaic (Sep 23, 2026) */
.hgal{background:#fff;padding:72px 0}
.hgal .section-head{margin-bottom:34px}
.hgal-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:230px;gap:14px;grid-auto-flow:dense}
.hgal-grid figure{margin:0;position:relative;overflow:hidden;border-radius:18px;background:#ECEDF7}
.hgal-grid img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s ease}
.hgal-grid figure:hover img{transform:scale(1.04)}
.hgal-grid figcaption{position:absolute;left:14px;bottom:12px;background:rgba(16,50,47,.82);color:#fff;font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;padding:7px 12px;border-radius:30px}
.hgal-grid .tall{grid-row:span 2}.hgal-grid .wide{grid-column:span 2}
@media (max-width:760px){.hgal{padding:52px 0}.hgal-grid{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:190px;gap:10px}.hgal-grid .tall{grid-row:span 2}.hgal-grid .wide{grid-column:span 2}.hgal-grid figcaption{font-size:.6rem;left:10px;bottom:9px;padding:6px 10px}}
"""

def build_v2_css():
    main = SL.CSS
    header = slice_css(main, "/* promo + header */", "/* hero */")
    footer = slice_css(main, "/* footer */", "/* reveal */")
    # nav/footer lines from the responsive blocks
    resp = []
    for m in re.finditer(r'@media \(max-width:(\d+)px\)\{', main):
        w = m.group(1); i = m.end(); depth = 1
        while depth and i < len(main):
            depth += {"{": 1, "}": -1}.get(main[i], 0); i += 1
        body = main[m.end():i - 1]
        rules = re.findall(r'[^{}]+\{[^{}]*\}', body)
        keep = [r.strip() for r in rules if re.search(r'\.nav|\.menu-toggle|\.locpick|\.mbar|\.promo-more|\.foot-|footer|\.drop|\.newsletter|body\{padding-bottom', r)]
        if keep: resp.append(f"@media (max-width:{w}px){{{''.join(keep)}}}")
    tokens = """
/* v2 tokens mapped onto the Hudson stylesheet's variables */
:root{--rose:#10322F;--rose-deep:#1B4A44;--peach:#3E7F78;--gold:#C9A56B;--mint:#3E7F78;--mint-soft:#ECEDF7;--blush:#F5F7FA;--blush-deep:#E5E7EB;--plum:#10322F;--ink:#121417;--muted:#8E919C;--white:#fff;
  --grad:linear-gradient(120deg,#10322F 0%,#10322F 100%);
  --forest:#10322F;--forest-700:#1B4A44;--forest-500:#3E7F78;--lav:#C4C7E6;--lav-100:#ECEDF7;--grey:#F5F7FA;--rule:#E5E7EB;--ink-soft:#4B5563;--r:20px;--shadow:0 20px 50px -24px rgba(16,50,47,.35);
  --teal-900:#10322F;--teal-700:#1B4A44;--teal-500:#3E7F78;--teal-100:#DDEBE5;--sage:#6F9A8F;--sage-100:#ECEDF7;--sand:#F5F7FA;--paper:#fff}
body{font-family:'Poppins',system-ui,sans-serif;color:#121417}
h1,h2,h3,h4{font-family:'Noto Serif Display',Georgia,serif;font-weight:400;color:#10322F}
h1,h2{text-transform:uppercase;letter-spacing:.035em;line-height:1.08}
.eyebrow{background:none;-webkit-text-fill-color:#10322F;color:#10322F;font-weight:600;letter-spacing:.24em;font-size:.68rem}
.btn{box-shadow:none;font-weight:600;letter-spacing:.2em;font-size:.76rem;border:1.5px solid #10322F;background:#10322F;font-family:'Poppins',sans-serif}
.btn:hover{background:#1B4A44;border-color:#1B4A44;box-shadow:var(--shadow);transform:translateY(-2px)}
.btn-outline{background:transparent;color:#10322F;border-color:#10322F}
.btn-outline:hover{background:#10322F;color:#fff}
.btn-ghost{background:transparent;border-color:rgba(255,255,255,.85);color:#fff}
.btn-ghost:hover{background:#fff;color:#10322F}
.btn-lav{background:#C4C7E6;border-color:#C4C7E6;color:#10322F}
.btn-sm{padding:12px 22px;font-size:.7rem}
.hidden{display:none!important}
/* header / footer from the main site (v2) */
"""
    resets = "\n.nav ul{margin:0}.nav img{height:50px}header .wrap{max-width:1240px}.nav ul a{white-space:nowrap}\n" + LINKS_CSS
    return tokens + header + resets + GALLERY_CSS + footer + "\n" + "\n".join(resp) + "\n"

def build_v2_js():
    scr = SL.SCRIPTS
    m = re.search(r"<script>\n\(function\(\)\{var LOC=.*?</script>", scr, re.S)
    loc = m.group(0)
    loc = loc.replace("<script>", "").replace("</script>", "")
    # a Hudson page always sets the visitor's office to Hudson (page context wins over the remembered choice)
    loc = loc.replace("apply(get());", "try{localStorage.setItem('serene_loc','hudson');}catch(e){}\napply('hudson');")
    m2 = re.search(r"document\.querySelectorAll\('\.nav ul li'\)\.forEach\(.*?\}\);\}\);", scr, re.S)
    menu = m2.group(0) if m2 else ""
    return loc + "\n(function(){" + menu + "})();\n"

# ------------------------------------------------------------------ office-specific home hero (so the two office pages are clearly different)
HOME_H1 = "Hudson&rsquo;s<br>physician-led med spa"
HOME_LEDE = ("Botox, fillers, laser and wellness at 50 W Streetsboro St in historic downtown Hudson &mdash; serving Stow, Twinsburg, Aurora, "
             "Cuyahoga Falls, Akron and Cleveland&rsquo;s east side. Board-certified physicians, complimentary consultations, same-week appointments.")
# the Hudson site was cloned from Barboursville and still carried Barboursville lounge/room photos -> real Hudson photos (Sep 23, 2026)
HOME_IMG_SWAP = {"/hudson/img/lobby-2.jpg": "/hudson/img/hudson-lounge.jpg", "/hudson/img/room-1.jpg": "/hudson/img/hudson-treatment-room.jpg",
                 "/hudson/img/lobby.jpg": "/hudson/img/hudson-lounge.jpg", "/hudson/img/facial-room.jpg": "/hudson/img/hudson-treatment-room.jpg"}


HOME_GALLERY = """
<section class="hgal reveal" id="gallery" aria-label="Inside our Hudson office">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Inside Our Hudson Office</div>
      <h2>A calm space in downtown Hudson</h2>
      <p>50 W Streetsboro St, Suite 2 &mdash; in the heart of historic downtown Hudson.</p>
    </div>
    <div class="hgal-grid">
      <figure class="tall"><img src="/hudson/img/hudson-exterior.jpg" alt="Serene Med Spa Hudson storefront at 50 W Streetsboro St, Hudson, Ohio" loading="lazy" decoding="async" width="1125" height="1500"><figcaption>Storefront</figcaption></figure>
      <figure class="wide"><img src="/hudson/img/hudson-lounge.jpg" alt="Serene Med Spa Hudson lounge and waiting area" loading="lazy" decoding="async" width="1800" height="1012"><figcaption>Lounge</figcaption></figure>
      <figure class="tall"><img src="/hudson/img/hudson-treatment-room.jpg" alt="Treatment room at Serene Med Spa Hudson" loading="lazy" decoding="async" width="1125" height="2000"><figcaption>Treatment room</figcaption></figure>
      <figure><img src="/hudson/img/hudson-retail.jpg" alt="Medical-grade skincare retail wall at Serene Med Spa Hudson" loading="lazy" decoding="async" width="1125" height="1500"><figcaption>Medical-grade skincare</figcaption></figure>
      <figure><img src="/hudson/img/hudson-entrance.jpg" alt="Entrance and hours at Serene Med Spa Hudson" loading="lazy" decoding="async" width="1125" height="1500"><figcaption>Entrance &amp; hours</figcaption></figure>
    </div>
  </div>
</section>

"""

def inject_home_videos(s):
    """Featured WSAZ video first thing on the home page; newest Vimeo video mid-page (shared blocks from site_lib)."""
    if 'id="studio3"' not in s and hasattr(SL, "featured_video_section"):
        feat = SL.featured_video_section(book_href="https://booking.mangomint.com/serenemedspa?serviceId=322", book_attrs="", pricing_href=PREFIX + "/ultherapy/#pricing")
        s = s.replace('<section class="hero">', feat + '<section class="hero">', 1)
    if 'id="latest-video"' not in s and hasattr(SL, "latest_video_section"):
        s = s.replace('<section class="about" id="about">', SL.latest_video_section() + '<section class="about" id="about">', 1)
    return s

def localize_home(s):
    s = re.sub(r'<h1>Glow that looks<br>effortlessly you</h1>', '<h1>' + HOME_H1 + '</h1>', s, count=1)
    s = re.sub(r'<h1>Glow that looks\s*<br>\s*effortlessly you</h1>', '<h1>' + HOME_H1 + '</h1>', s, count=1)
    s = re.sub(r'<p>Botox, dermal fillers, laser skin treatments, and advanced wellness[^<]*</p>', '<p>' + HOME_LEDE + '</p>', s, count=1)
    for a, b in HOME_IMG_SWAP.items(): s = s.replace(a, b)
    if 'id="gallery"' not in s:
        s = s.replace('<section class="location" id="location">', HOME_GALLERY + '<section class="location" id="location">', 1)
    return s

FONTS_RX = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?family=Cormorant[^"]*" rel="stylesheet">')
V2_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&family=Noto+Serif+Display:wght@400;500&family=Oooh+Baby&display=swap" rel="stylesheet">'

def swap_shell(s, cssv, jsv):
    s = re.sub(r'<div class="promo"[^>]*>.*?</div>\s*', "", s, count=1, flags=re.S)
    s = re.sub(r'<header\b.*?</header>', lambda m: SL.NAV, s, count=1, flags=re.S)
    s = re.sub(r'<div class="mbar">.*?</div>\s*', "", s, count=1, flags=re.S)
    s = re.sub(r'<footer\b.*?</footer>', lambda m: SL.FOOTER, s, count=1, flags=re.S)
    s = FONTS_RX.sub(V2_FONTS, s)
    s = re.sub(r'(<link rel="stylesheet" href="' + re.escape(PREFIX) + r'/styles\.css[^"]*">)', r'\1<link rel="stylesheet" href="' + PREFIX + f'/v2.css?v={cssv}">', s, count=1)
    if "v2.css" not in s:  # pages that load styles.css differently
        s = s.replace("</head>", f'<link rel="stylesheet" href="{PREFIX}/v2.css?v={cssv}"></head>', 1)
    s = s.replace("</body>", f'<script src="{PREFIX}/v2-shell.js?v={jsv}" defer></script>\n</body>', 1)
    return s

# ------------------------------------------------------------------ internal links (SEO pass 2, Sep 2026)
def load_guides():
    for p in (os.path.join(MAIN, "guides.json"), os.path.join(MAIN, "bundle", "site", "guides.json")):
        if os.path.exists(p):
            try: return json.load(open(p, encoding="utf-8"))
            except Exception: pass
    return {}
GUIDES = load_guides()
OFFICE = PREFIX.strip("/")

LINKS_CSS = """
.guides-block{padding:44px 0;background:#fff;border-top:1px solid var(--rule,#E5E7EB)}
.guides-block .wrap{max-width:1240px}
.guides-block h2{font-size:1.6rem;margin:6px 0 14px}
.guides-block ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px 28px}
.guides-block li a{color:#1B4A44;text-decoration:underline;text-underline-offset:3px;font-size:1rem}
.guides-block li a:hover{color:#10322F}
.area-more{max-width:900px;margin:22px auto 0;font-size:.95rem;color:#4B5563;line-height:1.9}
.area-more a{color:#1B4A44;text-decoration:underline;text-underline-offset:3px;white-space:nowrap}
"""

def inject_guides(s, rel):
    """Office treatment page -> 'From our treatment guides' links back to the main-site articles (LOCAL_MAP reversed)."""
    slug = rel.split("/")[0]
    g = GUIDES.get(slug)
    if not g or "guides-block" in s or rel == "index.html": return s
    name = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    name = re.sub(r"<[^>]+>|\s+", " ", name.group(1)).strip() if name else slug.replace("-", " ")
    name = re.sub(r"\s+in\s+(Hudson|Barboursville|Huntington).*$", "", name, flags=re.I)
    tele = ' <li><a href="/telehealth/">Telehealth weight &amp; hormone visits (OH, WV, KY, FL)</a></li>' if slug in ("weight-loss", "medical-weight-loss", "hormone-optimization", "longevity") else ""
    block = ('<section class="guides-block"><div class="wrap"><div class="eyebrow">From our treatment guides</div>'
             f'<h2>Learn more about {name}</h2><ul>' + "".join(f'<li><a href="{x["url"]}">{x["title"]}</a></li>' for x in g) + tele + '</ul></div></section>\n')
    for anchor in ('<section id="faq">', '<section class="location"', '<section class="cta">', '</main>'):
        i = s.find(anchor)
        if i != -1: return s[:i] + block + s[i:]
    return s

# parent treatment page -> its dedicated sub-pages (built from pages_data_new_zzz_pricing_gaps.py, Sep 2026). Only existing pages are linked.
SUBPAGES = {
    "botox": ["baby-botox", "masseter-botox", "shoulder-slimming-botox", "hyperhidrosis-treatment"],
    "fillers": ["radiesse", "hand-filler", "filler-dissolver"],
    "hormone-optimization": ["hormone-therapy-women", "testosterone-therapy-men"],
    "iv-therapy": ["iv-drip-menu", "vitamin-injections"],
    "hydration-bar": ["iv-drip-menu", "vitamin-injections"],
    "longevity": ["sermorelin", "low-dose-naltrexone", "iv-drip-menu"],
    "chemical-peels": ["acne-treatment"],
    "medical-facials": ["acne-treatment"],
    "laser-skin": ["sciton-moxi", "coolpeel", "deka-co2-laser", "pico-fractional-resurfacing"],
    "womens-sexual-wellness": ["v-renew", "vtone", "formav"],
    "mens-sexual-wellness": ["p-renew", "grow-girth", "alma-duo"],
    "alma-duo": ["p-renew", "grow-girth"],
}
def _page_name(slug):
    p = os.path.join(SITE, slug, "index.html")
    if not os.path.exists(p): return None
    h = open(p, encoding="utf-8", errors="ignore").read()
    m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    t = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip() if m else slug.replace("-", " ").title()
    return re.sub(r"\s+in\s+(Hudson|Barboursville|Huntington).*$", "", t, flags=re.I)

def inject_subpages(s, rel):
    """Parent treatment page -> 'Explore ... options' links to its dedicated sub-pages (so the new pages aren't orphaned)."""
    slug = rel.split("/")[0]
    kids = SUBPAGES.get(slug)
    if not kids or "subpages-block" in s or rel == "index.html": return s
    items = [(k, _page_name(k)) for k in kids]
    items = [(k, n) for k, n in items if n]
    if not items: return s
    name = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    name = re.sub(r"<[^>]+>|\s+", " ", name.group(1)).strip() if name else slug.replace("-", " ")
    name = re.sub(r"\s+in\s+(Hudson|Barboursville|Huntington).*$", "", name, flags=re.I)
    block = ('<section class="guides-block subpages-block"><div class="wrap"><div class="eyebrow">Explore your options</div>'
             f'<h2>More {name} treatments</h2><ul>' + "".join(f'<li><a href="{PREFIX}/{k}/">{n}</a></li>' for k, n in items) + '</ul></div></section>\n')
    for anchor in ('<section class="guides-block">', '<section id="faq">', '<section class="location"', '<section class="cta">', '</main>'):
        i = s.find(anchor)
        if i != -1: return s[:i] + block + s[i:]
    return s

def inject_area_links(s):
    """Office home -> link every city/treatment landing page that the 'areas' section doesn't already link."""
    i = s.find('<section class="areas"')
    if i == -1 or "area-more" in s: return s
    j = s.find("</section>", i)
    sec = s[i:j]
    pages = []
    for d in sorted(os.listdir(SITE)):
        if not re.search(r"-(oh|wv|ky)$", d) or not os.path.exists(os.path.join(SITE, d, "index.html")): continue
        href = f"{PREFIX}/{d}/"
        if href in sec: continue
        h = open(os.path.join(SITE, d, "index.html"), encoding="utf-8", errors="ignore").read()
        m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        t = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip() if m else d.replace("-", " ").title()
        if len(t) > 48:   # long H1 -> use the page title up to the separator
            mt = re.search(r"<title>(.*?)</title>", h, re.S)
            if mt: t = re.split(r"\s+[|\u2013\u2014-]\s+", mt.group(1).strip())[0]
        if "noindex" in h[:3000]: continue
        pages.append((href, t))
    if not pages: return s
    more = '<p class="area-more"><strong>Treatment pages by city:</strong> ' + " &middot; ".join(f'<a href="{h}">{t}</a>' for h, t in pages) + "</p>"
    k = sec.rfind("</div>")
    return s[:i] + sec[:k] + more + sec[k:] + s[j:]

def main():
    v2css = build_v2_css(); v2js = build_v2_js()
    cssv = hashlib.md5(v2css.encode()).hexdigest()[:8]; jsv = hashlib.md5(v2js.encode()).hexdigest()[:8]
    open(os.path.join(SITE, "v2.css"), "w", encoding="utf-8").write(v2css)
    open(os.path.join(SITE, "v2-shell.js"), "w", encoding="utf-8").write(v2js)
    n = 0
    for path in glob.glob(os.path.join(SITE, "**", "*"), recursive=True):
        if not os.path.isfile(path): continue
        ext = os.path.splitext(path)[1].lower()
        if ext not in (".html", ".css", ".js", ".xml", ".txt", ".json"): continue
        if os.path.basename(path) in ("v2.css", "v2-shell.js"): continue
        s = open(path, encoding="utf-8", errors="replace").read()
        already = "/hudson/" in s and OLD_HOST not in s and ext == ".html" and "v2-shell.js" in s   # merged on a previous run / template already carries the shell
        if ext == ".html":
            rel = os.path.relpath(path, SITE)
            if not already:
                s = prefix_html(s)
                if "<header" in s or "<footer" in s: s = swap_shell(s, cssv, jsv)
                for a, b in HOME_IMG_SWAP.items(): s = s.replace(a, b)
                if rel == "index.html": s = localize_home(s)
            s = inject_area_links(inject_home_videos(s)) if rel == "index.html" else inject_subpages(inject_guides(s, rel), rel)   # idempotent (home videos + area links run even on already-merged pages)
        elif ext == ".css":
            s = prefix_css(s)
            for a, b in HOME_IMG_SWAP.items(): s = s.replace(a, b)
        elif ext == ".js":
            s = prefix_js(s)
            for a, b in HOME_IMG_SWAP.items(): s = s.replace(a, b)
        else:
            s = s.replace(OLD_HOST + "/", NEW_HOST + "/").replace(OLD_HOST, NEW_HOST)
        open(path, "w", encoding="utf-8").write(s); n += 1
    # robots.txt is only meaningful at the domain root; leave a pointer
    open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8").write(f"# served under {NEW_HOST}/ — see https://serenemedspas.com/robots.txt\nUser-agent: *\nAllow: /\nSitemap: {NEW_HOST}/sitemap.xml\n")
    print(f"v2_merge: rewrote {n} files under {SITE} for {NEW_HOST}/ (shell from {MAIN})")

if __name__ == "__main__":
    main()
