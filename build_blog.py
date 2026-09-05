# -*- coding: utf-8 -*-
import os, json, html as _html
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://hudson.serenemedspas.com"

# ---------- posts registry ----------
POSTS = [{
  "slug":"male-lip-filler-juvederm-volbella",
  "title":"Male Lip Filler with Juv&eacute;derm Volbella",
  "h1":"Male Lip Filler Done Right: Natural Volume with Juv&eacute;derm Volbella",
  "desc":"How Dr. Robin Arora used Juv&eacute;derm Volbella for a natural male lip filler result — adding volume, correcting asymmetry, and softening the Cupid's bow.",
  "date":"2026-08-21","date_h":"August 21, 2026",
  "cat":"Lip Filler","cat_link":"/lip-filler/",
  "img":"/img/ba-lip-volbella.jpg",
  "excerpt":"Lip filler is uncommon for men &mdash; and done well, rarer still. Here&rsquo;s how I added natural volume, corrected side-to-side asymmetry, and kept a masculine lip using Juv&eacute;derm Volbella.",
  "body":'''
<p>Lip filler is still uncommon for men &mdash; and lip filler done <em>well</em> on a male patient is rarer still. So when this client came to me, I was glad he was clear about his goal: he wanted to <strong>add volume without losing definition</strong>, and keep the result unmistakably masculine. Here&rsquo;s how I approached it, and why Juv&eacute;derm Volbella was the right product for the job.</p>

<h2>Reading the lips first</h2>
<p>Before I touch a syringe, I study the lips. In this case a few things stood out:</p>
<ul>
  <li>The <strong>upper right lip was smaller</strong> than the upper left &mdash; a natural asymmetry most people never notice until you&rsquo;re looking closely.</li>
  <li>The <strong>Cupid&rsquo;s bow was more prominent</strong> than he wanted. A softer, flatter Cupid&rsquo;s bow reads as more masculine, so that became part of the plan.</li>
  <li>The <strong>lower lip</strong> needed a rounder, fuller center to balance the whole mouth.</li>
</ul>
<p>Good lip work is really a symmetry problem. I think about the lips in <strong>four quadrants</strong> &mdash; upper left, upper right, lower left, lower right &mdash; and dose each one independently so the finished result is balanced rather than simply bigger.</p>

<h2>The technique: 70/30, and correcting side to side</h2>
<p>For most lips, I place roughly <strong>70% of the filler in the upper lip and 30% in the lower</strong> &mdash; that ratio keeps the proportions natural. But the ratio is only the starting point. Because his upper right was smaller, I placed <strong>more product on the right than the left</strong> to bring the two sides into balance, softened the Cupid&rsquo;s bow as we&rsquo;d discussed, and built up the <strong>center of the lower lip</strong> to give it that rounder shape.</p>
<p>The result: more volume, better symmetry across all four quadrants, a softer Cupid&rsquo;s bow &mdash; and lips that still look like <em>his</em> lips, just refined.</p>

<h2>Why Juv&eacute;derm Volbella for a male lip</h2>
<p>I reached for <strong>Juv&eacute;derm Volbella</strong> here for a reason. It&rsquo;s designed to add volume and smooth the lip while preserving the natural shape and movement &mdash; it doesn&rsquo;t overfill or give that &ldquo;done&rdquo; look, which is exactly what a male patient (and most patients) want. It&rsquo;s also part of the Juv&eacute;derm family known for its <strong>longevity</strong>, so results tend to last well &mdash; often a year or more &mdash; which means fewer touch-ups over time.</p>

<h2>What&rsquo;s next for this patient</h2>
<p>I asked him to <strong>come back in a week</strong> so we can take proper &ldquo;after&rdquo; photos once any initial swelling has settled &mdash; that&rsquo;s when you see the true result. He&rsquo;s also returning next week for <strong>cheek filler</strong>, so stay tuned for that case in an upcoming post.</p>

<h2>Ready for a natural result?</h2>
<p>Male or female, the principles are the same: study the anatomy, respect the natural shape, and dose for balance. If you&rsquo;ve been considering <a href="/lip-filler/">lip filler</a> and want a result that looks like a better version of you &mdash; not someone else &mdash; I&rsquo;d love to help. See our <a href="/pricing/">pricing</a> or browse more results in the <a href="/before-after/">before &amp; after gallery</a>.</p>
<p>You can book with me at Serene Med Spa in <strong>Hudson, Ohio</strong> or <strong>Barboursville, West Virginia</strong>.</p>
''',
  "author_bio":"Dr. Robin Arora, MD is board-certified in aesthetic medicine by the American Academy of Aesthetic Medicine (AAAM). He completed an internal medicine residency through an NYU-affiliated program in the Bronx and a nephrology fellowship at Tulane University."
},{
  "slug":"iv-therapy-immune-support-fall",
  "title":"IV Therapy for Immune Support in Hudson &amp; Barboursville",
  "seo_title":"IV Therapy for Immune Support | Serene Med Spa, Hudson OH",
  "h1":"Getting Ahead of the Season: How IV Therapy Supports Your Wellness",
  "desc":"Physician-led IV drips at Serene Med Spa &mdash; Immune Armor, Myer&rsquo;s Cocktail, Glutathione &amp; more, all $149, in Hudson, OH &amp; Barboursville, WV.",
  "date":"2026-08-24","date_h":"August 24, 2026",
  "cat":"IV Therapy","cat_link":"/iv-therapy/",
  "img":"/img/iv-therapy-blog.jpg",
  "img_alt":"A physician-supervised team member preparing a custom IV vitamin drip at Serene Med Spa",
  "excerpt":"You can&rsquo;t control the season &mdash; but you can give your body better support heading into it. Here&rsquo;s how our $149 physician-led IV drips help you replenish, rehydrate, and support your immune health.",
  "body":'''
<p>Every year it&rsquo;s the same story: the calendar fills up, the weather turns, and everyone around you seems to be coming down with something. You can&rsquo;t control the season &mdash; but you <em>can</em> give your body better support heading into it. That&rsquo;s where IV therapy comes in.</p>

<h2>Why IV?</h2>
<p>When you take a vitamin by mouth, only a fraction is actually absorbed. Delivering nutrients directly through an IV drip bypasses the digestive system, so your body gets more of what it&rsquo;s receiving. For busy people who want a simple, efficient wellness step, that&rsquo;s the appeal.</p>

<figure class="post-fig">
  <img loading="lazy" src="/img/iv-therapy-supplies.jpg" alt="Sterile, single-use IV supplies prepared on a tray before a drip at Serene Med Spa" width="900" height="1200">
  <figcaption>Every drip is prepared with fresh, single-use sterile supplies in our physician-supervised IV bar.</figcaption>
</figure>

<h2>Our drips for seasonal support</h2>
<p>Every Serene infusion is <strong>$149</strong> and <strong>personalized by our physician-led team</strong> &mdash; we look at how you&rsquo;re feeling and what your body needs, rather than a one-size-fits-all approach. A few that patients reach for as the season shifts:</p>
<ul>
  <li><strong>Immune Armor</strong> &mdash; our drip formulated to support your immune system and overall wellness, combining hydration with key vitamins and antioxidants.</li>
  <li><strong>Myer&rsquo;s Cocktail</strong> &mdash; a time-tested blend of B vitamins, vitamin C, magnesium, and calcium, popular for general wellness and an energy lift.</li>
  <li><strong>Beauty Glow (Glutathione)</strong> &mdash; often called the body&rsquo;s &ldquo;master antioxidant,&rdquo; glutathione supports cellular health and gives skin a healthy glow.</li>
  <li><strong>Recovery &amp; Performance Pro</strong> &mdash; for when you&rsquo;re already feeling depleted after travel, a tough week, or a hard workout, and want to bounce back.</li>
  <li><strong>Quench+</strong> &mdash; deep hydration when you&rsquo;re running on empty.</li>
</ul>
<p>Prefer something targeted? We also offer <strong>Reboot Relief, Brain Boost, PMS Ease,</strong> and <strong>Get-Up-&amp;-Go</strong> &mdash; so we can match the drip to how you&rsquo;re actually feeling that day.</p>

<p class="post-callout">Not sure which drip is the best match for you? Try our exclusive <a href="/hydration-bar/">Serene Hydration Bar</a> to find the infusion that fits your goals &mdash; then book your visit in Hudson or Barboursville.</p>

<h2>The best time is before you need it</h2>
<p>Wellness is easier to maintain than to rebuild. A little consistency now &mdash; a drip when you&rsquo;re feeling depleted, a wellness visit as the season turns &mdash; helps you head into the busy months feeling steadier.</p>

<h2>Ready to give your body some backup?</h2>
<p><strong>Book a wellness visit</strong> at Serene Med Spa and our team will help you choose the right drip for you. Learn more about our <a href="/iv-therapy/">IV therapy menu</a> or see full <a href="/pricing/">pricing</a>. You can book with us in <strong>Hudson, Ohio</strong> or <strong>Barboursville, West Virginia</strong>.</p>
<p>Our Hudson IV bar is an easy drive for patients across Northeast Ohio &mdash; including <strong>Stow, Cuyahoga Falls, Twinsburg, Aurora, Streetsboro, Macedonia, Northfield, Tallmadge, Kent, Silver Lake, Munroe Falls,</strong> and the greater <strong>Akron</strong> area.</p>
<p><em>IV therapy is intended to support general wellness and is not intended to diagnose, treat, cure, or prevent any disease. Individual needs and results vary; our medical team will review your suitability at your visit.</em></p>
''',
  "author_bio":"Dr. Robin Arora, MD is board-certified in aesthetic medicine by the American Academy of Aesthetic Medicine (AAAM). He completed an internal medicine residency through an NYU-affiliated program in the Bronx and a nephrology fellowship at Tulane University."
}]

