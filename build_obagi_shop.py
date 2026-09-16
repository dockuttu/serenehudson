# -*- coding: utf-8 -*-
# build_obagi_shop.py — Obagi store (reserve online, pay & pick up in store). Identical in both repos.
# Builds: /shop/ (store), /shop/<product>/ (product pages), /cart/ (checkout, noindex),
#         /obagi/ (authorized-provider brand page), /shop.js (cart engine + catalog).
import json, os, re, hashlib, html as _h
ns = {}
exec(open("common.py", encoding="utf-8").read(), ns)
exec(open("shop_obagi_data.py", encoding="utf-8").read(), ns)
NAV, FOOTER, SCRIPTS, CONSULT, STICKY = ns["NAV"], ns["FOOTER"], ns["SCRIPTS"], ns["CONSULT_SECTION"], ns.get("STICKY_BAR", "")
BOOK = ns["BOOK"]
SKIN_BOOK = ns.get("BOOK_MAP", {}).get("medical-facials", BOOK)
PRODUCTS, COLLECTIONS = ns["PRODUCTS"], ns["COLLECTIONS"]
COLNAME = {k: n for k, n, d in COLLECTIONS}
ZX = ("29c1b6f4e6219d1e5682cd0434b1ce181ccda55241b6394ae70c33a7f83e1dfa",
      "139bc9e7ae4c09a2ea84b820c0c3b10459ed2d907a8c88693956f8d217af21d20ea75c0d1b75b947bf1bf59cc28d7274")

HUDSON = "barboursville" not in os.path.basename(os.getcwd()).lower()
LOCS = {
  "Hudson, OH": dict(addr="50 W Streetsboro St, Ste 2", city="Hudson", region="OH", zip="44236", tel="+13304605915", phone="(330) 460-5915", site="https://hudson.serenemedspas.com"),
  "Barboursville, WV": dict(addr="1 Chateau Grove Ln", city="Barboursville", region="WV", zip="25504", tel="+13045200461", phone="(304) 520-0461", site="https://barboursville.serenemedspas.com"),
}
if HUDSON:
    CITY, CITY_LONG, REGION, AREA = "Hudson, OH", "Hudson, Ohio", "US-OH", "Hudson, Akron, Stow and Northeast Ohio"
else:
    CITY, CITY_LONG, REGION, AREA = "Barboursville, WV", "Barboursville, West Virginia", "US-WV", "Barboursville, Huntington and the Tri-State"
L = LOCS[CITY]; SITE = L["site"]
OUT = os.path.join("bundle", "site")

def clean(s):
    s = _h.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"[®™]", "", s).replace("  ", " ").strip()
def esc(s): return _h.escape(s, quote=True)
def money(p): return ("$%d" % p) if float(p).is_integer() else ("$%.2f" % p)
def img(p, small=False):
    return "/img/obagi/%s%s.webp" % (p["img"], "-400" if small else "") if p["img"] else ""
def short_col(k): return re.sub(r" \(.*\)", "", COLNAME[k])
RETAIL = [p for p in PRODUCTS if not p["rx"]]
RX = [p for p in PRODUCTS if p["rx"]]

# ---------------- shop.js (cart engine) ----------------
CAT = {p["slug"]: {"n": clean(p["name"]), "s": p["size"], "p": p["price"], "i": img(p, True)} for p in RETAIL}
SHOP_JS = r"""/* Serene Med Spa - Obagi reserve & pick-up cart (no payment online) */
(function(){
var CAT=%(cat)s, KEY='serene_cart_v1';
function load(){try{var c=JSON.parse(localStorage.getItem(KEY)||'{}');for(var k in c){if(!CAT[k]||!(c[k]>0))delete c[k];}return c;}catch(e){return {};}}
function save(c){try{localStorage.setItem(KEY,JSON.stringify(c));}catch(e){} render();}
function count(c){var n=0;for(var k in c)n+=c[k];return n;}
function total(c){var t=0;for(var k in c)t+=CAT[k].p*c[k];return t;}
function fmt(v){return '$'+(Math.round(v*100)/100).toFixed(2).replace(/\.00$/,'');}
var S={cat:CAT,load:load,save:save,count:count,total:total,fmt:fmt,
  add:function(slug,q){var c=load();c[slug]=Math.min(20,(c[slug]||0)+(q||1));save(c);toast(slug);},
  set:function(slug,q){var c=load();if(q>0)c[slug]=Math.min(20,q);else delete c[slug];save(c);},
  clear:function(){save({});}};
window.SereneCart=S;
function css(){if(document.getElementById('sc-css'))return;var st=document.createElement('style');st.id='sc-css';st.textContent=
'.sc-fab{position:fixed;right:18px;bottom:88px;z-index:60;display:none;align-items:center;gap:8px;background:#1f2a5c;color:#fff;border-radius:999px;padding:12px 18px;font:600 1rem Jost,sans-serif;text-decoration:none;box-shadow:0 10px 28px rgba(0,0,0,.22)}'+
'.sc-fab.on{display:inline-flex}.sc-fab b{background:#fff;color:#1f2a5c;border-radius:999px;min-width:24px;height:24px;display:inline-flex;align-items:center;justify-content:center;font-size:.9rem}'+
'.sc-toast{position:fixed;left:50%%;bottom:26px;transform:translateX(-50%%) translateY(20px);opacity:0;pointer-events:none;z-index:70;background:#fff;color:#2b1d2a;border:1px solid rgba(0,0,0,.08);border-radius:14px;padding:12px 16px;box-shadow:0 14px 34px rgba(0,0,0,.18);font:500 1rem Jost,sans-serif;transition:.25s;display:flex;gap:12px;align-items:center;max-width:92vw}'+
'.sc-toast.on{opacity:1;pointer-events:auto;transform:translateX(-50%%) translateY(0)}.sc-toast a{font-weight:700;color:#1f2a5c;white-space:nowrap}'+
'@media(min-width:900px){.sc-fab{bottom:24px}}';document.head.appendChild(st);}
var fab,tst,tt;
function render(){var c=load(),n=count(c);
  document.querySelectorAll('[data-cart-count]').forEach(function(e){e.textContent=n;});
  if(fab){fab.querySelector('b').textContent=n;fab.classList.toggle('on',n>0&&location.pathname.indexOf('/cart/')!==0);}
  if(typeof window.SereneCartRender==='function')window.SereneCartRender();}
function toast(slug){if(!tst)return;tst.querySelector('span').innerHTML='<b>Added:</b> '+CAT[slug].n;tst.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){tst.classList.remove('on');},3200);}
function init(){css();
  fab=document.createElement('a');fab.className='sc-fab';fab.href='/cart/';fab.setAttribute('aria-label','View your pickup cart');fab.innerHTML='&#128717; Cart <b>0</b>';document.body.appendChild(fab);
  tst=document.createElement('div');tst.className='sc-toast';tst.setAttribute('role','status');tst.innerHTML='<span></span><a href="/cart/">View cart &rsaquo;</a>';document.body.appendChild(tst);
  document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-add]');if(!b)return;e.preventDefault();
    var slug=b.getAttribute('data-add');if(!CAT[slug])return;
    var q=1,qi=b.getAttribute('data-qty')&&document.getElementById(b.getAttribute('data-qty'));if(qi)q=Math.max(1,Math.min(20,parseInt(qi.value,10)||1));
    S.add(slug,q);b.classList.add('sc-added');var t=b.textContent;b.textContent='Added ✓';setTimeout(function(){b.classList.remove('sc-added');b.textContent=t;},1100);
    try{if(window.gtag)gtag('event','add_to_cart',{currency:'USD',value:CAT[slug].p*q,items:[{item_id:slug,item_name:CAT[slug].n,item_brand:'Obagi',price:CAT[slug].p,quantity:q}]});}catch(x){}});
  window.addEventListener('storage',render);render();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
""" % dict(cat=json.dumps(CAT, separators=(",", ":")))
open(os.path.join(OUT, "shop.js"), "w", encoding="utf-8").write(SHOP_JS)
JSV = hashlib.md5(SHOP_JS.encode()).hexdigest()[:8]
open(".shopjs_version", "w").write(JSV)

