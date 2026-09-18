# -*- coding: utf-8 -*-
# aftercare_pages_data.py — standalone post-care instruction pages, one per treatment.
#
# Source: the 25-page "Aftercare" master deck in Canva (design DAHLdqRaDXo). Those pages are
# flat images with no extractable text, so each one was transcribed by reading the page.
# Transcribed 2026-09-18. If the Canva deck changes, re-transcribe — nothing here is generated.
#
# Each page renders at /aftercare/<slug>/ on both location sites. Mangomint post-care Flows
# link to these pages rather than trying to fit clinical instructions into an SMS.
#
# Schema:
#   slug      URL segment
#   name      treatment name as the client knows it
#   tagline   one line under the H1
#   blocks    [(heading, [bullet, ...]), ...]  main instruction columns
#   note      optional emphasised callout inside the blocks area
#   normal    [what is normal / expected]
#   urgent    [contact provider if ...]
#   outlook   closing line about results/timeline
#   services  site service slugs this aftercare applies to (for cross-linking)

AFTERCARE_PAGES = [

{
 "slug": "botox", "name": "Botox", "title": "Botox Aftercare",
 "tagline": "A few simple steps for beautiful, natural results.",
 "blocks": [
   ("First 4&ndash;6 Hours", [
     "Stay upright &mdash; avoid lying flat or bending over.",
     "Do not rub, massage, or press on the treated areas.",
     "Avoid hats, tight headbands, facials, or anything putting pressure on the area.",
     "Try to gently move the treated muscles (smile, frown, raise brows) for about 1 hour if your injector advised."]),
   ("First 24 Hours", [
     "Avoid strenuous exercise or workouts.",
     "Avoid alcohol (can increase bruising).",
     "Avoid excessive heat: saunas, hot tubs, steam rooms, very hot showers.",
     "Avoid makeup for several hours if instructed."]),
   ("First 48 Hours", [
     "Avoid facial massages, chemical peels, microneedling, or laser treatments.",
     "Sleep on your back if possible the first night.",
     "Avoid lying face down or applying pressure to the treated areas."]),
 ],
 "normal": ["Small bumps at injection sites (15&ndash;30 minutes)", "Mild swelling or redness",
            "Minor bruising", "Temporary headache or tight feeling"],
 "urgent": ["Drooping eyelid", "Trouble swallowing or breathing", "Vision changes",
            "Severe swelling or rash", "Marked facial asymmetry"],
 "outlook": "You may see early results in 3&ndash;5 days, with full results in up to 10&ndash;14 days.",
 "services": ["botox"],
},

{
 "slug": "dermal-filler", "name": "Dermal Filler", "title": "Filler Aftercare",
 "tagline": "Love your results, protect your investment.",
 "blocks": [
   ("First 24 Hours", [
     "Avoid touching, rubbing, or massaging the area.",
     "Apply ice packs for swelling (10 minutes on / 10 off).",
     "Stay hydrated.",
     "Sleep with your head elevated.",
     "Avoid strenuous exercise.",
     "Avoid alcohol and excessive salt.",
     "Avoid excessive heat &mdash; saunas, hot tubs, steam rooms, tanning beds."]),
   ("First 48 Hours", [
     "Avoid facials, massage, microneedling, chemical peels, and laser treatments.",
     "Avoid pressure on the area: face-down sleeping, tight goggles, excessive facial massage."]),
   ("Lips Specifically", [
     "Expect more swelling the next morning.",
     "Use a straw normally for the first day.",
     "Small lumps are often swelling and usually soften over 1&ndash;2 weeks."]),
 ],
 "normal": ["Swelling", "Bruising", "Tenderness", "Firmness", "Mild itching"],
 "urgent": ["Severe or increasing pain", "Skin turning white, dusky or mottled",
            "Vision changes", "Signs of infection"],
 "outlook": "Most swelling improves in 2&ndash;5 days.",
 "services": ["fillers", "lip-filler", "cheek-filler", "under-eye-filler", "jawline-filler", "chin-filler", "skinvive"],
},

{
 "slug": "laser-hair-removal", "name": "Laser Hair Removal", "title": "Laser Hair Removal Aftercare",
 "tagline": "Proper aftercare helps reduce irritation and protects your skin while it heals for the best, longest-lasting results.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Avoid excessive heat: hot tubs, saunas, steam rooms, and very hot showers.",
     "Avoid strenuous exercise or sweating.",
     "Wear loose, breathable clothing over treated areas.",
     "Do not scratch, pick, or exfoliate the skin.",
     "Avoid perfumed lotions or irritating products."]),
   ("Sun Protection", [
     "Avoid direct sun exposure for at least 1&ndash;2 weeks.",
     "Wear SPF 30+ daily on exposed areas.",
     "Do not use tanning beds or self-tanner before or after treatment."]),
   ("Skin Care", [
     "Use gentle cleansers and moisturizers.",
     "Aloe vera or cool compresses may help soothe redness.",
     "Avoid retinoids, glycolic acids, exfoliants and harsh scrubs for several days or until irritation resolves."]),
   ("Hair Shedding", [
     "Hair may appear to &ldquo;grow&rdquo; after treatment &mdash; this is normal shedding.",
     "Shedding typically starts within 1&ndash;3 weeks.",
     "Do not wax, tweeze, or thread between sessions.",
     "Shaving is okay if needed."]),
 ],
 "normal": ["Redness", "Mild swelling", "Warmth", "Sensitivity similar to a mild sunburn",
            "Temporary swelling around the follicles"],
 "urgent": ["Blistering", "Severe swelling", "Signs of infection", "Persistent burns",
            "Worsening pain", "Significant pigment changes"],
 "outlook": "Redness and swelling usually improve within hours to a few days. Consistency between treatments gives the best results.",
 "services": ["laser-hair-removal"],
},

