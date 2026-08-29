# -*- coding: utf-8 -*-
import re, os, json
exec(open("/home/claude/hudson-site/common.py").read())  # NAV, FOOTER_TREAT, areas_section, AREA_SERVED, CATEGORIES
SITE="/home/claude/hudson-site/bundle/site"

nav_re=re.compile(r"<header>.*?</header>", re.DOTALL)
foot_re=re.compile(r"<div>\s*<h4>Treatments</h4>.*?</ul>\s*</div>", re.DOTALL)

hand = {
 "botox/index.html":"Botox and wrinkle relaxers",
 "fillers/index.html":"dermal fillers",
 "morpheus8/index.html":"Morpheus8 skin tightening",
 "weight-loss/index.html":"medical weight loss",
 "index.html":"aesthetic and wellness care",
}

for rel,kw in hand.items():
    path=os.path.join(SITE,rel); s=open(path).read(); before=s
    assert len(nav_re.findall(s))==1, rel+" nav"
    s=nav_re.sub(lambda m:NAV, s, count=1)
    assert len(foot_re.findall(s))==1, rel+" foot"
    s=foot_re.sub(lambda m:FOOTER_TREAT.strip(), s, count=1)
    # insert areas section before <footer>
    assert s.count("<footer>")==1, rel+" footer tag"
    s=s.replace("<footer>", areas_section(kw)+"\n\n<footer>", 1)
    assert s!=before
    open(path,"w").write(s)
    print("patched", rel)

# homepage schema: availableService (22) + areaServed
hp=os.path.join(SITE,"index.html"); s=open(hp).read()
avail=[]
for cat,items in CATEGORIES:
    for slug,label in items:
        avail.append({"@type":"MedicalProcedure","name":label,"url":"https://hudson.serenemedspas.com/%s/"%slug})
new_avail='"availableService":%s,"areaServed":%s,"parentOrganization"' % (
    json.dumps(avail,ensure_ascii=False), json.dumps(AREA_SERVED,ensure_ascii=False))
s2=re.sub(r'"availableService":\[.*?\],"parentOrganization"', lambda m:new_avail, s, count=1)
assert s2!=s, "availableService not replaced"
s=s2
open(hp,"w").write(s)
print("homepage schema: availableService=%d + areaServed"%len(avail))
