# -*- coding: utf-8 -*-
# pages_data_new_zzzzzzz_optimas.py — InMode OptimasMAX (both offices), Sep 27, 2026.
#   Robin: OptimasMAX at both offices with Lumecca Peak (IPL), DiolazeXL, Fusion Light / Fusion Dark and Forma.
#   Lumecca Peak: $400 full face, 3 for $1,050 (Mangomint package 33, sold online); neck or chest +$150 each.
#   * new page /lumecca/
#   * /photofacial/ now names Lumecca Peak (Barboursville also keeps Sciton BBL)
#   * /laser-hair-removal/ adds DiolazeXL + Fusion Light / Fusion Dark (all skin types)
#   Facts from the InMode QRG: Lumecca is not used on skin types V-VI or on tanned skin; leg veins are not a
#   recommended indication; melasma response is unpredictable. Hair removal wording: "long-term hair reduction".
# Identical file in both office repos. Hudson-voice copy; bv_localize rewrites place names for Barboursville.
# Avoid the bare token "OH" outside titles/eyebrows in this file (the Barboursville localizer rewrites it to "WV").

if "_p" not in globals():
    _BV = (globals().get("SITE_LOC") == "barboursville") if "SITE_LOC" in globals() else ("Barboursville" in globals().get("AREA_TOWNS", []))
    def _p(hud, bv): return bv if _BV else hud
if "_steps" not in globals():
    def _steps(a, b, c, d): return [("Consultation", a), ("Treatment", b), ("Results", c), ("Maintenance", d)]
if "_price_block" not in globals():
    def _price_block(eyebrow, h2, rows, note=""): return ""
if "PAGES6" not in globals():
    PAGES6 = []

_LUM, _LUM3, _LUM_ADD = "$400", "$1,050", "+$150"
_LUM_BUY = "https://clients.mangomint.com/serenemedspa/packages/33"

if "HERO_MAP" in globals():
    HERO_MAP["lumecca"] = "lumecca-hero"
if "IMG" in globals() and "RELATED_META" in globals():
    IMG["lumecca"] = "/img/lumecca-hero.jpg"
    RELATED_META["lumecca"] = ("Lumecca Peak IPL", "Sun spots and redness, often cleared in 1&ndash;2 sessions. From " + _LUM + ".")
    RELATED_META.setdefault("forma", ("Forma", "Gentle radiofrequency skin tightening, no downtime."))
    RELATED_META.setdefault("photofacial", ("Photofacial", "Clear sun spots and redness."))
    IMG.setdefault("forma", "/img/lumecca-hero.jpg")
    IMG.setdefault("photofacial", "/img/lumecca-hero.jpg")

def _gal(eyebrow, h2, items, note, intro="Clinical photos from InMode. The treating provider is named on each photo."):
    figs = "".join(f'<figure class="res reveal"><img loading="lazy" src="/img/{f}.jpg" alt="{alt}" style="height:auto;aspect-ratio:auto"><figcaption>{cap}</figcaption></figure>'
                   for f, cap, alt in items)
    return ('<section class="results"><div class="wrap"><div class="section-head reveal"><div class="eyebrow">' + eyebrow + '</div>'
            '<h2>' + h2 + '</h2><p>' + intro + '</p></div>'
            '<div class="res-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));align-items:start">' + figs + '</div>'
            '<p class="rev-note">' + note + '</p></div></section>')

_NOTE = "Photos courtesy of InMode, from other practices. They are not Serene Med Spa patients. Individual results vary."
_LUM_GALLERY = _gal("Clinical Photos", "Lumecca Peak before &amp; after", [
    ("lumecca-ba-face-2", "Sun damage &amp; redness, face &mdash; Lumecca Peak", "Before and after Lumecca Peak IPL of the cheek, angled view"),
    ("lumecca-ba-face-3", "Brown spots, face &mdash; Lumecca Peak", "Before and after Lumecca Peak IPL of the face"),
    ("lumecca-ba-chest", "Sun damage, chest &mdash; Lumecca Peak", "Before and after Lumecca Peak IPL of the chest"),
    ("lumecca-ba-face-1", "Pigment &amp; redness, face &mdash; Lumecca Peak", "Before and after Lumecca Peak IPL of the face, front view"),
], _NOTE)

_LUM_NOTE = ('The series is a standing price and can&rsquo;t be combined with another discount. Series sessions don&rsquo;t expire. '
             'The consultation is complimentary. See the full <a href="/pricing/">price list</a>.'
             f'<br>Prefer to prepay? <a href="{_LUM_BUY}" target="_blank" rel="noopener">Buy the Lumecca Peak series of 3 online</a>.')
