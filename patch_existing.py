# -*- coding: utf-8 -*-
import re, os
exec(open("/home/claude/hudson-site/gen_pages.py").read().split("# import page data")[0])  # get NAV, FOOTER_TREAT_NEW, SITE, etc.

SITE = "/home/claude/hudson-site/bundle/site"
existing = ["index.html","botox/index.html","fillers/index.html","morpheus8/index.html","weight-loss/index.html"]

nav_re = re.compile(r"<header>.*?</header>", re.DOTALL)
foot_re = re.compile(r"<div>\s*<h4>Treatments</h4>.*?</ul>\s*</div>", re.DOTALL)

for rel in existing:
    path = os.path.join(SITE, rel)
    s = open(path).read()
    before = s
    n1 = len(nav_re.findall(s)); n2 = len(foot_re.findall(s))
    s = nav_re.sub(lambda m: NAV, s, count=1)
    s = foot_re.sub(lambda m: FOOTER_TREAT_NEW.strip(), s, count=1)
    assert n1==1, "%s nav matches=%d" % (rel,n1)
    assert n2==1, "%s foot matches=%d" % (rel,n2)
    assert s!=before, "%s unchanged" % rel
    open(path,"w").write(s)
    print("patched", rel, "nav+footer")

# ---- homepage-specific tweaks ----
hp = os.path.join(SITE,"index.html")
s = open(hp).read()

# 1) link the "Laser & Skin" services card (currently a <div>) to /laser-skin/
old_card = '<div class="card reveal"><div class="ico">✦</div><h3>Laser &amp; Skin</h3><p>Laser hair removal, laser facials, nail fungus treatment, VI Peel, and the Perfect Derma Peel for radiant skin.</p></div>'
new_card = '<a class="card reveal" href="/laser-skin/"><div class="ico">✦</div><h3>Laser &amp; Skin</h3><p>PICO laser skin treatments, laser hair removal, HydraFacial &amp; DiamondGlow, and medical-grade peels for radiant skin.</p></a>'
assert old_card in s, "laser card not found"
s = s.replace(old_card, new_card)

# 2) update availableService schema to full list with URLs
new_avail = ('"availableService":['
 '{"@type":"MedicalProcedure","name":"Botox & Neurotoxins","url":"https://hudson.serenemedspas.com/botox/"},'
 '{"@type":"MedicalProcedure","name":"Dermal Fillers","url":"https://hudson.serenemedspas.com/fillers/"},'
 '{"@type":"MedicalProcedure","name":"Morpheus8 RF Microneedling","url":"https://hudson.serenemedspas.com/morpheus8/"},'
 '{"@type":"MedicalProcedure","name":"EMSCULPT NEO Body Sculpting","url":"https://hudson.serenemedspas.com/emsculpt-neo/"},'
 '{"@type":"MedicalProcedure","name":"PICO Laser Skin Treatment","url":"https://hudson.serenemedspas.com/laser-skin/"},'
 '{"@type":"MedicalProcedure","name":"Laser Hair Removal","url":"https://hudson.serenemedspas.com/laser-hair-removal/"},'
 '{"@type":"MedicalProcedure","name":"HydraFacial","url":"https://hudson.serenemedspas.com/hydrafacial/"},'
 '{"@type":"MedicalProcedure","name":"DiamondGlow Facial","url":"https://hudson.serenemedspas.com/diamondglow/"},'
 '{"@type":"MedicalProcedure","name":"Medical Weight Loss","url":"https://hudson.serenemedspas.com/weight-loss/"}'
 '],"parentOrganization"')
s2 = re.sub(r'"availableService":\[.*?\],"parentOrganization"', lambda m: new_avail, s, count=1)
assert s2 != s, "availableService not replaced"
s = s2

# 3) enrich homepage meta + og description with new services
old_desc = "Botox, dermal fillers, laser, Morpheus8, PRP, and medical weight loss — natural results, personalized care. Book online today."
new_desc = "Botox, dermal fillers, Morpheus8, EMSCULPT NEO, laser skin & hair removal, HydraFacial, DiamondGlow & medical weight loss — natural, physician-led care. Book online today."
if old_desc in s:
    s = s.replace(old_desc, new_desc)
    print("updated meta description")

open(hp,"w").write(s)
print("homepage tweaks done")
