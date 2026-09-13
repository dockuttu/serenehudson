#!/usr/bin/env python3
"""zoho_form_patch.py — swap the HubSpot consult form for a native Zoho CRM web-to-lead form.

Run from a site repo root (serenehudson / serenebarboursville):
    python3 zoho_form_patch.py "Hudson, OH" https://hudson.serenemedspas.com

What it does (idempotent):
  1. common.py  — replaces the CONSULT_SECTION block with a self-hosted form that POSTs to
                  Zoho CRM's WebToLeadForm (form "Request a Consultation", Leads module).
  2. bundle/site/styles.css — replaces the .hs-* form styles with .zf-* styles.
  3. build_thankyou.py — new page /thank-you/ (noindex) used as the no-JS fallback redirect.
  4. build.sh — runs build_thankyou.py after the other section pages.
"""
import re, sys, os

LOCATION = sys.argv[1] if len(sys.argv) > 1 else ""
SITE_URL = (sys.argv[2] if len(sys.argv) > 2 else "").rstrip("/")
if not LOCATION or not SITE_URL:
    sys.exit("usage: zoho_form_patch.py 'Hudson, OH' https://hudson.serenemedspas.com")

# ---- Zoho web-to-lead identifiers (form "Request a Consultation", org 939012486) ----
ZOHO_ACTION = "https://crm.zoho.com/crm/WebToLeadForm"
XNQ = "29c1b6f4e6219d1e5682cd0434b1ce181ccda55241b6394ae70c33a7f83e1dfa"
XMI = "139bc9e7ae4c09a2ea84b820c0c3b10459ed2d907a8c88693956f8d217af21d20ea75c0d1b75b947bf1bf59cc28d7274"
RETURN_URL = SITE_URL + "/thank-you/"

LOC_OPTIONS = ["Hudson, OH", "Barboursville, WV"]
opts = "".join(
    '<option value="%s"%s>%s</option>' % (o, ' selected' if o == LOCATION else '', o) for o in LOC_OPTIONS
)