{
 "slug": "laser-toenail-fungus", "name": "Laser Toenail Fungus Removal", "title": "Laser Toenail Fungus Removal Aftercare",
 "tagline": "Proper aftercare helps promote healthy nail growth and maximizes your laser treatment results.",
 "blocks": [
   ("Day of Treatment", [
     "You may resume normal activities immediately.",
     "Keep toenails clean and dry.",
     "Avoid tight-fitting shoes if tenderness occurs."]),
   ("First 24&ndash;48 Hours", [
     "Avoid soaking your feet in water (baths, pools, hot tubs).",
     "Do not apply nail polish or other topical products to the treated nails."]),
   ("First 7 Days", [
     "Wear breathable socks and well-fitting shoes.",
     "Continue to keep nails clean and dry.",
     "Do not pick, trim, or file the nail."]),
   ("First 2 Weeks", [
     "Avoid harsh chemicals and strong cleaning products.",
     "Do not use over-the-counter antifungal products unless advised by your provider."]),
   ("Ongoing Care", [
     "Maintain good foot hygiene.",
     "Change socks daily.",
     "Keep feet dry and breathable."]),
 ],
 "note": "Nails grow slowly. It may take several months to see full improvement as the healthy nail grows out, and healthy nail growth can take 6&ndash;12 months. Multiple treatments are usually recommended for best results.",
 "normal": ["Mild redness or warmth", "Slight tenderness or sensitivity", "Temporary nail thickening",
            "Nail may look worse before it looks better"],
 "urgent": ["Severe pain or discomfort", "Signs of infection", "Persistent swelling or heat",
            "Any concerns or unusual symptoms"],
 "outlook": "Be patient and consistent &mdash; healthy nails take time. Complete all recommended treatment sessions.",
 "services": ["laser-nail-fungus"],
},

{
 "slug": "tattoo-removal", "name": "Laser Tattoo Removal", "title": "Tattoo Removal Aftercare",
 "tagline": "Proper aftercare is essential for safe healing, minimizing complications, and achieving the best results.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Keep the treated area clean and dry.",
     "Apply a thin layer of healing ointment if instructed.",
     "Cover with a clean bandage if needed.",
     "Use cool compresses for comfort and relief.",
     "Avoid touching, scratching, or picking."]),
   ("Important Healing Instructions", [
     "Do <strong>not</strong> pop blisters.",
     "Do <strong>not</strong> pick scabs.",
     "Allow the skin to heal naturally to reduce the risk of scarring.",
     "Avoid tight or irritating clothing over the area."]),
   ("Avoid Until Healed", [
     "Swimming pools", "Hot tubs", "Saunas", "Excessive sweating",
     "Exfoliants", "Harsh skincare products"]),
   ("Sun Protection &amp; Skin Care", [
     "Avoid direct sun exposure while healing.",
     "Wear SPF 30+ once the skin has healed.",
     "Avoid tanning beds and self-tanner.",
     "Wash gently with mild soap and water; pat dry, do not rub.",
     "Keep the area moisturized if instructed by your provider."]),
 ],
 "normal": ["Redness", "Swelling", "Tenderness", "Blistering", "Pinpoint bleeding", "Scabbing", "Itching"],
 "urgent": ["Excessive swelling", "Pus or signs of infection", "Fever",
            "Worsening redness or warmth", "Severe pain", "Allergic reaction"],
 "outlook": "Initial healing takes about 1&ndash;2 weeks, and fading continues for several weeks after treatment. Multiple sessions are typically needed for best results.",
 "services": ["laser-tattoo-removal"],
},

