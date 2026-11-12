# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzzzzzz_regenerative.py — Exosome and PDRN regenerative microneedling pages (Nov 2 2026).
# Prices from Mangomint: Microneedling with Exosomes $299 (serviceId 18), Microneedling with PDRN $299 (116),
# Vampire Facial / PRP $299, 3 for $799 (16), Under-Eye PRP/PRF $400 (333), Exosomes add-on $100 (add-on to any treatment).
# Hudson-only file (Hudson, OH).

if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_EXO, _PDRN, _PRP, _PRP3, _UE, _ADDON = "$299", "$299", "$299", "$799", "$400", "$100"

if "HERO_MAP" in globals():
    HERO_MAP["exosomes"] = "morpheus8"; HERO_MAP["pdrn"] = "morpheus8"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.setdefault("exosomes", "/img/morpheus8.jpg"); IMG.setdefault("pdrn", "/img/morpheus8.jpg"); IMG.setdefault("microneedling", "/img/morpheus8.jpg"); IMG.setdefault("skinvive", "/img/filler-inject.jpg")
    RELATED_META["exosomes"] = ("Exosome Microneedling", "Lab-grown growth-factor signals for faster healing and a brighter result. " + _EXO + ".")
    RELATED_META.setdefault("microneedling", ("Microneedling &amp; PRP", "Classic collagen induction, with optional PRP."))
    RELATED_META.setdefault("skinvive", ("Skinvive", "Injectable hyaluronic-acid skin booster for lasting glow."))
    RELATED_META["pdrn"] = ("PDRN (Salmon DNA) Microneedling", "The Korean &ldquo;salmon DNA&rdquo; skin booster, delivered by microneedling. " + _PDRN + ".")

_REGEN_NOTE = ('All regenerative microneedling treatments are performed by our physician-led team. Prices are per treatment; a series of three '
               'spaced four to six weeks apart gives the best result. See the full <a href="/pricing/">price list</a>.')

