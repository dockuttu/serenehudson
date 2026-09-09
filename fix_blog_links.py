# fix_blog_links.py — the blog lives at blog.serenemedspas.com now. Rewrite any leftover
# site-relative /blog/ links in built pages (incl. hand-built static pages) to the blog domain.
import glob, re, os
BLOG = "https://blog.serenemedspas.com"
n = 0
for f in glob.glob("bundle/site/**/*.html", recursive=True):
    if f.startswith("bundle/site/blog/"): continue
    t = open(f, encoding="utf-8").read(); o = t
    t = t.replace('href="/blog/"', 'href="%s/"' % BLOG)
    t = re.sub(r'href="/blog/([a-z0-9\-]+)/"', lambda m: 'href="%s/%s/"' % (BLOG, m.group(1)), t)
    if t != o: open(f, "w", encoding="utf-8").write(t); n += 1
print("fix_blog_links: %d page(s) updated" % n)
