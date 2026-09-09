# -*- coding: utf-8 -*-
# Harmony Bio-Boost (Alma Harmony XL Pro) — added Sept 2026 from Alma's Bio-Boost launch kit.
# Hudson-voice copy; the Barboursville build localizes it automatically (bv_localize.py swaps
# "Alma IQ" for VISIA, since Barboursville uses VISIA for skin analysis).
def _steps(a,b,c,d): return [("Consultation",a),("Treatment",b),("Results",c),("Maintenance",d)]

_BB_RESULTS = '''<section class="results" id="bio-boost-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>Harmony Bio-Boost Results</h2><p>Baseline vs. one month after a single Harmony Bio-Boost session, captured with Alma IQ skin analysis.</p></div>
    <div class="res-grid" style="grid-template-columns:repeat(3,1fr)">
      <figure class="res reveal"><img loading="lazy" src="/img/bio-boost-daylight-1.webp" alt="Harmony Bio-Boost before and after, daylight view, one month after one treatment" width="787" height="596"><figcaption><b>Tone &amp; Texture</b><span>Daylight view &middot; 1 month after 1 treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/bio-boost-pigmentation-1.webp" alt="Harmony Bio-Boost before and after, pigmentation view, one month after one treatment" width="787" height="596"><figcaption><b>Sun Damage &amp; Pigment</b><span>Pigmentation view &middot; 1 month after 1 treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/bio-boost-vascularity-1.webp" alt="Harmony Bio-Boost before and after, vascularity view, one month after one treatment" width="954" height="596"><figcaption><b>Redness &amp; Vessels</b><span>Vascularity view &middot; 1 month after 1 treatment</span></figcaption></figure>
    </div>
    <p class="rev-note">Individual results may vary. Photos courtesy of Alma, Inc. and Pina Panchal, MD &mdash; not Serene patients.</p>
  </div>
</section>
<section class="tint-mint" id="bio-boost-modes">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Three Steps, One Visit</div><h2>What Happens in a Bio-Boost Session</h2></div>
    <div class="grid">
      <div class="card reveal"><div class="ico">&#10022;</div><h3>1 &middot; Dye-VL Pulsed Light</h3><p>Narrow-band pulsed light targets brown spots, freckling, and diffuse redness so tone looks clearer and more even.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>2 &middot; ClearSkin Pro Fractional Laser</h3><p>A non-ablative fractional laser heats the deeper skin to stimulate collagen and elastin, improving texture, pores, and fine lines.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>3 &middot; SupErb Micro-Resurfacing</h3><p>A light erbium pass refreshes the surface and boosts glow &mdash; gentle enough for a lunchtime visit.</p></div>
    </div>
    <p style="text-align:center;margin-top:18px;color:var(--muted);font-size:.95rem">Every session is mapped to your skin with Alma IQ skin analysis, so the settings match your concerns and skin type.</p>
  </div>
</section>'''

