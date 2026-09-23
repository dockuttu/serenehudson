# footer_telehealth.py -- add the Serene telehealth (Spruce) lines to the footer of any page
# that does not already have them (hand-built static pages bypass common.FOOTER).
# Usage: python3 footer_telehealth.py bundle/site
import os, sys

root = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
ANCHOR = 'Visit our WV location &rsaquo;</a></li>'
ADD = ('\n<li style="margin-top:10px;font-weight:600">Telehealth with Dr. Arora</li>'
       '\n<li><a href="tel:+13307752452">(330) 775-2452</a></li>'
       '\n<li><a href="sms:+13307752452">Text us: (330) 775-2452</a></li>'
       '\n<li><a href="https://spruce.care/serene-telehealth" target="_blank" rel="noopener">Message Dr. Arora securely &rsaquo;</a></li>')
n = 0
for d, _, files in os.walk(root):
    if "index.html" not in files:
        continue
    p = os.path.join(d, "index.html")
    s = open(p, encoding="utf-8").read()
    if "serene-telehealth" in s or ANCHOR not in s:
        continue
    open(p, "w", encoding="utf-8").write(s.replace(ANCHOR, ANCHOR + ADD, 1))
    n += 1
print(f"footer_telehealth: added to {n} page(s)")