HEAD_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

CSS = """<style>
:root{--ob:#1f2a5c}
.ob-body{padding:40px 0 64px}
.ob-body p,.ob-body li{font-size:1.1rem;line-height:1.7;color:var(--ink);font-weight:500}
.ob-body h2{font-family:'Cormorant Garamond',serif;font-size:2.1rem;color:var(--ink);margin:40px 0 12px}
.ob-auth{display:inline-flex;align-items:center;gap:14px;background:#fff;border:1px solid rgba(31,42,92,.18);border-radius:999px;padding:8px 18px 8px 12px;margin:10px 0 6px;text-decoration:none}
.ob-auth img{height:38px;width:auto;display:block}
.ob-auth span{color:var(--ob);font-weight:600;font-size:1rem;line-height:1.2}
.ob-auth small{display:block;color:var(--ink);font-weight:500;opacity:.8;font-size:.85rem}
.ob-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0 6px}
.ob-steps div{background:#fff;border:1px solid rgba(31,42,92,.14);border-radius:16px;padding:16px 18px}
.ob-steps b{display:block;color:var(--ob);font-size:1.1rem;margin-bottom:4px}
.ob-steps span{color:var(--ink);font-weight:500;font-size:1rem;line-height:1.5;display:block}
.ob-tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:24px 0 18px}
.ob-chip{border:1.5px solid rgba(31,42,92,.25);background:#fff;color:var(--ob);border-radius:999px;padding:8px 14px;font:600 .98rem Jost,sans-serif;cursor:pointer}
.ob-chip.on{background:var(--ob);color:#fff;border-color:var(--ob)}
.ob-search{flex:1 1 220px;min-width:200px;border:1.5px solid rgba(31,42,92,.25);border-radius:999px;padding:10px 16px;font:500 1rem Jost,sans-serif;color:var(--ink)}
.ob-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}
.ob-card{background:#fff;border:1px solid rgba(31,42,92,.12);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}
.ob-card .ob-img{display:block;background:#ededed;aspect-ratio:1/1}
.ob-card .ob-img img{width:100%;height:100%;object-fit:cover;display:block}
.ob-card .ob-txt{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.ob-col{font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ob);font-weight:600}
.ob-card h3{font-size:1.08rem;line-height:1.35;margin:0;color:var(--ink);font-family:Jost,sans-serif;font-weight:600}
.ob-card h3 a{color:inherit;text-decoration:none}
.ob-size{color:var(--ink);opacity:.85;font-size:.95rem;font-weight:500}
.ob-row{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:auto;padding-top:8px}
.ob-price{font-size:1.3rem;font-weight:700;color:var(--ink)}
.ob-add{background:var(--ob);color:#fff;border:0;border-radius:999px;padding:10px 16px;font:600 .98rem Jost,sans-serif;cursor:pointer;white-space:nowrap;text-decoration:none;text-align:center}
.ob-add:hover{filter:brightness(1.15)}.ob-add.sc-added{background:#2e7d4f}
.ob-rx{background:#fff;border:1.5px dashed rgba(31,42,92,.3);border-radius:18px;padding:18px}
.ob-rx h3{font-size:1.05rem;margin:0 0 4px;color:var(--ink);font-family:Jost,sans-serif}
.ob-rx p{font-size:.98rem!important;margin:0}
.ob-colhead{margin:34px 0 4px}
.ob-colhead h2{margin:0 0 4px}
.ob-colhead p{margin:0 0 14px}
.ob-note{background:#f3f5fb;border-radius:16px;padding:16px 20px;margin-top:28px}
.ob-pd{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:start}
.ob-pd .ob-img{border-radius:20px;overflow:hidden;background:#ededed}
.ob-pd .ob-img img{width:100%;height:auto;display:block}
.ob-pd h1{font-size:2.3rem;line-height:1.15;margin:6px 0}
.ob-buy{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:16px 0}
.ob-qty{width:74px;border:1.5px solid rgba(31,42,92,.25);border-radius:12px;padding:10px;font:600 1.05rem Jost,sans-serif;text-align:center}
.ob-tags{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.ob-tags span{border:1px solid rgba(31,42,92,.2);border-radius:999px;padding:5px 12px;font-size:.95rem;font-weight:500;color:var(--ink);background:#fff}
.ob-back{display:inline-flex;gap:8px;font-weight:600;color:var(--ob);text-decoration:none;margin-bottom:14px}
.ob-links{display:flex;flex-wrap:wrap;gap:8px}
.ob-links a{font-weight:600;color:var(--ob);border:1px solid rgba(31,42,92,.25);border-radius:999px;padding:6px 14px;text-decoration:none;background:#fff}
.ob-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.ob-cols a{display:block;border:1.5px solid rgba(31,42,92,.14);border-radius:16px;padding:16px 18px;text-decoration:none;background:#fff}
.ob-cols b{display:block;color:var(--ink);font-size:1.12rem}
.ob-cols span{display:block;color:var(--ink);font-size:.98rem;margin-top:4px;line-height:1.5;font-weight:500}
.ob-cta{background:var(--ob);color:#fff;border-radius:20px;padding:26px 28px;margin-top:40px}
.ob-cta h2,.ob-cta p{color:#fff!important;margin-top:0}
.ob-cta .btn{background:#fff;color:var(--ob);margin:4px 6px 4px 0}
.cart-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:28px;align-items:start}
.cart-box{background:#fff;border:1px solid rgba(31,42,92,.14);border-radius:18px;padding:20px}
.cart-line{display:grid;grid-template-columns:64px 1fr auto;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid rgba(0,0,0,.07)}
.cart-line img{width:64px;height:64px;border-radius:10px;background:#ededed;object-fit:cover}
.cart-line b{display:block;color:var(--ink);font-size:1.02rem;line-height:1.3}
.cart-line small{color:var(--ink);opacity:.85;font-size:.92rem;font-weight:500}
.cart-q{display:flex;align-items:center;gap:6px;margin-top:6px}
.cart-q button{width:30px;height:30px;border-radius:50%;border:1.5px solid rgba(31,42,92,.3);background:#fff;font:700 1rem Jost,sans-serif;color:var(--ob);cursor:pointer}
.cart-q .rm{width:auto;border:0;background:none;text-decoration:underline;font-weight:500;font-size:.9rem;margin-left:8px}
.cart-amt{font-weight:700;color:var(--ink);font-size:1.08rem}
.cart-tot{display:flex;justify-content:space-between;font-size:1.25rem;font-weight:700;color:var(--ink);padding-top:14px}
.cart-empty{text-align:center;padding:30px 10px}
.co label{display:block;font-weight:600;color:var(--ink);margin:10px 0 4px}
.co input,.co select,.co textarea{width:100%;border:1.5px solid rgba(31,42,92,.25);border-radius:12px;padding:11px 12px;font:500 1rem Jost,sans-serif;color:var(--ink);box-sizing:border-box;background:#fff}
.co .two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.co .chk{display:flex;gap:10px;align-items:flex-start;font-weight:500;margin-top:14px}
.co .chk input{width:auto;margin-top:5px}
.co button{width:100%;margin-top:16px;background:var(--ob);color:#fff;border:0;border-radius:999px;padding:14px;font:600 1.1rem Jost,sans-serif;cursor:pointer}
.co button[disabled]{opacity:.55;cursor:not-allowed}
.co-err{color:#b3261e;font-weight:600;min-height:1.2em;margin-top:8px}
.co-pick{background:#f3f5fb;border-radius:12px;padding:10px 14px;margin-top:8px;font-size:.98rem;color:var(--ink);font-weight:500;line-height:1.5}
.co-done{text-align:center}
.co-done .ok{width:64px;height:64px;border-radius:50%;background:#2e7d4f;color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center;margin:0 auto 12px}
@media(max-width:900px){.ob-pd,.cart-grid{grid-template-columns:1fr}.ob-steps{grid-template-columns:1fr}}
@media(max-width:520px){.ob-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.ob-card .ob-txt{padding:10px}.ob-card h3{font-size:.98rem}.ob-row{flex-direction:column;align-items:stretch}.ob-add{width:100%}.co .two{grid-template-columns:1fr}.ob-pd h1{font-size:1.8rem}.ob-body h2{font-size:1.75rem}.ob-chip{padding:7px 11px;font-size:.92rem}}
</style>"""

