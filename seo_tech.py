# seo_tech.py — post-build technical SEO pass (pure stdlib, idempotent). Same file in both location repos.
#  1. MedicalBusiness JSON-LD: drop self-serving aggregateRating/review markup (not eligible for
#     Google review rich results and the counts were stale), and expand "founder" into full
#     Person entities linked to the blog author (@id) and the physician's public profiles.
#  2. Adds a default og:image to any indexable page that is missing one.
#  3. Writes a branded 404.html (served by nginx error_page) built from the homepage chrome.
# Usage: python3 seo_tech.py bundle/site
import glob, json, os, re, sys
SITE_DIR = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
DEFAULT_OG = "https://serenemedspas.com/wp-content/uploads/2024/11/Serene_Logo-1024x574.png"
ROBIN = {"@type": ["Person", "Physician"], "@id": "https://blog.serenemedspas.com/#robin-arora",
    "name": "Robin Arora, MD", "honorificSuffix": "MD, MBA",
    "jobTitle": "Founder and Medical Director, Serene Med Spa",
    "url": "https://blog.serenemedspas.com/a-personal-introduction-dr-robin-arora/",
    "image": "https://blog.serenemedspas.com/img/dr-robin-arora-headshot.jpg",
    "identifier": {"@type": "PropertyValue", "propertyID": "NPI", "value": "1144481565"},
    "sameAs": ["https://npiregistry.cms.hhs.gov/provider-view/1144481565",
               "https://www.doximity.com/pub/robin-arora-md",
               "https://www.healthgrades.com/physician/dr-robin-arora-3q9pd",
               "https://doctor.webmd.com/doctor/robin-arora-793728b1-3629-4ab6-9285-11bdfa32a9d4-overview",
               "https://health.usnews.com/doctors/robin-arora-680252"]}
SHWETA = {"@type": ["Person", "Physician"], "name": "Shweta Arora, MD",
    "jobTitle": "Aesthetic Physician and Co-Founder, Serene Med Spa"}
LD = re.compile(r'(<script type="application/ld\+json">\s*)(.*?)(\s*</script>)', re.S)

def fix_ld(m):
    raw = m.group(2)
    try:
        d = json.loads(raw)
    except Exception:
        return m.group(0)
    if not isinstance(d, dict) or d.get("@type") != "MedicalBusiness":
        return m.group(0)
    changed = False
    for k in ("aggregateRating", "review"):
        if k in d:
            d.pop(k); changed = True
    f = d.get("founder")
    if isinstance(f, list) and f and not any(isinstance(x, dict) and x.get("@id") for x in f):
        d["founder"] = [ROBIN, SHWETA]; changed = True
    if not changed:
        return m.group(0)
    return m.group(1) + json.dumps(d, ensure_ascii=False) + m.group(3)

n_ld = n_og = 0
for p in glob.glob(os.path.join(SITE_DIR, "**", "*.html"), recursive=True):
    s = open(p, encoding="utf-8", errors="ignore").read(); t = s
    t = LD.sub(fix_ld, t)
    if t != s: n_ld += 1
    noindex = re.search(r'name="robots"[^>]*content="[^"]*noindex', t, re.I)
    if not noindex and 'property="og:image"' not in t and "</head>" in t:
        t = t.replace("</head>", '<meta property="og:image" content="%s">\n</head>' % DEFAULT_OG, 1)
        if 'name="twitter:card"' not in t:
            t = t.replace("</head>", '<meta name="twitter:card" content="summary_large_image">\n</head>', 1)
        n_og += 1
    if t != s:
        open(p, "w", encoding="utf-8").write(t)

# ---- branded 404 page ----
home = open(os.path.join(SITE_DIR, "index.html"), encoding="utf-8").read()
head_end = home.find("</head>"); hdr_end = home.find("</header>"); ftr = home.find("<footer")
if head_end > 0 and hdr_end > 0 and ftr > 0:
    head = home[:head_end]
    head = re.sub(r"<title>.*?</title>", "<title>Page Not Found | Serene Med Spa</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description"[^>]*>', '<meta name="description" content="This page could not be found.">', head)
    head = re.sub(r'<link rel="canonical"[^>]*>\s*', "", head)
    head = re.sub(r'<meta name="robots"[^>]*>', "", head)
    head = re.sub(r'<meta property="og:[^>]*>\s*', "", head)
    head = LD.sub("", head)
    head = head.replace("<head>", '<head>\n<meta name="robots" content="noindex, follow">', 1)
    body_start = home[head_end:hdr_end + len("</header>")]
    main = '''
<section class="svc-hero"><div class="wrap" style="text-align:center;padding:60px 0">
  <div class="eyebrow">Error 404</div>
  <h1>We couldn&rsquo;t find that page</h1>
  <p style="max-width:560px;margin:14px auto 26px">The page may have moved. Try one of these instead:</p>
  <p><a class="btn" href="/">Home</a> <a class="btn btn-outline" href="/pricing/">Pricing</a> <a class="btn btn-outline" href="/#services">Treatments</a> <a class="btn btn-outline" href="/before-after/">Gallery</a></p>
</div></section>
'''
    page = head + body_start + main + home[ftr:]
    open(os.path.join(SITE_DIR, "404.html"), "w", encoding="utf-8").write(page)
print("seo_tech: schema fixed on %d page(s), og:image added to %d page(s), 404.html written" % (n_ld, n_og))
