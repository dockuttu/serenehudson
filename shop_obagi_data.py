# -*- coding: utf-8 -*-
"""Obagi retail catalog for the Serene Med Spa website store (pay & pick up in store).
Prices = Obagi 2026 suggested retail. Keep in sync with Mangomint (brand "Obagi", category Skincare).
Fields: slug, name, collection, size, price (None = Rx / consult), img handle (obagi.com image source), rx, blurb, concerns
"""
COLLECTIONS = [
 ("nu-derm", "Obagi Nu-Derm&reg; &amp; Nu-Derm Fx", "The original Obagi transformation system for discoloration, uneven tone and texture."),
 ("vitamin-c", "Professional-C&reg; &amp; Obagi-C&reg;", "Medical-grade vitamin C for brightness, antioxidant defense and a more even tone."),
 ("elastiderm", "ELASTIderm&reg;", "Firming care for the eyes, face, neck and d&eacute;collet&eacute;."),
 ("hydration", "Hydration &amp; Barrier", "Moisturizers and serums that hydrate, soothe and support the skin barrier."),
 ("retinol", "Retinol", "Over-the-counter retinol for smoother-looking skin and fine lines."),
 ("acne", "CLENZIderm M.D.&reg;", "Daily acne care with benzoyl peroxide and salicylic acid."),
 ("sun", "Sun Protection", "Broad-spectrum mineral sunscreens for daily wear."),
 ("suzanobagimd", "SUZANOBAGIMD&reg;", "Gentle, targeted care for sensitive and reactive skin."),
 ("lash-brow", "Nu-Cil&reg; Lash, Brow &amp; Scalp", "Serums for fuller-looking lashes, brows and hair."),
 ("travel", "Travel Sizes", "Try a favorite or pack it for the road."),
 ("rx", "Prescription Systems (Physician Visit Required)", "Prescription-strength Obagi products dispensed only after an exam with one of our physicians."),
]

P = []
def add(slug, name, col, size, price, img, blurb, concerns=(), rx=False):
    P.append(dict(slug=slug, name=name, collection=col, size=size, price=price, img=img, blurb=blurb, concerns=list(concerns), rx=rx))

# ---- Nu-Derm / Nu-Derm Fx (non-Rx) ----
add("nu-derm-gentle-cleanser", "Obagi Nu-Derm&reg; Gentle Cleanser", "nu-derm", "6.7 fl oz", 55, "obagi-nu-derm-fx-face-cleanser-sensitive-skin",
    "A mild gel cleanser for normal to dry skin that removes makeup and impurities without stripping.", ["Dry skin", "Sensitive skin"])
add("nu-derm-foaming-gel", "Obagi Nu-Derm&reg; Foaming Gel", "nu-derm", "6.7 fl oz", 55, "obagi-nu-derm-foaming-gel",
    "A foaming gel cleanser for normal to oily skin that lifts away oil and debris for a fresh, clean feel.", ["Oily skin"])
add("nu-derm-toner", "Obagi Nu-Derm&reg; Toner", "nu-derm", "6.7 fl oz", 55, "obagi-nu-derm-toner",
    "An alcohol-free toner that rebalances skin after cleansing and preps it for treatment.", ["All skin types"])
add("nu-derm-exfoderm", "Obagi Nu-Derm&reg; Exfoderm&reg;", "nu-derm", "2.0 oz", 105, "obagi-nu-derm-fx-exfoliant",
    "A lightweight exfoliating lotion for normal to dry skin that smooths texture and brightens dullness.", ["Texture", "Dullness"])
add("nu-derm-exfoderm-forte", "Obagi Nu-Derm&reg; Exfoderm&reg; Forte", "nu-derm", "2.0 oz", 105, "obagi-nu-derm-fx-aha-exfoliant",
    "An AHA exfoliating lotion for normal to oily skin that refines pores and evens skin texture.", ["Oily skin", "Texture"])
