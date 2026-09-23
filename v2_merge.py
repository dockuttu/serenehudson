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
import os, re, sys, hashlib, glob

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
    resets = "\n.nav ul{margin:0}.nav img{height:50px}header .wrap{max-width:1240px}.nav ul a{white-space:nowrap}\n"
    return tokens + header + resets + footer + "\n" + "\n".join(resp) + "\n"

def build_v2_js():
    scr = SL.SCRIPTS
    m = re.search(r"<script>\n\(function\(\)\{var LOC=.*?</script>", scr, re.S)
    loc = m.group(0)
    loc = loc.replace("<script>", "").replace("</script>", "")
    # on a Hudson page the default office is Hudson
    loc = loc.replace("apply(get());", "if(!get()){try{localStorage.setItem('serene_loc','hudson');}catch(e){}}\napply(get()||'hudson');")
    m2 = re.search(r"document\.querySelectorAll\('\.nav ul li'\)\.forEach\(.*?\}\);\}\);", scr, re.S)
    menu = m2.group(0) if m2 else ""
    return loc + "\n(function(){" + menu + "})();\n"

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
        if "/hudson/" in s and OLD_HOST not in s and ext == ".html" and "v2-shell.js" in s:
            continue  # already merged (idempotent re-run)
        if ext == ".html":
            s = prefix_html(s)
            if "<header" in s or "<footer" in s: s = swap_shell(s, cssv, jsv)
        elif ext == ".css":
            s = prefix_css(s)
        elif ext == ".js":
            s = prefix_js(s)
        else:
            s = s.replace(OLD_HOST + "/", NEW_HOST + "/").replace(OLD_HOST, NEW_HOST)
        open(path, "w", encoding="utf-8").write(s); n += 1
    # robots.txt is only meaningful at the domain root; leave a pointer
    open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8").write(f"# served under {NEW_HOST}/ — see https://serenemedspas.com/robots.txt\nUser-agent: *\nAllow: /\nSitemap: {NEW_HOST}/sitemap.xml\n")
    print(f"v2_merge: rewrote {n} files under {SITE} for {NEW_HOST}/ (shell from {MAIN})")

if __name__ == "__main__":
    main()