FORM = '''<section class="consult" id="consult">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Get In Touch</div><h2>Request a Consultation</h2><p>Tell us what you&rsquo;re interested in and our team will reach out to schedule your visit.</p></div>
    <div class="consult-card reveal">
      <form class="zf" id="zf-consult" action="%(action)s" method="POST" accept-charset="UTF-8" novalidate>
        <input type="hidden" name="xnQsjsdp" value="%(xnq)s">
        <input type="hidden" name="xmIwtLD" value="%(xmi)s">
        <input type="hidden" name="actionType" value="TGVhZHM=">
        <input type="hidden" name="returnURL" value="%(ret)s">
        <input type="hidden" name="zc_gad" id="zc_gad" value="">
        <input type="hidden" name="Lead Status" value="Not Contacted">
        <input type="hidden" name="LEADCF1" id="zf-src" value="Website form: %(host)s">
        <input type="text" name="aG9uZXlwb3Q" value="" tabindex="-1" autocomplete="off" class="zf-hp" aria-hidden="true">
        <div class="zf-grid">
          <div class="zf-field"><label for="zf-fn">First name</label><input type="text" id="zf-fn" name="First Name" maxlength="40" autocomplete="given-name"></div>
          <div class="zf-field"><label for="zf-ln">Last name <span>*</span></label><input type="text" id="zf-ln" name="Last Name" maxlength="80" required autocomplete="family-name"></div>
          <div class="zf-field"><label for="zf-em">Email <span>*</span></label><input type="email" id="zf-em" name="Email" maxlength="100" required autocomplete="email" inputmode="email"></div>
          <div class="zf-field"><label for="zf-ph">Phone <span>*</span></label><input type="tel" id="zf-ph" name="Phone" maxlength="30" required autocomplete="tel" inputmode="tel"></div>
          <div class="zf-field zf-full"><label for="zf-loc">Preferred location</label><select id="zf-loc" name="LEADCF3">%(opts)s</select></div>
          <div class="zf-field zf-full"><label for="zf-msg">What are you interested in?</label><textarea id="zf-msg" name="Description" rows="4" placeholder="e.g. Botox for forehead lines, a weight-loss consult, Morpheus8 &hellip;"></textarea></div>
        </div>
        <p class="zf-fine">By submitting, you agree to be contacted by Serene Med Spa about your request. We never sell your information.</p>
        <div class="zf-actions"><button type="submit" class="btn zf-btn">Request Consultation</button><span class="zf-err" id="zf-err" role="alert"></span></div>
      </form>
      <div class="zf-done" id="zf-done" hidden>
        <div class="zf-done-icon">&#10003;</div>
        <h3>Thank you &mdash; we got your request.</h3>
        <p>A member of our team will reach out within one business day. Prefer not to wait? <a href="%(book)s" target="_blank" rel="noopener">Book online now</a> or call <a href="%(tel)s">%(phone)s</a>.</p>
      </div>
    </div>
  </div>
  <script>
  (function(){
    var f=document.getElementById('zf-consult'); if(!f) return;
    var src=document.getElementById('zf-src'); if(src) src.value='Website form: '+location.host+location.pathname;
    var err=document.getElementById('zf-err'), btn=f.querySelector('.zf-btn');
    f.addEventListener('submit',function(e){
      e.preventDefault(); err.textContent='';
      var bad=[].slice.call(f.querySelectorAll('[required]')).filter(function(i){return !i.value.trim();});
      var em=document.getElementById('zf-em');
      if(bad.length){bad[0].focus();err.textContent='Please fill in the required fields.';return;}
      if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]{2,}$/.test(em.value.trim())){em.focus();err.textContent='Please enter a valid email address.';return;}
      btn.disabled=true; btn.textContent='Sending\\u2026';
      var data=new FormData(f);
      fetch(f.action,{method:'POST',body:new URLSearchParams(data),mode:'no-cors',credentials:'omit'}).then(function(){
        f.hidden=true; var d=document.getElementById('zf-done'); d.hidden=false; d.scrollIntoView({behavior:'smooth',block:'center'});
        try{ if(window.gtag){ gtag('event','generate_lead',{event_category:'form',event_label:'consult'}); } }catch(x){}
      }).catch(function(){ f.submit(); });
    });
  })();
  </script>
</section>'''

CSS = '''/* --- Zoho consult form --- */
.consult-card .zf{font-family:'Jost',sans-serif}
.zf-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px 18px}
.zf-full{grid-column:1/-1}
.zf-field label{font-size:.85rem;color:var(--plum);font-weight:500;display:block;margin-bottom:6px}
.zf-field label span{color:#b0163f}
.zf-field input,.zf-field select,.zf-field textarea{width:100%;font:inherit;font-size:1rem;padding:12px 14px;border:1.5px solid rgba(0,0,0,.12);border-radius:12px;background:#fff;color:inherit;box-sizing:border-box;-webkit-appearance:none;appearance:none}
.zf-field select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%23555' stroke-width='1.6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:38px}
.zf-field textarea{min-height:110px;resize:vertical}
.zf-field input:focus,.zf-field select:focus,.zf-field textarea:focus{outline:none;border-color:var(--rose);box-shadow:0 0 0 3px rgba(201,79,116,.15)}
.zf-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;opacity:0}
.zf-fine{font-size:.78rem;color:var(--muted);margin:14px 0 0}
.zf-actions{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:16px}
.zf-btn{border:0;cursor:pointer;font:inherit}
.zf-btn:disabled{opacity:.7;cursor:default;transform:none}
.zf-err{color:#b0163f;font-size:.85rem}
.zf-done{text-align:center;padding:24px 8px}
.zf-done-icon{width:56px;height:56px;border-radius:50%;background:var(--rose);color:#fff;font-size:1.6rem;line-height:56px;margin:0 auto 14px}
.zf-done h3{margin:0 0 8px}
@media (max-width:640px){.zf-grid{grid-template-columns:1fr}}
'''