add("nu-derm-clear-fx", "Obagi Nu-Derm&reg; Clear Fx", "nu-derm", "2.0 oz", 125, "obagi-nu-derm-fx-clear-fx-serum",
    "A hydroquinone-free brightening cream with arbutin to help fade the look of dark spots.", ["Dark spots", "Uneven tone"])
add("nu-derm-blend-fx", "Obagi Nu-Derm&reg; Blend Fx", "nu-derm", "2.0 oz", 125, "obagi-nu-derm-fx-blend-fx-serum",
    "A hydroquinone-free blending cream that helps even out skin tone and discoloration.", ["Dark spots", "Uneven tone"])
add("nu-derm-fx-system-normal-oily", "Obagi Nu-Derm Fx&reg; Starter System &ndash; Normal to Oily", "nu-derm", "Full-size system", 540, "skin-brightening-system-normal-to-oily",
    "The complete non-prescription Nu-Derm Fx regimen for normal to oily skin: cleanse, tone, brighten, exfoliate and protect.", ["Dark spots", "Uneven tone"])
add("nu-derm-fx-system-normal-dry", "Obagi Nu-Derm Fx&reg; Starter System &ndash; Normal to Dry", "nu-derm", "Full-size system", 525, "obagi-nu-derm-fx-system-normal-to-dry",
    "The complete non-prescription Nu-Derm Fx regimen for normal to dry skin.", ["Dark spots", "Uneven tone"])

# ---- Vitamin C ----
add("professional-c-serum-10", "Obagi Professional-C&reg; Serum 10%", "vitamin-c", "1.0 fl oz", 115, "professional-c-serum-10",
    "An entry-strength L-ascorbic acid serum for sensitive skin or first-time vitamin C users.", ["Dullness", "Antioxidant"])
add("professional-c-serum-15", "Obagi Professional-C&reg; Serum 15%", "vitamin-c", "1.0 fl oz", 130, "professional-c-serum",
    "A mid-strength vitamin C serum for normal to combination skin that brightens and defends.", ["Dullness", "Antioxidant"])
add("professional-c-serum-20", "Obagi Professional-C&reg; Serum 20%", "vitamin-c", "1.0 fl oz", 155, "professional-c-serum-20",
    "Obagi&rsquo;s most potent vitamin C serum for normal to oily skin &mdash; a Serene favorite.", ["Dullness", "Fine lines", "Antioxidant"])
add("professional-c-microdermabrasion-polish-mask", "Obagi Professional-C&reg; Microdermabrasion Polish + Mask", "vitamin-c", "2.8 oz", 95, "professional-c-microdermabrasion-polish-mask",
    "An at-home polish and mask with vitamin C that buffs away dullness for smoother, glowing skin.", ["Texture", "Dullness"])
add("professional-c-peptide-complex", "Obagi Professional-C&reg; Peptide Complex", "vitamin-c", "1.0 fl oz", 130, "peptide-complex-anti-aging",
    "A peptide and vitamin C serum that helps skin look firmer and smoother.", ["Fine lines", "Firmness"])
add("obagi-c-cleansing-gel", "Obagi-C&reg; C-Cleansing Gel", "vitamin-c", "6.0 fl oz", 50, "obagi-c-fx-cleansing-gel",
    "A vitamin C&ndash;infused gel cleanser that starts every brightening routine.", ["Dullness"])
add("obagi-c-balancing-toner", "Obagi-C&reg; C-Balancing Toner", "vitamin-c", "6.7 fl oz", 50, "obagi-c-fx-balancing-toner",
    "A refreshing toner that balances skin and preps it for Obagi-C serums.", ["All skin types"])
add("obagi-c-exfoliating-day-lotion", "Obagi-C&reg; C-Exfoliating Day Lotion", "vitamin-c", "2.0 fl oz", 90, "obagi-c-fx-exfoliating-day-lotion",
    "A daytime exfoliating lotion that smooths texture and boosts radiance.", ["Texture", "Dullness"])