POSTS.append({
  "slug":"hormone-optimization-signs-symptoms",
  "title":"Signs Your Hormones May Be Out of Balance",
  "seo_title":"Hormone Optimization &amp; BHRT: Signs Your Levels Are Off",
  "h1":"Feeling Off? The Signs Your Hormones May Be Out of Balance",
  "desc":"Tired, foggy, gaining weight? Learn the signs of hormone imbalance and how physician-supervised hormone optimization at Serene Med Spa may help.",
  "date":"2026-09-05","date_h":"September 5, 2026",
  "cat":"Hormone Optimization","cat_link":"/hormone-optimization/",
  "img":"/img/serene-front-desk.jpg",
  "img_alt":"The reception area at Serene Med Spa, a Certified Biote Provider offering hormone optimization in Hudson, OH and Barboursville, WV",
  "excerpt":"Tired, foggy, or gaining weight around the middle that won&rsquo;t budge? Those changes often trace back to shifting hormones. Here are the signs to watch for &mdash; and how physician-supervised hormone optimization may help.",
  "body":'''
<p>If you&rsquo;re constantly tired, struggling to sleep, gaining weight around your middle despite eating well, or just not feeling like yourself, it&rsquo;s easy to chalk it up to &ldquo;getting older.&rdquo; But for many adults, those changes trace back to something specific and manageable: <strong>shifting hormone levels.</strong></p>

<p>At Serene Med Spa, our physician-led team helps women and men in <strong>Hudson, OH and Barboursville, WV</strong> understand what&rsquo;s happening and, where appropriate, restore balance through <strong>physician-supervised hormone optimization.</strong> As a <strong>Certified Biote Provider</strong>, we offer a personalized, evidence-informed approach that starts with a simple lab test &mdash; not guesswork.</p>

<h2>Signs your hormones may be out of balance</h2>
<p>Hormones influence energy, sleep, mood, metabolism, focus, and libido, so an imbalance can show up in a lot of different ways. Many patients tell us they&rsquo;re experiencing several of these at once.</p>
<p><strong>In women</strong> (often related to perimenopause and menopause):</p>
<ul>
  <li>Lack of energy and persistent fatigue</li>
  <li>Difficulty sleeping through the night</li>
  <li>Weight gain, especially around the midsection, that won&rsquo;t budge with diet and exercise</li>
  <li>Mood swings, irritability, or feeling &ldquo;on edge&rdquo;</li>
  <li>Reduced mental focus and memory (&ldquo;brain fog&rdquo;)</li>
  <li>Low libido and changes in intimate wellness</li>
</ul>
<p><strong>In men</strong> (often related to declining testosterone with age):</p>
<ul>
  <li>Fatigue and reduced stamina</li>
  <li>Decreased muscle strength</li>
  <li>Difficulty losing weight and increased fat around the midsection</li>
  <li>Low mood, irritability, or feeling flat</li>
  <li>Reduced mental clarity and focus</li>
  <li>Reduced sexual desire and performance</li>
</ul>
<p>If several of these sound familiar, it doesn&rsquo;t automatically mean your hormones are the cause &mdash; but it&rsquo;s a good reason to get tested and talk with a provider.</p>

<h2>What is hormone optimization?</h2>
<p>Hormone optimization is a <strong>physician-supervised</strong> approach to restoring hormones toward healthy, balanced levels using <strong>bioidentical hormones</strong> &mdash; hormones that are structurally identical to the ones your body produces naturally. It&rsquo;s often referred to as <strong>bioidentical hormone replacement therapy (BHRT).</strong></p>
<p>The goal isn&rsquo;t to &ldquo;cure&rdquo; anything &mdash; it&rsquo;s to help you feel more like yourself again by addressing symptoms that come with hormonal changes, always under medical supervision and tailored to your individual lab results and goals.</p>

<h2>Our approach as a Certified Biote Provider</h2>
<p>We&rsquo;re proud to be a <strong>Certified Biote Provider</strong>, offering <strong>hormone pellet therapy</strong> as one of our options. Biote pellets are small, bioidentical hormone pellets placed just under the skin during a quick in-office visit. They release a steady, low dose of hormones over several months, so there&rsquo;s no daily cream or pill to remember.</p>
<p>Because every body is different, hormone therapy isn&rsquo;t one-size-fits-all. Depending on your evaluation, your provider may recommend pellet therapy or another physician-supervised delivery method that fits your needs and lifestyle. Whatever the approach, it&rsquo;s always personalized to <em>you</em> and monitored with follow-up labs.</p>

<h2>What to expect at Serene Med Spa</h2>
<ol>
  <li><strong>A simple test.</strong> We start with lab work to see where your hormone levels actually are &mdash; the foundation for any recommendation.</li>
  <li><strong>A consultation with a provider.</strong> We review your results, symptoms, and goals together, and answer your questions.</li>
  <li><strong>A personalized plan.</strong> If hormone optimization is appropriate for you, we build a plan tailored to your labs and lifestyle.</li>
  <li><strong>Ongoing support.</strong> We monitor your progress with follow-up visits and labs, adjusting as needed.</li>
</ol>
<p>Every step is guided by our physician-led team, so you&rsquo;re supported the whole way. Learn more about our <a href="/hormone-optimization/">hormone optimization services</a> or see full <a href="/pricing/">pricing</a>.</p>

<h2>Frequently asked questions</h2>
<h3>Is hormone optimization only for menopause?</h3>
<p>No. While many women pursue it during perimenopause and menopause, men experiencing symptoms of low testosterone can also benefit. Both start with the same simple lab test.</p>
<h3>What are bioidentical hormones?</h3>
<p>They&rsquo;re hormones that are structurally identical to the ones your body makes naturally. Your provider will explain the options during your consultation.</p>
<h3>How do I know if it&rsquo;s right for me?</h3>
<p>The only way to know is to get tested and talk with a provider. We&rsquo;ll review your labs, symptoms, and goals and give you an honest recommendation &mdash; hormone therapy isn&rsquo;t right for everyone.</p>
<h3>Do you offer this at both locations?</h3>
<p>Yes &mdash; hormone optimization is available at both our Hudson, OH and Barboursville, WV offices.</p>

<h2>Ready to feel more like yourself?</h2>
<p>Serene Med Spa serves <strong>Hudson, Ohio</strong> and <strong>Barboursville, West Virginia</strong>. Book a consultation to talk with our physician-led team about whether hormone optimization is right for you.</p>

<p class="post-disclaimer"><em>These statements have not been evaluated by the Food and Drug Administration. This information is for general educational purposes only and is not medical advice. Individual results vary and are not guaranteed. Hormone therapy is provided only after consultation and evaluation by a licensed provider, and is not intended to diagnose, treat, cure, or prevent any disease.</em></p>

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is hormone optimization only for menopause?","acceptedAnswer":{"@type":"Answer","text":"No. Many women pursue it during perimenopause and menopause, but men with symptoms of low testosterone can also benefit. Both start with a simple lab test."}},{"@type":"Question","name":"What are bioidentical hormones?","acceptedAnswer":{"@type":"Answer","text":"They are hormones that are structurally identical to the ones your body makes naturally. Your provider will explain the options during your consultation."}},{"@type":"Question","name":"How do I know if hormone optimization is right for me?","acceptedAnswer":{"@type":"Answer","text":"The only way to know is to get tested and talk with a provider, who will review your labs, symptoms, and goals and give an honest recommendation."}},{"@type":"Question","name":"Do you offer hormone optimization at both locations?","acceptedAnswer":{"@type":"Answer","text":"Yes, hormone optimization is available at both the Hudson, OH and Barboursville, WV offices of Serene Med Spa."}}]}
</script>
''',
  "author_bio":"Dr. Robin Arora, MD is board-certified in aesthetic medicine by the American Academy of Aesthetic Medicine (AAAM). He completed an internal medicine residency through an NYU-affiliated program in the Bronx and a nephrology fellowship at Tulane University."
})