AUTH_BADGE = ('<a class="ob-auth" href="/obagi/"><img src="/img/obagi/obagi-medical-logo.webp" alt="Obagi Medical" width="89" height="38">'
              '<span>Authorized Obagi Medical Provider<small>Authentic products, physician guidance</small></span></a>')
STEPS = ('<div class="ob-steps">'
         '<div><b>1. Reserve online</b><span>Add products to your cart and reserve them. No payment online.</span></div>'
         '<div><b>2. We confirm</b><span>Our team confirms stock and texts or calls you when your order is ready, usually within 1&ndash;2 business days.</span></div>'
         '<div><b>3. Pay &amp; pick up</b><span>Pay in store at pickup. Orders are held for 7 days, and our team is happy to answer skincare questions.</span></div>'
         '</div>')

def page(title, desc, url, body, schemas, og_img, ogtype="website", robots="index, follow, max-image-preview:large"):
    sj = "\n".join('<script type="application/ld+json">\n%s\n</script>' % json.dumps(s, ensure_ascii=False) for s in schemas)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="{REGION}"><meta name="geo.placename" content="{CITY}">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
{HEAD_FONTS}
{sj}
{CSS}
</head>
<body>

{NAV}

{body}

{CONSULT}

{FOOTER}
{STICKY}
{SCRIPTS}
<script src="/shop.js?v={JSV}" defer></script>
</body>
</html>'''

def fit(t, limit=60):
    return t if len(clean(t)) <= limit else None

def write(rel, s):
    d = os.path.join(OUT, rel); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(s)

STORE_ORG = {"@type": "MedicalBusiness", "name": "Serene Med Spa — " + L["city"], "url": SITE + "/",
             "telephone": L["phone"], "address": {"@type": "PostalAddress", "streetAddress": L["addr"], "addressLocality": L["city"], "addressRegion": L["region"], "postalCode": L["zip"], "addressCountry": "US"}}

def offer(p, url):
    return {"@type": "Offer", "price": "%.2f" % p["price"], "priceCurrency": "USD", "url": url,
            "availability": "https://schema.org/InStoreOnly", "itemCondition": "https://schema.org/NewCondition",
            "seller": STORE_ORG,
            "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy", "applicableCountry": "US", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"},
            "shippingDetails": {"@type": "OfferShippingDetails", "doesNotShip": True, "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"}}}

def card(p):
    url = "/shop/%s/" % p["slug"]
    q = esc(clean(p["name"]).lower() + " " + " ".join(p["concerns"]).lower() + " " + clean(COLNAME[p["collection"]]).lower())
    return (f'<div class="ob-card" data-col="{p["collection"]}" data-q="{q}">'
            f'<a class="ob-img" href="{url}"><img loading="lazy" src="{img(p, True)}" alt="{esc(clean(p["name"]))} {esc(p["size"])}" width="400" height="400"></a>'
            f'<div class="ob-txt"><div class="ob-col">{short_col(p["collection"])}</div>'
            f'<h3><a href="{url}">{p["name"]}</a></h3><div class="ob-size">{p["size"]}</div>'
            f'<div class="ob-row"><span class="ob-price">{money(p["price"])}</span>'
            f'<button type="button" class="ob-add" data-add="{p["slug"]}" aria-label="Add {esc(clean(p["name"]))} to cart">Add to cart</button></div></div></div>')

def rx_card(p):
    return (f'<div class="ob-rx" data-col="rx" data-q="{esc(clean(p["name"]).lower())} prescription rx"><h3>{p["name"]}</h3>'
            f'<p>{p["size"]} &middot; Requires a physician visit. <a href="{SKIN_BOOK}" target="_blank" rel="noopener">Book a skin consult &rsaquo;</a></p></div>')

# ---------------- /shop/ ----------------
chips = '<button type="button" class="ob-chip on" data-f="all">All</button>' + "".join(
    f'<button type="button" class="ob-chip" data-f="{k}">{short_col(k)}</button>' for k, n, d in COLLECTIONS)
sections = ""
for k, n, d in COLLECTIONS:
    items = [p for p in PRODUCTS if p["collection"] == k]
    inner = "".join(rx_card(p) if p["rx"] else card(p) for p in items)
    sections += (f'<div class="ob-sec" data-sec="{k}" id="{k}"><div class="ob-colhead"><h2>{n}</h2><p>{d}</p></div>'
                 f'<div class="ob-grid">{inner}</div></div>')
FILTER_JS = """<script>
(function(){var chips=document.querySelectorAll('.ob-chip'),q=document.getElementById('ob-q');
function cur(){var c=document.querySelector('.ob-chip.on');return c?c.getAttribute('data-f'):'all';}
function apply(){var f=cur(),t=(q&&q.value||'').trim().toLowerCase();
document.querySelectorAll('.ob-sec').forEach(function(s){var any=false;s.querySelectorAll('[data-col]').forEach(function(c){var ok=(f==='all'||c.getAttribute('data-col')===f)&&(!t||c.getAttribute('data-q').indexOf(t)>-1);c.style.display=ok?'':'none';if(ok)any=true;});s.style.display=any?'':'none';});
var pp=document.getElementById('prepay');if(pp)pp.style.display=(f==='all'&&!t)?'':'none';}
chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');apply();});});
if(q)q.addEventListener('input',apply);
var h=location.hash.replace('#','');if(h){var c=document.querySelector('.ob-chip[data-f="'+h+'"]');if(c){c.click();}}
})();
</script>"""

PREPAY = ""
if HUDSON:
    ITEMS = [("HydraFacial", "/img/hydrafacial.jpg", 150, 120, "1 HydraFacial"), ("Botox &mdash; 20 Units", "/img/botox-inject.jpg", 220, 198, "20 units of Botox"),
             ("Morpheus8 RF", "/img/morpheus8.jpg", 800, 640, "1 Morpheus8 treatment"), ("Laser Facial", "/img/laser.jpg", 400, 320, "1 Laser Facial"),
             ("DiamondGlow", "/img/facial-2.jpg", 150, 120, "1 DiamondGlow facial"), ("Microneedling with PRP", "/img/facial-3.jpg", 500, 400, "1 Microneedling + PRP"),
             ("VI Chemical Peel", "/img/facial-4.jpg", 250, 200, "1 VI Peel"), ("Serene IV Infusion", "/img/iv-therapy-blog.jpg", 149, 119, "1 IV drip of your choice")]
    pc = "".join(f'<div class="ob-card"><div class="ob-img"><img loading="lazy" src="{i}" alt="{clean(n)} at Serene Med Spa, Hudson OH"></div><div class="ob-txt"><div class="ob-col">Prepay &amp; save {round((1 - pre / reg) * 100)}%</div><h3>{n}</h3><div class="ob-size">Redeems for {r} &middot; reg. ${reg}</div><div class="ob-row"><span class="ob-price">${pre}</span><a class="ob-add" href="{BOOK}" target="_blank" rel="noopener">Book now</a></div></div></div>' for n, i, reg, pre, r in ITEMS)
    PREPAY = (f'<div id="prepay"><div class="ob-colhead"><h2>Prepay &amp; Save on Treatments</h2>'
              f'<p>Buy select treatments in advance and save up to 20%. Book your visit and our team will apply your prepaid price.</p></div><div class="ob-grid">{pc}</div></div>')

shop_url = SITE + "/shop/"
shop_title = f"Shop Obagi Skincare | {CITY} | Serene Med Spa"
if len(clean(shop_title)) > 60: shop_title = f"Shop Obagi Skincare | {CITY}"
shop_desc = f"Shop authentic Obagi Medical skincare at Serene Med Spa in {CITY}. Reserve Professional-C, Nu-Derm Fx, ELASTIderm &amp; more online; pay and pick up in store."
if len(clean(shop_desc)) > 155:
    shop_desc = f"Authentic Obagi Medical skincare in {CITY}. Reserve Professional-C, Nu-Derm Fx, ELASTIderm &amp; more online; pay and pick up in store."
shop_body = f'''<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Shop</div>
    <div class="svc-hero-txt" style="max-width:860px">
      <div class="eyebrow">Medical-Grade Skincare &middot; {CITY}</div>
      <h1>Shop Obagi Medical Skincare in {CITY}</h1>
      <p style="font-size:1.15rem;font-weight:500;color:var(--ink)">Obagi is our main professional skincare line. Reserve your products online, then pay and pick them up at Serene Med Spa, where our physician-led team can help you choose.</p>
      {AUTH_BADGE}
    </div>
  </div>
