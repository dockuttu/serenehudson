#!/usr/bin/env python3
"""build_offer_lp.py: stripped-down ad landing pages (Oct 11, 2026, Robin approved).

Writes /lp/laser-hair-removal-offer/ and /lp/tattoo-removal-offer/ for one office.
These are "offer" pages for Google Demand Gen (laser hair removal) and Search
(tattoo removal), modeled on high-converting single-offer pages:
  - no site menu
  - one offer
  - repeated Book / Text / Call buttons
  - price table and short FAQ
Self-contained HTML (inline CSS). noindex, and kept out of the sitemap.
Runs LAST in build.sh (after v2_merge + add_text_links), so the files are served
exactly as written. Links therefore carry the /<office>/ prefix themselves.

Rules baked in:
  - no "best" or guaranteed claims, no prescription drug names
  - Hudson/Barboursville = "physician-led"
  - standard 20% first-visit wording
  - Text before Call
  - Google Ads tag only (no Meta pixel); no form, so no form data in URLs

Usage: python3 build_offer_lp.py bundle/site hudson|barboursville
"""
import os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
OFFICE = sys.argv[2] if len(sys.argv) > 2 else "hudson"

OFFICES = {
    "hudson": dict(name="Hudson, OH", city="Hudson", addr="50 W Streetsboro St, Suite 2, Hudson, OH 44236",
                   tel="+13304605915", tel_d="(330) 460-5915", sms="+13303032031", sms_d="(330) 303-2031",
                   area="Hudson, Stow, Twinsburg &amp; Akron"),
    "barboursville": dict(name="Barboursville, WV", city="Barboursville", addr="1 Chateau Grove Ln, Barboursville, WV 25504",
                   tel="+13045200461", tel_d="(304) 520-0461", sms="+13043960295", sms_d="(304) 396-0295",
                   area="Barboursville, Huntington &amp; the Tri-State"),
}
O = OFFICES[OFFICE]
MM = "https://booking.mangomint.com/serenemedspa?serviceId=%s"
BOOK_LHR = MM % 339       # Laser Hair Removal
BOOK_CONSULT = MM % 321   # Free Consultation
OFFER = "20% off your first visit &mdash; applies to any product or service; can&rsquo;t be combined with another discount."

GTAG = """<script async src="https://www.googletagmanager.com/gtag/js?id=AW-788907512"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());gtag('config','AW-788907512');gtag('config','G-BE2Z65PN2X');
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('booking.mangomint.com')>-1){gtag('event','conversion',{'send_to':'AW-788907512/lQdCCL31zvUcEPiLl_gC'});}
else if(h.indexOf('tel:')===0){gtag('event','call_click',{'send_to':'AW-788907512'});gtag('event','conversion',{'send_to':'AW-788907512/d4kvCJjh6_0cEPiLl_gC'});}
else if(h.indexOf('sms:')===0){gtag('event','text_click',{'send_to':'AW-788907512'});}},true);
</script>"""

