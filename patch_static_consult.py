#!/usr/bin/env python3
"""patch_static_consult.py — build step: make sure NO page in bundle/site still carries the HubSpot form.

 1. Every bundle/site/**/index.html that still contains the HubSpot embed gets its
    <section class="consult" ...>...</section> replaced with CONSULT_SECTION from common.py
    (covers hand-built pages that gen_pages doesn't regenerate).
 2. bundle/site/popup.js — the New-Client offer popup: swap the HubSpot embed for a compact
    Zoho web-to-lead form (same Zoho form as the consult section; source tagged "Website popup").
Idempotent; run from the repo root after the page builders (build.sh does this).
"""
import os, re, sys
exec(open("common.py").read())   # CONSULT_SECTION, BOOK

ROOT = "bundle/site"
HS = ("hs-form-frame", "hsforms.net")

# ---------- 1. hand-built pages ----------
n = 0
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f != "index.html": continue
        p = os.path.join(dp, f)
        s = open(p, encoding="utf-8").read()
        if not any(h in s for h in HS): continue
        i = s.find('<section class="consult"')
        j = s.find("</section>", i)
        if i < 0 or j < 0:
            print("  !! hubspot ref but no consult section:", p); continue
        s = s[:i] + CONSULT_SECTION + s[j + len("</section>"):]
        # stray HubSpot loader outside the section
        s = re.sub(r'\s*<script src="https://js-na2\.hsforms\.net/forms/embed/\d+\.js" defer></script>', "", s)
        open(p, "w", encoding="utf-8").write(s); n += 1
print("patch_static_consult: %d hand-built page(s) switched to the Zoho form" % n)

