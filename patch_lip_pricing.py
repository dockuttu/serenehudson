# re-run safe: split lip filler into full / half syringe rows on the pricing page (both repos)
fn = "build_pricing.py"
s = open(fn, encoding="utf-8").read(); o = s
s = s.replace('row("Lip Filler","$500","/syringe")+row("Mini Pout","$300")+',
  'row("Lip Filler &mdash; Full Syringe (1 mL)","$500")+row("Lip Filler &mdash; Half Syringe (0.5 mL, Mini Pout)","$300")+'
  '\'<div class="price-row" style="border:0"><span class="price-name" style="font-size:.85rem;color:var(--ink)">Lip filler uses Juv&eacute;derm Volbella XC or Ultra XC &mdash; <a href="https://blog.serenemedspas.com/full-syringe-lip-filler-cost-barboursville-wv/" style="text-decoration:underline">which is right for you?</a></span></div>\'+')
s = s.replace('("Lip Filler",500),', '("Lip Filler - Full Syringe (1 mL)",500),("Lip Filler - Half Syringe (0.5 mL)",300),')
if s != o:
    open(fn, "w", encoding="utf-8").write(s)
print(fn, "updated" if s != o else "unchanged")