_LUM_ROWS = [
    ("Lumecca Peak &mdash; Full Face", _LUM + " / session", "About 20&ndash;30 minutes"),
    ("Lumecca Peak &mdash; Series of 3", _LUM3, "$350 a session &middot; save $150"),
    ("Add Neck or Chest", _LUM_ADD + " each", "Same visit"),
]
_LUM_ROWS_BV = _LUM_ROWS + [("Sciton BBL Heroic Photofacial", "$400 / session", "Also available in Barboursville")]

_LUM_PAGE = {
 "slug":"lumecca","crumb":"Lumecca Peak","area_kw":"Lumecca Peak IPL photofacial",
 "title":"Lumecca Peak IPL in Hudson, OH | $400 or 3 for $1,050 | Serene",
 "desc":"Lumecca Peak IPL in Hudson, Ohio: InMode's high-power photofacial for sun spots, freckles, redness, rosacea and small facial vessels. $400 full face or 3 for $1,050. Little downtime.",
 "ogtitle":"Lumecca Peak IPL in Hudson, OH","ogdesc":"Clear sun spots and redness, often in 1&ndash;2 sessions. $400 full face, or a series of 3 for $1,050.",
 "proc_name":"Lumecca Peak IPL","proc_alt":"Intense pulsed light (IPL) photorejuvenation, InMode OptimasMAX",
 "how":"Lumecca Peak delivers intense pulsed light through a cooled crystal tip. The light is absorbed by excess pigment and by the blood in small, visible vessels; the pigment darkens and flakes away and the vessels fade over the following days. Two filters (515 and 580 nm) let us match the light to your skin type.",
 "body":"Face, Neck, Chest, Hands, Arms, Shoulders",
 "eyebrow":"Lumecca Peak &middot; InMode OptimasMAX &middot; Hudson, OH","h1":"Lumecca Peak IPL in Hudson, Ohio",
 "hero":"InMode&rsquo;s most powerful IPL for sun spots, freckles, redness and rosacea, with a cooled tip for comfort. Many people see a clear difference after one or two sessions. $400 full face, or three for $1,050.",
 "trust":["Little Downtime","Cooled Tip","Results in 1&ndash;2 Sessions","3 for $1,050"],
 "introh2":"More peak power, fewer sessions",
 "introlead":"Lumecca Peak is the newest IPL on our InMode OptimasMAX. Its higher peak power clears pigment and redness efficiently, so many people need fewer sessions than with older IPL devices.",
 "intropara":"At Serene Med Spa in Hudson, Lumecca Peak treats brown spots, freckles, sun damage, redness, rosacea and small facial vessels on the face, neck, chest, hands and arms. A full-face session takes about 20 to 30 minutes. Lumecca is for skin that isn&rsquo;t tanned and suits light to olive skin tones; for deeper skin tones we&rsquo;ll recommend a safer option. For texture and firmness we often pair it with Morpheus8 or Forma. Results vary from person to person.",
 "treyebrow":"What It Treats","treh2":"Common Concerns",
 "cards":[
   ("Sun Spots &amp; Freckles","Brown spots darken, then flake away within about a week."),
   ("Redness &amp; Rosacea","Diffuse facial redness and flushing calm down."),
   ("Broken Capillaries","Small visible vessels on the nose and cheeks fade."),
   ("Chest &amp; Neck","Sun-damaged, blotchy skin on the d&eacute;colletage and neck."),
   ("Hands &amp; Arms","Age spots on the backs of the hands and forearms."),
   ("With Morpheus8 or Forma","Clear tone with Lumecca, improve texture and firmness with RF."),
 ],
 "steps":_steps(
   "A skin assessment to confirm your skin type and goals. Avoid tanning for 4 to 6 weeks before treatment.",
   "A thin layer of cool gel, then quick pulses of light through the cooled tip. Most people describe a warm snap. About 20 to 30 minutes for the face.",
   "Brown spots darken like coffee grounds and flake off over 7 to 10 days; redness settles within a day or two. Use SPF 30+ daily.",
   "One to three sessions 3 to 4 weeks apart, then a yearly touch-up to keep new sun damage in check."),
 "whyh2":"Why choose Serene for Lumecca Peak in Hudson",
 "whypara":"Light-based treatments are safest when skin type is judged carefully. Our physician-led team tests settings on your skin first and tells you honestly when a different treatment is the better fit.",
 "faqh2":"Lumecca Peak FAQ",
 "faqs":[
   ("How much does Lumecca Peak cost?","$400 for a full-face session at Serene Med Spa in Hudson, or $1,050 for a series of three ($350 a session). Neck or chest can be added for $150 each. "
    f"You can <a href=\"{_LUM_BUY}\" target=\"_blank\" rel=\"noopener\">buy the series online</a>."),
   ("How many sessions will I need?","Many people see a clear change after one or two sessions. For heavier sun damage or rosacea we usually recommend three, 3 to 4 weeks apart."),
   ("Does it hurt?","Most people feel a quick warm snap, like a rubber band. The cooled tip keeps it comfortable, and no numbing is usually needed."),
   ("What is the downtime?","Very little. Brown spots look darker for about a week before flaking off, and there may be mild redness for a day or two. Makeup is fine the next day."),
   ("Who is not a good candidate?","Lumecca isn&rsquo;t used on tanned skin or on deeper skin tones (skin types V and VI). It&rsquo;s also not ideal for melasma, where results are unpredictable. We&rsquo;ll recommend another option if IPL isn&rsquo;t right for you."),
   ("Can it treat leg veins?","Leg veins respond better to sclerotherapy, which we also offer. Lumecca is best for facial redness and small facial vessels."),
 ],
 "related":["morpheus8","forma","photofacial"],
 "pricing_html":_LUM_GALLERY + _price_block("Pricing","Lumecca Peak pricing",_LUM_ROWS,_LUM_NOTE),
 "ctah2":"Ready for clearer, more even skin?","ctapara":"Book a Lumecca Peak photofacial with our Hudson team, or buy a series of three online.",
}
if not any(pg.get("slug") == "lumecca" for pg in PAGES6):
    PAGES6.append(_LUM_PAGE)

