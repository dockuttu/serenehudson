# -*- coding: utf-8 -*-
# fitz_quiz.py — "What's my skin type?" Fitzpatrick quiz widget for laser pages.
# Self-contained (inline CSS + JS), nothing is stored or transmitted. Shared by Hudson & Barboursville.
# Usage in gen_pages.py:  exec(open("fitz_quiz.py").read())  then  quiz_html(slug, book_url)

QUIZ_SLUGS = {"laser-hair-removal", "laser-skin", "photofacial", "harmony-bio-boost", "laser-tattoo-removal",
              "laser-facial", "hyperpigmentation", "laser-nail-fungus"}

_Q = [
 # (group, question, [labels for score 0..4])
 ("Genetics", "What best describes your eye color?", ["Light blue / gray", "Green", "Blue", "Brown", "Dark brown"]),
 ("Genetics", "What is your natural hair color?", ["Red", "Blonde", "Chestnut / dark blonde", "Dark brown", "Black"]),
 ("Genetics", "What is the color of your skin in non-exposed areas?", ["White", "Very pale", "Pale with a beige tint", "Light brown", "Dark brown"]),
 ("Genetics", "Do you have freckles on unexposed areas?", ["Many", "Several", "Few", "Incidental", "None"]),
 ("Sun reaction", "What happens when you stay in the sun?", ["Painful redness, blistering, peeling", "Blistering followed by peeling", "Burns, sometimes followed by peeling", "Rare burns", "Never had burns"]),
 ("Sun reaction", "To what degree do you brown?", ["Hardly or not at all", "Light tan", "Reasonable tan", "Tan very easily", "Turn dark brown very quickly"]),
 ("Sun reaction", "Do you turn brown within several hours after sun exposure?", ["Never", "Seldom", "Sometimes", "Often", "Always"]),
 ("Sun reaction", "How does your face react to the sun?", ["Very sensitive", "Sensitive", "Normal", "Very resistant", "Never had a problem"]),
 ("Tanning habits", "When did you last expose your body to the sun or artificially tan?", ["More than 3 months ago", "2–3 months ago", "1–2 months ago", "Less than a month ago", "Less than 2 weeks ago"]),
 ("Tanning habits", "Did you expose the area to be treated to the sun?", ["Never", "Hardly ever", "Sometimes", "Often", "Always"]),
]

# Result copy per Fitzpatrick type. Keep claims general and accurate.
_RESULTS = {
 "I":   ("Type I &mdash; Very fair", "Always burns, never tans. Very light-sensitive skin.",
         "Excellent candidate for laser hair removal and light-based skin treatments (photofacial/IPL, resurfacing). We use conservative first-session settings and strict sun protection because your skin reacts strongly to light."),
 "II":  ("Type II &mdash; Fair", "Burns easily, tans minimally.",
         "Excellent candidate for laser hair removal and for photofacial, resurfacing and PICO treatments. Sun avoidance for two weeks before and after each session keeps results clean and predictable."),
 "III": ("Type III &mdash; Light to medium", "Sometimes burns, tans gradually.",
         "Great candidate for the full range of laser and light treatments. Your provider will tune energy settings to your skin and may recommend a test spot for resurfacing or IPL."),
 "IV":  ("Type IV &mdash; Olive / light brown", "Rarely burns, tans easily.",
         "Laser hair removal is safe and effective with the right device &mdash; our diode laser platform is designed for all skin types, including IV&ndash;VI. For skin concerns we lean on Morpheus8, RF microneedling, PICO and melanin-safe peels rather than IPL, which is not a good fit for your skin type."),
 "V":   ("Type V &mdash; Brown", "Very rarely burns, tans very easily.",
         "Laser hair removal is safe and effective on our diode laser platform, which is built to treat darker skin safely. For pigment, texture or tightening, we favor Morpheus8, RF microneedling, PICO and peels formulated for melanin-rich skin; IPL/photofacial is not recommended for your skin type."),
 "VI":  ("Type V&ndash;VI &mdash; Deep brown", "Never burns, deeply pigmented.",
         "Laser hair removal is safe and effective on our diode laser platform, which is built to treat darker skin safely. For pigment, texture or tightening, we favor Morpheus8, RF microneedling, PICO and peels formulated for melanin-rich skin; IPL/photofacial is not recommended for your skin type."),
}

def _type(score):
    if score <= 7: return "I"
    if score <= 16: return "II"
    if score <= 25: return "III"
    if score <= 30: return "IV"
    return "VI"

