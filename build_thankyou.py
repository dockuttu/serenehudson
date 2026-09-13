# -*- coding: utf-8 -*-
# build_thankyou.py — /thank-you/ : landing page after a consult-form submission (noindex).
import os
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, BOOK, STICKY_BAR
SITE="https://hudson.serenemedspas.com"
PHONE_TEL=globals().get("PHONE_TEL","tel:+13304605915"); PHONE_DISPLAY=globals().get("PHONE_DISPLAY","(330) 460-5915")
HTML=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thank You | Serene Med Spa</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{SITE}/thank-you/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
</head>
<body>
{NAV}
<section class="tint-blush" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap">
    <div class="section-head reveal in"><div class="eyebrow">Request received</div><h2>Thank you &mdash; we got your request.</h2>
    <p>A member of our team will reach out within one business day to answer your questions and find a time that works for you. Prefer not to wait? <a href="{BOOK}" target="_blank" rel="noopener">Book online now</a> or call <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
    <p style="margin-top:22px"><a class="btn" href="/">Back to home</a></p></div>
  </div>
</section>
{FOOTER}
{SCRIPTS}
</body>
</html>"""
os.makedirs("bundle/site/thank-you",exist_ok=True)
open("bundle/site/thank-you/index.html","w",encoding="utf-8").write(HTML)
print("thank-you page written")