HEAD_FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

# ---------- individual post pages ----------
for p in POSTS:
    url=f"{SITE}/blog/{p['slug']}/"
    crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Blog","item":SITE+"/blog/"},
      {"@type":"ListItem","position":3,"name":p["cat"],"item":url}]}
    art={"@context":"https://schema.org","@type":"BlogPosting","headline":_html.unescape(p["h1"]),
      "description":_html.unescape(p["desc"]),"image":SITE+p["img"],"datePublished":p["date"],"dateModified":p["date"],
      "author":{"@type":"Person","name":"Dr. Robin Arora, MD"},
      "publisher":{"@type":"MedicalBusiness","name":"Serene Med Spa","logo":{"@type":"ImageObject","url":LOGO}},
      "mainEntityOfPage":url,"articleSection":p["cat"]}
    HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p.get("seo_title", p["title"]+" | Serene Med Spa")}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="article">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{p['img']}">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(art)}
</script>
</head>
<body>

{NAV}

<article class="post">
  <div class="wrap post-wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/blog/">Blog</a> &nbsp;&#8250;&nbsp; {p["cat"]}</div>
    <a class="post-cat" href="{p['cat_link']}">{p["cat"]}</a>
    <h1>{p["h1"]}</h1>
    <div class="post-meta">By <strong>Dr. Robin Arora, MD</strong> &middot; {p["date_h"]}</div>
    <img class="post-hero" src="{p['img']}" alt="{p.get('img_alt', p['cat']+' before and after at Serene Med Spa')}" width="1148" height="790">
    <div class="post-body">
{p["body"]}
    </div>
    <div class="post-bio"><p>{p["author_bio"]}</p></div>
    <div class="post-cta">
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Consultation</a>
      <a class="btn btn-outline" href="/before-after/">See More Results</a>
    </div>
  </div>