_FUSION_SECTION = ('<section class="tint-blush" id="optimasmax-hair"><div class="wrap"><div class="section-head reveal"><div class="eyebrow">InMode OptimasMAX</div>'
    '<h2>DiolazeXL and Fusion Light / Fusion Dark</h2>'
    '<p>Our InMode OptimasMAX adds two hair-removal technologies. DiolazeXL is a fast diode laser with a large, cooled tip for bigger areas. Fusion uses two '
    'wavelengths with a continuously cooled tip: Fusion Light for fair to medium skin, and Fusion Dark for coarse hair on deeper skin tones. '
    'Together they let us treat every skin type comfortably. Most people need a series of treatments for long-term hair reduction.</p></div>'
    '<div class="res-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));align-items:start">'
    '<figure class="res reveal"><img loading="lazy" src="/img/fusion-ba-back.jpg" alt="Before and after Fusion laser hair removal on the back" style="height:auto;aspect-ratio:auto"><figcaption>Back &mdash; Fusion</figcaption></figure>'
    '<figure class="res reveal"><img loading="lazy" src="/img/fusion-ba-underarm.jpg" alt="Before and after Fusion laser hair removal of the underarm" style="height:auto;aspect-ratio:auto"><figcaption>Underarm &mdash; Fusion</figcaption></figure>'
    '</div><p class="rev-note">' + _NOTE + '</p></div></section>')

def _photofacial(p):
    p["crumb"] = _p("Lumecca Peak IPL Photofacial", "Photofacial (BBL &amp; Lumecca IPL)")
    p["title"] = _p("IPL Photofacial in Hudson, OH | Lumecca Peak, $400 | Serene", "Photofacial in Hudson, OH | BBL &amp; Lumecca IPL, $400 | Serene")
    p["hero"] = _p("Clear sun spots, redness and uneven tone with Lumecca Peak, InMode&rsquo;s most powerful IPL. Little downtime. $400 full face, or three for $1,050.",
                   "Clear sun spots, redness and uneven tone with Sciton BBL Heroic or InMode&rsquo;s Lumecca Peak IPL. Little downtime. $400 a session, or three Lumecca sessions for $1,050.")
    p["intropara"] = p["intropara"] + (" Our photofacials now use <a href=\"/lumecca/\">Lumecca Peak</a> on the InMode OptimasMAX; many people see a clear change after one or two sessions." if not _p(False, True)
                                       else " Along with Sciton BBL Heroic, we now offer <a href=\"/lumecca/\">Lumecca Peak</a> IPL on the InMode OptimasMAX; your provider will choose the best light for your skin.")
    p["related"] = ["lumecca", "morpheus8", "forma"]
    p["pricing_html"] = _LUM_GALLERY + _price_block("Pricing", "Photofacial pricing", _p(_LUM_ROWS, _LUM_ROWS_BV), _LUM_NOTE)

def _lhr(p):
    add = (" Our InMode OptimasMAX adds DiolazeXL and Fusion Light / Fusion Dark, so we can treat fair, olive and deeper skin tones with the right technology for each.")
    if "OptimasMAX" not in p.get("intropara", ""):
        p["intropara"] = p.get("intropara", "") + add
    p["pricing_html"] = _FUSION_SECTION + p.get("pricing_html", "")

for _pg in [x for n in ("PAGES6", "PAGES5", "PAGES4", "PAGES3", "PAGES2", "PAGES") for x in globals().get(n, [])]:
    if _pg.get("slug") == "photofacial" and not _pg.get("_optimas"):
        _photofacial(_pg); _pg["_optimas"] = True
    elif _pg.get("slug") == "laser-hair-removal" and not _pg.get("_optimas"):
        _lhr(_pg); _pg["_optimas"] = True