PAGES6 += [
# ---------------- EXOSOME MICRONEEDLING ----------------
{
 "slug":"exosomes","crumb":"Exosome Microneedling","area_kw":"exosome microneedling and regenerative skin treatments",
 "title":"Exosome Microneedling in Hudson, OH | $299 | Serene Med Spa",
 "desc":"Microneedling with exosomes in Hudson, Ohio: lab-derived growth-factor signals applied over fresh micro-channels for faster healing, brighter tone and smoother texture. $299 per treatment, or add exosomes to any laser or Morpheus8 for $100. Physician-led.",
 "ogtitle":"Exosome Microneedling in Hudson, OH","ogdesc":"The regenerative facial: microneedling plus exosomes for smoother, brighter skin with less downtime. $299 at Serene Med Spa.",
 "proc_name":"Microneedling with Exosomes","proc_alt":"Exosome skin regeneration, exosome facial",
 "how":"Microneedling opens thousands of controlled micro-channels; a topical exosome serum is applied immediately so the growth-factor and signaling cargo inside the exosomes reaches the dermis, where it tells your own cells to calm inflammation, build collagen and repair faster.","body":"Face, neck, chest, hands, scalp",
 "eyebrow":"Exosomes &middot; Regenerative Aesthetics &middot; Hudson, OH","h1":"Exosome Microneedling in Hudson, Ohio",
 "hero":"Exosomes are the signals your cells use to tell each other to repair. Applied over microneedling, they shorten the redness, deepen the result and leave skin visibly smoother and brighter. " + _EXO + " per treatment at Serene Med Spa, or add exosomes to any laser or Morpheus8 session for " + _ADDON + ".",
 "trust":["Faster Healing","Brighter, Smoother Skin","Add to Any Laser","Physician-Led"],
 "introh2":"Regenerative medicine for your skin",
 "introlead":"Exosomes are tiny vesicles released by cells that carry growth factors, peptides and genetic messengers. In aesthetics they are purified from lab-grown stem-cell cultures (never from another person&rsquo;s blood) and applied to skin that has just been microneedled, so the signals get past the surface and into the dermis where collagen is made.",
 "intropara":"At Serene Med Spa in Hudson, exosome microneedling is the treatment we recommend when you want more than a standard microneedling result: less downtime, a more even tone, softer fine lines and a glow that keeps building for weeks. Because exosomes are a topical, they also pair beautifully with our lasers and Morpheus8 &mdash; many patients add them to a resurfacing treatment to cut recovery time roughly in half. The treatment is comfortable with numbing cream, takes about an hour, and most people are back to normal the next day.",
 "treyebrow":"What It Improves","treh2":"Concerns We Target",
 "cards":[
   ("Dull, Tired Skin","A visible glow within a week as inflammation settles and cell turnover picks up."),
   ("Fine Lines &amp; Texture","Collagen stimulation from microneedling, amplified by exosome signaling."),
   ("Uneven Tone &amp; Redness","Exosomes calm inflammation, which helps blotchy tone and post-treatment redness."),
   ("Acne Scars &amp; Pores","Over a series, pitted scarring softens and pores look smaller."),
   ("Post-Laser Recovery","Added after Halo, MOXI, CO&sup2; or Morpheus8 to speed healing and reduce downtime."),
   ("Thinning Hair","Applied to the scalp with microneedling as part of a hair-restoration plan."),
 ],
 "steps":_steps(
   "We look at your skin, your goals and how much downtime you can take, then decide between exosomes alone, exosomes with PRP or PDRN, or exosomes added to a laser or Morpheus8 session.",
   "Numbing cream for 20&ndash;30 minutes, then microneedling across the treatment area with the exosome serum applied in layers as we go. About an hour start to finish.",
   "Mild pinkness for 12&ndash;24 hours, noticeably less than microneedling alone. The glow shows within a week and collagen keeps building for 6&ndash;12 weeks.",
   "A series of three, four to six weeks apart, gives the best result; one or two sessions a year maintain it. Daily sunscreen and no actives for 48 hours."),
 "whyh2":"Why choose Serene for exosomes in Hudson",
 "whypara":"Not all exosome products are equal. We use a pharmaceutical-grade, lab-purified exosome serum with a verified particle count, stored and handled correctly, and applied by a physician-led team that also offers PRP, PRF and PDRN &mdash; so we can recommend the right biologic for your skin rather than the only one on the shelf. Pricing is published and the consultation is complimentary.",
 "faqh2":"Exosome Microneedling FAQ",
 "faqs":[
   ("How much does exosome microneedling cost?","Microneedling with exosomes is " + _EXO + " per treatment at Serene Med Spa in Hudson. Adding exosomes to any other treatment &mdash; Morpheus8, Halo, MOXI, CO&sup2; or a chemical peel &mdash; is " + _ADDON + "."),
   ("What are exosomes, exactly?","Exosomes are nano-sized vesicles that cells release to communicate. They carry growth factors, cytokines and microRNA. The exosomes we use are purified from lab-grown stem-cell cultures, sterilized and tested; they contain no cells and no DNA from a donor."),
   ("Exosomes vs. PRP: which is better?","PRP (the &ldquo;vampire facial&rdquo;) uses growth factors from your own blood, so it depends on your platelets. Exosomes deliver a standardized, higher concentration of signaling molecules and don&rsquo;t require a blood draw. Many patients do best with both: PRP for your own biology, exosomes for consistency. PRP is " + _PRP + "; exosomes are " + _EXO + "."),
   ("Exosomes vs. PDRN?","PDRN (salmon DNA) is a tissue-repair molecule that mainly boosts hydration, elasticity and wound healing. Exosomes carry a broader mix of signals that also calm inflammation and support collagen. For dull, inflamed or post-laser skin we lean toward exosomes; for dehydrated, crepey skin we often start with <a href=\"/pdrn/\">PDRN</a>."),
   ("Is there any downtime?","Expect light pinkness for 12 to 24 hours. Most patients wear makeup the next day. Avoid retinol, acids and heavy sweating for 48 hours."),
   ("How many treatments do I need?","You will see a glow after one. For texture, scarring or lines we recommend a series of three, four to six weeks apart, then maintenance once or twice a year."),
   ("Can I add exosomes to my laser treatment?","Yes, and it is one of the best uses for them. Applied right after Halo, MOXI, CO&sup2; or Morpheus8, exosomes typically shorten redness and peeling noticeably. The add-on is " + _ADDON + "."),
   ("Are exosomes safe?","Topical exosomes applied after microneedling have an excellent safety record. They are not injected. We do not treat pregnant or nursing patients, active skin infections or anyone with a history of certain cancers without physician clearance."),
 ],
 "related":["pdrn","microneedling","morpheus8"],
 "pricing_html":_price_block("Pricing","Exosome treatment pricing in Hudson",[
   ("Microneedling with Exosomes", _EXO + " / treatment", "Face; neck, chest or hands quoted at consultation"),
   ("Exosome Add-On to Any Treatment", _ADDON, "Morpheus8, Halo, MOXI, CO&sup2;, chemical peel"),
   ("Microneedling with PDRN", _PDRN + " / treatment", "Salmon-DNA skin booster"),
   ("Microneedling with PRP (Vampire Facial)", _PRP + " / treatment", "Your own platelet-rich plasma &middot; <a href=\"https://clients.mangomint.com/serenemedspa/packages/41\" target=\"_blank\" rel=\"noopener\">series of 3 " + _PRP3 + "</a>"),
   ("Under-Eye PRP / PRF", _UE, "Dark circles and hollows, no filler"),
   ("Consultation", "Complimentary", "No commitment"),
 ], _REGEN_NOTE),
 "ctah2":"Ready for regenerative skin?","ctapara":"Book exosome microneedling online or schedule a complimentary consultation with our Hudson team.",
},
# ---------------- PDRN (SALMON DNA) MICRONEEDLING ----------------
{
 "slug":"pdrn","crumb":"PDRN Salmon DNA","area_kw":"PDRN salmon DNA skin booster treatments",
 "title":"PDRN Salmon DNA Microneedling in Hudson, OH | $299 | Serene",
 "desc":"PDRN (polydeoxyribonucleotide, the Korean &lsquo;salmon DNA&rsquo; skin booster) delivered by microneedling in Hudson, Ohio. Repairs, hydrates and firms crepey, dehydrated skin. $299 per treatment at physician-led Serene Med Spa.",
 "ogtitle":"PDRN Salmon DNA Microneedling in Hudson, OH","ogdesc":"The K-beauty skin booster is here: PDRN microneedling for hydrated, elastic, glass-skin results. $299 at Serene Med Spa.",
 "proc_name":"Microneedling with PDRN","proc_alt":"Polydeoxyribonucleotide skin booster, salmon DNA facial, Rejuran-style treatment",
 "how":"PDRN is a chain of DNA fragments purified from salmon that binds to adenosine A2A receptors in skin cells, switching on tissue repair, new blood-vessel growth and collagen production. Microneedling carries it through the skin barrier into the dermis.","body":"Face, neck, chest, hands, under-eyes",
 "eyebrow":"PDRN &middot; Salmon DNA Skin Booster &middot; Hudson, OH","h1":"PDRN Salmon DNA Microneedling in Hudson, Ohio",
 "hero":"The &ldquo;salmon DNA&rdquo; treatment behind Korea&rsquo;s glass-skin results is now at Serene Med Spa. PDRN tells damaged skin cells to repair, rehydrate and rebuild elasticity &mdash; the fix for crepey, dehydrated, tired-looking skin. " + _PDRN + " per treatment.",
 "trust":["Deep Hydration","Elasticity &amp; Firmness","Repairs Damaged Skin","Physician-Led"],
 "introh2":"Skin repair at the DNA level",
 "introlead":"PDRN (polydeoxyribonucleotide) is a purified DNA extract that has been used in wound care and surgery for decades. In aesthetics it became famous through Korean skin boosters, where it is prized for turning thin, dry, crepey skin into plump, elastic, luminous skin without adding volume or freezing movement.",
 "intropara":"At Serene Med Spa in Hudson we deliver PDRN with microneedling, which creates thousands of micro-channels so the serum reaches the dermis where it works. The treatment takes about an hour with numbing, leaves light pinkness for a day, and builds results over a series: better hydration first, then firmness and a smoother, brighter surface. It is our go-to for the neck, chest and under-eyes, where filler and strong lasers are poor fits, and it stacks well with <a href=\"/exosomes/\">exosomes</a> for inflamed or post-laser skin.",
 "treyebrow":"What It Improves","treh2":"Concerns We Target",
 "cards":[
   ("Crepey, Thin Skin","Rebuilds elasticity in the neck, chest, hands and under-eye area."),
   ("Dehydrated Skin","Improves the skin&rsquo;s own water-holding capacity rather than sitting on top of it."),
   ("Dullness &amp; Uneven Tone","A brighter, more reflective surface as repair and turnover increase."),
   ("Fine Lines","Softens early lines by restoring the dermis rather than filling or relaxing."),
   ("Acne Scars &amp; Damage","Supports healing in scarred or sun-damaged skin over a series."),
   ("Post-Procedure Repair","Speeds recovery after laser, peels or Morpheus8."),
 ],
 "steps":_steps(
   "We assess hydration, elasticity, sun damage and your goals, and decide whether PDRN alone, PDRN with exosomes, or PDRN on top of a laser or Morpheus8 plan is right for you.",
   "Numbing cream for 20&ndash;30 minutes, then microneedling with PDRN serum layered into the skin. About an hour start to finish.",
   "Light pinkness for a day. Hydration and glow improve within one to two weeks; elasticity and texture build over two to three months.",
   "A series of three, four weeks apart, is standard; maintenance every three to six months. Sunscreen daily, no actives for 48 hours."),
 "whyh2":"Why choose Serene for PDRN in Hudson",
 "whypara":"PDRN is new to most of the region, and results depend on a real polynucleotide product delivered properly, not a &ldquo;salmon DNA&rdquo; serum from a facial menu. Our physician-led team uses a medical-grade PDRN, delivers it with controlled-depth microneedling, and can combine it with exosomes, PRP or PRF based on what your skin actually needs. Pricing is published and the consultation is complimentary.",
 "faqh2":"PDRN FAQ",
 "faqs":[
   ("How much does PDRN cost?","Microneedling with PDRN is " + _PDRN + " per treatment at Serene Med Spa in Hudson. A series of three gives the best result."),
   ("What is PDRN and where does it come from?","Polydeoxyribonucleotide is a mix of DNA fragments purified from salmon, chosen because salmon DNA is nearly identical to human DNA in structure and triggers no immune reaction. It has been used in European wound care since the 1990s."),
   ("Is this the same as Rejuran?","Rejuran is a Korean brand of injectable polynucleotide that is not FDA-approved in the United States. We deliver PDRN topically with microneedling, which brings the same active into the skin without injection."),
   ("PDRN vs. exosomes?","PDRN primarily repairs tissue and improves hydration and elasticity. Exosomes carry a broader set of growth factors and anti-inflammatory signals. For crepey, dry skin we start with PDRN; for dull, inflamed or post-laser skin we lean toward <a href=\"/exosomes/\">exosomes</a>. Many patients alternate or combine them."),
   ("PDRN vs. Skinvive or a hyaluronic acid booster?","Hyaluronic acid boosters add water to the skin for a few months. PDRN teaches the skin to hold its own water and rebuild collagen, so results develop more slowly but last longer and improve texture, not just hydration."),
   ("Does it work on the neck and under-eyes?","Yes. These are the areas we use it most, because PDRN firms thin skin without the lumps or puffiness that filler can cause there."),
   ("Is there downtime?","Mild pinkness for about a day. Makeup the next day is fine."),
   ("Who is not a candidate?","Anyone with a fish allergy (ask us; purified PDRN contains no fish protein, but we screen), active skin infection, pregnancy or nursing, or a history of keloid scarring should talk with our physician first."),
 ],
 "related":["exosomes","microneedling","skinvive"],
 "pricing_html":_price_block("Pricing","PDRN treatment pricing in Hudson",[
   ("Microneedling with PDRN", _PDRN + " / treatment", "Face; neck, chest, hands or under-eyes quoted at consultation"),
   ("Microneedling with Exosomes", _EXO + " / treatment", "Growth-factor signaling"),
   ("Exosome Add-On to Any Treatment", _ADDON, "Stack with PDRN, laser or Morpheus8"),
   ("Microneedling with PRP (Vampire Facial)", _PRP + " / treatment", "Your own platelet-rich plasma &middot; <a href=\"https://clients.mangomint.com/serenemedspa/packages/41\" target=\"_blank\" rel=\"noopener\">series of 3 " + _PRP3 + "</a>"),
   ("Consultation", "Complimentary", "No commitment"),
 ], _REGEN_NOTE),
 "ctah2":"Ready for glass skin?","ctapara":"Book PDRN microneedling online or schedule a complimentary consultation with our Hudson team.",
},
]

