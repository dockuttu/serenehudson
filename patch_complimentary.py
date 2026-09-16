# re-run safe: "free consultation" -> "complimentary, no-commitment consultation" in the tattoo / lip filler content
import os
R = {
 "tattoo_pricing.py": [
  ("or just come in: <b>your consultation is always free</b>, and we&rsquo;ll confirm", "or just come in: <b>your consultation is complimentary, with no commitment</b>, and we&rsquo;ll confirm"),
  ("are priced individually at your free consultation.", "are priced individually at your complimentary, no-commitment consultation."),
  (">Book a Free Consultation</a><a class=\"btn btn-outline\" href=\"/pricing/#cat-laser-skin\">", ">Book a Complimentary Consultation</a><a class=\"btn btn-outline\" href=\"/pricing/#cat-laser-skin\">"),
  ('"name": "Laser Tattoo Removal Consultation", "price": "0"', '"name": "Laser Tattoo Removal Consultation (complimentary, no commitment)", "price": "0"'),
 ],
 "build_pricing.py": [
  ('<td colspan="2">Quoted at your free consultation</td>', '<td colspan="2">Quoted at your complimentary, no-commitment consultation</td>'),
  ('<tr><td>Tattoo Removal Consultation</td><td colspan="2"><span class="price-free">Free</span></td></tr>', '<tr><td>Tattoo Removal Consultation (no commitment)</td><td colspan="2"><span class="price-free">Complimentary</span></td></tr>'),
 ],
 "pages_data_new2.py": [
  ("from $125 per session. Free consultations, and buy 5 sessions, get the 6th free.", "from $125/session. Complimentary, no-commitment consults; buy 5 sessions, get the 6th free."),
  ('("Free Consultation","Every tattoo removal consultation is free &mdash; no need to wait to get a price."),', '("Complimentary Consultation","Every tattoo removal consultation is complimentary with no commitment &mdash; no need to wait to get a price."),'),
  ("are quoted at your free consultation.", "are quoted at your complimentary, no-commitment consultation."),
  ("is quoted at your free consultation.", "is quoted at your complimentary, no-commitment consultation."),
  ('("Is the tattoo removal consultation free?","Yes. Consultations are always free, so you don&rsquo;t have to wait',
   '("Is the tattoo removal consultation free?","Yes. Consultations are always complimentary with no commitment, so you don&rsquo;t have to wait'),
 ],
 "posts/2026-09-16_half-syringe-lip-filler-cost.py": [],
 "posts/2026-09-16_full-syringe-lip-filler-cost.py": [],
}
BLOG = [
  ("<li><strong>Consultation:</strong> always free</li>", "<li><strong>Consultation:</strong> always complimentary, with no commitment</li>"),
  ("<p>Consultations are free, and paying over time", "<p>Every consultation is complimentary with no commitment, and paying over time"),
  ("<h2>Book a free lip filler consultation</h2>", "<h2>Book a complimentary, no-commitment lip filler consultation</h2>"),
  ("<li><strong>Consultation:</strong> We look at your lip shape", "<li><strong>Complimentary consultation (no commitment):</strong> We look at your lip shape"),
  ("*   Lip filler consultations are free.", "*   Lip filler consultations are complimentary, with no commitment."),
]
for fn, pairs in R.items():
    if not os.path.exists(fn): continue
    if fn.startswith("posts/"): pairs = BLOG
    s = open(fn, encoding="utf-8").read(); o = s
    for a, b in pairs: s = s.replace(a, b)
    if s != o: open(fn, "w", encoding="utf-8").write(s)
    print(fn, "updated" if s != o else "unchanged")
