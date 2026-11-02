# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzzzzz_sciton_hudson.py — Sciton Halo, BBL HEROic and MOXI arrive in Hudson (Robin, Nov 1 2026;
# device delivered Tue Nov 3). Adds /halo/, un-hides /sciton-moxi/ (see gen_pages.py SKIP) and adds BBL HEROic to /photofacial/.
# Hudson-only file. November launch pricing: Halo $1,199 (reg. $1,399), Halo + BBL $1,399 (reg. $1,799),
# BBL + MOXI $750 (reg. $900), BBL HEROic buy 3 get 1 free. Standing prices: Halo $1,399, BBL HEROic $400, MOXI $500.

if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_HALO, _HALO_REG, _HALO_BBL, _HALO_BBL_REG, _BBL, _MOXI = "$1,199", "$1,399", "$1,399", "$1,799", "$400", "$500"

if "HERO_MAP" in globals():
    HERO_MAP["halo"] = "laser"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.setdefault("halo", "/img/laser.jpg")
    RELATED_META["halo"] = ("Halo Hybrid Laser", "Tone, texture, pores and sun damage in one treatment. Launch pricing " + _HALO + ".")
    RELATED_META.setdefault("coolpeel", ("CoolPeel CO&sup2;", "Light CO&sup2; resurfacing with a few days of peeling. $400."))
    RELATED_META.setdefault("sciton-moxi", ("MOXI", "The lunchtime laser: brighter tone with 1&ndash;2 days of downtime. " + _MOXI + "."))
    IMG.setdefault("sciton-moxi", "/img/aftercare-moxi.jpg")
    IMG.setdefault("coolpeel", "/img/laser.jpg")

_HALO_NOTE = ('November launch pricing is good through November 30, 2026 and can&rsquo;t be combined with another discount. '
              'The consultation is complimentary. See the full <a href="/pricing/">price list</a>.')

