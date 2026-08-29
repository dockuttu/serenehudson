# Restore original meta descriptions from source data, then trim <title> (<=60)
# and description (<=155) cleanly on word/sentence boundaries (no mid-word or
# dangling-preposition cuts). Idempotent: always trims from the ORIGINAL source,
# so re-running fixes any earlier awkward truncations. Build step.
import glob, re, os
from html import unescape
BASE="bundle/site"

# ---- originals for generated (data-driven) pages, keyed by slug ----
ns={}
exec(open("common.py").read(), ns)
exec(open("pages_data.py").read(), ns)
ns['PAGES2']=[]; ns['PAGES3']=[]
exec(open("pages_data_new.py").read(), ns)
exec(open("pages_data_new2.py").read(), ns)
ORIG_DESC={}
for p in ns['PAGES']+ns['PAGES2']+ns['PAGES3']:
    ORIG_DESC[p['slug']]=p['desc']

SPECIAL_TITLES={
 "index.html":"Serene Med Spa &mdash; Hudson, OH | Botox, Fillers &amp; More",
 "training/index.html":"Provider Training &mdash; Serene Aesthetics Academy | Hudson",
 "pricing/index.html":"Menu &amp; Pricing &mdash; Serene Med Spa, Hudson, OH",
 "botox/index.html":"Botox in Hudson, OH | Serene Med Spa",
 "hyperpigmentation/index.html":"Hyperpigmentation Treatment in Hudson, OH | Serene Med Spa",
 "peptide-therapy/index.html":"Peptide Therapy in Hudson, OH | Serene Med Spa",
}
# Clean, hand-written descriptions for hand-built pages whose original long
# text is not in the data files (so they can't be sourced/re-trimmed).
SPECIAL_DESCS={
 "index.html":"Physician-led medical spa in Hudson, Ohio — Botox, fillers, Morpheus8, EMSCULPT NEO, laser, HydraFacial, weight loss & IV wellness. Book online today.",
 "fillers/index.html":"Physician-injected dermal fillers in Hudson, Ohio — lip, cheek, jawline & under-eye filler for natural volume and definition. Book your consultation.",
 "morpheus8/index.html":"Morpheus8 RF microneedling in Hudson, Ohio at Serene Med Spa — tighten, smooth, and resurface skin on the face and body. Physician-led. Book today.",
 "weight-loss/index.html":"Physician-supervised medical weight loss in Hudson, Ohio — personalized GLP-1 programs guided by board-certified providers. Book a consultation.",
 "pricing/index.html":"Serene Med Spa Hudson pricing — Botox from $11/unit, fillers, Morpheus8, laser hair removal packages, HydraFacial, weight loss & IV infusions.",
 "emsculpt-neo/index.html":"Non-invasive EMSCULPT NEO body sculpting in Hudson, Ohio — build muscle and reduce fat with no surgery and no downtime. Physician-led care.",
}

def dlen(x): return len(unescape(x))

def short_title(raw):
    if dlen(raw)<=60: return raw
    parts=raw.split(" | ")
    if len(parts)>=3 and parts[-1].strip()=="Serene Med Spa":
        return parts[0]+" | "+parts[-1]          # drop middle descriptor
    if len(parts)==2 and "&mdash;" in parts[1]:
        return parts[0]+" | "+parts[1].split("&mdash;")[0].strip()  # drop tagline
    return raw

WEAK={'a','an','the','and','with','for','to','of','in','on','at','without','that','or','your',
 '&','&amp;','&mdash;','&ndash;','—','–','using','over','into','from','by','than'}
def _clean(x): return re.sub(r'[.,;:&—–-]','',x).lower()
def _tidy(s):
    toks=s.split(" "); changed=True
    while changed and toks:
        changed=False
        if _clean(toks[-1]) in WEAK|{''}:
            toks.pop(); changed=True; continue
        if len(toks)>=2 and not toks[-1].endswith('.') and _clean(toks[-2]) in WEAK:
            toks=toks[:-2]; changed=True
    return " ".join(toks).rstrip(" ,;:-&—–")
def short_desc(raw, target=153):
    if dlen(raw)<=155: return raw
    out=""
    for tok in raw.split(" "):
        cand=(out+" "+tok).strip()
        if dlen(cand)>target: break
        out=cand
    lp=out.rfind('.')
    if lp>=90: return out[:lp+1]
    lc=out.rfind(',')
    if lc>=90: return _tidy(out[:lc])
    return _tidy(out)

changed=0
pages=sorted(set(glob.glob(os.path.join(BASE,"**","index.html"),recursive=True))|{os.path.join(BASE,"index.html")})
for p in pages:
    rel=os.path.relpath(p,BASE)
    slug=rel[:-len("/index.html")] if rel.endswith("/index.html") else ""  # "" for homepage
    s=open(p).read(); orig=s
    # ---- title ----
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    if m:
        raw=m.group(1); new=SPECIAL_TITLES.get(rel, short_title(raw))
        if new!=raw: s=s.replace("<title>%s</title>"%raw,"<title>%s</title>"%new,1)
    # ---- description (+ og:description) ----
    md=re.search(r'name="description" content="(.*?)"',s,re.S)
    if md:
        cur=md.group(1)
        source = SPECIAL_DESCS.get(rel) or ORIG_DESC.get(slug) or cur
        new=short_desc(source)
        if new!=cur:
            s=s.replace('name="description" content="%s"'%cur,'name="description" content="%s"'%new,1)
            s=s.replace('property="og:description" content="%s"'%cur,'property="og:description" content="%s"'%new,1)
    if s!=orig:
        open(p,"w").write(s); changed+=1
print("seo_trim: updated",changed,"pages")

# ---- verify ----
over_t=over_d=0
for p in pages:
    s=open(p).read()
    t=(re.search(r'<title>(.*?)</title>',s,re.S) or [None,""])[1]
    d=(re.search(r'name="description" content="(.*?)"',s,re.S) or [None,""])[1]
    if dlen(t)>60: over_t+=1; print("  long title (%d): %s"%(dlen(t),unescape(t)))
    if dlen(d)>155: over_d+=1; print("  long desc (%d): %s"%(dlen(d),unescape(d)[-40:]))
print("remaining over-length -> titles:",over_t," descriptions:",over_d)