add("obagi-c-fx-clarifying-serum", "Obagi-C&reg; Fx C-Clarifying Serum", "vitamin-c", "1.0 fl oz", 145, "obagi-c-fx-clarifying-serum",
    "A non-prescription brightening serum with vitamin C and arbutin for a more even-looking tone.", ["Dark spots", "Uneven tone"])
add("obagi-c-fx-c-therapy-night-cream", "Obagi-C&reg; Fx C-Therapy Night Cream", "vitamin-c", "2.0 oz", 120, "obagi-c-fx-c-therapy-night-cream",
    "A nourishing night cream with vitamin C and arbutin that works while you sleep.", ["Dark spots", "Dryness"])

# ---- ELASTIderm ----
add("elastiderm-firming-eye-cream", "Obagi ELASTIderm&reg; Firming Eye Cream", "elastiderm", "0.5 oz", 130, "elastiderm-eye-cream-fine-lines-wrinkles",
    "A rich eye cream that helps the delicate eye area look firmer and smoother.", ["Eyes", "Fine lines", "Firmness"])
add("elastiderm-eye-serum", "Obagi ELASTIderm&reg; Eye Serum", "elastiderm", "0.47 fl oz", 130, "elastiderm-eye-serum-fine-line-wrinkles",
    "A cooling roller-ball eye serum that helps reduce the look of puffiness and fine lines.", ["Eyes", "Puffiness"])
add("elastiderm-facial-serum", "Obagi ELASTIderm&reg; Facial Serum", "elastiderm", "1.0 fl oz", 220, "elastiderm-facial-moisturizing-serum",
    "A lightweight firming serum for a smoother, more lifted-looking complexion.", ["Firmness", "Fine lines"])
add("elastiderm-neck-decollete-concentrate", "Obagi ELASTIderm&reg; Neck &amp; D&eacute;collet&eacute; Concentrate", "elastiderm", "2.0 fl oz", 260, "neck-and-decollete-concentrate",
    "A targeted concentrate for crepey-looking skin on the neck and chest.", ["Neck", "Firmness"])
add("elastiderm-advanced-filler-concentrate", "Obagi ELASTIderm&reg; Advanced Filler Concentrate", "elastiderm", "0.68 fl oz", 120, "advanced-filler-concentrate",
    "A plumping concentrate that helps smooth the look of lines and wrinkles.", ["Fine lines", "Volume"])
add("elastiderm-lift-up-sculpt-moisturizer", "Obagi ELASTIderm&reg; Lift Up &amp; Sculpt Moisturizer", "elastiderm", "1.7 fl oz", 140, "lift-up-sculpt-facial-moisturizer",
    "A firming moisturizer that hydrates and helps skin look more sculpted.", ["Firmness", "Dryness"])

# ---- Hydration ----
add("hydrate-light", "Obagi Hydrate Light&reg; Weightless Gel Cream", "hydration", "1.7 oz", 70, "hydrate-light",
    "An oil-free gel cream for lasting, weightless hydration &mdash; ideal for combination and oily skin.", ["Oily skin", "Dryness"])
add("hydrate", "Obagi Hydrate&reg; Facial Moisturizer", "hydration", "1.7 oz", 70, "hydrate-facial-moisturizer",
    "A lightweight everyday moisturizer that provides long-lasting hydration.", ["Dryness", "All skin types"])
add("hydrate-luxe", "Obagi Hydrate Luxe&reg;", "hydration", "1.7 oz", 85, "hydrate-luxe-moisturizer",
    "A rich, cushiony night cream for very dry or mature skin.", ["Dryness", "Mature skin"])
add("rebalance-skin-barrier-recovery-cream", "OBAGI&reg; REBALANCE Skin Barrier Recovery Cream", "hydration", "1.7 oz", 125, "skin-barrier-recovery-cream",
    "A soothing cream that supports a compromised skin barrier &mdash; a great partner after in-office treatments.", ["Sensitive skin", "Post-procedure"])
add("daily-hydro-drops-serum", "Obagi Daily Hydro-Drops&reg; Facial Serum", "hydration", "1.0 fl oz", 115, "daily-hydro-drops-moisturizer",
    "A hydrating facial serum that leaves skin plump, dewy and smooth.", ["Dryness", "Dullness"])