</section>
<section class="ob-body">
  <div class="wrap">
    {STEPS}
    <div class="ob-tools" role="toolbar" aria-label="Filter products">{chips}<input id="ob-q" class="ob-search" type="search" placeholder="Search (e.g. vitamin C, eye, acne)" aria-label="Search Obagi products"></div>
    {sections}
    {PREPAY}
    <div class="ob-note"><p style="margin:0"><b>Good to know:</b> Prices shown are Obagi suggested retail prices. Sales tax is added at pickup. Our team confirms stock before your order is ready. Prescription Obagi products are dispensed only after a physician visit. Not sure where to start? <a href="/obagi/">Read our Obagi guide</a> or <a href="{SKIN_BOOK}" target="_blank" rel="noopener">book a skin consultation</a>.</p></div>
    <p style="margin-top:18px"><a class="btn" href="/cart/">View cart &amp; reserve (<span data-cart-count>0</span>)</a></p>
  </div>
</section>
{FILTER_JS}'''
shop_schema = [
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": shop_url}]},
    {"@context": "https://schema.org", "@type": "CollectionPage", "name": clean(shop_title), "url": shop_url, "description": clean(shop_desc),
     "mainEntity": {"@type": "ItemList", "numberOfItems": len(RETAIL), "itemListElement": [
         {"@type": "ListItem", "position": i + 1, "url": SITE + "/shop/%s/" % p["slug"], "name": clean(p["name"])} for i, p in enumerate(RETAIL)]}},
]
OG_DEFAULT = SITE + img(ns["BY_SLUG"]["professional-c-serum-20"])
write("shop", page(shop_title, shop_desc, shop_url, shop_body, shop_schema, OG_DEFAULT))

# ---------------- product pages ----------------
FAQ_P = [
    ("Is this authentic Obagi?", "Yes. Serene Med Spa is an authorized Obagi Medical provider and orders through Obagi&rsquo;s professional program, so every product is authentic and properly stored."),
    ("How does reserve and pickup work?", "Add the product to your cart and reserve it online. We confirm stock and contact you when it&rsquo;s ready, usually within 1&ndash;2 business days. You pay at pickup, and orders are held for 7 days."),
    ("Can I get help choosing the right product?", "Yes. Our team can recommend a routine when you pick up, or you can book a skin consultation for a personalized plan that pairs Obagi with in-office treatments."),
]
n = 0
for p in RETAIL:
    url = SITE + "/shop/%s/" % p["slug"]
    nm = clean(p["name"])
    title = fit(f"{nm} | {CITY}") or fit(f"{nm} | Serene Med Spa") or fit(nm) or nm[:60]
    desc = f"{clean(p['blurb'])} Reserve online, then pay and pick up at Serene Med Spa in {CITY}."
    if len(desc) > 155: desc = f"{nm} ({p['size']}), {money(p['price'])}. Reserve online, pay and pick up at Serene Med Spa in {CITY}."
    if len(desc) > 155: desc = f"{nm}, {money(p['price'])}. Reserve online and pick up at Serene Med Spa in {CITY}."
    if len(desc) > 155: desc = desc[:150].rsplit(" ", 1)[0] + "..."
    rel = [x for x in RETAIL if x["collection"] == p["collection"] and x["slug"] != p["slug"]][:4]
    if len(rel) < 4: rel += [x for x in RETAIL if x["collection"] != p["collection"] and x["collection"] != "travel" and x not in rel][: 4 - len(rel)]
    faq_html = "".join(f'<div class="faq reveal"><button>{q}<span class="plus">+</span></button><div class="ans"><p>{a}</p></div></div>' for q, a in FAQ_P)
    tags = "".join(f"<span>{c}</span>" for c in p["concerns"])
    body = f'''<section class="ob-body" style="padding-top:28px">
  <div class="wrap">
    <div class="crumbs" style="margin-bottom:10px"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/shop/">Shop</a> &nbsp;&#8250;&nbsp; <a href="/shop/#{p["collection"]}">{short_col(p["collection"])}</a></div>
    <a class="ob-back" href="/shop/#{p["collection"]}">&larr; Back to all Obagi products</a>
    <div class="ob-pd">
      <div class="ob-img"><img src="{img(p)}" alt="{esc(nm)} {esc(p["size"])}" width="800" height="800"></div>
      <div>
        <div class="ob-col">{short_col(p["collection"])}</div>
        <h1>{p["name"]}</h1>
        <p class="ob-size" style="margin:4px 0">{p["size"]}</p>
        <p class="ob-price" style="font-size:1.8rem;margin:10px 0 4px">{money(p["price"])}</p>
        <p style="margin:0 0 6px">{p["blurb"]}</p>
        <div class="ob-tags">{tags}</div>
        <div class="ob-buy"><input id="qty" class="ob-qty" type="number" min="1" max="20" value="1" aria-label="Quantity"><button type="button" class="ob-add" style="padding:13px 24px;font-size:1.05rem" data-add="{p["slug"]}" data-qty="qty">Add to cart</button><a href="/cart/" style="font-weight:600;color:var(--ob)">View cart (<span data-cart-count>0</span>)</a></div>
        <div class="co-pick"><b>Reserve online &middot; pay &amp; pick up in store</b><br>Serene Med Spa, {L["addr"]}, {L["city"]}, {L["region"]} {L["zip"]} &middot; <a href="tel:{L["tel"]}">{L["phone"]}</a></div>
        {AUTH_BADGE}
      </div>
    </div>

    <h2>Why buy {nm} at Serene Med Spa</h2>
    <p>Serene Med Spa is a physician-led medical spa and an authorized Obagi Medical provider serving {AREA}. Buying from an authorized provider means authentic, properly stored product and expert advice on how to fit {nm} into your routine and your in-office treatments.</p>
    {STEPS}

    <h2>Frequently asked questions</h2>
    <div class="faq-list">{faq_html}</div>

    <h2>You may also like</h2>
    <div class="ob-grid">{"".join(card(x) for x in rel)}</div>

    <div class="ob-cta reveal">
      <h2>Want a personalized skincare plan?</h2>
      <p>Book a skin consultation in {CITY}. We&rsquo;ll match Obagi products to your skin type and goals and pair them with treatments like HydraFacial, chemical peels or Morpheus8.</p>
      <a class="btn" href="{SKIN_BOOK}" target="_blank" rel="noopener">Book a Skin Consultation</a>
    </div>
    <p style="margin-top:22px;font-size:.98rem!important">Price shown is the Obagi suggested retail price; sales tax is added at pickup. Individual results vary. Obagi and Obagi product names are trademarks of Obagi Cosmeceuticals LLC.</p>
  </div>
