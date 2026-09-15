# -*- coding: utf-8 -*-
# Longevity & NAD+ (Niagen IV/injections, NAD+ IV/injections, longevity drips) — both locations.
# Added Sept 2026 (Olympia Pharmaceuticals products). Hudson-voice copy; Barboursville localizes it.
def _steps_l(a,b,c,d): return [("Consultation",a),("Treatment",b),("Results",c),("Maintenance",d)]

_LONGEVITY_PRICING = '''<section id="pricing" class="tint-blush">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Investment</div><h2>Longevity Menu &amp; Pricing</h2><p>Published pricing, no surprises. Every first visit includes a health screening with our medical team.</p></div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
      <div class="card reveal" style="text-align:center"><h3>Niagen&reg; IV &mdash; 500mg</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$499</strong>About a 1-hour infusion</p></div>
      <div class="card reveal" style="text-align:center"><h3>Niagen&reg; IV &mdash; 250mg</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$299</strong>A shorter introductory infusion</p></div>
      <div class="card reveal" style="text-align:center"><h3>Niagen&reg; Injection</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$55</strong>50mg per injection &middot; 10 for $499</p></div>
      <div class="card reveal" style="text-align:center"><h3>NAD+ IV</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$199 / $299</strong>250mg or 500mg &middot; a slower, longer infusion</p></div>
      <div class="card reveal" style="text-align:center"><h3>NAD+ Injection</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$35</strong>50mg per injection</p></div>
      <div class="card reveal" style="text-align:center"><h3>Longevity &amp; Glow Drips</h3><p><strong style="display:block;font-size:2.4rem;line-height:1.15;color:var(--plum);font-weight:600;margin:6px 0">$149</strong>Antioxidant &amp; vitamin IV blends</p></div>
    </div>
    <div class="prose reveal" style="text-align:center;max-width:720px;margin:28px auto 0">
      <p><strong>Add-on injections:</strong> Glutathione $35 &middot; CoQ10 $25 &middot; Vitamin D3 $25</p>
      <p style="font-size:.95rem;color:var(--ink)">Our Niagen&reg; and NAD+ treatments are prepared by a licensed compounding pharmacy. Compounded products are not FDA-approved, and individual results vary. A medical screening is required before treatment.</p>
    </div>
  </div>
</section>'''

