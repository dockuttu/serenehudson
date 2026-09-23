# -*- coding: utf-8 -*-
# seo_targeting.py — final SEO pass: sets <title> + meta/OG/Twitter descriptions for the
# highest-value pages so they target the searches patients actually use.
# Runs near the end of build.sh (after seo_trim/seo_tech), so these values win. Idempotent.
import os, re, sys, html
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"

def _set(doc, title, desc):
    n = 0
    if title:
        t = html.escape(title, quote=False)
        doc, k = re.subn(r"<title>.*?</title>", "<title>%s</title>" % t, doc, count=1, flags=re.S); n += k
        for prop in ('property="og:title"', 'name="twitter:title"'):
            doc = re.sub(r'(<meta\s+%s\s+content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + html.escape(title) + m.group(2), doc)
    if desc:
        d = html.escape(desc)
        for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
            doc, k = re.subn(r'(<meta\s+%s\s+content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + d + m.group(2), doc)
            n += k
    return doc, n

def run(PAGES):
    done = 0
    for path, (title, desc) in PAGES.items():
        f = os.path.join(SITE, path.strip("/"), "index.html") if path.strip("/") else os.path.join(SITE, "index.html")
        if not os.path.exists(f):
            print("seo_targeting: missing", path); continue
        doc = open(f, encoding="utf-8").read()
        new, n = _set(doc, title, desc)
        if new != doc:
            open(f, "w", encoding="utf-8").write(new); done += 1
    print("seo_targeting: updated %d pages" % done)

PAGES = {'/': ('Med Spa in Hudson, OH | Near Cleveland & Akron | Serene', 'Physician-led med spa in Hudson, OH, serving Cleveland and Akron: Botox $11/unit, fillers, Morpheus8, EMSCULPT NEO, laser, weight loss and IV wellness.'),
 '/botox/': (None, 'Botox, Dysport and Xeomin from $11/unit in Hudson, OH, serving Cleveland and Akron. Physician-injected for smooth, natural-looking results.'),
 '/fillers/': (None, 'Physician-injected Juvéderm and Restylane fillers in Hudson, OH, serving Cleveland and Akron: lips, cheeks, jawline and under-eyes.'),
 '/lip-filler/': (None, 'Lip filler in Hudson, OH, serving Cleveland and Akron: $500 full syringe or $300 half syringe, physician-injected for natural shape and volume.'),
 '/under-eye-filler/': (None, 'Physician-injected under-eye filler in Hudson, OH, serving Cleveland and Akron. Softens hollows and dark circles for a rested look.'),
 '/jawline-filler/': (None, 'Physician-injected jawline filler in Hudson, OH, serving Cleveland and Akron, to sculpt a defined, contoured jawline and refresh your profile.'),
 '/morpheus8/': (None, 'Morpheus8 RF microneedling in Hudson, OH, serving Cleveland and Akron. Tighten, smooth and resurface face and body skin with physician-led care.'),
 '/weight-loss/': (None, 'Physician-supervised medical weight loss in Hudson, OH, serving Cleveland and Akron: semaglutide and tirzepatide programs with monthly check-ins.'),
 '/hormone-optimization/': (None, 'Biote hormone pellet therapy in Hudson, OH, serving Cleveland and Akron, guided by Labcorp panels for hormones, thyroid and vitamins.'),
 '/photofacial/': (None, 'BBL and IPL photofacials in Hudson, OH, serving Cleveland and Akron, to clear sun spots, redness and rosacea-prone skin.'),
 '/microneedling/': (None, 'Microneedling and microneedling with PRP in Hudson, OH, serving Cleveland and Akron, for texture, acne scars and fine lines.'),
 '/laser-skin/': (None, 'CO2, MOXI, Opus Plasma, CoolPeel and PICO laser resurfacing in Hudson, OH, serving Cleveland and Akron. Smooth texture, lines and sun damage.'),
 '/ultherapy/': (None, 'Ultherapy PRIME in Hudson, OH, serving Cleveland and Akron: non-invasive ultrasound lifting for the brow, chin and neck with no downtime.'),
 '/thread-lift/': (None, 'PDO thread lift in Hudson, OH, serving Cleveland and Akron: a non-surgical lift for the jawline, cheeks and brows. Physician-performed.'),
 '/sculptra/': (None, 'Sculptra collagen stimulator in Hudson, OH, serving Cleveland and Akron, for gradual, natural volume. Physician-injected.'),
 '/under-eye-prp/': (None, 'Under-eye PRP and PRF in Hudson, OH, serving Cleveland and Akron: your own platelets soften dark circles and hollows without filler.'),
 '/iv-therapy/': (None, 'IV hydration, vitamin and NAD+ drips in Hudson, OH, serving Cleveland and Akron. Physician-supervised IV wellness.'),
 '/aftercare/botox/': (None, 'Botox aftercare from Serene Med Spa Hudson: what to do and avoid in the first 24 hours, when results appear and when to call us.'),
 '/aftercare/dermal-filler/': (None, 'Dermal filler aftercare from Serene Med Spa Hudson: swelling and bruising tips, activities to avoid, and warning signs that need a call.'),
 '/aftercare/o-shot/': (None, 'O-Shot aftercare from Serene Med Spa Hudson: comfort tips, activity guidance, what is normal after treatment and when to contact us.')}

if __name__ == "__main__":
    run(PAGES)
