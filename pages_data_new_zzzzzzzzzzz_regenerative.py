# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzzzzzz_regenerative.py — PDRN regenerative microneedling page (Nov 2 2026). Regenerative page for the removed biologic add-on retired Nov 20 2026 (LegitScript).
# Prices from Mangomint: Microneedling with PDRN $299 (116),
# Vampire Facial / PRP $299, 3 for $799 (16), Under-Eye PRP/PRF $400 (333).
# Hudson-only file (Hudson, OH).

if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_EXO, _PDRN, _PRP, _PRP3, _UE, _ADDON = "$299", "$299", "$299", "$799", "$400", "$100"

if "HERO_MAP" in globals():
    HERO_MAP["pdrn"] = "morpheus8"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG.setdefault("pdrn", "/img/morpheus8.jpg"); IMG.setdefault("microneedling", "/img/morpheus8.jpg"); IMG.setdefault("skinvive", "/img/filler-inject.jpg")
    RELATED_META.setdefault("microneedling", ("Microneedling &amp; PRP", "Classic collagen induction, with optional PRP."))
    RELATED_META.setdefault("skinvive", ("Skinvive", "Injectable hyaluronic-acid skin booster for lasting glow."))
    RELATED_META["pdrn"] = ("PDRN (Salmon DNA) Microneedling", "The Korean &ldquo;salmon DNA&rdquo; skin booster, delivered by microneedling. " + _PDRN + ".")

_REGEN_NOTE = ('All regenerative microneedling treatments are performed by our physician-led team. Prices are per treatment; a series of three '
               'spaced four to six weeks apart gives the best result. See the full <a href="/pricing/">price list</a>.')

PAGES6 += [
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
 "intropara":"At Serene Med Spa in Hudson we deliver PDRN with microneedling, which creates thousands of micro-channels so the serum reaches the dermis where it works. The treatment takes about an hour with numbing, leaves light pinkness for a day, and builds results over a series: better hydration first, then firmness and a smoother, brighter surface. It is our go-to for the neck, chest and under-eyes, where filler and strong lasers are poor fits.",
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
   "We assess hydration, elasticity, sun damage and your goals, and decide whether PDRN alone, PDRN with PRP, or PDRN on top of a laser or Morpheus8 plan is right for you.",
   "Numbing cream for 20&ndash;30 minutes, then microneedling with PDRN serum layered into the skin. About an hour start to finish.",
   "Light pinkness for a day. Hydration and glow improve within one to two weeks; elasticity and texture build over two to three months.",
   "A series of three, four weeks apart, is standard; maintenance every three to six months. Sunscreen daily, no actives for 48 hours."),
 "whyh2":"Why choose Serene for PDRN in Hudson",
 "whypara":"PDRN is new to most of the region, and results depend on a real polynucleotide product delivered properly, not a &ldquo;salmon DNA&rdquo; serum from a facial menu. Our physician-led team uses a medical-grade PDRN, delivers it with controlled-depth microneedling, and can combine it with PRP or PRF based on what your skin actually needs. Pricing is published and the consultation is complimentary.",
 "faqh2":"PDRN FAQ",
 "faqs":[
   ("How much does PDRN cost?","Microneedling with PDRN is " + _PDRN + " per treatment at Serene Med Spa in Hudson. A series of three gives the best result."),
   ("What is PDRN and where does it come from?","Polydeoxyribonucleotide is a mix of DNA fragments purified from salmon, chosen because salmon DNA is nearly identical to human DNA in structure and triggers no immune reaction. It has been used in European wound care since the 1990s."),
   ("Is this the same as Rejuran?","Rejuran is a Korean brand of injectable polynucleotide that is not FDA-approved in the United States. We deliver PDRN topically with microneedling, which brings the same active into the skin without injection."),
   ("PDRN vs. Skinvive or a hyaluronic acid booster?","Hyaluronic acid boosters add water to the skin for a few months. PDRN teaches the skin to hold its own water and rebuild collagen, so results develop more slowly but last longer and improve texture, not just hydration."),
   ("Does it work on the neck and under-eyes?","Yes. These are the areas we use it most, because PDRN firms thin skin without the lumps or puffiness that filler can cause there."),
   ("Is there downtime?","Mild pinkness for about a day. Makeup the next day is fine."),
   ("Who is not a candidate?","Anyone with a fish allergy (ask us; purified PDRN contains no fish protein, but we screen), active skin infection, pregnancy or nursing, or a history of keloid scarring should talk with our physician first."),
 ],
 "related":["microneedling","skinvive","morpheus8"],
 "pricing_html":_price_block("Pricing","PDRN treatment pricing in Hudson",[
   ("Microneedling with PDRN", _PDRN + " / treatment", "Face; neck, chest, hands or under-eyes quoted at consultation"),
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
            _p["related"] = ["pdrn", "morpheus8", "skinvive"]
            _p["title"] = "Microneedling &amp; PRP in Hudson, OH | Vampire Facial $299 | Serene"
            _p["desc"] = "Microneedling ($200) and microneedling with PRP, the vampire facial ($299, or 3 for $799), in Hudson, OH at physician-led Serene Med Spa. Smoother texture, softer scars, fresher skin. PDRN option $299."
            _p["faqs"] = [("How much does microneedling with PRP cost?", "Microneedling with PRP, the vampire facial, is " + _PRP + " per treatment at Serene Med Spa in Hudson, or " + _PRP3 + " for a series of three. Plain microneedling is $200; microneedling with PDRN is " + _PDRN + ".")] + [q for q in _p.get("faqs", []) if "cost" not in q[0].lower()]
            _p["pricing_html"] = _price_block("Pricing", "Microneedling pricing in Hudson", [
                ("Microneedling", "$200 / treatment", "Serene&rsquo;s signature collagen-induction treatment"),
                ("Microneedling with PRP (Vampire Facial)", _PRP + " / treatment", "Your own platelet-rich plasma"),
                ("Vampire Facial &mdash; Series of 3", _PRP3, "Four to six weeks apart &middot; <a href=\"https://clients.mangomint.com/serenemedspa/packages/41\" target=\"_blank\" rel=\"noopener\">buy the series online</a>"),
                ("Microneedling with PDRN", _PDRN + " / treatment", "Salmon-DNA skin booster"),
                ("Consultation", "Complimentary", ""),
            ], _REGEN_NOTE)