{
 "slug": "hormone-pellets", "name": "Bi&ouml;te Hormone Replacement", "title": "Bi&ouml;te Hormone Replacement Aftercare",
 "tagline": "Proper aftercare helps reduce irritation and supports proper pellet absorption and healing.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Keep the bandage clean and dry.",
     "Leave steri-strips in place until they fall off naturally or as instructed.",
     "You may shower after 24 hours unless otherwise directed.",
     "Avoid soaking: baths, hot tubs, swimming pools, lakes and oceans."]),
   ("Activity Restrictions &mdash; 2 to 7 Days", [
     "Avoid strenuous lower-body exercise.",
     "Avoid squats, lunges, running, and heavy lifting.",
     "Limit excessive stretching of the gluteal area.",
     "Walking is encouraged."]),
   ("Incision Care", [
     "Do not pick at steri-strips or scabbing.",
     "Watch for signs of infection: spreading redness, warmth, drainage, fever."]),
   ("Hormone Expectations", [
     "Hormones do not work immediately.",
     "Many patients begin noticing improvement within 1&ndash;3 weeks.",
     "Full optimization may take 4&ndash;6 weeks.",
     "Temporary changes during adjustment can include mild acne, breast tenderness, mood changes, increased energy, and spotting in some women."]),
 ],
 "note": "Following the activity restrictions helps prevent pellet extrusion, bleeding, bruising and delayed healing.",
 "normal": ["Soreness at the insertion site", "Bruising", "Mild swelling",
            "Itching during healing", "A small lump under the skin"],
 "urgent": ["Fever", "Worsening redness or swelling", "Drainage or pus", "Severe pain",
            "Pellet coming through the skin", "Rash or allergic reaction"],
 "outlook": "Stay hydrated, follow your recommended lab schedule, and keep your follow-up appointments for hormone monitoring.",
 "services": ["hormone-optimization"],
},

{
 "slug": "bbl-hero", "name": "BBL HERO", "title": "BBL HERO Aftercare",
 "tagline": "Proper aftercare is essential to protect your skin, reduce irritation, and maximize your beautiful results.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Expect redness, warmth, and mild swelling.",
     "Use gentle cleanser and moisturizer.",
     "Avoid touching or scratching treated areas."]),
   ("Pigmented Spots &mdash; &ldquo;Coffee Grounds&rdquo;", [
     "Brown spots may darken temporarily before flaking off naturally.",
     "Do <strong>not</strong> pick or scrub."]),
   ("Avoid for Several Days", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools"]),
   ("Skin Care &amp; Sun Protection", [
     "Avoid until healed: retinoids/Retin-A, exfoliants, glycolic acids, scrubs, harsh actives.",
     "Avoid direct sun exposure.",
     "Wear SPF 30+ daily and reapply frequently.",
     "Avoid tanning beds and self-tanner.",
     "Avoid makeup for at least 24 hours if skin is intact; mineral makeup is preferred."]),
 ],
 "normal": ["Redness", "Swelling", "Warmth", "Temporary darkening"],
 "urgent": ["Blistering", "Severe swelling", "Signs of infection", "Worsening pain",
            "Unusual rash", "Persistent burns or pigment changes"],
 "outlook": "Redness and swelling typically settle in 1&ndash;3 days, pigment darkening and flaking take about 5&ndash;10 days, and improvement continues over several weeks.",
 "services": ["photofacial"],
},

{
 "slug": "moxi", "name": "Sciton MOXI", "title": "MOXI Aftercare",
 "tagline": "Proper aftercare helps protect your skin, minimize irritation, and optimize your glow and collagen stimulation results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Expect redness, warmth, and mild swelling.",
     "Use gentle cleanser and moisturizer.",
     "Keep skin hydrated.",
     "Avoid rubbing, scratching, or picking."]),
   ("&ldquo;MENDs&rdquo; &mdash; Tiny Dark Dots", [
     "Tiny dark spots called MENDs may appear as the skin heals.",
     "These are normal and expected.",
     "Do <strong>not</strong> scrub or pick them off.",
     "They typically flake away naturally within several days."]),
   ("Avoid for Several Days", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools"]),
   ("Skin Care &amp; Sun Protection", [
     "Avoid until healed: retinoids/Retin-A, exfoliants, glycolic acids, irritating vitamin C, scrubs, harsh actives.",
     "Avoid direct sun exposure before and after treatment.",
     "Wear SPF 30+ daily and reapply often.",
     "Avoid tanning beds and self-tanner.",
     "Avoid makeup for at least 24 hours if skin is intact; mineral makeup is preferred."]),
 ],
 "normal": ["Redness", "Swelling", "Dryness", "Rough texture", "Mild itching",
            "Temporary bronzing or darkening"],
 "urgent": ["Blistering", "Severe swelling", "Signs of infection",
            "Worsening redness or swelling", "Unusual rash", "Persistent burns or pigment changes"],
 "outlook": "Redness and swelling last 1&ndash;3 days and MENDs flake at about 3&ndash;7 days, with collagen remodeling and brightening continuing over several weeks.",
 "services": ["laser-skin"],
},