# ---------- 2. popup.js ----------
P = os.path.join(ROOT, "popup.js")
if os.path.exists(P):
    js = open(P, encoding="utf-8").read()
    if "hsforms" in js:
        # pull the Zoho hidden-field values straight out of CONSULT_SECTION so they stay in sync
        def val(name):
            m = re.search(r'name="%s" value="([^"]*)"' % re.escape(name), CONSULT_SECTION); return m.group(1)
        xnq, xmi, ret = val("xnQsjsdp"), val("xmIwtLD"), val("returnURL")
        js = js.replace('hs: { region: "na2", portal: "242695075", form: "16625e0e-6a46-4664-98c6-2cbf264da060" },',
                        'zoho: { action: "https://crm.zoho.com/crm/WebToLeadForm", xnq: "%s", xmi: "%s", ret: "%s" },' % (xnq, xmi, ret))
        js = js.replace("Captures leads into the existing HubSpot form", "Captures leads into the Zoho CRM web-to-lead form")
        # loader -> no-op
        js = re.sub(r'  function loadHubSpot\(\) \{.*?\n  \}\n', '  function loadHubSpot() {}\n', js, flags=re.S)
        # embed -> compact native form
        form = (
            '<form class="np-zf" novalidate>' +
            '<input type="hidden" name="xnQsjsdp" value="\' + CFG.zoho.xnq + \'">' +
            '<input type="hidden" name="xmIwtLD" value="\' + CFG.zoho.xmi + \'">' +
            '<input type="hidden" name="actionType" value="TGVhZHM=">' +
            '<input type="hidden" name="returnURL" value="\' + CFG.zoho.ret + \'">' +
            '<input type="hidden" name="Lead Status" value="Not Contacted">' +
            '<input type="hidden" name="LEADCF1" value="Website popup: \' + location.host + \'">' +
            '<input type="hidden" name="LEADCF3" value="\' + (CFG.location || "") + \'">' +
            '<input type="hidden" name="Description" value="New Client Special popup (free consult + 20% off first treatment)">' +
            '<input type="text" name="aG9uZXlwb3Q" value="" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">' +
            '<div class="np-row"><input class="np-in" name="First Name" placeholder="First name" autocomplete="given-name"><input class="np-in" name="Last Name" placeholder="Last name" autocomplete="family-name" required></div>' +
            '<input class="np-in" type="email" name="Email" placeholder="Email" autocomplete="email" required>' +
            '<input class="np-in" type="tel" name="Phone" placeholder="Mobile number" autocomplete="tel" required>' +
            '<button type="submit" class="np-btn np-send">Send My Offer &rsaquo;</button>' +
            '<div class="np-err" role="alert"></div>' +
            '</form>'
        )
        js, k = re.subn(r"'<div class=\"np-form\"><div class=\"hs-form-frame\".*?</div></div>' \+",
                        lambda m: "'<div class=\"np-form\">" + form + "</div>' +", js, flags=re.S)
        if k != 1: sys.exit("popup.js: hs-form-frame block not found (%d)" % k)
        locm = re.search(r'<option value="([^"]+)" selected>', CONSULT_SECTION)
        js = js.replace('    image: "/img/lobby.jpg",', '    location: "%s",\n    image: "/img/lobby.jpg",' % (locm.group(1) if locm else ""))
        # styles for the inputs
        js = js.replace('".np-form{min-height:60px;margin:6px 0 4px;text-align:left}",',
            '".np-form{min-height:60px;margin:6px 0 4px;text-align:left}",\n'
            '      ".np-row{display:flex;gap:8px}",\n'
            '      ".np-in{width:100%;box-sizing:border-box;font-family:\'Jost\',sans-serif;font-size:.98rem;padding:12px 14px;margin:0 0 8px;border:1.5px solid rgba(63,43,61,.18);border-radius:12px;background:#fff;color:#3f2b3d}",\n'
            '      ".np-in:focus{outline:none;border-color:#c94f74;box-shadow:0 0 0 3px rgba(201,79,116,.15)}",\n'
            '      ".np-err{color:#b0163f;font-size:.8rem;min-height:1em;margin-top:6px}",\n'
            '      ".np-ok{background:#fff;border-radius:14px;padding:16px;text-align:center;color:#3f2b3d;font-weight:500}",')
        # submit handler, right after the close-button handler
        handler = '''    var zf = ov.querySelector(".np-zf");
    if (zf) zf.addEventListener("submit", function (e) {
      e.preventDefault();
      var err = zf.querySelector(".np-err"); err.textContent = "";
      var need = [].slice.call(zf.querySelectorAll("[required]")).filter(function (i) { return !i.value.trim(); });
      if (need.length) { need[0].focus(); err.textContent = "Please fill in name, email and mobile."; return; }
      var em = zf.querySelector("[name=Email]");
      if (!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]{2,}$/.test(em.value.trim())) { em.focus(); err.textContent = "Please enter a valid email."; return; }
      var b = zf.querySelector(".np-send"); b.disabled = true; b.textContent = "Sending\\u2026";
      fetch(CFG.zoho.action, { method: "POST", body: new URLSearchParams(new FormData(zf)), mode: "no-cors", credentials: "omit" })
        .then(function () {
          zf.outerHTML = '<div class="np-ok">&#10003; Your offer is on its way &mdash; check your email. Book below to lock in your spot.</div>';
          try { if (window.gtag) gtag("event", "generate_lead", { event_category: "form", event_label: "popup" }); } catch (x) {}
        })
        .catch(function () { b.disabled = false; b.textContent = "Send My Offer \\u203a"; err.textContent = "Something went wrong \\u2014 please call us."; });
    });
'''
        js = js.replace('    ov.querySelector(".np-x").addEventListener("click", function () { close(ov); });\n',
                        '    ov.querySelector(".np-x").addEventListener("click", function () { close(ov); });\n' + handler)
        open(P, "w", encoding="utf-8").write(js)
        print("patch_static_consult: popup.js switched to the Zoho form (hs refs left: %d)" % js.count("hsforms"))
    else:
        print("patch_static_consult: popup.js already on Zoho")
