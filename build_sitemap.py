# build_sitemap.py — regenerate sitemap.xml from indexable pages in bundle/site.
# Excludes any page carrying a noindex robots meta. Pure stdlib. Build step.
import glob, os, re, datetime
BASE="bundle/site"
SITE="https://hudson.serenemedspas.com"
urls=[]
for p in sorted(glob.glob(os.path.join(BASE,"**","index.html"), recursive=True)):
    html=open(p,encoding="utf-8",errors="ignore").read()
    if re.search(r'name="robots"[^>]*content="[^"]*noindex', html, re.I):
        continue
    rel=os.path.relpath(p, BASE)
    if rel.startswith("blog/"): continue   # blog moved to blog.serenemedspas.com
    path="" if rel=="index.html" else rel[:-len("index.html")]
    loc=SITE.rstrip("/")+"/"+path
    lastmod=datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()
    urls.append((loc,lastmod))
lines=['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc,lm in urls:
    lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod></url>")
lines.append("</urlset>")
open(os.path.join(BASE,"sitemap.xml"),"w",encoding="utf-8").write("\n".join(lines)+"\n")
print(f"build_sitemap: wrote {len(urls)} indexable urls")