CSS = """
:root{--forest:#10322F;--forest-700:#1d4a45;--lav:#C4C7E6;--lav-100:#EEEFF8;--grey:#F5F7FA;--ink:#121417;--muted:#5b6470;--line:#e3e6ec}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:Poppins,system-ui,-apple-system,Segoe UI,sans-serif;font-weight:300;color:var(--ink);background:#fff;line-height:1.6;padding-bottom:76px}
a{color:var(--forest)}img{max-width:100%;display:block}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
header.top{border-bottom:1px solid var(--line);background:#fff}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;height:64px}
.brand{font-family:'Noto Serif Display',Georgia,serif;font-size:1.15rem;letter-spacing:.08em;text-transform:uppercase;color:var(--forest);text-decoration:none;font-weight:500}
.brand small{display:block;font-family:Poppins,sans-serif;font-size:.62rem;letter-spacing:.18em;color:var(--muted)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border-radius:999px;padding:13px 22px;font-weight:500;font-size:.95rem;text-decoration:none;border:1.5px solid var(--forest);white-space:nowrap}
.btn-p{background:var(--forest);color:#fff}.btn-p:hover{background:var(--forest-700)}
.btn-o{background:#fff;color:var(--forest)}
.btn-sm{padding:9px 16px;font-size:.85rem}
.hero{background:linear-gradient(180deg,var(--lav-100),#fff);padding:40px 0 28px}
.eyebrow{display:inline-block;background:var(--lav);color:var(--forest);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;padding:5px 12px;border-radius:999px;font-weight:500}
h1,h2{font-family:'Noto Serif Display',Georgia,serif;font-weight:500;color:var(--forest);line-height:1.15;margin:.5em 0 .35em}
h1{font-size:clamp(2rem,6.5vw,3.1rem)}h2{font-size:clamp(1.5rem,4.5vw,2.05rem)}
.lead{font-size:1.08rem;color:#2a3138;max-width:640px}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0}
.chip{background:#fff;border:1px solid var(--line);border-radius:14px;padding:10px 14px;flex:1 1 140px;max-width:220px}
.chip b{display:block;font-size:1.35rem;color:var(--forest);font-weight:600}.chip span{font-size:.8rem;color:var(--muted)}
.ctas{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 8px}
.fine{font-size:.8rem;color:var(--muted)}
.offer{background:var(--forest);color:#fff;border-radius:18px;padding:18px 20px;margin:22px 0}
.offer b{color:var(--lav)}
section{padding:36px 0}section.alt{background:var(--grey)}
.steps{display:grid;grid-template-columns:1fr;gap:14px;counter-reset:s}
.step{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px}
.step:before{counter-increment:s;content:counter(s);display:inline-flex;width:28px;height:28px;border-radius:50%;background:var(--lav);color:var(--forest);font-weight:600;align-items:center;justify-content:center;margin-bottom:6px}
.step h3{margin:.2em 0;font-size:1.02rem;font-weight:600}
table.pr{width:100%;border-collapse:collapse;background:#fff;border-radius:14px;overflow:hidden;font-size:.95rem}
table.pr th,table.pr td{padding:11px 12px;border-bottom:1px solid var(--line);text-align:left}
table.pr th{background:var(--forest);color:#fff;font-weight:500;font-size:.85rem}
table.pr td:not(:first-child),table.pr th:not(:first-child){text-align:right;white-space:nowrap}
table.pr tr.hl td{background:var(--lav-100);font-weight:500}
details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:10px 0}
summary{cursor:pointer;font-weight:500;color:var(--forest)}
.trust{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:.88rem;color:#2a3138;margin:14px 0 0;padding:0;list-style:none}
.trust li:before{content:"\\2713";color:var(--forest);font-weight:700;margin-right:6px}
.cardsz{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.sz{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px}
.sz h3{margin:0 0 2px;font-size:1rem;font-weight:600;color:var(--forest)}.sz p{margin:0;font-size:.8rem;color:var(--muted)}
.sz .p{font-size:1.4rem;font-weight:600;color:var(--forest);margin-top:8px}.sz .k{font-size:.8rem}
footer{border-top:1px solid var(--line);padding:22px 0;font-size:.82rem;color:var(--muted)}
.mbar{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid var(--line);display:flex;gap:8px;padding:10px 12px;z-index:50}
.mbar .btn{flex:1;padding:12px 8px}
@media(min-width:760px){.steps{grid-template-columns:repeat(3,1fr)}.cardsz{grid-template-columns:repeat(4,1fr)}.mbar{display:none}body{padding-bottom:0}}
@media(max-width:420px){header.top .btn-sm.hide-xs{display:none}}
"""

def page(slug, title, desc, body, book):
    o = O
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="https://serenemedspas.com/{OFFICE}/lp/{slug}/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Display:wght@500&family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
{GTAG}
</head><body>
<header class="top"><div class="wrap">
<a class="brand" href="/{OFFICE}/">Serene Med Spa<small>{o['name']}</small></a>
<span style="display:flex;gap:8px"><a class="btn btn-o btn-sm hide-xs" href="sms:{o['sms']}">Text us</a><a class="btn btn-p btn-sm" href="{book}" target="_blank" rel="noopener">Book</a></span>
</div></header>
{body}
<footer><div class="wrap">
<p><b style="color:var(--forest)">Serene Med Spa &middot; {o['name']}</b><br>{o['addr']}<br>
Text <a href="sms:{o['sms']}">{o['sms_d']}</a> &middot; Call <a href="tel:{o['tel']}">{o['tel_d']}</a></p>
<p>Individual results vary. Treatment eligibility is confirmed at your consultation. Prices are per session unless noted and may change; packages are prepaid.
<br><a href="/privacy-practices/">Privacy</a> &middot; <a href="/{OFFICE}/">Visit our full site</a></p>
<p>&copy; 2026 Serene Med Spa</p></div></footer>
<div class="mbar"><a class="btn btn-o" href="sms:{o['sms']}">Text us</a><a class="btn btn-o" href="tel:{o['tel']}">Call</a><a class="btn btn-p" href="{book}" target="_blank" rel="noopener">Book</a></div>
</body></html>"""

def ctas(book, label):
    o = O
    return f"""<div class="ctas"><a class="btn btn-p" href="{book}" target="_blank" rel="noopener">{label}</a>
