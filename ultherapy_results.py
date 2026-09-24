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
# ---- WSAZ Studio 3 live demo + October special (Sep 24, 2026). Idempotent; inserted before the before/after section.
STUDIO3 = '''<section id="studio3" class="tint-sand"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">As seen on WSAZ Studio 3</div><h2>Watch Dr. Arora&rsquo;s live Ultherapy demo</h2>
    <p style="max-width:720px;margin:10px auto 0">Dr. Robin Arora demonstrated Ultherapy PRIME live on WSAZ&rsquo;s Studio 3 on September 18, 2026 &mdash; see what a treatment looks like, how the ultrasound imaging guides each pass, and why there&rsquo;s no downtime.</p></div>
  <div class="studio3-wrap reveal"><iframe src="https://player.vimeo.com/video/1228988348?dnt=1&amp;title=0&amp;byline=0&amp;portrait=0" title="Ultherapy live demo on WSAZ Studio 3 with Dr. Robin Arora" loading="lazy" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>
  <div class="card reveal studio3-offer"><div class="ico">&#10022;</div><h3>Studio 3 special: 30% off Ultherapy</h3>
    <p>The first 20 clients who book Ultherapy after the segment save <strong>30%</strong> on any Ultherapy PRIME treatment at either Serene office &mdash; Hudson or Barboursville. Mention <strong>&ldquo;Studio 3&rdquo;</strong> when you book. Offer ends <strong>October 31, 2026</strong>; can&rsquo;t be combined with other discounts.</p>
    <p><a class="btn" href="__BOOK__">Book a Consultation</a> <a class="btn btn-outline" href="#pricing">See Ultherapy pricing</a></p></div>
  <style>
  .studio3-wrap{position:relative;padding-top:56.25%;border-radius:18px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.12);margin:0 auto 28px;max-width:960px;background:#000}
  .studio3-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  .studio3-offer{max-width:760px;margin:0 auto;text-align:center}
  .studio3-offer .btn{margin:6px 4px 0}
  </style>
</div></section>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"VideoObject","name":"Ultherapy Live Demo on WSAZ Studio 3 — Dr. Robin Arora, Serene Med Spa","description":"Dr. Robin Arora of Serene Med Spa performs a live Ultherapy PRIME demonstration on WSAZ's Studio 3 (aired September 18, 2026): a non-surgical ultrasound lift for the brow, jawline, under-chin, neck and décolletage.","thumbnailUrl":["https://i.vimeocdn.com/video/2203534769-9df18cf4bcf6ef3f14c3a1ce6c37a5fdaa4957b5937dff689e47836bf0f9886f-d_1280"],"uploadDate":"2026-09-21T18:27:07-04:00","duration":"PT6M4S","embedUrl":"https://player.vimeo.com/video/1228988348","contentUrl":"https://vimeo.com/1228988348","publisher":{"@type":"Organization","name":"Serene Med Spa","url":"https://serenemedspas.com/"},"actor":{"@type":"Person","name":"Robin Arora, MD","url":"https://serenemedspas.com/our-providers/robin-arora-md/"}}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Offer","name":"Studio 3 special: 30% off Ultherapy PRIME","description":"First 20 clients who book Ultherapy after the WSAZ Studio 3 segment save 30% at Serene Med Spa (Hudson, OH or Barboursville, WV). Mention Studio 3 when booking.","url":"https://serenemedspas.com/hudson/ultherapy/#studio3","validFrom":"2026-09-18","validThrough":"2026-10-31","category":"Promotion","areaServed":["Hudson, OH","Barboursville, WV"],"offeredBy":{"@type":"MedicalBusiness","name":"Serene Med Spa — Hudson","url":"https://serenemedspas.com/hudson/"}}</script>
'''
import re as _re
if 'id="studio3"' not in s:
    _m = _re.search(r'href="(https://booking\.mangomint\.com/[^"]*)"', s)
    _book = _m.group(1) if _m else "https://booking.mangomint.com/serenemedspa"
    _k = s.find('<section class="results" id="ultherapy-results">')
    if _k == -1: _k = s.find('<section id="pricing"')
    if _k != -1:
        s = s[:_k] + STUDIO3.replace("__BOOK__", _book) + s[_k:]

if s != o:
    open(f, "w", encoding="utf-8").write(s)
print("ultherapy_results:", "updated" if s != o else "already present")
