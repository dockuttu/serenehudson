# one-time source patch (safe to re-run): pricing page table + tattoo page copy/FAQs
import re, sys
# ---- build_pricing.py
p = open("build_pricing.py", encoding="utf-8").read()
if "TATTOO_PRICING" not in p:
    TT = r'''# TATTOO_PRICING — per-session by size; 6-pack = buy 5, 6th free (same tattoo)
TATTOO_HTML = ('<div class="sub">Laser Tattoo Removal (PICO) &mdash; per session / 6-session package (buy 5, 6th free, same tattoo)</div>'+
  """<table class="lhr-table"><thead><tr><th>Tattoo size</th><th>Per session</th><th>Package of 6</th></tr></thead><tbody>
  <tr><td>Micro &mdash; under 1 sq in (fingernail)</td><td>$125</td><td>$625</td></tr>
  <tr><td>Small &mdash; 1&ndash;4 sq in (postage stamp to business card)</td><td>$150</td><td>$750</td></tr>
  <tr><td>Medium &mdash; 5&ndash;9 sq in (Post-it note to palm)</td><td>$250</td><td>$1,250</td></tr>
  <tr><td>Large &mdash; 10&ndash;16 sq in (iPhone size)</td><td>$400</td><td>$2,000</td></tr>
  <tr><td>Over 16 sq in (sleeves, back pieces)</td><td colspan="2">Quoted at your free consultation</td></tr>
  <tr><td>Tattoo Removal Consultation</td><td colspan="2"><span class="price-free">Free</span></td></tr>
  </tbody></table>""")

'''
    i = p.find('CATS.append(("Laser &amp; Skin"')
    assert i != -1
    p = p[:i] + TT + p[i:]
    j = p.find("</tbody></table>'''))", i + len(TT))
    assert j != -1
    p = p[:j] + "</tbody></table>'''+TATTOO_HTML))" + p[j + len("</tbody></table>'''))"):]
    p = re.sub(r'\("Laser Hair Removal",(\d+)\),', r'("Laser Hair Removal",\1),("Laser Tattoo Removal",125),', p, count=1)
    open("build_pricing.py", "w", encoding="utf-8").write(p)
    print("build_pricing.py patched")
# ---- pages_data_new2.py
d = open("pages_data_new2.py", encoding="utf-8").read()
if "Is the tattoo removal consultation free?" not in d:
    a = d.find('"slug":"laser-tattoo-removal"'); b = d.find('# =====', a)
    blk = d[a:b]; nb = blk
    nb = re.sub(r'"desc":"[^"]*"', '"desc":"PICO laser tattoo removal in Hudson, OH from $125 per session. Free consultations, and buy 5 sessions, get the 6th free. Book at Serene Med Spa."', nb, count=1)
    nb = nb.replace('("All Sizes","From tiny script to larger pieces — priced by size."),',
                    '("Priced by Size","Per session from $125 (micro) to $400 (large). Buy 5 sessions, get the 6th free."),')
    nb = nb.replace('("Physician-Led Care","Treatment overseen by our board-certified physicians."),',
                    '("Free Consultation","Every tattoo removal consultation is free &mdash; no need to wait to get a price."),')
    NEW = '''   ("How much does laser tattoo removal cost?","Pricing is per session and based on tattoo size: Micro (under 1 sq in) $125, Small (1&ndash;4 sq in) $150, Medium (5&ndash;9 sq in) $250, and Large (10&ndash;16 sq in) $400. Tattoos larger than 16 sq in, such as sleeves and back pieces, are quoted at your free consultation."),
   ("How do you define micro, small, medium and large tattoos?","We measure the rectangle that fits around the whole design. Micro is under 1 square inch (about a fingernail). Small is 1&ndash;4 sq in (a postage stamp to a business card). Medium is 5&ndash;9 sq in (a Post-it note to the palm of your hand). Large is 10&ndash;16 sq in (about the size of an iPhone)."),
   ("Is the tattoo removal consultation free?","Yes. Consultations are always free, so you don&rsquo;t have to wait to find out your tattoo&rsquo;s size, price, and estimated number of sessions."),
   ("Do you offer tattoo removal packages?","Yes. Buy 5 sessions and get the 6th session free for the same tattoo: Micro $625, Small $750, Medium $1,250, or Large $2,000 for 6 sessions."),
'''
    k = nb.find(' "faqs":[\n') + len(' "faqs":[\n')
    nb = nb[:k] + NEW + nb[k:]
    assert nb != blk
    d = d[:a] + nb + d[b:]
    open("pages_data_new2.py", "w", encoding="utf-8").write(d)
    print("pages_data_new2.py patched")
# ---- build.sh
sh = open("build.sh", encoding="utf-8").read()
if "tattoo_pricing.py" not in sh:
    sh = sh.replace("python3 home_obagi.py bundle/site", "python3 tattoo_pricing.py bundle/site   # tattoo size guide + prices + 5+1 offer on /laser-tattoo-removal/\npython3 home_obagi.py bundle/site", 1)
    open("build.sh", "w", encoding="utf-8").write(sh)
    print("build.sh patched")