add("daily-hydro-drops-eye-gel-cream", "Obagi Daily Hydro-Drops&reg; Rejuvenating Eye Gel Cream", "hydration", "0.5 fl oz", 80, "rejuvenating-eye-gel-cream",
    "A refreshing eye gel cream that hydrates and helps brighten tired-looking eyes.", ["Eyes", "Dryness"])

# ---- Retinol ----
add("retinol-0-5", "Obagi&reg; Retinol 0.5", "retinol", "1.0 oz", 80, "obagi360-retinol-0-5-serum-fine-lines-wrinkles",
    "A gentle starter retinol cream that helps smooth fine lines and refine texture.", ["Fine lines", "Texture"])
add("retinol-1-0", "Obagi&reg; Retinol 1.0", "retinol", "1.0 oz", 90, "obagi360-retinol-1-0-serum-fine-lines-wrinkles",
    "A higher-strength retinol cream for experienced retinol users.", ["Fine lines", "Texture"])
add("retinol-pha-night-cream", "Obagi&reg; Retinol + PHA Refining Night Cream", "retinol", "1.7 oz", 135, "retinol-pha",
    "A retinol night cream with gentle PHA exfoliation for smoother, clearer-looking skin.", ["Fine lines", "Texture"])

# ---- Acne ----
add("clenziderm-acne-therapeutic-system", "CLENZIderm M.D.&reg; Acne Therapeutic System", "acne", "3-piece system", 175, "clenziderm-acne-therapeutic-system-3",
    "A complete three-step acne system: cleanser, pore therapy and 5% benzoyl peroxide lotion.", ["Acne", "Oily skin"])
add("clenziderm-daily-care-foaming-cleanser", "CLENZIderm M.D.&reg; Daily Care Foaming Cleanser", "acne", "4.0 fl oz", 50, "clenziderm-acne-daily-care-foaming-cleanser-3",
    "A salicylic acid foaming cleanser that helps clear breakouts and control oil.", ["Acne", "Oily skin"])
add("clenziderm-pore-therapy", "CLENZIderm M.D.&reg; Pore Therapy", "acne", "5.0 fl oz", 50, "clenziderm-acne-pore-therapy",
    "A salicylic acid toner that helps unclog pores and prevent new blemishes.", ["Acne", "Pores"])
add("clenziderm-therapeutic-lotion", "CLENZIderm M.D.&reg; Therapeutic Lotion 5% BPO", "acne", "1.6 fl oz", 105, "clenziderm-acne-therapeutic-lotion",
    "A 5% benzoyl peroxide lotion that treats acne and helps prevent new breakouts.", ["Acne"])
add("clenziderm-therapeutic-moisturizer", "CLENZIderm M.D.&reg; Therapeutic Moisturizer", "acne", "1.7 fl oz", 50, "clenziderm-acne-therapeutic-moisturizer",
    "An oil-free moisturizer that soothes skin during acne treatment.", ["Acne", "Dryness"])

# ---- Sun ----
add("sun-shield-mineral-spf-50", "Obagi Sun Shield&trade; Mineral Broad Spectrum SPF 50", "sun", "3.0 oz", 60, "mineral-broad-spectrum-spf-50",
    "A sheer mineral sunscreen with zinc oxide for daily broad-spectrum protection.", ["Sun protection"])
add("sun-shield-tint-cool-spf-50", "Obagi Sun Shield&trade; Tint Cool SPF 50", "sun", "3.0 oz", 60, "tint-broad-spectrum-spf-50-cool",
    "A tinted mineral sunscreen with a cool undertone for fair to light skin tones.", ["Sun protection"])
add("sun-shield-tint-warm-spf-50", "Obagi Sun Shield&trade; Tint Warm SPF 50", "sun", "3.0 oz", 60, "tint-broad-spectrum-spf-50-warm",
    "A tinted mineral sunscreen with a warm undertone for medium to deep skin tones.", ["Sun protection"])

