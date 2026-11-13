# -*- coding: utf-8 -*-
# lip_results.py — idempotent post-build pass (identical in both repos):
# adds a "Real Results" lip filler before/after section to /lip-filler/ (Serene patients, shared with consent; Nov 2026).
import os, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "lip-filler", "index.html")
if not os.path.exists(f):
    print("lip_results: page missing"); sys.exit(0)
s = open(f, encoding="utf-8").read(); o = s

def fig(img, w, h, alt, title, cap):
    return ('<figure class="res reveal"><picture><source srcset="/img/%s.webp" type="image/webp">'
            '<img loading="lazy" src="/img/%s.jpg" alt="%s" width="%d" height="%d"></picture>'
            '<figcaption><b>%s</b><span>%s</span></figcaption></figure>' % (img, img, alt, w, h, title, cap))

SECTION = '''<section class="results" id="lip-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>Real Lip Filler Results</h2>
      <p style="font-size:1.12rem;color:var(--ink);font-weight:500">Recent lip filler patients at Serene Med Spa. After photos were taken right after treatment, so some swelling is normal; lips settle into their final shape over about two weeks.</p></div>
    <div class="lip-grid">
''' + "\n".join([
    fig("ba-lip-fuller-front", 1600, 500, "Lip filler before and after, front view: fuller lips with smoother lip lines",
        "Fuller, smoother lips &mdash; front", "Volume added to both lips and fine vertical lines softened, keeping a natural shape."),
    fig("ba-lip-fuller-side", 1600, 500, "Lip filler before and after, side view: more projection of the upper and lower lip",
        "Fuller, smoother lips &mdash; side", "More projection and a hydrated, even surface from the side."),
    fig("ba-lip-define-front", 1600, 542, "Lip filler before and after, front view: balanced volume and a defined lip border",
        "Natural volume &amp; definition &mdash; front", "A balanced boost to the upper and lower lip with a crisper border."),
    fig("ba-lip-define-left", 1600, 542, "Lip filler before and after, left side view",
        "Natural volume &amp; definition &mdash; left", "Soft projection that still looks like her own lips."),
    fig("ba-lip-define-right", 1600, 542, "Lip filler before and after, right side view",
        "Natural volume &amp; definition &mdash; right", "Even shape from every angle."),
]) + '''
    </div>
    <p class="rev-note" style="font-size:.95rem;color:var(--ink)">Individual results vary. Photos of our own patients, shared with consent.</p>
  </div>
  <style>
  .lip-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;align-items:start}
  .lip-grid .res img{height:auto;max-height:none;object-fit:contain}
  @media(max-width:800px){.lip-grid{grid-template-columns:1fr}}
  </style>
</section>
'''
if 'id="lip-results"' not in s:
    k = s.find('<section id="pricing"')
    if k == -1:
        k = s.find('<section id="faq">')
    if k == -1:
        k = s.find('<footer')
    if k != -1:
        s = s[:k] + SECTION + s[k:]
if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("lip_results:", "updated" if s != o else "already present")