</article>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
    d=f"bundle/site/blog/{p['slug']}"
    os.makedirs(d,exist_ok=True)
    open(d+"/index.html","w").write(HTML)
    print("post written:", p["slug"], len(HTML), "bytes")

# ---------- blog index ----------
POSTS_SORTED=sorted(POSTS,key=lambda x:x["date"],reverse=True)
cards="\n".join(f'''      <a class="blog-card reveal" href="/blog/{p['slug']}/">
        <div class="blog-thumb"><img loading="lazy" src="{p['img']}" alt="{p['title']}"></div>
        <div class="blog-txt"><span class="blog-tag">{p['cat']}</span><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="blog-date">{p['date_h']}</span></div>
      </a>''' for p in POSTS_SORTED)

idx_url=f"{SITE}/blog/"
idx_crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"Blog","item":idx_url}]}
blog_schema={"@context":"https://schema.org","@type":"Blog","name":"Serene Med Spa Blog","url":idx_url,
  "blogPost":[{"@type":"BlogPosting","headline":_html.unescape(p["title"]),"url":f"{SITE}/blog/{p['slug']}/","datePublished":p["date"]} for p in POSTS]}

IDX=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog &mdash; Serene Med Spa, Hudson OH</title>
<meta name="description" content="Aesthetic insights, treatment techniques, and patient case studies from the physician-led team at Serene Med Spa in Hudson, OH and Barboursville, WV.">
<link rel="canonical" href="{idx_url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-OH"><meta name="geo.placename" content="Hudson, Ohio">
<meta property="og:type" content="website">
<meta property="og:title" content="Blog &mdash; Serene Med Spa, Hudson OH">
<meta property="og:description" content="Aesthetic insights &amp; case studies from our physician-led team.">
<meta property="og:url" content="{idx_url}">
<meta property="og:image" content="{LOGO}">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(idx_crumb)}
</script>
<script type="application/ld+json">
{json.dumps(blog_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>From Our Team</strong> &mdash; techniques, results &amp; aesthetic insights. <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Blog</div>
    <div class="svc-hero-txt" style="max-width:720px">
      <div class="eyebrow">Aesthetic Insights</div>
      <h1>The Serene Blog</h1>
      <p>Technique breakdowns, patient case studies, and honest guidance from our physician-led team &mdash; serving Hudson, Ohio and Barboursville, West Virginia.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="blog-grid">
{cards}
    </div>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
os.makedirs("bundle/site/blog",exist_ok=True)
open("bundle/site/blog/index.html","w").write(IDX)
print("blog index written:", len(IDX), "bytes;", len(POSTS), "posts")
