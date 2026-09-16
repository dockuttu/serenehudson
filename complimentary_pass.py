# -*- coding: utf-8 -*-
# complimentary_pass.py — idempotent post-build pass (identical in all Serene repos):
# site copy says "complimentary, no-commitment consultation" instead of "free consultation".
# Only touches visible wording (space-separated phrases), never URLs or hyphenated slugs.
import glob, os, re, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
EXACT = [
 ("Book a Free Consultation", "Book a Complimentary Consultation"),
 ("Book a free consultation", "Book a complimentary, no-commitment consultation"),
 ("start with a free consultation", "start with a complimentary, no-commitment consultation"),
 ("Pick a free consultation", "Pick a complimentary consultation"),
 ("Choose a free consultation", "Choose a complimentary consultation"),
 ("choose a free consultation", "choose a complimentary consultation"),
 ("Free consultations", "Complimentary, no-commitment consultations"),
 ("Free consults.", "Complimentary consults."),
 ("consultation is free.", "consultation is complimentary, with no commitment."),
 ("Consultations are free.", "Consultations are complimentary, with no commitment."),
 ("Consultations are free, and", "Consultations are complimentary with no commitment, and"),
 ("Consultations are free and", "Consultations are complimentary, with no commitment, and"),
 ("Free Consultation <b>+ 20% Off</b>", "Complimentary Consultation <b>+ 20% Off</b>"),
]
FALLBACK = [
 (re.compile(r'(?<![-\w/])Free Consultation(?![-\w])'), "Complimentary Consultation"),
 (re.compile(r'(?<![-\w/])free consultation(?![-\w])'), "complimentary, no-commitment consultation"),
 (re.compile(r'(?<![-\w/])Free consultation(?![-\w])'), "Complimentary, no-commitment consultation"),
]
files = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True) + glob.glob(os.path.join(SITE, "*.js"))
n = 0
for f in files:
    s = open(f, encoding="utf-8").read(); o = s
    for a, b in EXACT:
        s = s.replace(a, b)
    for rx, b in FALLBACK:
        s = rx.sub(b, s)
    if s != o:
        open(f, "w", encoding="utf-8").write(s); n += 1
print("complimentary_pass: updated", n, "file(s)")
