# build_sitemap.py — regenerate sitemap.xml from indexable pages in bundle/site.
# Excludes any page carrying a noindex robots meta. Pure stdlib. Build step.
# <lastmod> only changes when a page's content actually changes (tracked by a content
# hash in sitemap_state.json, committed with the repo), so Google can trust it.
import glob, os, re, datetime, hashlib, json, subprocess
BASE = "bundle/site"
SITE = "https://hudson.serenemedspas.com"
STATE_FILE = "sitemap_state.json"
try:
    state = json.load(open(STATE_FILE))
except Exception:
    state = {}
today = datetime.date.today().isoformat()

def content_hash(html):
    html = re.sub(r'\?v=[0-9a-zA-Z]+', '', html)          # cache-bust tokens
    html = re.sub(r'\s+', ' ', html)
    return hashlib.sha1(html.encode("utf-8")).hexdigest()[:16]

def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                             capture_output=True, text=True, timeout=10).stdout.strip()
        return out or today
    except Exception:
        return today

urls = []; new_state = {}
for p in sorted(glob.glob(os.path.join(BASE, "**", "index.html"), recursive=True)):
    html = open(p, encoding="utf-8", errors="ignore").read()
    if re.search(r'name="robots"[^>]*content="[^"]*noindex', html, re.I):
        continue
    rel = os.path.relpath(p, BASE)
    if rel.startswith("blog/") or rel.startswith("lp/"):
        continue   # blog moved to blog.serenemedspas.com; /lp/ = ads-only pages
    path = "" if rel == "index.html" else rel[:-len("index.html")]
    loc = SITE.rstrip("/") + "/" + path
    h = content_hash(html)
    old = state.get(loc)
    if old and old[0] == h:
        lastmod = old[1]
    elif old:
        lastmod = today
    else:
        lastmod = git_date(p)
    new_state[loc] = [h, lastmod]
    urls.append((loc, lastmod))
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, lm in urls:
    lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod></url>")
lines.append("</urlset>")
open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
json.dump(new_state, open(STATE_FILE, "w"), indent=0, sort_keys=True)
print(f"build_sitemap: wrote {len(urls)} indexable urls")
