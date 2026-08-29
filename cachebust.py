# Append a content-hash version to every /styles.css reference so browsers
# always fetch fresh CSS when it changes (idempotent).
import hashlib, glob, re, os
BASE="bundle/site"
css=open(os.path.join(BASE,"styles.css"),"rb").read()
h=hashlib.sha256(css).hexdigest()[:8]
pages=set(glob.glob(os.path.join(BASE,"**","index.html"),recursive=True))|{os.path.join(BASE,"index.html")}
n=0
for f in pages:
    s=open(f).read()
    s2=re.sub(r'/styles\.css(\?v=[0-9a-f]+)?', '/styles.css?v='+h, s)
    if s2!=s:
        open(f,"w").write(s2); n+=1
print("cache-bust: /styles.css?v=%s applied to %d pages" % (h, n))
