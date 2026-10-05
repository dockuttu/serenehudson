#!/usr/bin/env python3
"""video_embeds.py — add a "Watch" video section (Vimeo, unlisted) to selected treatment pages.

Usage: python3 video_embeds.py bundle/site [barboursville|hudson]
Idempotent: the block sits between <!--video-embeds--> markers and is replaced on every run.
Placement: right after the page's intro section (the first plain <section> after the stats band).
Videos are Alma / SKNLAB manufacturer videos hosted on Serene's Vimeo (unlisted, embeddable).
"""
import json, os, re, sys

SITE_DIR = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
LOC = (sys.argv[2] if len(sys.argv) > 2 else "barboursville").lower()
SITE_URL = {"barboursville": "https://serenemedspas.com/barboursville",
            "hudson": "https://serenemedspas.com/hudson"}[LOC]

V = {  # key: (vimeo id, unlisted hash, title, seconds, thumbnail id, upload date)
 "hybrid":  ("1230567201", "5e8f0817e7", "Alma Hybrid: how it works", 119,
             "2205496920-4fedb8c344507eec1ad229203f9f4010ef840648154e6183f1d5260d955852e4", "2026-09-26T17:05:50-04:00"),
 "soprano": ("1230567248", "d7900eb4e2", "Soprano laser hair removal", 60,
             "2205495909-4a0dea8e3e95165889656d5b47a49afb5a1e56ec3c7519aa331df0f5d6841308", "2026-09-26T17:06:04-04:00"),
 "shr":     ("1230567652", "d6c4e7b2ff", "How Soprano SHR technology works", 113,
             "2205496420-58f81c270ba609336d361f264f51907b38c42489925e878693aa8bcb08c91610", "2026-09-26T17:09:15-04:00"),
 "opus":    ("1230568009", "6de18ff37b", "Opus Plasma skin resurfacing, explained", 304,
             "2205496772-6a8a5e01354dfcea4b5a0830219e971e3c165355391df6ccb425fbf288f6b76a", "2026-09-26T17:12:32-04:00"),
 "ted":     ("1230566782", "eab4362a60", "Alma TED: needle-free hair restoration", 94,
             "2205494975-17f78f4b38334aa0fdaacd74b6e122427f4666262e7df5efd54984aef9d0a3d1", "2026-09-26T17:03:07-04:00"),
 "duo":     ("1230566915", "bca5deb205", "Alma Duo: how it works", 52,
             "2205495068-a82403ff001af2f61910801f07c9da73456209e35d9d81f0dd36dded74ef1be4", "2026-09-26T17:03:57-04:00"),
 "sknlab":  ("1230565683", "31f3092344", "The SKNLAB facial", 61,
             "2205494714-1227119e503170a572957ee3a8dfb6b8af1f1b0cd531cbcfd857210814140274", "2026-09-26T17:01:00-04:00"),
}

PAGES = {  # slug: (eyebrow, h2, intro paragraph, [video keys], credit)
 "alma-hybrid": ("Watch", "See Alma Hybrid in action",
   "Two lasers in one treatment: a gentle 1570 nm pass for tone and a CO&#8322; pass for texture, blended to your skin and your downtime. Here&rsquo;s a two-minute look at how it works.",
   ["hybrid"], "Video courtesy of Alma Lasers."),
 "laser-hair-removal": ("Watch", "Soprano laser hair removal, up close",
   "Soprano uses SHR (Super Hair Removal): many quick, low-energy pulses that gradually heat the follicle, which is why most clients describe it as warm rather than snapping. See it in action, and how the technology works.",
   ["soprano", "shr"], "Videos courtesy of Alma Lasers."),
 "opus-plasma": ("Watch", "Opus Plasma, explained",
   "How fractional plasma resurfaces fine lines, crepey skin and texture, including the delicate areas around the eyes and neck where many lasers can&rsquo;t go.",
   ["opus"], "Video courtesy of Alma Lasers. Individual results vary."),
 "sknlab": ("Watch", "Inside the SKNLAB facial",
   "A one-minute look at the SKNLAB experience: a customized, results-driven facial built around your skin that day.",
   ["sknlab"], "Video courtesy of SKNLAB."),
 "alma-ted": ("Watch", "Alma TED, in 90 seconds",
   "TED delivers a hair-growth serum through the scalp with ultrasound and air pressure instead of needles, so there&rsquo;s no injection pain and no downtime. Here&rsquo;s what a session looks like.",
   ["ted"], "Video courtesy of Alma Lasers. Individual results vary."),
 "alma-duo": ("Watch", "How Alma Duo works",
   "A short look at Alma Duo: low-intensity shockwave sessions of about 15 minutes, no needles and no downtime.",
   ["duo"], "Video courtesy of Alma Lasers. Individual results vary."),
}
ONLY = {"barboursville": list(PAGES), "hudson": ["opus-plasma", "alma-ted", "alma-duo"]}[LOC]

