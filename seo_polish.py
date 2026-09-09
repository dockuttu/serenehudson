# seo_polish.py — post-build pass over bundle/site/**/*.html (pure stdlib).
#  * adds width/height to <img> tags that lack them (reads JPEG/PNG/WebP/GIF headers) -> no layout shift (CLS)
#  * adds loading="lazy" + decoding="async" to images after the first two on a page
#  * adds <meta name="twitter:card"> when og:image exists and the tag is missing
# Idempotent; safe to run repeatedly. Usage: python3 seo_polish.py [site_dir]
import glob, os, re, struct, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"

def dims(path):
    try:
        with open(path, "rb") as f: h = f.read(32)
        if h[:8] == b"\x89PNG\r\n\x1a\n": return struct.unpack(">II", h[16:24])
        if h[:6] in (b"GIF87a", b"GIF89a"): return struct.unpack("<HH", h[6:10])
        if h[:4] == b"RIFF" and h[8:12] == b"WEBP":
            with open(path, "rb") as f: f.seek(12); c = f.read(18)
            if c[:4] == b"VP8X": return (int.from_bytes(c[8:11], "little") + 1, int.from_bytes(c[11:14], "little") + 1)
            if c[:4] == b"VP8 ": return (struct.unpack("<H", c[10:12])[0] & 0x3fff, struct.unpack("<H", c[12:14])[0] & 0x3fff)
            if c[:4] == b"VP8L":
                b = c[5:9]; w = 1 + (((b[1] & 0x3F) << 8) | b[0]); hh = 1 + (((b[3] & 0xF) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6)); return (w, hh)
        if h[:2] == b"\xff\xd8":
            with open(path, "rb") as f:
                f.seek(2)
                while True:
                    m = f.read(1)
                    if not m: break
                    if m != b"\xff": continue
                    while (t := f.read(1)) == b"\xff": pass
                    if t in (b"\xc0", b"\xc1", b"\xc2", b"\xc3", b"\xc5", b"\xc6", b"\xc7", b"\xc9", b"\xca", b"\xcb", b"\xcd", b"\xce", b"\xcf"):
                        f.read(3); hgt, wid = struct.unpack(">HH", f.read(4)); return (wid, hgt)
                    ln = struct.unpack(">H", f.read(2))[0]; f.seek(ln - 2, 1)
    except Exception: return None
    return None

KNOWN = {"https://serenemedspas.com/wp-content/uploads/2024/11/Serene_Logo-1024x574.png": (1024, 574)}
IMG = re.compile(r"<img\b[^>]*>", re.I)
changed = 0
for page in glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True):
    html = open(page, encoding="utf-8", errors="ignore").read(); orig = html
    n = [0]
    def fix(m):
        tag = m.group(0); n[0] += 1
        src = re.search(r'\bsrc="([^"]+)"', tag)
        if src and not re.search(r"\bwidth=", tag):
            s = src.group(1)
            d = KNOWN.get(s)
            if not d and s.startswith("/") and not s.startswith("//"):
                d = dims(os.path.join(SITE, s.lstrip("/").split("?")[0]))
            if d: tag = tag[:-1].rstrip("/") + ' width="%d" height="%d">' % d
        if n[0] > 2 and "loading=" not in tag: tag = tag[:-1].rstrip("/") + ' loading="lazy" decoding="async">'
        return tag
    html = IMG.sub(fix, html)
    if 'property="og:image"' in html and 'name="twitter:card"' not in html:
        html = html.replace('<meta property="og:image"', '<meta name="twitter:card" content="summary_large_image">\n<meta property="og:image"', 1)
    if html != orig:
        open(page, "w", encoding="utf-8").write(html); changed += 1
print("seo_polish: %d page(s) updated" % changed)