# ---- SUZANOBAGIMD ----
add("suzanobagimd-foaming-cleanser", "SUZANOBAGIMD&reg; Foaming Cleanser", "suzanobagimd", "6.7 fl oz", 50, "suzanobagi-md-foaming-cleanser-sensitive-skin",
    "A gentle foaming cleanser for sensitive and redness-prone skin.", ["Sensitive skin"])
add("suzanobagimd-balancing-toner", "SUZANOBAGIMD&reg; Balancing Toner", "suzanobagimd", "6.7 fl oz", 50, "suzaniobagi-md-balancing-toner-sensitive-skin",
    "A calming toner that rebalances sensitive skin.", ["Sensitive skin"])
add("suzanobagimd-cleansing-wipes", "SUZANOBAGIMD&reg; Cleansing Wipes", "suzanobagimd", "25 ct", 30, "suzanobagi-md-facial-cleansing-wipes-sensitive-skin",
    "Soft, gentle wipes for cleansing on the go.", ["Sensitive skin", "Travel"])
add("suzanobagimd-acne-cleansing-wipes", "SUZANOBAGIMD&reg; Acne Cleansing Wipes", "suzanobagimd", "25 ct", 30, "suzanobagi-md-facial-cleansing-wipes-acne",
    "Cleansing wipes with salicylic acid for blemish-prone skin.", ["Acne", "Travel"])
add("suzanobagimd-super-antioxidant-serum", "SUZANOBAGIMD&reg; Super Antioxidant Serum", "suzanobagimd", "1.0 fl oz", 159, "suzanobagimd-super-antioxidant-face-brightening-serum",
    "An antioxidant serum that helps defend against daily environmental stressors.", ["Antioxidant", "Dullness"])
add("suzanobagimd-retivance", "SUZANOBAGIMD&reg; Retivance&reg; Skin Rejuvenating Complex", "suzanobagimd", "1.0 oz", 155, "suzanobagi-md-retivance-skin-rejuvenating-complex",
    "A retinoid complex formulated to be gentle enough for sensitive skin.", ["Fine lines", "Sensitive skin"])
add("suzanobagimd-intensive-daily-repair", "SUZANOBAGIMD&reg; Intensive Daily Repair", "suzanobagimd", "2.0 oz", 90, "suzanobgi-md-intensive-daily-repair-moisturizer",
    "An exfoliating and hydrating lotion that helps smooth rough, dry skin.", ["Dryness", "Texture"])
add("suzanobagimd-moisture-restore", "SUZANOBAGIMD&reg; Moisture Restore", "suzanobagimd", "1.7 fl oz", 78, "suzanobagimd-moisture-restore-hydrating-face-moisturizer",
    "A comforting moisturizer that restores hydration to sensitive skin.", ["Dryness", "Sensitive skin"])
add("suzanobagimd-claribright", "SUZANOBAGIMD&reg; Claribright", "suzanobagimd", "1.7 fl oz", 178, "suzanobagimd-claribright-radiance-brightening-lotion",
    "A brightening lotion that helps improve the look of uneven skin tone.", ["Dark spots", "Uneven tone"])
add("suzanobagimd-physical-defense-tinted-spf-50", "SUZANOBAGIMD&reg; Physical Defense Tinted SPF 50", "suzanobagimd", "3.4 oz", 70, "suzaneobagi-md-tinted-physical-defense-spf-50",
    "A tinted mineral sunscreen designed for sensitive skin.", ["Sun protection", "Sensitive skin"])

# ---- Nu-Cil ----
add("nu-cil-eyelash-enhancing-serum", "Obagi Nu-Cil&reg; Eyelash Enhancing Serum", "lash-brow", "0.10 fl oz", 125, "obagi-nu-cil-eyelash-enhancing-serum",
    "A lash serum for the look of longer, fuller, thicker lashes.", ["Lashes"])
add("nu-cil-eyebrow-boosting-serum", "Obagi Nu-Cil&reg; Eyebrow Boosting Serum", "lash-brow", "0.17 fl oz", 150, "obagi-nu-cil-eyebrow-boosting-serum",
    "A brow serum for the look of fuller, bolder brows.", ["Brows"])