CSS = """<style>
.vid-grid{display:grid;gap:22px;max-width:960px;margin:0 auto}
.vid-grid.two{grid-template-columns:repeat(auto-fit,minmax(300px,1fr));max-width:1100px}
.vid-card figcaption{font-size:.92rem;margin-top:10px;text-align:center;opacity:.85}
.vid-wrap{position:relative;padding-top:56.25%;border-radius:18px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.12);background:#000}
.vid-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.vid-credit{text-align:center;font-size:.82rem;opacity:.7;margin:16px auto 0}
</style>"""

def iso_dur(s):
    return "PT%dM%dS" % (s // 60, s % 60)

def block(slug, page_url):
    eyebrow, h2, lead, keys, credit = PAGES[slug]
    figs, schema = [], []
    for k in keys:
        vid, h, title, secs, thumb, up = V[k]
        src = "https://player.vimeo.com/video/%s?h=%s&amp;dnt=1&amp;title=0&amp;byline=0&amp;portrait=0" % (vid, h)
        figs.append('<figure class="vid-card reveal"><div class="vid-wrap"><iframe src="%s" title="%s" loading="lazy" '
                    'allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>%s</figure>'
                    % (src, title, ("<figcaption>%s</figcaption>" % title) if len(keys) > 1 else ""))
        schema.append({"@context": "https://schema.org", "@type": "VideoObject", "name": title,
                       "description": "%s — %s" % (title, re.sub(r"&[a-z#0-9]+;", "", lead)[:200]),
                       "thumbnailUrl": ["https://i.vimeocdn.com/video/%s-d_1280" % thumb],
                       "uploadDate": up, "duration": iso_dur(secs),
                       "embedUrl": "https://player.vimeo.com/video/%s?h=%s" % (vid, h),
                       "publisher": {"@type": "Organization", "name": "Serene Med Spa", "url": SITE_URL + "/"}})
    return ("<!--video-embeds-->\n<section id=\"watch\" class=\"tint-sand\"><div class=\"wrap\">\n"
            "  <div class=\"section-head reveal\"><div class=\"eyebrow\">%s</div><h2>%s</h2>\n"
            "    <p style=\"max-width:720px;margin:10px auto 0\">%s</p></div>\n"
            "  <div class=\"vid-grid%s\">%s</div>\n  <p class=\"vid-credit\">%s</p>\n%s\n"
            "  <script type=\"application/ld+json\">%s</script>\n</div></section>\n<!--/video-embeds-->"
            % (eyebrow, h2, lead, " two" if len(keys) > 1 else "", "".join(figs), credit, CSS,
               json.dumps(schema if len(schema) > 1 else schema[0], ensure_ascii=False)))

MARK = re.compile(r"\n?<!--video-embeds-->.*?<!--/video-embeds-->\n?", re.S)

def inject(html, slug):
    html = MARK.sub("", html)
    i = html.find('<section class="stats"')
    if i < 0:
        return None
    j = html.find("<section>", i + 10)
    if j < 0:
        return None
    k = html.find("</section>", j)
    if k < 0:
        return None
    k += len("</section>")
    return html[:k] + "\n" + block(slug, SITE_URL + "/%s/" % slug) + "\n" + html[k:]

n = 0
for slug in ONLY:
    p = os.path.join(SITE_DIR, slug, "index.html")
    if not os.path.exists(p):
        print("  video_embeds: missing", p); continue
    html = open(p, encoding="utf-8").read()
    out = inject(html, slug)
    if out is None:
        print("  video_embeds: no anchor on", slug); continue
    if out != html:
        open(p, "w", encoding="utf-8").write(out); n += 1
print("  video_embeds (%s): %d page(s) updated" % (LOC, n))
