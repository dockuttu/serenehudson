# form_guard_inject.py — idempotent: load /form-guard.js (spam screening for the Zoho lead forms)
# on every built page, and keep the popup's lead-source tag in the exact format Zoho's
# Lead Source rule expects ("Website popup: <host>", no page path).
import glob, os, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
TAG = '<script src="/form-guard.js" defer></script>'
n = 0
for p in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True):
    s = open(p, encoding="utf-8", errors="ignore").read()
    if "form-guard.js" in s or "</body>" not in s:
        continue
    s = s.replace("</body>", TAG + "\n</body>", 1)
    open(p, "w", encoding="utf-8").write(s); n += 1
pj = os.path.join(BASE, "popup.js")
if os.path.exists(pj):
    s = open(pj, encoding="utf-8").read()
    t = s.replace("Website popup: ' + location.host + location.pathname + '", "Website popup: ' + location.host + '")
    if t != s:
        open(pj, "w", encoding="utf-8").write(t); print("form_guard_inject: popup lead-source tag restored")
print("form_guard_inject: script added to", n, "page(s)")