<a class="btn btn-o" href="sms:{o['sms']}">Text {o['sms_d']}</a><a class="btn btn-o" href="tel:{o['tel']}">Call</a></div>"""

LHR_ROWS = [("Bikini Line",69,345,1),("Brazilian",89,445,1),("Underarms",75,375,1),("Upper Lip",75,375,0),("Chin",99,495,0),
            ("Full Face",99,495,0),("Neck (+ Beard Line)",160,800,0),("Stomach",160,800,0),("Half Arms",180,900,0),
            ("Lower Legs",240,1200,0),("Upper Legs",240,1200,0),("Full Arms",280,1400,0),("Full Back",310,1550,0),
            ("Chest + Abdomen",310,1550,0),("Full Legs",360,1800,1),("Full Body",510,2550,0)]

def lhr():
    o = O
    rows = "".join(f'<tr class="{"hl" if h else ""}"><td>{a}</td><td>${p:,}</td><td>${k:,}</td></tr>' for a,p,k,h in LHR_ROWS)
    body = f"""
<div class="hero"><div class="wrap">
<span class="eyebrow">Laser hair removal &middot; {o['name']}</span>
<h1>Start now. Smooth by summer.</h1>
<p class="lead">Laser hair removal takes a series of sessions spaced 4&ndash;6 weeks apart, so starting this fall or winter lets most people finish their series before swimsuit season. No more shaving, waxing or ingrown hairs.</p>
<div class="chips">
<div class="chip"><b>$69</b><span>Bikini line / session</span></div>
<div class="chip"><b>$89</b><span>Brazilian / session</span></div>
<div class="chip"><b>$75</b><span>Underarms / session</span></div>
<div class="chip"><b>6 for 5</b><span>Every package of 6</span></div>
</div>
{ctas(BOOK_LHR, "Book laser hair removal")}
<p class="fine">Not sure yet? <a href="{BOOK_CONSULT}" target="_blank" rel="noopener">Book a complimentary, no-commitment consultation</a>.</p>
<ul class="trust"><li>Physician-led team</li><li>Medical-grade lasers</li><li>Packages of 6 for the price of 5</li><li>Serving {o['area']}</li></ul>
<div class="offer"><b>New clients:</b> {OFFER}</div>
</div></div>

<section><div class="wrap">
<h2>How it works</h2>
<div class="steps">
<div class="step"><h3>Quick consult</h3><p>We check your hair and skin type, talk through areas and set your plan. Hair needs some color for the laser to see it, so very light blond, gray or red hair responds less.</p></div>
<div class="step"><h3>Fast sessions</h3><p>Most areas take 5&ndash;30 minutes. Most people describe a quick snap or warmth, and cooling keeps it comfortable.</p></div>
<div class="step"><h3>Smoother with each visit</h3><p>Hair grows in cycles, so a series of about 6 sessions catches each one. Some areas need an occasional touch-up.</p></div>
</div>
{ctas(BOOK_LHR, "Book your first session")}
</div></section>

<section class="alt"><div class="wrap">
<h2>Simple, posted prices</h2>
<p>Pay per session, or prepay a package of 6 for the price of 5.</p>
<table class="pr"><thead><tr><th>Area</th><th>Per session</th><th>Package of 6</th></tr></thead><tbody>{rows}</tbody></table>
<p class="fine">Other areas (sideburns, ears, hands, shoulders and more) are on our <a href="/{OFFICE}/pricing/">full price list</a>.</p>
{ctas(BOOK_LHR, "Book laser hair removal")}
</div></section>

<section><div class="wrap">
<h2>Questions</h2>
<details><summary>How many sessions will I need?</summary><p>Most people need about 6, spaced 4&ndash;6 weeks apart (face areas a bit sooner). Results vary with hair color, thickness and hormones, and some people need occasional touch-ups.</p></details>
<details><summary>Does it hurt?</summary><p>Most people describe a quick snap or warm sensation. Sessions are short, and cooling keeps them comfortable.</p></details>
<details><summary>How do I prepare?</summary><p>Shave the area the day before. Skip waxing, plucking and threading for 4 weeks before your session (they remove the root the laser targets). Avoid sun and self-tanner for 2 weeks.</p></details>
<details><summary>Is it right for my skin?</summary><p>We match the laser setting to your skin and hair type at your consultation. If laser isn&rsquo;t a good fit for you, we&rsquo;ll tell you.</p></details>
{ctas(BOOK_LHR, "Book laser hair removal")}
</div></section>
"""
    return page("laser-hair-removal-offer", f"Laser Hair Removal {o['city']} | Bikini $69, Brazilian $89 | Serene",
                f"Laser hair removal in {o['name']}: bikini $69, Brazilian $89, underarms $75 per session; packages of 6 for the price of 5. Physician-led team.",
                body, BOOK_LHR)

TAT = [("Micro","Under 1 sq in &middot; about a quarter",125,625),("Small","1&ndash;4 sq in &middot; passport photo",150,750),
       ("Medium","5&ndash;9 sq in &middot; credit card",250,1250),("Large","10&ndash;16 sq in &middot; dollar bill",400,2000)]

def tattoo():
    o = O
    cards = "".join(f'<div class="sz"><h3>{n}</h3><p>{d}</p><div class="p">${p:,}</div><div class="k">per session &middot; 6 for ${k:,}</div></div>' for n,d,p,k in TAT)
    body = f"""