THANKYOU = r'''# -*- coding: utf-8 -*-
# build_thankyou.py — /thank-you/ : landing page after a consult-form submission (noindex).
import os
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, BOOK, STICKY_BAR
SITE="%(site)s"
PHONE_TEL=globals().get("PHONE_TEL","tel:+13304605915"); PHONE_DISPLAY=globals().get("PHONE_DISPLAY","(330) 460-5915")
HTML=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thank You | Serene Med Spa</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{SITE}/thank-you/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
</head>
<body>
{NAV}
<section class="tint-blush" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap">
    <div class="section-head reveal in"><div class="eyebrow">Request received</div><h2>Thank you &mdash; we got your request.</h2>
    <p>A member of our team will reach out within one business day to answer your questions and find a time that works for you. Prefer not to wait? <a href="{BOOK}" target="_blank" rel="noopener">Book online now</a> or call <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
    <p style="margin-top:22px"><a class="btn" href="/">Back to home</a></p></div>
  </div>
</section>
{FOOTER}
{SCRIPTS}
</body>
</html>"""
os.makedirs("bundle/site/thank-you",exist_ok=True)
open("bundle/site/thank-you/index.html","w",encoding="utf-8").write(HTML)
print("thank-you page written")
'''

def patch_common():
    s = open("common.py", encoding="utf-8").read()
    # find PHONE vars (BV has them; Hudson may not)
    has_phone = re.search(r"^PHONE_TEL\s*=", s, re.M) is not None
    m = re.search(r"CONSULT_SECTION = '''.*?'''(?:\s*%\s*\([^\n]*\))?", s, re.S)
    if not m:
        sys.exit("CONSULT_SECTION block not found in common.py")
    host = SITE_URL.split("//", 1)[1]
    new = "CONSULT_SECTION = '''" + FORM % dict(
        action=ZOHO_ACTION, xnq=XNQ, xmi=XMI, ret=RETURN_URL, host=host, opts=opts,
        book="%(book)s", tel="%(tel)s", phone="%(phone)s") + "'''"
    if has_phone:
        new += ' % dict(book=BOOK, tel=PHONE_TEL, phone=PHONE_DISPLAY.replace(" ","&nbsp;"))'
    else:
        new += ' % dict(book=BOOK, tel="tel:+13304605915", phone="(330)&nbsp;460-5915")'
    s = s[:m.start()] + new + s[m.end():]
    open("common.py", "w", encoding="utf-8").write(s)
    print("common.py: CONSULT_SECTION replaced (hubspot refs left:", s.count("hsforms"), ")")

def patch_css():
    p = "bundle/site/styles.css"
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"\.consult-card \.hs-[^\n]*\n?", "", s)
    s = re.sub(r"\.consult-card form\{[^}]*\}\n?", "", s)
    if "/* --- Zoho consult form --- */" in s:
        s = re.sub(r"/\* --- Zoho consult form --- \*/.*?(?=\n/\*|\Z)", CSS.rstrip("\n"), s, flags=re.S)
    else:
        s = s.rstrip("\n") + "\n" + CSS
    open(p, "w", encoding="utf-8").write(s)
    print("styles.css: zf styles in place; hs refs left:", s.count(".hs-"))

def add_thankyou():
    open("build_thankyou.py", "w", encoding="utf-8").write(THANKYOU % dict(site=SITE_URL))
    b = open("build.sh", encoding="utf-8").read()
    if "build_thankyou.py" not in b:
        b = b.replace("python3 build_sitemap.py", "python3 build_thankyou.py\npython3 build_sitemap.py", 1)
        open("build.sh", "w", encoding="utf-8").write(b)
    print("build_thankyou.py + build.sh hook in place")

patch_common(); patch_css(); add_thankyou()
