#!/usr/bin/env python3
"""build_wl_ads.py — Google-Ads landing page for the Weight loss ad group.

Google's "Healthcare & medicines" policy flags any destination page that names
prescription drugs (semaglutide, tirzepatide, Wegovy, Zepbound, GLP-1 …) as
"prescription drug sale — certificate required", which limits/disapproves the
ads that point to it.  The public /weight-loss/ page keeps its full copy for
SEO; this script derives an ads-only copy at /medical-weight-loss/ with every
drug name removed, noindex'd so it never competes with /weight-loss/ in search.

Run from the repo root after gen_pages (build.sh does this). Stdlib only.
"""
import os, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
SRC  = os.path.join(SITE, "weight-loss", "index.html")
DST  = os.path.join(SITE, "medical-weight-loss", "index.html")

s = open(SRC, encoding="utf-8").read()
host = re.search(r'<link rel="canonical" href="(https://[^/]+)/', s).group(1)

# --- text replacements (order matters: longest first) -----------------------
REPL = [
    # meta / schema / hero
    ("personalized GLP-1 programs guided by board-certified providers",
     "personalized programs designed and monitored by board-certified physicians"),
    ("prescription medications such as GLP-1 options when appropriate",
     "medical treatment options prescribed by our physicians when appropriate"),
    ("prescription medications such as GLP-1 options when clinically appropriate",
     "medical treatment options prescribed by our physicians when clinically appropriate"),
    ("prescription options such as GLP-1 medications when clinically appropriate",
     "treatment options prescribed by our physicians when clinically appropriate"),
    ("modern options like GLP-1 medications when appropriate",
     "modern treatment options when appropriate"),
    ("GLP-1 Options When Appropriate", "Physician-Prescribed Options"),
    # FAQ (visible + schema)
    ("Do you offer GLP-1 medications like semaglutide?", "Does the program include medication?"),
    ("Do you offer GLP-1 medications?", "Does the program include medication?"),
    ("our physicians may include GLP-1 medications as part of your plan",
     "our physicians may include treatment options as part of your plan"),
    # treatment card
    ("<h3>GLP-1 Options</h3><p>Modern medications such as semaglutide-class options, prescribed when clinically appropriate.</p>",
     "<h3>Physician-Prescribed Options</h3><p>Modern, evidence-based treatment options, prescribed by our physicians only when clinically appropriate for you.</p>"),
]
for a, b in REPL:
    s = s.replace(a, b)

# disclaimer block — rewrite without drug names
i = s.find('<div class="wl-disc">')
if i > -1:
    j = s.find('</div>', i) + len('</div>')
    disc = ('<div class="wl-disc">\n<h2>Medical Weight Loss &mdash; Important Information</h2>\n'
            '<p>Any prescription treatment requires a consultation with our licensed medical provider, who reviews your '
            'health history and determines whether it is appropriate for you. When a prescription is appropriate it is sent to '
            '<strong>your pharmacy of choice</strong>; the medication is billed by your pharmacy and may be covered by insurance. '
            'Serene Med Spa charges for the medical visit only. Treatment is not appropriate for everyone and individual results vary. '
            'Please review the full prescribing and safety information with your provider and pharmacist.</p>\n</div>')
    s = s[:i] + disc + s[j:]

# safety net — any remaining drug names anywhere in the page
DRUGS = r"(?i)\b(semaglutide|tirzepatide|wegovy|zepbound|ozempic|mounjaro|liraglutide|saxenda|glp-?1)\b(\s*&reg;)?"
s = re.sub(DRUGS, "physician-prescribed treatment", s)

# --- URL / indexing -----------------------------------------------------------
s = s.replace(host + "/weight-loss/", host + "/medical-weight-loss/")
s = re.sub(r'<meta name="robots"[^>]*>\s*', "", s)
s = s.replace("</title>", "</title>\n<meta name=\"robots\" content=\"noindex,follow\">", 1)
# ads-only page: keep the visitor on it — the sticky/booking CTAs stay, nothing else changes

os.makedirs(os.path.dirname(DST), exist_ok=True)
open(DST, "w", encoding="utf-8").write(s)
left = re.findall(DRUGS, s)
print("build_wl_ads:", DST, "written;", "residual drug terms:", len(left))