FITZ_CSS = """
<style>
.fitz{background:#fff;border:1px solid var(--blush-deep);border-radius:22px;padding:34px 30px;box-shadow:0 18px 40px -28px rgba(63,43,61,.35);max-width:860px;margin:0 auto}
.fitz .fz-group{margin:26px 0 8px;font-family:'Cormorant Garamond',serif;font-size:1.35rem;color:var(--plum);font-weight:600}
.fitz .fz-q{margin:14px 0 6px;font-weight:500;color:var(--plum)}
.fitz .fz-opts{display:flex;flex-wrap:wrap;gap:8px}
.fitz .fz-opts label{cursor:pointer;border:1.5px solid var(--blush-deep);border-radius:30px;padding:8px 14px;font-size:.88rem;color:#5a4a54;transition:.2s;background:var(--blush)}
.fitz .fz-opts label:hover{border-color:var(--rose)}
.fitz .fz-opts input{position:absolute;opacity:0;width:0;height:0}
.fitz .fz-opts input:checked+span{color:#fff}
.fitz .fz-opts label:has(input:checked){background:var(--grad);border-color:transparent;color:#fff}
.fitz .fz-actions{margin-top:28px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.fitz .fz-note{font-size:.8rem;color:var(--muted);margin-top:14px}
.fitz .fz-err{color:var(--rose-deep);font-size:.9rem;display:none;margin-top:10px}
.fitz .fz-result{display:none;margin-top:26px;padding:26px;border-radius:18px;background:var(--mint-soft);border:1px solid #cdeee7}
.fitz .fz-result h3{font-size:1.7rem;margin-bottom:4px}
.fitz .fz-result .fz-sub{color:var(--muted);margin-bottom:12px}
.fitz .fz-scale{display:flex;gap:4px;margin:14px 0 18px}
.fitz .fz-scale span{flex:1;height:12px;border-radius:6px;opacity:.35}
.fitz .fz-scale span.on{opacity:1;outline:2px solid var(--plum);outline-offset:2px}
@media(max-width:600px){.fitz{padding:24px 18px}}
</style>
"""

def _questions_html():
    out=[]; last=None
    for i,(g,q,labels) in enumerate(_Q):
        if g!=last:
            out.append('<div class="fz-group">%s</div>' % g); last=g
        out.append('<fieldset style="border:0"><div class="fz-q">%d. %s</div><div class="fz-opts">' % (i+1,q))
        for s,l in enumerate(labels):
            out.append('<label><input type="radio" name="fz%d" value="%d"><span>%s</span></label>' % (i,s,l))
        out.append('</div></fieldset>')
    return "\n".join(out)

def quiz_html(slug, book):
    import json
    res = {k:list(v) for k,v in _RESULTS.items()}
    cta = "Book Laser Hair Removal" if slug=="laser-hair-removal" else "Book a Consultation"
    return FITZ_CSS + '''
<section class="tint-blush" id="skin-type-quiz">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Am I a candidate?</div><h2>What&rsquo;s My Skin Type?</h2>
      <p style="max-width:640px;margin:0 auto">Laser settings are chosen by Fitzpatrick skin type. Answer ten quick questions to see yours and which treatments suit you. Nothing is saved or sent &mdash; it stays on your screen.</p></div>
    <form class="fitz reveal" id="fzform" onsubmit="return false">
%s
      <div class="fz-err" id="fzerr">Please answer every question to see your result.</div>
      <div class="fz-actions"><button class="btn" type="button" id="fzgo">See My Skin Type</button><button class="btn btn-outline" type="button" id="fzreset">Start Over</button></div>
      <div class="fz-result" id="fzres">
        <div class="eyebrow">Your result</div>
        <h3 id="fzt"></h3><div class="fz-sub" id="fzs"></div>
        <div class="fz-scale" id="fzscale"><span style="background:#fde8dc"></span><span style="background:#f5d2b8"></span><span style="background:#d9a877"></span><span style="background:#b07a4a"></span><span style="background:#7a4f2e"></span><span style="background:#4a2f1d"></span></div>
        <p id="fzp"></p>
        <div class="fz-actions"><a class="btn" href="%s" target="_blank" rel="noopener">%s</a></div>
      </div>
      <div class="fz-note">Based on the standard Fitzpatrick questionnaire. For guidance only &mdash; your provider confirms your skin type and settings in person.</div>
    </form>
  </div>
</section>
<script>
(function(){
var R=%s, N=%d;
var go=document.getElementById('fzgo'), rs=document.getElementById('fzreset'), err=document.getElementById('fzerr'), res=document.getElementById('fzres');
go.addEventListener('click',function(){
  var sum=0, ok=true;
  for(var i=0;i<N;i++){var c=document.querySelector('input[name=fz'+i+']:checked'); if(!c){ok=false;break;} sum+=parseInt(c.value,10);}
  if(!ok){err.style.display='block';res.style.display='none';return;}
  err.style.display='none';
  var t = sum<=7?'I': sum<=16?'II': sum<=25?'III': sum<=30?'IV':'VI';
  var idx = {'I':0,'II':1,'III':2,'IV':3,'V':4,'VI':5}[t];
  document.getElementById('fzt').innerHTML=R[t][0]; document.getElementById('fzs').innerHTML=R[t][1]; document.getElementById('fzp').innerHTML=R[t][2];
  var sp=document.querySelectorAll('#fzscale span'); for(var j=0;j<sp.length;j++){sp[j].className=(j===idx||(t==='VI'&&j===4))?'on':'';}
  res.style.display='block'; res.scrollIntoView({behavior:'smooth',block:'nearest'});
});
rs.addEventListener('click',function(){document.getElementById('fzform').reset();res.style.display='none';err.style.display='none';});
})();
</script>
''' % (_questions_html(), book, cta, json.dumps(res, ensure_ascii=False), len(_Q))

def quiz_for(slug, book):
    return quiz_html(slug, book) if slug in QUIZ_SLUGS else ""
