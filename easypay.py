# -*- coding: utf-8 -*-
# easypay.py — shared "Easy Pay" financing config (Cherry + CareCredit). Identical in both site repos.
# To change a link, edit it here and rebuild. Logos live in bundle/site/img/logos/.
import os

CHERRY_URL = "https://pay.withcherry.com/serene-medical-spa-llc?utm_source=practice&m=30323"
# TODO: replace with Serene's own CareCredit link from the CareCredit Provider Center
# (the link in the Sept 2026 CareCredit email, go.carecredit.com/consumer/home?sitecode=CCCALDS2X, returns "page not found").
CARECREDIT_URL = "https://www.carecredit.com/apply/"

_SITE_DIR = os.path.join("bundle", "site")   # builders run from the repo root

def _cc_logo():
    for f in ("carecredit.svg", "carecredit.png", "carecredit.jpg", "carecredit.webp"):
        if os.path.exists(os.path.join(_SITE_DIR, "img", "logos", f)):
            return '<img src="/img/logos/%s" alt="CareCredit" class="ep-logo" loading="lazy">' % f
    return '<span class="ep-word ep-word-cc">CareCredit</span>'

def ep_option_links():
    return ('<a class="ep-opt" href="%s" target="_blank" rel="noopener">'
            '<img src="/img/logos/cherry.svg" alt="Cherry" class="ep-logo" loading="lazy">'
            '<span>See your payment options</span></a>'
            '<a class="ep-opt" href="%s" target="_blank" rel="noopener">%s'
            '<span>Apply for CareCredit</span></a>') % (CHERRY_URL, CARECREDIT_URL, _cc_logo())

def ep_band():
    return ('<section class="ep-band" id="easy-pay" aria-label="Easy Pay financing">'
            '<div class="wrap ep-inner">'
            '<div class="ep-copy"><div class="ep-eyebrow">Easy Pay</div>'
            '<h3>Get the care you want now. Pay over time.</h3>'
            '<p>Monthly payment plans through <strong>Cherry</strong> and <strong>CareCredit</strong>, with 0%% APR options for qualified patients. '
            'Applying with Cherry doesn&rsquo;t affect your credit score.</p>'
            '<a class="ep-more" href="/easy-pay/">How Easy Pay works &rsaquo;</a></div>'
            '<div class="ep-opts">%s</div>'
            '</div></section>') % ep_option_links()

EP_CSS = """
/* ---- Easy Pay (Cherry + CareCredit) ---- */
.ep-band{background:#fff;border-top:1px solid rgba(63,43,61,.10);border-bottom:1px solid rgba(63,43,61,.10);padding:34px 0}
.ep-inner{display:flex;align-items:center;justify-content:space-between;gap:28px;flex-wrap:wrap}
.ep-copy{flex:1 1 380px;max-width:620px}
.ep-eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--rose-deep,#c94f74);font-weight:700;margin-bottom:6px}
.ep-copy h3{font-family:'Cormorant Garamond',serif;font-size:1.9rem;line-height:1.15;color:var(--ink,#2b2330);margin:0 0 8px}
.ep-copy p{font-size:1.08rem;line-height:1.6;color:var(--ink,#2b2330);font-weight:500;margin:0 0 10px}
.ep-more{font-weight:600;color:var(--rose-deep,#c94f74);text-decoration:none}
.ep-more:hover{text-decoration:underline}
.ep-opts{display:flex;gap:14px;flex-wrap:wrap}
.ep-opt{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;min-width:210px;padding:18px 22px;background:#fff;border:1.5px solid rgba(63,43,61,.18);border-radius:16px;text-decoration:none;color:var(--ink,#2b2330);font-weight:600;font-size:1rem;transition:border-color .2s,box-shadow .2s,transform .2s}
.ep-opt:hover{border-color:var(--rose-deep,#c94f74);box-shadow:0 8px 22px rgba(63,43,61,.12);transform:translateY(-2px)}
.ep-opt span{font-size:.95rem;color:var(--rose-deep,#c94f74)}
.ep-logo{height:34px;width:auto;display:block}
.ep-word,.ep-opt span.ep-word{font-size:1.7rem;font-weight:700;letter-spacing:-.01em;line-height:34px;color:#1f5f56}
@media(max-width:640px){.ep-opts{width:100%}.ep-opt{flex:1 1 100%}.ep-copy h3{font-size:1.6rem}}
/* Easy Pay page */
.ep-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}
.ep-card{background:#fff;border:1.5px solid rgba(63,43,61,.12);border-radius:20px;padding:30px}
.ep-card .ep-logo{height:40px;margin-bottom:14px}
.ep-card .ep-word,.ep-card span.ep-word{font-size:2rem;line-height:40px;margin-bottom:14px;display:block}
.ep-card ul{margin:10px 0 18px;padding-left:20px}
.ep-card li,.ep-card p{font-size:1.06rem;line-height:1.6;color:var(--ink,#2b2330);font-weight:500}
.ep-fine{font-size:.9rem;color:var(--ink,#2b2330);opacity:.8;line-height:1.55;margin-top:18px}
/* ---- /Easy Pay ---- */
"""
