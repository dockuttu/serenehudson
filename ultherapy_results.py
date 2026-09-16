# -*- coding: utf-8 -*-
# ultherapy_results.py — idempotent post-build pass (identical in both repos):
# adds an Ultherapy PRIME before/after section to /ultherapy/ (manufacturer photos, credited).
import os, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
f = os.path.join(SITE, "ultherapy", "index.html")
if not os.path.exists(f):
    print("ultherapy_results: page missing"); sys.exit(0)
s = open(f, encoding="utf-8").read(); o = s
SECTION = '''<section class="results" id="ultherapy-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>Ultherapy PRIME Results</h2>
      <p style="font-size:1.12rem;color:var(--ink);font-weight:500">A non-surgical lift for the brow, chin and neck &mdash; Ultherapy uses focused ultrasound to rebuild collagen, so results build gradually over two to three months.</p></div>
    <div class="ulth-grid">
      <figure class="res reveal"><img loading="lazy" src="/img/ultherapy-brow-lift-70-days.webp" alt="Ultherapy PRIME before and after: lifted brow and more open upper eyelid, 70 days after treatment" width="1320" height="595"><figcaption><b>Brow Lift</b><span>70 days after one Ultherapy treatment &mdash; a lifted brow and a more open-looking eye.</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/ultherapy-neck-chin.webp" alt="Ultherapy before and after: firmer chin and neck with smoother neck lines" width="660" height="1260"><figcaption><b>Chin &amp; Neck</b><span>Tighter under-chin skin and softer neck lines after Ultherapy.</span></figcaption></figure>
    </div>
    <p class="rev-note" style="font-size:.95rem;color:var(--ink)">Individual results may vary. Photos courtesy of Merz Aesthetics (brow photo courtesy of Jeffrey W. Hall, MD) &mdash; not Serene patients.</p>
  </div>
  <style>
  .ulth-grid{display:grid;grid-template-columns:1.6fr 1fr;gap:22px;align-items:start}
  .ulth-grid .res img{height:auto;max-height:520px;object-fit:contain}
  @media(max-width:800px){.ulth-grid{grid-template-columns:1fr}}
  </style>
</section>
'''
if 'id="ultherapy-results"' not in s:
    k = s.find('<section id="pricing"')
    if k == -1:
        k = s.find('<section id="faq">')
    if k != -1:
        s = s[:k] + SECTION + s[k:]
if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("ultherapy_results:", "updated" if s != o else "already present")