{
 "slug": "morpheus8", "name": "Morpheus8", "title": "Morpheus8 Aftercare",
 "tagline": "Proper aftercare is essential for healing, minimizing irritation, and optimizing collagen stimulation and results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Expect redness, warmth, swelling, and a sandpaper-like texture.",
     "Use gentle cleanser and moisturizer.",
     "Keep skin hydrated.",
     "Avoid touching or picking."]),
   ("Avoid for 48&ndash;72 Hours", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools", "Hot showers"]),
   ("Skin Care Restrictions", [
     "Avoid until fully healed: retinoids/Retin-A, exfoliants, glycolic acids, irritating vitamin C, scrubs, harsh actives.",
     "Avoid makeup for at least 24 hours or as directed; mineral makeup is preferred when restarting."]),
   ("Sun Protection &amp; Recovery", [
     "Avoid direct sun exposure.",
     "Wear SPF 30+ daily.",
     "Avoid tanning beds and self-tanner.",
     "Use gentle hydrating products and stay hydrated.",
     "Use cool compresses if needed."]),
 ],
 "note": "Heat can worsen swelling and irritation while you heal.",
 "normal": ["Redness", "Swelling", "Pinpoint marks or grid pattern", "Dryness and flaking",
            "Tightness", "Itching during healing"],
 "urgent": ["Severe pain", "Blistering", "Signs of infection",
            "Worsening redness or swelling", "Pus or drainage", "Fever"],
 "outlook": "Redness and swelling last 1&ndash;5 days. Collagen remodeling continues for months, and best results are usually seen after a series of treatments.",
 "services": ["morpheus8"],
},

{
 "slug": "opus-plasma", "name": "Opus Plasma", "title": "Opus Aftercare",
 "tagline": "Proper aftercare is essential for healing, minimizing irritation, and optimizing your skin rejuvenation results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Expect redness, warmth, swelling, and a rough texture.",
     "Use gentle cleanser and moisturizer.",
     "Keep skin hydrated.",
     "Avoid touching, rubbing, or picking.",
     "Sleep with your head elevated if swollen."]),
   ("Avoid for 48&ndash;72 Hours", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools", "Hot showers"]),
   ("Skin Care Restrictions", [
     "Avoid until fully healed: retinoids/Retin-A, exfoliants, glycolic acids, irritating vitamin C, scrubs, harsh actives.",
     "Avoid makeup for at least 24 hours or until irritation improves; mineral makeup is preferred."]),
   ("Sun Protection &amp; Recovery", [
     "Avoid direct sun exposure.",
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid tanning beds and self-tanner.",
     "Use gentle hydrating products and avoid picking flaking skin.",
     "Use cool compresses if needed."]),
 ],
 "normal": ["Redness", "Swelling", "Dryness and flaking", "Pinpoint marks",
            "Bronzing or darkening", "Tightness", "Itching during healing"],
 "urgent": ["Severe pain", "Blistering", "Signs of infection",
            "Worsening redness or swelling", "Pus or drainage", "Fever"],
 "outlook": "Redness and swelling last 1&ndash;5 days with several days of flaking. Collagen remodeling continues for months, and best results are often seen after a series of treatments.",
 "services": ["opus-plasma"],
},

{
 "slug": "pico-resurfacing", "name": "PICO Fractional Resurfacing", "title": "PICO Resurfacing Aftercare",
 "tagline": "Proper aftercare helps protect your skin, minimize irritation, and optimize collagen and skin rejuvenation results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Expect redness, warmth, mild swelling, and dryness.",
     "Skin may feel tight or rough.",
     "Use only gentle cleanser and moisturizer.",
     "Keep skin hydrated.",
     "Avoid rubbing, scratching, or picking at the skin."]),
   ("Avoid for Several Days", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools", "Hot showers"]),
   ("Skin Care Restrictions", [
     "Avoid until fully healed: retinoids/Retin-A, exfoliants, glycolic acids, irritating vitamin C, scrubs, harsh actives.",
     "Avoid makeup for at least 24 hours or until irritation improves; mineral makeup is preferred."]),
   ("Sun Protection &amp; Recovery", [
     "Avoid direct sun exposure.",
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid tanning beds and self-tanner.",
     "Use gentle hydrating products and avoid picking flaking skin."]),
 ],
 "normal": ["Redness", "Swelling", "Dryness and flaking", "Bronzing or darkening",
            "Tightness", "Mild itching during healing"],
 "urgent": ["Severe pain", "Blistering", "Signs of infection",
            "Worsening redness or swelling", "Pus or drainage", "Fever"],
 "outlook": "Redness and swelling last 1&ndash;5 days. Collagen remodeling continues for weeks to months, and best results are often seen after a series of treatments.",
 "services": ["laser-skin"],
},

