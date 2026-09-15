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

# Same for /popup.js (the New Client popup), so edits reach returning visitors right away.
pj=os.path.join(BASE,"popup.js")
if os.path.exists(pj):
    hj=hashlib.sha256(open(pj,"rb").read()).hexdigest()[:8]
    m=0
    for f in pages:
        s=open(f).read()
        s2=re.sub(r'/popup\.js(\?v=[0-9a-f]+)?', '/popup.js?v='+hj, s)
        if s2!=s:
            open(f,"w").write(s2); m+=1
    print("cache-bust: /popup.js?v=%s applied to %d pages" % (hj, m))