</section>'''
    schema = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Shop", "item": SITE + "/shop/"},
            {"@type": "ListItem", "position": 3, "name": nm, "item": url}]},
        {"@context": "https://schema.org", "@type": "Product", "name": nm, "description": clean(p["blurb"]),
         "image": [SITE + img(p)], "brand": {"@type": "Brand", "name": "Obagi Medical"}, "sku": "OBAGI-" + p["slug"].upper(),
         "size": p["size"], "category": "Skin Care", "offers": offer(p, url)},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in FAQ_P]},
    ]
    write(os.path.join("shop", p["slug"]), page(esc(title), esc(desc), url, body, schema, SITE + img(p), ogtype="product"))
    n += 1

# ---------------- /cart/ ----------------
loc_opts = "".join(f'<option value="{k}"{" selected" if k == CITY else ""}>{k}</option>' for k in LOCS)
LOCJS = json.dumps({k: f'Serene Med Spa, {v["addr"]}, {v["city"]}, {v["region"]} {v["zip"]} &middot; {v["phone"]}' for k, v in LOCS.items()})
CART_JS = r"""<script>
(function(){
var LOCS=__LOCS__, Z={a:"https://crm.zoho.com/crm/WebToLeadForm",x:"__X__",m:"__M__"};
function S(){return window.SereneCart;}
var sel=document.getElementById('co-loc'),pick=document.getElementById('co-pick'),btn=document.getElementById('co-btn');
function sp(){pick.innerHTML='<b>Pickup at:</b> '+LOCS[sel.value];} sel.addEventListener('change',sp); sp();
window.SereneCartRender=function(){var s=S();if(!s)return;var c=s.load(),box=document.getElementById('cart-lines'),tot=document.getElementById('cart-total'),h='',keys=Object.keys(c);
  if(!document.getElementById('co').hidden)btn.disabled=!keys.length;
  if(!keys.length){box.innerHTML='<div class="cart-empty"><p><b>Your cart is empty.</b></p><p><a class="btn" href="/shop/">Shop Obagi skincare</a></p></div>';tot.innerHTML='';return;}
  keys.forEach(function(k){var p=s.cat[k];h+='<div class="cart-line"><img src="'+p.i+'" alt="" width="64" height="64"><div><b>'+p.n+'</b><small>'+p.s+' &middot; '+s.fmt(p.p)+' each</small><div class="cart-q"><button type="button" data-d="'+k+'" aria-label="Decrease quantity">&minus;</button><span>'+c[k]+'</span><button type="button" data-i="'+k+'" aria-label="Increase quantity">+</button><button type="button" class="rm" data-r="'+k+'">Remove</button></div></div><div class="cart-amt">'+s.fmt(p.p*c[k])+'</div></div>';});
  box.innerHTML=h; tot.innerHTML='<div class="cart-tot"><span>Estimated total</span><span>'+s.fmt(s.total(c))+'</span></div><p style="margin:4px 0 0;font-size:.95rem">Plus sales tax. Paid in store at pickup.</p>';
};
document.getElementById('cart-lines').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var s=S(),c=s.load(),k;
  if((k=b.getAttribute('data-i')))s.set(k,(c[k]||0)+1); else if((k=b.getAttribute('data-d')))s.set(k,(c[k]||0)-1); else if((k=b.getAttribute('data-r')))s.set(k,0);});
var f=document.getElementById('co'),err=document.getElementById('co-err');
f.addEventListener('submit',function(e){e.preventDefault();err.textContent='';var s=S();if(!s)return;var c=s.load(),keys=Object.keys(c);
  if(!keys.length){err.textContent='Your cart is empty.';return;}
  var bad=[].slice.call(f.querySelectorAll('[required]')).filter(function(i){return i.type==='checkbox'?!i.checked:!i.value.trim();});
  if(bad.length){bad[0].focus();err.textContent=bad[0].type==='checkbox'?'Please confirm the pickup terms.':'Please fill in the required fields.';return;}
  var em=document.getElementById('co-em').value.trim();if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(em)){err.textContent='Please enter a valid email address.';return;}
  var ph=document.getElementById('co-ph').value.replace(/\D/g,'');if(ph.length<10){err.textContent='Please enter a valid phone number.';return;}
  var d=new Date(),id='SO-'+String(d.getFullYear()).slice(2)+('0'+(d.getMonth()+1)).slice(-2)+('0'+d.getDate()).slice(-2)+'-'+Math.random().toString(36).slice(2,6).toUpperCase();
  var lines=keys.map(function(k){var p=s.cat[k];return c[k]+' x '+p.n+' ('+p.s+') @ '+s.fmt(p.p)+' = '+s.fmt(p.p*c[k]);});
  var notes=document.getElementById('co-notes').value.trim(),total=s.total(c);
  var desc='OBAGI PICKUP ORDER '+id+'\nPickup location: '+sel.value+'\n\n'+lines.join('\n')+'\n\nEstimated total (before tax): '+s.fmt(total)+'\nPayment: in store at pickup (not paid online)'+(notes?'\n\nCustomer notes: '+notes:'')+'\n\nPlaced on '+location.host+' at '+d.toLocaleString();
  var fd=new URLSearchParams();fd.append('xnQsjsdp',Z.x);fd.append('xmIwtLD',Z.m);fd.append('actionType','TGVhZHM=');fd.append('returnURL',location.origin+'/thank-you/');
  fd.append('Lead Status','Not Contacted');fd.append('LEADCF1','Obagi pickup order '+id+' ('+location.host+')');
  ['First Name','Last Name','Email','Phone','LEADCF3','aG9uZXlwb3Q'].forEach(function(n){var el=f.querySelector('[name="'+n+'"]');fd.append(n,el?el.value.trim():'');});
  fd.append('Description',desc);
  btn.disabled=true;btn.textContent='Reserving…';
  var items=keys.map(function(k){return {item_id:k,item_name:s.cat[k].n,item_brand:'Obagi',price:s.cat[k].p,quantity:c[k]};});
  fetch(Z.a,{method:'POST',body:fd,mode:'no-cors',credentials:'omit'}).then(function(){
    try{if(window.gtag){gtag('event','generate_lead',{event_category:'obagi_order',value:total,currency:'USD'});gtag('event','obagi_reserve',{transaction_id:id,value:total,currency:'USD',items:items});}}catch(x){}
    try{if(window.fbq)fbq('track','Lead',{value:total,currency:'USD'});}catch(x){}
    var done=document.getElementById('co-done');f.hidden=true;done.hidden=false;
    done.innerHTML='<div class="ok">&#10003;</div><h2 style="margin:0 0 6px">Order reserved!</h2><p>Your order number is <b>'+id+'</b>.</p><p>We&rsquo;ll confirm stock and contact you when it&rsquo;s ready (usually 1&ndash;2 business days). Pay at pickup.</p><p class="co-pick" style="text-align:left">'+LOCS[sel.value]+'</p><p style="text-align:left;font-size:.98rem">'+lines.join('<br>')+'<br><b>Estimated total: '+s.fmt(total)+' + tax</b></p><p><a class="btn" href="/shop/">Continue shopping</a></p>';
    s.clear();done.scrollIntoView({behavior:'smooth',block:'center'});
  }).catch(function(){btn.disabled=false;btn.textContent='Reserve My Order';err.textContent='Something went wrong. Please try again or call us to reserve your order.';});
});
if(window.SereneCart)window.SereneCartRender();
})();
</script>""".replace("__LOCS__", LOCJS).replace("__X__", ZX[0]).replace("__M__", ZX[1])
cart_body = f'''<section class="ob-body" style="padding-top:28px">
  <div class="wrap">
    <div class="crumbs" style="margin-bottom:10px"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/shop/">Shop</a> &nbsp;&#8250;&nbsp; Cart</div>
    <h1 style="margin:0 0 6px">Your Pickup Cart</h1>
    <p style="margin:0 0 18px">Reserve now and <b>pay in store when you pick up</b>. No card is needed online.</p>
    <div class="cart-grid">
      <div class="cart-box"><div id="cart-lines"><p>Loading your cart&hellip;</p></div><div id="cart-total"></div><p style="margin:14px 0 0"><a href="/shop/" style="font-weight:600;color:var(--ob)">&larr; Keep shopping</a></p></div>
      <div class="cart-box">
        <form class="co" id="co" novalidate>
          <h2 style="margin:0 0 4px;font-size:1.7rem">Reserve for pickup</h2>
          <div class="two"><div><label for="co-fn">First name *</label><input id="co-fn" name="First Name" autocomplete="given-name" required maxlength="40"></div>
          <div><label for="co-ln">Last name *</label><input id="co-ln" name="Last Name" autocomplete="family-name" required maxlength="80"></div></div>
          <label for="co-em">Email *</label><input id="co-em" type="email" name="Email" autocomplete="email" required maxlength="100" inputmode="email">
          <label for="co-ph">Mobile phone *</label><input id="co-ph" type="tel" name="Phone" autocomplete="tel" required maxlength="30" inputmode="tel">
          <label for="co-loc">Pickup location *</label><select id="co-loc" name="LEADCF3">{loc_opts}</select>
          <div class="co-pick" id="co-pick"></div>
          <label for="co-notes">Notes (optional)</label><textarea id="co-notes" rows="3" maxlength="600" placeholder="Questions, preferred pickup day, etc."></textarea>
          <input type="text" name="aG9uZXlwb3Q" value="" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
          <label class="chk"><input type="checkbox" id="co-ok" required><span>I understand payment is collected in store at pickup, prices do not include sales tax, and my order is held for 7 days.</span></label>
          <button type="submit" id="co-btn" disabled>Reserve My Order</button>
          <div class="co-err" id="co-err" role="alert"></div>
          <p style="font-size:.9rem;margin:8px 0 0">By reserving, you agree to be contacted by Serene Med Spa about your order. We never sell your information.</p>
        </form>
        <div class="co-done" id="co-done" hidden></div>
      </div>
    </div>
  </div>