# Point the classic microneedling page at the new regenerative pages.
for _lst in [globals().get(_n, []) for _n in ("PAGES", "PAGES2", "PAGES3", "PAGES4", "PAGES5", "PAGES6")]:
    for _p in _lst:
        if _p.get("slug") == "microneedling":
            _p["related"] = ["exosomes", "pdrn", "morpheus8"]
            _p["title"] = "Microneedling &amp; PRP in Hudson, OH | Vampire Facial $299 | Serene"
            _p["desc"] = "Microneedling ($200) and microneedling with PRP, the vampire facial ($299, or 3 for $799), in Hudson, OH at physician-led Serene Med Spa. Smoother texture, softer scars, fresher skin. Exosome and PDRN options $299."
            _p["faqs"] = [("How much does microneedling with PRP cost?", "Microneedling with PRP, the vampire facial, is " + _PRP + " per treatment at Serene Med Spa in Hudson, or " + _PRP3 + " for a series of three. Plain microneedling is $200; microneedling with exosomes or PDRN is " + _EXO + ".")] + [q for q in _p.get("faqs", []) if "cost" not in q[0].lower()]
            _p["pricing_html"] = _price_block("Pricing", "Microneedling pricing in Hudson", [
                ("Microneedling", "$200 / treatment", "Serene&rsquo;s signature collagen-induction treatment"),
                ("Microneedling with PRP (Vampire Facial)", _PRP + " / treatment", "Your own platelet-rich plasma"),
                ("Vampire Facial &mdash; Series of 3", _PRP3, "Four to six weeks apart &middot; <a href=\"https://clients.mangomint.com/serenemedspa/packages/41\" target=\"_blank\" rel=\"noopener\">buy the series online</a>"),
                ("Microneedling with Exosomes", _EXO + " / treatment", "Lab-purified growth-factor signals"),
                ("Microneedling with PDRN", _PDRN + " / treatment", "Salmon-DNA skin booster"),
                ("Consultation", "Complimentary", ""),
            ], _REGEN_NOTE)