{
 "slug": "hydrafacial", "name": "HydraFacial", "title": "HydraFacial Aftercare",
 "tagline": "Proper aftercare helps maintain hydration, protect your skin, and maximize your glow.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Expect your skin to feel fresh, hydrated, and radiant.",
     "Mild redness or tightness may occur temporarily.",
     "Avoid touching or picking at the skin.",
     "Keep skin hydrated with a gentle moisturizer."]),
   ("Avoid for 24&ndash;48 Hours", [
     "Strenuous exercise", "Excessive sweating", "Saunas",
     "Hot tubs", "Steam rooms", "Swimming pools"]),
   ("Skin Care Restrictions", [
     "Avoid for several days: retinoids/Retin-A, exfoliants, glycolic acids, scrubs, harsh actives.",
     "Avoid heavy makeup for at least 24 hours if possible; mineral makeup is preferred."]),
   ("Sun Protection &amp; Tips", [
     "Avoid excessive sun exposure.",
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid tanning beds and self-tanner.",
     "Drink plenty of water and use gentle skincare only.",
     "Avoid over-exfoliating."]),
 ],
 "note": "Heat and sweat can irritate freshly treated skin.",
 "normal": ["Mild redness", "Tightness", "Temporary sensitivity", "Increased glow and hydration"],
 "urgent": ["Prolonged irritation", "Rash", "Excessive swelling", "Blistering",
            "Signs of allergic reaction"],
 "outlook": "Any mild redness usually improves within hours to a day. Continue daily SPF to protect your results.",
 "services": ["hydrafacial", "sknlab", "medical-facials"],
},

{
 "slug": "co2-laser", "name": "CO&sup2; Laser Resurfacing", "title": "CO&sup2; Laser Resurfacing Aftercare",
 "tagline": "Proper aftercare is essential for healing, minimizing complications, and achieving your best results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Expect redness, swelling, warmth, and a sunburn-like sensation.",
     "Skin may feel tight, rough, or ooze slightly during early healing.",
     "Cleanse gently as directed.",
     "Keep skin continuously moisturized with the recommended ointment.",
     "Avoid touching, rubbing, or picking at the skin."]),
   ("Healing Instructions", [
     "Do <strong>not</strong> pick peeling or flaking skin.",
     "Allow skin to heal naturally.",
     "Sleep with your head elevated if swollen.",
     "Use cool compresses if needed for comfort."]),
   ("Avoid Until Fully Healed", [
     "Strenuous exercise", "Excessive sweating", "Saunas", "Hot tubs",
     "Steam rooms", "Swimming pools", "Direct sun exposure"]),
   ("Skin Care &amp; Sun Protection", [
     "Avoid until cleared by your provider: retinoids/Retin-A, exfoliants, glycolic acids, irritating vitamin C, scrubs, harsh actives.",
     "Avoid makeup until your provider approves; mineral makeup is preferred when restarting.",
     "Strict sun protection is essential &mdash; SPF 30+ daily once approved, reapplied regularly.",
     "Wear hats and avoid prolonged outdoor exposure.",
     "Avoid tanning beds and self-tanner."]),
 ],
 "normal": ["Redness", "Swelling", "Peeling and flaking", "Bronzing or crusting",
            "Dryness", "Itching during healing", "Temporary sensitivity"],
 "urgent": ["Severe pain", "Fever", "Worsening redness or warmth", "Worsening swelling",
            "Signs of infection", "Pus or drainage", "Unusual blistering"],
 "outlook": "Initial healing takes about 5&ndash;10 days and redness may persist for several weeks. Collagen remodeling continues for months, with results improving over time.",
 "services": ["laser-skin", "alma-hybrid"],
},

{
 "slug": "alma-duo", "name": "Alma Duo", "title": "Alma Duo Aftercare",
 "tagline": "Proper aftercare helps support healing, circulation, and optimal treatment results.",
 "blocks": [
   ("First 24 Hours", [
     "You may resume most normal daily activities immediately.",
     "Mild soreness or tenderness may occur temporarily.",
     "Stay hydrated.",
     "Avoid excessive pressure or friction to the treated area."]),
   ("Avoid for 24&ndash;48 Hours", [
     "Strenuous exercise", "Excessive heat", "Hot tubs", "Saunas",
     "Prolonged cycling or pressure to the area"]),
   ("Helpful Recovery Tips", [
     "Drink plenty of water.",
     "Maintain healthy circulation with light activity and walking.",
     "Follow your provider&rsquo;s treatment schedule for best results.",
     "Healthy lifestyle habits may improve outcomes."]),
 ],
 "normal": ["Mild soreness", "Temporary sensitivity", "Tingling sensation",
            "Mild swelling", "Temporary warmth"],
 "urgent": ["Severe pain", "Worsening swelling", "Bruising that worsens",
            "Signs of infection", "Unusual or persistent symptoms"],
 "outlook": "Results may improve gradually over several weeks. Multiple sessions are often recommended, and consistency matters.",
 "services": ["alma-duo", "mens-sexual-wellness", "womens-sexual-wellness"],
},