PAGES4 += [
{
 "slug":"longevity","crumb":"Longevity &amp; NAD+","area_kw":"longevity and NAD+ care",
 "title":"NAD+ &amp; Niagen IV in Hudson, OH | Longevity | Serene Med Spa",
 "desc":"Longevity care in Hudson, OH: Niagen IV in about an hour, NAD+ IV from $199, injections from $35, and antioxidant drips. Physician-led at Serene Med Spa.",
 "ogtitle":"Longevity &amp; NAD+ Therapy in Hudson, OH",
 "ogdesc":"Niagen IV, NAD+ IV and injections, and longevity drips in Hudson, Ohio. Physician-led, with published pricing.",
 "proc_name":"NAD+ and Niagen (Nicotinamide Riboside) Therapy","proc_alt":"Longevity IV &amp; Injection Therapy",
 "how":"Niagen (nicotinamide riboside, a form of vitamin B3) or NAD+ is given by IV infusion or injection under medical supervision to help support healthy NAD+ levels.",
 "body":"Systemic (IV, intramuscular or subcutaneous)",
 "eyebrow":"Longevity &amp; NAD+ &middot; Hudson, OH",
 "h1":"Longevity &amp; NAD+ Therapy in Hudson, Ohio",
 "hero":"Support healthy NAD+ levels, cellular energy and healthy aging with physician-led Niagen&reg; and NAD+ treatments &mdash; including a Niagen IV that takes about an hour.",
 "trust":["Physician-Led","Niagen&reg; IV in About 1 Hour","Published Pricing","Health Screening First"],
 "introh2":"Why NAD+ matters as we age",
 "introlead":"NAD+ is a molecule every cell uses to make energy and keep itself healthy, and NAD+ levels naturally decline with age. Our longevity menu is built around helping support healthy NAD+ levels.",
 "intropara":"At Serene Med Spa in Hudson, you can choose Niagen&reg; (nicotinamide riboside, one of the most-researched NAD+ precursors) or NAD+ itself, as an IV infusion or a quick injection. Niagen IV infusions typically take about an hour, compared with the longer infusion times usually needed for NAD+. Every plan starts with a medical screening, and these treatments support wellness and healthy aging; they are not a treatment for any disease.",
 "treyebrow":"The Longevity Menu","treh2":"Treatments We Offer",
 "cards":[
   ("Niagen&reg; IV","A ready-to-use NAD+ precursor infusion, typically about an hour, to help support healthy NAD+ levels."),
   ("Niagen&reg; Injections","A quick in-office injection, often scheduled every few days as a series."),
   ("NAD+ IV","The classic NAD+ infusion, given slowly over a longer visit for comfort."),
   ("NAD+ Injections","A convenient in-office NAD+ injection for ongoing support between infusions."),
   ("Longevity Drip","An antioxidant and vitamin blend with N-acetyl cysteine, B12, B-complex and magnesium."),
   ("Glow Drip","Glutathione, vitamin C and alpha-lipoic acid, a favorite for skin and antioxidant support."),
 ],
 "steps":_steps_l(
   "We review your health history, medications and goals, and confirm which treatment is appropriate for you.",
   "You relax while your infusion or injection is given by our medical team. Niagen IV visits usually take about an hour.",
   "Many people report feeling more energized, but experiences vary. We&rsquo;ll check in on how you feel after each visit.",
   "Longevity care works best as a routine. We&rsquo;ll suggest a schedule, such as weekly infusions or an injection series."),
 "whyh2":"Why choose Serene for longevity care in Hudson",
 "whypara":"Longevity treatments should be physician-led and honest about what they can and can&rsquo;t do. At Serene, our board-certified physicians screen every patient, use products from a licensed pharmacy, and publish our pricing, right here in Hudson.",
 "faqh2":"Longevity &amp; NAD+ FAQ",
 "faqs":[
   ("What is NAD+?","NAD+ is a molecule your cells need to produce energy and stay healthy. Levels naturally decline with age, which is why supporting healthy NAD+ levels is a focus of longevity care."),
   ("How is Niagen&reg; different from NAD+?","Niagen&reg; is nicotinamide riboside, a form of vitamin B3 your body uses to make NAD+. It is one of the most-researched NAD+ precursors, and Niagen IV infusions typically take about an hour, while NAD+ infusions are usually given more slowly over a longer visit."),
   ("How much does it cost?","Niagen IV is $499 for 500mg or $299 for 250mg. Niagen injections are $55 each or 10 for $499. NAD+ IV is $199 for 250mg or $299 for 500mg, NAD+ injections (50mg) are $35, and our longevity and glow drips are $149. Add-on glutathione is $35, and CoQ10 or vitamin D3 injections are $25."),
   ("Who should not have these treatments?","Niagen and NAD+ are not recommended if you have active cancer or a history of cancer, or are pregnant or breastfeeding. Niagen is also not recommended with rheumatoid arthritis, and NAD+ is not recommended with uncontrolled heart disease. Please tell us if you take diabetes medications, blood thinners, blood pressure medications or opioids. We screen every patient before treatment."),
   ("Are these treatments FDA-approved?","Our Niagen&reg; and NAD+ treatments are prepared by a licensed compounding pharmacy. Compounded products are not FDA-approved or evaluated for safety or effectiveness, and results vary. They support general wellness and are not a treatment for any disease."),
   ("How often should I come in?","It depends on your goals. Common plans are a weekly Niagen IV or a Niagen injection every few days as a series. We&rsquo;ll recommend a schedule at your visit."),
 ],
 "related":["hormone-optimization","weight-loss","morpheus8"],
 "ctah2":"Ready to invest in how you age?",
 "ctapara":"Book a longevity visit with our Hudson team. We&rsquo;ll screen your health and build a Niagen&reg; or NAD+ plan around your goals.",
 "pricing_html":_LONGEVITY_PRICING,
},
]
