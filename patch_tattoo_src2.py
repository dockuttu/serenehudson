# re-run safe: switch size comparisons to everyday objects (quarter / passport photo / credit card / dollar bill)
R = {
 "build_pricing.py": [
  ("Micro &mdash; under 1 sq in (fingernail)", "Micro &mdash; under 1 sq in (fits under a quarter)"),
  ("Small &mdash; 1&ndash;4 sq in (postage stamp to business card)", "Small &mdash; 1&ndash;4 sq in (up to a 2&times;2&Prime; passport photo)"),
  ("Medium &mdash; 5&ndash;9 sq in (Post-it note to palm)", "Medium &mdash; 5&ndash;9 sq in (credit card up to a 3&times;3&Prime; Post-it)"),
  ("Large &mdash; 10&ndash;16 sq in (iPhone size)", "Large &mdash; 10&ndash;16 sq in (up to a dollar bill)"),
  ("Over 16 sq in (sleeves, back pieces)", "Bigger than a dollar bill (sleeves, back pieces)"),
 ],
 "pages_data_new2.py": [
  ("Micro is under 1 square inch (about a fingernail). Small is 1&ndash;4 sq in (a postage stamp to a business card). Medium is 5&ndash;9 sq in (a Post-it note to the palm of your hand). Large is 10&ndash;16 sq in (about the size of an iPhone).",
   "Micro is under 1 square inch &mdash; it fits under a quarter. Small is 1&ndash;4 sq in &mdash; up to a 2&times;2 inch passport photo. Medium is 5&ndash;9 sq in &mdash; about a credit card or business card, up to a 3&times;3 inch Post-it note. Large is 10&ndash;16 sq in &mdash; up to the size of a dollar bill. Anything bigger than a dollar bill is quoted at your free consultation."),
  ("Tattoos larger than 16 sq in, such as sleeves and back pieces, are quoted at your free consultation.",
   "Tattoos bigger than a dollar bill (over 16 sq in), such as sleeves and back pieces, are quoted at your free consultation."),
 ],
}
for fn, pairs in R.items():
    s = open(fn, encoding="utf-8").read(); o = s
    for a, b in pairs:
        s = s.replace(a, b)
    if s != o:
        open(fn, "w", encoding="utf-8").write(s)
    print(fn, "updated" if s != o else "unchanged")