{
 "slug": "forma", "name": "Forma", "title": "Forma Aftercare",
 "tagline": "Proper aftercare helps optimize your results, support healing, and keep you comfortable.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Avoid strenuous exercise.",
     "Avoid excessive heat &mdash; no saunas, hot tubs, steam rooms, or tanning.",
     "Avoid alcohol and excessive caffeine.",
     "Stay hydrated."]),
   ("Skin Care Guidelines", [
     "Use gentle cleanser and moisturizer.",
     "Avoid active ingredients (retinol, acids, exfoliants) for 3&ndash;5 days.",
     "Do not use harsh products or scrubs."]),
   ("Sun Protection &amp; Makeup", [
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid direct sun exposure.",
     "No tanning beds or self-tanner.",
     "You may wear mineral makeup the next day.",
     "Avoid heavy makeup if skin is still sensitive."]),
 ],
 "normal": ["Mild warmth", "Redness", "Swelling", "Slight tightness or sensitivity"],
 "urgent": ["Severe pain", "Increased redness or swelling", "Blistering or skin irritation",
            "Signs of infection", "Any concerns or discomfort"],
 "outlook": "Symptoms typically improve within a few hours to a few days. Collagen remodeling continues for weeks to months.",
 "services": ["forma"],
},

{
 "slug": "o-shot", "name": "O-Shot", "title": "O-Shot Aftercare",
 "tagline": "Proper aftercare helps support healing, comfort, and optimal results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Mild swelling, tenderness, or sensitivity is normal.",
     "Apply ice packs intermittently for comfort.",
     "Keep the area clean and dry.",
     "Wear supportive underwear.",
     "Stay hydrated."]),
   ("Avoid for 3&ndash;5 Days", [
     "Sexual activity", "Strenuous exercise", "Heavy lifting",
     "Biking or horse riding", "Aspirin, NSAIDs, and alcohol"]),
   ("Hygiene Care", [
     "Keep the area clean and dry.",
     "Use gentle cleansing only.",
     "Avoid harsh soaps, lotions, or fragrances.",
     "Do not submerge in water (baths, hot tubs, pools) for 3&ndash;5 days.",
     "Wear loose, breathable clothing."]),
 ],
 "note": "These restrictions help prevent increased swelling, irritation and bruising.",
 "normal": ["Mild swelling", "Tenderness", "Temporary sensitivity"],
 "urgent": ["Severe pain", "Excessive swelling", "Signs of infection",
            "Unusual discharge", "Any concerns or unusual symptoms"],
 "outlook": "Results may continue to improve over several weeks. A series of treatments may be recommended, and results vary for each individual.",
 "services": ["womens-sexual-wellness"],
},

{
 "slug": "p-shot", "name": "P-Shot", "title": "P-Shot Aftercare",
 "tagline": "Following these aftercare instructions helps support healing and optimize your results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Mild swelling, bruising, or sensitivity is normal.",
     "Apply cold packs for comfort.",
     "Wear supportive underwear.",
     "Avoid strenuous activity.",
     "Stay hydrated."]),
   ("Avoid for 3&ndash;5 Days", [
     "Sexual activity", "Strenuous exercise", "Heavy lifting",
     "Bicycling or activities that put pressure on the area",
     "Hot tubs, saunas, and swimming pools"]),
   ("Hygiene &amp; Helpful Tips", [
     "You may shower gently.",
     "Avoid harsh soaps, lotions, or irritants on the area.",
     "Do not massage the area.",
     "Drink plenty of water and eat a healthy, balanced diet.",
     "Avoid alcohol and smoking for 24&ndash;48 hours."]),
 ],
 "normal": ["Mild swelling", "Bruising", "Temporary sensitivity"],
 "urgent": ["Severe pain", "Excessive swelling", "Signs of infection",
            "Any concerns or unusual symptoms"],
 "outlook": "You may notice improved sensitivity and performance over the next few weeks. Follow-up treatments may be recommended for optimal results.",
 "services": ["mens-sexual-wellness"],
},


{
 "slug": "pdo-threads", "name": "PDO Thread Lift", "title": "PDO Threads Aftercare",
 "tagline": "Proper aftercare helps support healing, minimize swelling, and optimize your results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Mild swelling, bruising, tenderness, or tightness is normal.",
     "Apply cold packs intermittently for comfort.",
     "Keep your head elevated when resting.",
     "Stay hydrated."]),
   ("Avoid for 7&ndash;14 Days", [
     "Strenuous exercise", "Heavy lifting",
     "Excessive facial expression or wide mouth movements",
     "Alcohol", "Smoking", "Sleeping on your face"]),
   ("Skin Care Guidelines", [
     "Use gentle cleanser and moisturizer.",
     "Avoid active ingredients (retinols, acids, exfoliants) for 5&ndash;7 days.",
     "Do not use harsh products or scrubs."]),
   ("Sun Protection &amp; Tips", [
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid direct sun exposure for at least 7 days.",
     "Be gentle with your skin and sleep on your back when possible.",
     "Drink plenty of water."]),
 ],
 "note": "These restrictions help prevent increased swelling and discomfort, and protect your result.",
 "normal": ["Mild swelling", "Bruising", "Tenderness", "Tightness"],
 "urgent": ["Severe pain", "Excessive swelling", "Asymmetry that worsens",
            "Any concerns or unusual symptoms"],
 "outlook": "Results improve gradually over several weeks as collagen builds, with optimal results in 2&ndash;3 months. Results can last 12&ndash;18 months or longer with proper care.",
 "services": ["thread-lift"],
},