PAGES5 = [
{
 "slug":"harmony-bio-boost","crumb":"Harmony Bio-Boost","area_kw":"Harmony Bio-Boost skin rejuvenation",
 "title":"Harmony Bio-Boost in Hudson, OH | Serene Med Spa",
 "desc":"Harmony Bio-Boost in Hudson, Ohio: a personalized Alma Harmony laser session that stimulates your own collagen and clears pigment and redness. Book today.",
 "ogtitle":"Harmony Bio-Boost in Hudson, OH","ogdesc":"New collagen, new you. Personalized Alma Harmony Bio-Boost laser rejuvenation in Hudson, Ohio — minimal downtime, natural-looking results.",
 "proc_name":"Harmony Bio-Boost","proc_alt":"Alma Harmony Bio-Stimulation Laser Rejuvenation",
 "how":"A personalized combination of pulsed light and fractional laser on the Alma Harmony platform stimulates the skin's own collagen and elastin while clearing pigment and redness, refining tone and texture with minimal downtime.","body":"Face, Neck, Chest, Hands",
 "eyebrow":"Harmony Bio-Boost &middot; Hudson, OH","h1":"Harmony Bio-Boost in Hudson, Ohio",
 "hero":"New collagen, new you. A personalized Alma Harmony laser session that boosts your skin&rsquo;s own collagen, clears sun damage and redness, and refines texture &mdash; in about an hour, with minimal downtime.",
 "trust":["Stimulates Your Own Collagen","Lunchtime Treatment","Results After 1 Session","Physician-Led"],
 "introh2":"Lose the filters. Keep your natural look.",
 "introlead":"Harmony Bio-Boost is a bio-stimulation treatment: laser and pulsed-light energy from the Alma Harmony platform prompts your skin to rebuild its own collagen and elastin &mdash; the proteins that keep skin firm, smooth, and bright &mdash; instead of adding anything from the outside.",
 "intropara":"At Serene Med Spa in Hudson, every Bio-Boost begins with Alma IQ skin analysis, which maps pigment, redness, and texture beneath the surface so your physician can tailor each pass to your skin. Three complementary technologies are layered in a single visit: Dye-VL pulsed light for brown spots and redness, ClearSkin Pro fractional laser for collagen and texture, and a gentle SupErb resurfacing pass for glow. Most people see brighter, more even skin within a few weeks of one session, with continued improvement as new collagen forms over the following months. Individual results vary.",
 "treyebrow":"What It Treats","treh2":"Concerns Bio-Boost Targets",
 "cards":[
   ("Sun Damage &amp; Age Spots","Clear freckling and brown spots from years of sun exposure."),
   ("Redness &amp; Rosacea-Prone Skin","Calm diffuse redness and the look of small visible vessels."),
   ("Fine Lines &amp; Laxity","Stimulate collagen and elastin for firmer, smoother-looking skin."),
   ("Texture &amp; Pores","Refine rough texture, enlarged pores, and mild acne scarring."),
   ("Dullness","Restore a brighter, more radiant, healthy-looking glow."),
   ("Neck, Chest &amp; Hands","Treat the areas that give away sun exposure beyond the face."),
 ],
 "steps":_steps(
   "We scan your skin with Alma IQ, review your concerns and skin type, and design your personalized Bio-Boost plan.",
   "In about an hour, your physician layers Dye-VL pulsed light, ClearSkin Pro fractional laser, and a light SupErb pass, with cooling for comfort.",
   "Expect mild redness for a day or two and brown spots that darken briefly then flake away. Brighter, smoother skin appears over the following weeks as collagen rebuilds.",
   "Many patients love the result of a single session; a series of two to three spaced about a month apart delivers the most dramatic change, followed by a yearly boost."),
 "whyh2":"Why choose Serene for Harmony Bio-Boost in Hudson",
 "whypara":"Bio-Boost is only as good as the settings behind it. At Serene, treatments are physician-supervised, matched to your Fitzpatrick skin type, and planned from your own Alma IQ skin analysis &mdash; not a one-size-fits-all preset. Everything happens right here in Hudson.",
 "faqh2":"Harmony Bio-Boost FAQ",
 "faqs":[
   ("What is Harmony Bio-Boost?","It&rsquo;s a personalized, combination laser treatment on the Alma Harmony platform that uses bio-stimulation &mdash; energy that prompts your skin to produce its own new collagen and elastin &mdash; while clearing pigment and redness. Think of it as a laser facial that works from the inside out."),
   ("Is there downtime?","Minimal. Most people have mild redness for a day or so, and brown spots may darken and flake for several days. Makeup can usually be worn the next day, and you can return to your routine right away with sunscreen."),
   ("Does it hurt?","You&rsquo;ll feel warm snaps and heat, kept comfortable with cooling and, when needed, topical numbing. Sessions take about an hour."),
   ("How many treatments will I need?","Many patients see a visible difference after one session. For the best result we typically recommend two to three sessions about a month apart, then a maintenance boost once or twice a year."),
   ("How is Bio-Boost different from a photofacial or a laser facial?","A photofacial treats pigment and redness alone; a fractional laser facial treats texture alone. Bio-Boost combines both, plus a light resurfacing pass, in a single tailored visit &mdash; so tone, texture, and collagen are addressed together."),
   ("Is it safe for my skin tone?","Settings are matched to your Fitzpatrick skin type after your Alma IQ scan. Some steps are adjusted or omitted for deeper skin tones. Take the skin-type quiz on this page and we&rsquo;ll review the safest plan at your consultation."),
   ("Can I combine it with other treatments?","Yes &mdash; Bio-Boost pairs well with Botox, fillers, Skinvive, and medical-grade skincare. We&rsquo;ll sequence everything so each treatment gets the best result."),
 ],
 "related":["morpheus8","botox","fillers"],
 "pricing_html":_BB_RESULTS,
 "ctah2":"Ready to boost your skin&rsquo;s true potential?",
 "ctapara":"Book a Harmony Bio-Boost consultation with our Hudson team and start rebuilding your own collagen.",
},
]
