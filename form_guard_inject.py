# form_guard_inject.py — idempotent: load /form-guard.js (spam screening for the Zoho lead forms)
# on every built page, and keep the popup's lead-source tag in the exact format Zoho's
# Lead Source rule expects ("Website popup: <host>", no page path).
import glob, os, re, sys, hashlib
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
V = hashlib.sha256(open(os.path.join(BASE, "form-guard.js"), "rb").read()).hexdigest()[:8]
TAG = '<script src="/form-guard.js?v=%s" defer></script>' % V
n = 0
for p in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True):
    s = open(p, encoding="utf-8", errors="ignore").read()
    if "</body>" not in s:
        continue
    if "form-guard.js" in s:
        t2 = re.sub(r'<script src="/form-guard\.js(\?v=[0-9a-f]+)?" defer></script>', TAG, s)
    else:
        t2 = s.replace("</body>", TAG + "\n</body>", 1)
    if t2 != s:
        open(p, "w", encoding="utf-8").write(t2); n += 1
pj = os.path.join(BASE, "popup.js")
if os.path.exists(pj):
    s = open(pj, encoding="utf-8").read()
    t = s.replace("Website popup: ' + location.host + location.pathname + '", "Website popup: ' + location.host + '")
    if t != s:
        open(pj, "w", encoding="utf-8").write(t); print("form_guard_inject: popup lead-source tag restored")
print("form_guard_inject: script added to", n, "page(s)")