{
 "slug": "chemical-peel", "name": "Chemical Peel", "title": "Post-Peel Aftercare",
 "tagline": "Proper aftercare helps support healing, protect your skin, and enhance your results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Keep skin clean and dry.",
     "Use only gentle cleanser and moisturizer.",
     "Avoid touching, picking, or peeling.",
     "Stay hydrated.",
     "You may resume normal activities as tolerated."]),
   ("Skin Care Guidelines", [
     "Use gentle cleanser and soothing moisturizer.",
     "Avoid active ingredients (retinol, acids, exfoliants) for 3&ndash;5 days.",
     "Do not use harsh products or scrubs."]),
   ("Sun Protection &amp; Tips", [
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid direct sun exposure and heat for 3&ndash;7 days.",
     "No tanning beds or self-tanner.",
     "Keep skin moisturized and drink plenty of water.",
     "Avoid excessive heat, sweating, and friction."]),
 ],
 "normal": ["Mild redness", "Tightness", "Sensitivity", "Peeling or flaking"],
 "urgent": ["Severe pain", "Worsening redness", "Swelling",
            "Signs of infection", "Any concerns or unusual symptoms"],
 "outlook": "Symptoms typically improve within a few days to one week. Skin appears brighter and smoother as it heals, and a series of treatments may be recommended.",
 "services": ["chemical-peels", "hyperpigmentation"],
},

{
 "slug": "sculptra", "name": "Sculptra", "title": "Sculptra Aftercare",
 "tagline": "Following these aftercare instructions helps ensure beautiful, natural-looking results.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Mild swelling, redness, tenderness, or bruising at the injection sites is normal.",
     "Avoid touching, rubbing, or applying pressure to the area.",
     "Avoid strenuous exercise, heat, and alcohol.",
     "Stay hydrated."]),
   ("Massage &mdash; the 5-5-5 Rule", [
     "Massage the treated area <strong>5 minutes, 5 times a day, for 5 days</strong>.",
     "Use firm pressure.",
     "This helps Sculptra distribute evenly and supports optimal results."]),
   ("Skin Care Guidelines", [
     "Use gentle cleanser and moisturizer.",
     "Avoid active ingredients (retinol, acids, exfoliants) for 24&ndash;48 hours.",
     "Do not use harsh products or scrubs for 48 hours.",
     "You may wear makeup after 24 hours."]),
   ("Sun Protection", [
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid direct sun exposure for at least 24 hours.",
     "Drink plenty of water and maintain a healthy lifestyle to support collagen production."]),
 ],
 "normal": ["Mild swelling", "Redness", "Tenderness", "Bruising at injection sites"],
 "urgent": ["Severe pain", "Excessive swelling", "Any concerns or unusual symptoms"],
 "outlook": "Results develop gradually as collagen builds, with optimal results in 6&ndash;12 weeks. A series of treatments is recommended and results can last 2 years or longer.",
 "services": ["sculptra", "sculptra-bbl"],
},

{
 "slug": "vtone", "name": "Vtone", "title": "Vtone Aftercare",
 "tagline": "Proper aftercare helps support healing, comfort, and optimal results from your Vtone treatment.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Avoid strenuous exercise.",
     "Avoid excessive heat (saunas, hot tubs).",
     "Avoid tight clothing or friction.",
     "Stay hydrated.",
     "You may resume normal activities as tolerated."]),
   ("Skin Care Guidelines", [
     "Use gentle cleanser and moisturizer.",
     "Avoid active ingredients (retinols, acids, exfoliants) for 2&ndash;3 days.",
     "Do not use harsh products."]),
   ("Sun Protection &amp; Tips", [
     "Wear SPF 30+ daily and reapply regularly.",
     "Avoid direct sun exposure for 24&ndash;48 hours.",
     "No tanning beds or self-tanner.",
     "Drink plenty of water and maintain a healthy lifestyle."]),
 ],
 "normal": ["Mild warmth", "Tingling", "Sensitivity", "Slight redness"],
 "urgent": ["Severe pain", "Increased redness or swelling",
            "Signs of infection", "Any concerns or discomfort"],
 "outlook": "Symptoms typically resolve within a few hours to a day. Improvement continues over time, and a series of treatments is often recommended.",
 "services": ["womens-sexual-wellness"],
},