</section>
{CART_JS}'''
write("cart", page(f"Your Cart | Serene Med Spa {L['city']}", "Review your Obagi order and reserve it for in-store pickup and payment.", SITE + "/cart/", cart_body, [], OG_DEFAULT, robots="noindex, follow"))

# ---------------- /obagi/ brand page ----------------
feat_slugs = ["professional-c-serum-20", "nu-derm-fx-system-normal-oily", "elastiderm-firming-eye-cream", "hydrate-luxe",
              "sun-shield-mineral-spf-50", "retinol-1-0", "clenziderm-acne-therapeutic-system", "nu-cil-eyelash-enhancing-serum"]
feat = "".join(card(ns["BY_SLUG"][s]) for s in feat_slugs)
colcards = "".join(f'<a href="/shop/#{k}"><b>{n}</b><span>{d}</span></a>' for k, n, d in COLLECTIONS if k != "travel")
FAQ_O = [
    ("Is Serene Med Spa an authorized Obagi provider?", f"Yes. Serene Med Spa in {CITY} is an authorized Obagi Medical provider. Obagi is our main professional skincare line, and we order through Obagi&rsquo;s professional program."),
    ("Why buy Obagi from a medical spa instead of an online marketplace?", "Obagi Medical is sold through physicians and licensed skincare professionals. Buying from an authorized provider helps you avoid counterfeit, expired or improperly stored products, and you get expert guidance on how to use them."),
    ("What is the difference between Obagi Nu-Derm and Nu-Derm Fx?", "The classic Obagi Nu-Derm system includes prescription-strength products and is dispensed only after a physician visit. Nu-Derm Fx is a hydroquinone-free, non-prescription version that uses ingredients such as arbutin to brighten and even skin tone."),
    ("Which Obagi vitamin C serum should I choose?", "Professional-C Serum comes in 10%, 15% and 20%. We usually suggest 10% for sensitive skin or first-time users, 15% for normal to combination skin and 20% for normal to oily skin that already tolerates vitamin C."),
    ("Can I order Obagi online and pick it up?", f"Yes. Add products to your cart on our website and reserve them. We&rsquo;ll contact you when your order is ready, and you pay when you pick it up at {L['addr']}, {L['city']}."),
    ("Does Obagi work with in-office treatments?", "Yes. A consistent Obagi routine helps prepare the skin for, and maintain results from, treatments like chemical peels, HydraFacial, microneedling, laser facials and Morpheus8. Your provider will tell you when to pause active products around a treatment."),
]
faq_o = "".join(f'<div class="faq reveal"><button>{q}<span class="plus">+</span></button><div class="ans"><p>{a}</p></div></div>' for q, a in FAQ_O)
ob_url = SITE + "/obagi/"
ob_title = f"Authorized Obagi Provider | {CITY} | Serene Med Spa"
if len(clean(ob_title)) > 60: ob_title = f"Authorized Obagi Medical Provider | {CITY}"
ob_desc = f"Serene Med Spa is an authorized Obagi Medical provider in {CITY}. Physician guidance on Nu-Derm, Professional-C and ELASTIderm; reserve online, pick up in store."
if len(clean(ob_desc)) > 155:
    ob_desc = f"Authorized Obagi Medical provider in {CITY}. Physician guidance on Nu-Derm, Professional-C and ELASTIderm. Reserve online, pick up in store."
ob_body = f'''<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/shop/">Shop</a> &nbsp;&#8250;&nbsp; Obagi Medical</div>
    <div class="svc-hero-txt" style="max-width:860px">
      <img src="/img/obagi/obagi-medical-logo.webp" alt="Obagi Medical logo" width="173" height="74" style="height:74px;width:auto;margin-bottom:8px">
      <div class="eyebrow">Authorized Obagi Medical Provider &middot; {CITY}</div>
      <h1>Obagi Medical Skincare in {CITY_LONG}</h1>
      <p style="font-size:1.15rem;font-weight:500;color:var(--ink)">Obagi is the professional skincare line we trust most at Serene Med Spa. As an authorized Obagi provider, we help patients across {AREA} choose the right products, and you can reserve them online for in-store pickup.</p>
      <p><a class="btn" href="/shop/">Shop Obagi Products</a> &nbsp; <a class="btn btn-outline" href="{SKIN_BOOK}" target="_blank" rel="noopener">Book a Skin Consult</a></p>
    </div>
  </div>