<div class="hero"><div class="wrap">
<span class="eyebrow">Laser tattoo removal &middot; {o['name']}</span>
<h1>Ready to fade it?</h1>
<p class="lead">Remove a tattoo completely, or lighten it for a cover-up. Pricing is by size, so you&rsquo;ll know the cost up front. Start with a complimentary, no-commitment consultation.</p>
<div class="chips">
<div class="chip"><b>From $125</b><span>per session</span></div>
<div class="chip"><b>Buy 5, get the 6th</b><span>free with any package</span></div>
<div class="chip"><b>$0</b><span>consultation</span></div>
</div>
{ctas(BOOK_CONSULT, "Book a free consultation")}
<ul class="trust"><li>Physician-led team</li><li>PICO laser technology</li><li>Removal or cover-up fading</li><li>Serving {o['area']}</li></ul>
<div class="offer"><b>New clients:</b> {OFFER}</div>
</div></div>

<section class="alt"><div class="wrap">
<h2>Priced by size</h2>
<p>Measure your tattoo, or text us a photo and we&rsquo;ll tell you the size tier.</p>
<div class="cardsz">{cards}</div>
<p class="fine">Larger pieces (sleeves, back pieces) are quoted at your consultation.</p>
{ctas(BOOK_CONSULT, "Book a free consultation")}
</div></section>

<section><div class="wrap">
<h2>How it works</h2>
<div class="steps">
<div class="step"><h3>Consultation</h3><p>We look at the ink colors, depth, age and your skin, then give you a size price and a realistic plan for full removal or cover-up fading.</p></div>
<div class="step"><h3>Short sessions</h3><p>The laser breaks ink into tiny particles. Most sessions take just minutes.</p></div>
<div class="step"><h3>Your body does the rest</h3><p>Your immune system clears the ink between visits, so sessions are spaced about 6&ndash;8 weeks apart. Each one fades it further.</p></div>
</div>
{ctas(BOOK_CONSULT, "Book a free consultation")}
</div></section>

<section class="alt"><div class="wrap">
<h2>Questions</h2>
<details><summary>How many sessions will I need?</summary><p>It depends on the ink, colors, age of the tattoo and where it is on the body. Many tattoos need several sessions, and some need more. We&rsquo;ll give you an estimate at your consultation. Results vary.</p></details>
<details><summary>Does it hurt?</summary><p>Most people compare it to a rubber-band snap. Sessions are short, and we use cooling to keep you comfortable.</p></details>
<details><summary>Can you just lighten it for a cover-up?</summary><p>Yes. Fading usually takes fewer sessions than full removal and gives your artist a cleaner canvas.</p></details>
<details><summary>Are some colors harder to remove?</summary><p>Black and dark blue usually respond best. Some colors, like light green, light blue and yellow, can take more sessions. We&rsquo;ll set expectations at your consultation.</p></details>
<details><summary>What&rsquo;s aftercare like?</summary><p>Expect redness and swelling for a few days, sometimes blisters. Keep it clean and covered, and avoid sun on the area. We&rsquo;ll give you written aftercare.</p></details>
{ctas(BOOK_CONSULT, "Book a free consultation")}
</div></section>
"""
    return page("tattoo-removal-offer", f"Tattoo Removal {o['city']} | From $125, Priced by Size | Serene",
                f"Laser tattoo removal in {o['name']}, priced by size from $125 a session. Buy 5 sessions, get the 6th free. Complimentary consultation. Physician-led team.",
                body, BOOK_CONSULT)

for slug, html in (("laser-hair-removal-offer", lhr()), ("tattoo-removal-offer", tattoo())):
    d = os.path.join(ROOT, "lp", slug); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    print("build_offer_lp:", OFFICE, "/lp/%s/" % slug, len(html), "bytes")