{
 "slug": "waxing", "name": "Waxing", "title": "Waxing Aftercare",
 "tagline": "Proper aftercare helps soothe the skin, prevent irritation, and maintain smooth results.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Redness and sensitivity are normal.",
     "Avoid touching or scratching the area.",
     "Wear loose, breathable clothing.",
     "Apply a cool compress if needed."]),
   ("Avoid for 24&ndash;48 Hours", [
     "Hot showers or baths", "Saunas and steam rooms", "Swimming",
     "Intense workouts", "Direct sun exposure", "Tanning beds"]),
   ("Skin Care Guidelines", [
     "Keep the area clean and dry.",
     "Use gentle, fragrance-free products.",
     "Avoid exfoliants, retinoids, acids, and harsh scrubs for 2&ndash;3 days.",
     "Moisturize daily to keep skin soft and healthy."]),
   ("Sun Protection &amp; Tips", [
     "Avoid direct sun exposure for 48&ndash;72 hours.",
     "Use SPF 30+ if the area will be exposed.",
     "Exfoliate gently after 2&ndash;3 days to help prevent ingrown hairs.",
     "Stay hydrated and wear loose clothing."]),
 ],
 "note": "Heat, sweat, and friction can cause irritation or breakouts, and sun exposure can cause irritation and dark spots.",
 "normal": ["Redness", "Sensitivity", "Mild tenderness"],
 "urgent": ["Severe redness or swelling", "Bumps or pustules", "Rash or irritation",
            "Signs of infection", "Any concerns or unusual symptoms"],
 "outlook": "Consistent waxing helps maintain smooth, healthy skin.",
 "services": ["waxing"],
},

{
 "slug": "alma-ted", "name": "Alma TED Hair Restoration", "title": "Alma TED Aftercare",
 "tagline": "Proper aftercare helps support healing, minimize irritation, and optimize your results.",
 "blocks": [
   ("First 24&ndash;72 Hours", [
     "Mild redness, swelling, or tenderness is normal.",
     "Keep the area clean and dry.",
     "Apply a cool compress as needed.",
     "Stay hydrated."]),
   ("Avoid for 3&ndash;5 Days", [
     "Hot baths, saunas, and steam rooms", "Swimming",
     "Strenuous exercise", "Alcohol and excessive caffeine"]),
   ("Hair &amp; Scalp Care", [
     "Use gentle, fragrance-free cleansers.",
     "Avoid actives such as retinol, acids, and exfoliants for 3&ndash;5 days.",
     "No harsh scrubs or aggressive products.",
     "Moisturize daily to support the skin barrier."]),
   ("Sun Protection &amp; Tips", [
     "Avoid direct sun exposure for 7 days.",
     "Wear SPF 30+ daily.",
     "Use protective clothing and a hat.",
     "Drink plenty of water and follow your provider&rsquo;s treatment plan."]),
 ],
 "normal": ["Mild redness", "Swelling", "Tenderness"],
 "urgent": ["Severe pain", "Excessive swelling", "Signs of infection",
            "Burning or unusual irritation", "Any concerns or worsening symptoms"],
 "outlook": "You may notice gradual improvement over the next few weeks, and results continue to improve with proper aftercare and a full treatment plan.",
 "services": ["alma-ted", "prp-hair-restoration"],
},

{
 "slug": "brow-tint-lamination", "name": "Brow Tint &amp; Lamination", "title": "Brow Tint &amp; Lamination Aftercare",
 "tagline": "Proper aftercare helps maintain your results and keep your brows healthy and beautiful.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Keep brows dry.",
     "Avoid water, steam, sweat, and saunas.",
     "Do not apply makeup, skincare, or oils to the brow area.",
     "Avoid touching or rubbing your brows."]),
   ("Days 2&ndash;7", [
     "Continue to keep brows clean and dry.",
     "Avoid exfoliating products and active ingredients around the brow area.",
     "Do not use retinol, acids, or harsh skincare near brows."]),
   ("Ongoing Care", [
     "Brush brows gently into place daily.",
     "Avoid oil-based products directly on brows.",
     "Book regular touch-ups to maintain your results."]),
 ],
 "normal": ["Mild sensitivity around the brow area"],
 "urgent": ["Redness or irritation that does not settle", "Signs of allergic reaction",
            "Any concerns"],
 "outlook": "Results may last 4&ndash;6 weeks. Proper aftercare helps your tint last longer and your brows stay in place.",
 "services": ["brow-lamination"],
},

{
 "slug": "lash-lift-tint", "name": "Lash Lift &amp; Tint", "title": "Lash Lift &amp; Tint Aftercare",
 "tagline": "Proper aftercare helps maintain your results and keeps your lashes healthy and beautiful.",
 "blocks": [
   ("First 24&ndash;48 Hours", [
     "Keep lashes dry.",
     "Avoid water, steam, sweat, and saunas.",
     "Do not rub or touch your eyes.",
     "Avoid eye makeup, mascara, and eyelash serums."]),
   ("Days 2&ndash;7", [
     "Continue to keep lashes clean and dry.",
     "Avoid oil-based products and heavy eye creams.",
     "Be gentle when cleansing around the eye area."]),
   ("Ongoing Care", [
     "Use oil-free makeup remover.",
     "Brush lashes gently with a clean spoolie.",
     "Book regular lifts to maintain your results."]),
 ],
 "normal": ["Mild sensitivity around the eye area"],
 "urgent": ["Eye redness or irritation that does not settle",
            "Signs of allergic reaction", "Any concerns"],
 "outlook": "Results typically last 6&ndash;8 weeks and tint may last up to 4 weeks. Lash serums can be used after 48 hours.",
 "services": ["lash-lift"],
},

]