PAGES6 += [
{
 "slug":"halo","crumb":"Halo","area_kw":"Halo hybrid fractional laser",
 "title":"Halo Laser in Hudson, OH | Sciton Halo from $1,199 | Serene",
 "desc":"Sciton Halo hybrid fractional laser in Hudson, Ohio: ablative and non-ablative wavelengths in one pass for tone, texture, pores, fine lines and sun damage with about 5 days of downtime. November launch pricing $1,199 (regularly $1,399). Physician-led.",
 "ogtitle":"Halo Hybrid Laser in Hudson, OH","ogdesc":"The Halo glow: tone, texture, pores and sun damage in one treatment, about five days of downtime. Now in Hudson from $1,199.",
 "proc_name":"Halo Hybrid Fractional Laser Resurfacing","proc_alt":"Sciton Halo dual-wavelength (1470 nm non-ablative + 2940 nm ablative) fractional laser",
 "how":"Halo delivers a non-ablative 1470 nm wavelength and an ablative 2940 nm wavelength through the same handpiece, treating the deeper dermis for collagen and pigment while lightly resurfacing the surface, so you get the result of a deeper laser with far less downtime.","body":"Face, neck, chest, hands",
 "eyebrow":"Halo &middot; New in Hudson, OH","h1":"Halo Hybrid Laser in Hudson, Ohio",
 "hero":"The laser people fly to other cities for is now in Hudson. Halo treats tone, texture, pores, fine lines and sun damage in one visit, with about five days of downtime and the famous &ldquo;Halo glow&rdquo; by day seven. November launch pricing: " + _HALO + " (regularly " + _HALO_REG + ").",
 "trust":["Two Wavelengths, One Pass","About 5 Days Downtime","Face, Neck, Chest &amp; Hands","Launch Pricing " + _HALO],
 "introh2":"Resurfacing results without the resurfacing week",
 "introlead":"Halo is Sciton&rsquo;s hybrid fractional laser. It combines a non-ablative wavelength that remodels collagen and breaks up pigment deep in the skin with an ablative wavelength that gently renews the surface. Older lasers made you choose between a dramatic result and a short recovery; Halo gives you both.",
 "intropara":"At Serene Med Spa in Hudson, Halo is the treatment we recommend when you want visible change from a single session: sun damage and uneven tone, enlarged pores, rough texture, fine lines and dull skin. Most patients take about five days of social downtime, see the glow by the end of week one, and keep improving for three months as new collagen builds. Your physician sets the depth and density to your skin and your goals, and can pair it with BBL HEROic in the same visit for redness and brown spots.",
 "treyebrow":"Who It Helps","treh2":"Good Candidates",
 "cards":[
   ("Sun Damage &amp; Uneven Tone","Freckling, brown spots and blotchy tone on the face, neck, chest and hands."),
   ("Enlarged Pores &amp; Texture","Visibly smaller pores and smoother skin, the signature Halo result."),
   ("Fine Lines","Softens fine lines around the eyes, mouth and cheeks with one treatment."),
   ("Dull Skin","Restores reflectivity &mdash; the &ldquo;Halo glow&rdquo; patients describe."),
   ("Acne Scars","Shallow scars improve over a series as collagen remodels."),
   ("Busy Schedules","One treatment, about five days of downtime, no bandages or ointment week."),
 ],
 "steps":_steps(
   "Your physician assesses your skin type, concerns and how much downtime you can take, then sets Halo&rsquo;s depth and density to match. A Fitzpatrick skin-type check keeps settings safe.",
   "Numbing cream for 45&ndash;60 minutes, then 30&ndash;45 minutes of passes with cooling. Most describe it as heat and prickling; the treatment ends with a cooling mask.",
   "Expect sunburn-like redness and swelling for 2&ndash;3 days, then a sandpaper feel as microscopic dots (MENDs) lift off around days 3&ndash;5. The glow shows by day 7 and keeps improving for 3 months.",
   "One treatment gives a visible result; a second Halo at 3&ndash;6 months or yearly maintenance keeps it. Sunscreen daily."),
 "whyh2":"Why choose Serene for Halo in Hudson",
 "whypara":"Halo results depend on choosing the right settings for your skin, and our board-certified physicians set and perform every treatment. We publish our pricing, the consultation is complimentary, and we can pair Halo with BBL HEROic or MOXI on the same Sciton platform when that gives you more.",
 "faqh2":"Halo FAQ",
 "faqs":[
   ("How much does Halo cost?","November 2026 launch pricing at Serene Med Spa in Hudson is " + _HALO + " for the full face (regularly " + _HALO_REG + "). Halo plus a BBL HEROic photofacial in the same visit is " + _HALO_BBL + " (regularly " + _HALO_BBL_REG + ")."),
   ("What is the downtime?","About five days. Days one to three bring redness and swelling like a sunburn; days three to five the skin feels rough as the treated dots slough off; by day seven most patients are glowing and wearing makeup."),
   ("Does Halo hurt?","With an hour of numbing cream and integrated cooling, most patients rate it a 4&ndash;6 out of 10: heat and prickling rather than pain. No anesthesia is needed."),
   ("How many treatments do I need?","Most people see a clear result after one. Deeper texture or acne scarring may take two, spaced three to six months apart. Many patients repeat Halo yearly."),
   ("Halo vs. MOXI?","MOXI is gentler, non-ablative, with one to two days of downtime, ideal for prevention and maintenance. Halo adds an ablative wavelength for a stronger single-visit result on texture, pores and lines, with about five days of downtime."),
   ("Halo vs. CO&sup2; laser?","Our Deka CO&sup2; goes deeper for etched lines and significant scarring and needs 7&ndash;10 days of healing. Halo delivers most of the visible improvement with half the downtime and is safe on more skin types."),
   ("Can Halo be combined with BBL?","Yes, and it&rsquo;s our favorite pairing: BBL HEROic clears redness and brown spots while Halo handles texture and lines. We do both in one visit."),
   ("Is Halo safe for darker skin?","Halo can be tuned for most skin types; your physician will confirm settings at your consultation. For the deepest skin tones we often recommend MOXI instead."),
 ],
 "related":["sciton-moxi","photofacial","coolpeel"],
 "pricing_html":_price_block("Launch Pricing","Halo pricing in Hudson",[
   ("Halo &mdash; Full Face", _HALO + " / treatment", "Regularly " + _HALO_REG + " &middot; November launch pricing"),
   ("Halo + BBL HEROic (same visit)", _HALO_BBL, "Regularly " + _HALO_BBL_REG + " &middot; texture, lines, redness and brown spots together"),
   ("BBL HEROic Photofacial", _BBL + " / session", "Buy 3, get 1 free in November"),
   ("MOXI", _MOXI + " / treatment", "BBL + MOXI same visit $750 (regularly $900)"),
   ("Add Neck, Chest or Hands", "Quoted at your consultation", ""),
   ("Consultation", "Complimentary", "No commitment"),
 ], _HALO_NOTE),
 "ctah2":"Ready for the Halo glow?","ctapara":"Book a complimentary Halo consultation with our Hudson physicians. Treatments begin November 3.",
},
]

# /photofacial/ in Hudson named only Lumecca Peak; add Sciton BBL HEROic now that the platform is here.
for _pg in [x for _l in ("PAGES","PAGES2","PAGES3","PAGES4","PAGES5","PAGES6") for x in globals().get(_l, [])]:
    if _pg.get("slug") == "photofacial" and "Sciton BBL HEROic" not in _pg.get("intropara", ""):
        _pg["intropara"] = _pg.get("intropara", "") + " As of November 2026, Hudson also offers <strong>Sciton BBL HEROic</strong>, the broadband light platform that pairs with Halo and MOXI: " + _BBL + " per session, buy 3 get 1 free in November, and BBL + MOXI in the same visit for $750."
        _pg["faqs"] = list(_pg.get("faqs", [])) + [("Do you have Sciton BBL in Hudson?", "Yes. Sciton BBL HEROic arrived in Hudson in November 2026 alongside Halo and MOXI. BBL HEROic is " + _BBL + " per session, buy 3 get 1 free through November 30, or $750 with MOXI in the same visit.")]