add("nu-cil-biostim-scalp-serum", "Obagi Nu-Cil&reg; BioStim&trade; Scalp Serum", "lash-brow", "2.0 fl oz", 125, "obagi-nu-cil-biostim-scalp-serum",
    "A lightweight scalp serum for the look of thicker, fuller hair.", ["Hair"])

# ---- Travel ----
add("nu-derm-foaming-gel-travel", "Obagi Nu-Derm&reg; Foaming Gel (Travel)", "travel", "2.0 fl oz", 19, "obagi-nu-derm-foaming-gel",
    "Travel size of our best-selling foaming cleanser for normal to oily skin.", ["Travel"])
add("nu-derm-gentle-cleanser-travel", "Obagi Nu-Derm&reg; Gentle Cleanser (Travel)", "travel", "2.0 fl oz", 25, "obagi-nu-derm-fx-face-cleanser-sensitive-skin",
    "Travel size of the gentle cleanser for normal to dry skin.", ["Travel"])
add("nu-derm-toner-travel", "Obagi Nu-Derm&reg; Toner (Travel)", "travel", "2.0 fl oz", 19, "obagi-nu-derm-toner",
    "Travel size of the alcohol-free Nu-Derm Toner.", ["Travel"])
add("professional-c-serum-10-travel", "Obagi Professional-C&reg; Serum 10% (Travel)", "travel", "0.42 fl oz", 60, "professional-c-serum-10",
    "A travel-size introduction to Professional-C 10%.", ["Travel"])
add("professional-c-serum-15-travel", "Obagi Professional-C&reg; Serum 15% (Travel)", "travel", "0.42 fl oz", 75, "professional-c-serum",
    "A travel-size Professional-C 15%.", ["Travel"])
add("professional-c-serum-20-travel", "Obagi Professional-C&reg; Serum 20% (Travel)", "travel", "0.42 fl oz", 85, "professional-c-serum-20",
    "A travel-size Professional-C 20%.", ["Travel"])

# ---- Prescription (no online reservation; physician visit required) ----
RX_BLURB = "Prescription product. Available only after an exam with one of our physicians, who will decide if it is right for you."
for slug, name, size in [
    ("nu-derm-clear-rx", "Obagi Nu-Derm&reg; Clear Rx", "2.0 oz"),
    ("nu-derm-blender-rx", "Obagi Nu-Derm&reg; Blender&reg; Rx", "2.0 oz"),
    ("nu-derm-sunfader-rx", "Obagi Nu-Derm&reg; Sunfader&reg; Rx", "2.0 oz"),
    ("nu-derm-transformation-kit-normal-oily-rx", "Obagi Nu-Derm&reg; Transformation Kit &ndash; Normal to Oily (Rx)", "System"),
    ("nu-derm-transformation-kit-normal-dry-rx", "Obagi Nu-Derm&reg; Transformation Kit &ndash; Normal to Dry (Rx)", "System"),
    ("obagi-tretinoin-cream", "Obagi&reg; Tretinoin Cream 0.025%, 0.05%, 0.1% (Rx)", "0.7 oz"),
    ("obagi-tretinoin-gel", "Obagi&reg; Tretinoin Gel 0.05% (Rx)", "0.7 oz"),
    ("obagi-c-rx-clarifying-serum", "Obagi-C&reg; Rx C-Clarifying Serum (Rx)", "1.0 fl oz"),
    ("obagi-c-rx-therapy-night-cream", "Obagi-C&reg; Rx C-Therapy Night Cream (Rx)", "2.0 oz"),
    ("obagi-c-rx-system", "Obagi-C&reg; Rx System &ndash; Normal to Oily or Normal to Dry (Rx)", "System"),
]:
    add(slug, name, "rx", size, None, None, RX_BLURB, ["Prescription"], rx=True)

PRODUCTS = P
BY_SLUG = {p["slug"]: p for p in P}