</section>
<section class="ob-body">
  <div class="wrap" style="max-width:1100px">
    <h2>Why Obagi is our main skincare line</h2>
    <p>For more than 30 years, Obagi Medical has built its reputation on science-backed formulas made for use under professional guidance. We chose Obagi because it gives our physicians a complete toolkit, from gentle daily cleansers to potent vitamin C, retinol and brightening systems, that pairs naturally with the treatments we perform every day.</p>
    <ul>
      <li><b>Authentic, properly stored product</b> ordered through Obagi&rsquo;s professional program.</li>
      <li><b>Physician-led recommendations</b> matched to your skin type, goals and treatment plan.</li>
      <li><b>Reserve online, pick up in store</b> in {L["city"]}, and pay when you arrive.</li>
    </ul>

    <h2>Best-selling Obagi products</h2>
    <div class="ob-grid">{feat}</div>
    <p style="margin-top:14px"><a href="/shop/" style="font-weight:600">See all {len(RETAIL)} Obagi products &rsaquo;</a></p>

    <h2>Shop by collection</h2>
    <div class="ob-cols">{colcards}</div>

    <h2>Obagi Nu-Derm: prescription vs. Nu-Derm Fx</h2>
    <p>The <b>Obagi Nu-Derm&reg; System</b> is Obagi&rsquo;s best-known program for visible discoloration, sun damage and uneven texture. The classic prescription version is dispensed only after an exam with one of our physicians, who will decide whether it is appropriate for you and monitor your progress.</p>
    <p><b>Nu-Derm Fx&reg;</b> is the non-prescription, hydroquinone-free option. It uses brightening ingredients such as arbutin and can be reserved online. Not sure which is right for you? A <a href="{SKIN_BOOK}" target="_blank" rel="noopener">skin consultation</a> is the best place to start.</p>

    <h2>Pair Obagi with in-office treatments</h2>
    <p>A consistent home routine helps you get more from professional treatments and keeps results looking fresh longer. Popular pairings at Serene include:</p>
    <div class="ob-links"><a href="/hydrafacial/">HydraFacial</a><a href="/chemical-peels/">Chemical Peels</a><a href="/microneedling/">Microneedling</a><a href="/laser-facial/">Laser Facial</a><a href="/morpheus8/">Morpheus8</a><a href="/hyperpigmentation/">Hyperpigmentation Treatment</a></div>

    <h2>How to order</h2>
    {STEPS}
    <div class="co-pick" style="margin-top:12px"><b>Pickup location:</b> Serene Med Spa, {L["addr"]}, {L["city"]}, {L["region"]} {L["zip"]} &middot; <a href="tel:{L["tel"]}">{L["phone"]}</a></div>

    <h2>Obagi FAQs</h2>
    <div class="faq-list">{faq_o}</div>

    <div class="ob-cta reveal">
      <h2>Build your Obagi routine with a physician</h2>
      <p>Book a skin consultation at Serene Med Spa in {CITY}. We&rsquo;ll recommend the right Obagi products for your skin and goals.</p>
      <a class="btn" href="{SKIN_BOOK}" target="_blank" rel="noopener">Book a Skin Consultation</a><a class="btn" href="/shop/">Shop Obagi</a>
    </div>
    <p style="margin-top:22px;font-size:.98rem!important">Prescription products are dispensed only after a physician visit. Individual results vary. Obagi, Nu-Derm, Professional-C, ELASTIderm, CLENZIderm, Nu-Cil and SUZANOBAGIMD are trademarks of Obagi Cosmeceuticals LLC.</p>
  </div>
</section>'''
ob_schema = [
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": SITE + "/shop/"},
        {"@type": "ListItem", "position": 3, "name": "Obagi Medical", "item": ob_url}]},
    {"@context": "https://schema.org", "@type": "WebPage", "name": clean(ob_title), "url": ob_url, "description": clean(ob_desc),
     "about": {"@type": "Brand", "name": "Obagi Medical", "logo": SITE + "/img/obagi/obagi-medical-logo.png"},
     "publisher": STORE_ORG},
    {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in FAQ_O]},
]
write("obagi", page(ob_title, ob_desc, ob_url, ob_body, ob_schema, SITE + "/img/obagi/obagi-medical-logo.png"))
print(f"build_obagi_shop: /shop/ + {n} product pages + /cart/ + /obagi/ ({CITY}); shop.js v{JSV}")
