# -*- coding: utf-8 -*-
# fix_charset.py — make <meta charset="UTF-8"> the first thing inside <head> on every page.
# Browsers only look for it in the first 1024 bytes; injected tracking scripts had pushed it
# past that, so pages rendered as Windows-1252 (curly quotes/dashes showed up as "â€™").
import glob, os, re, sys
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
META = '<meta charset="UTF-8">'
pat = re.compile(r'\s*<meta charset=["\']?utf-8["\']?\s*/?>', re.I)
n = 0
for f in glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True):
    s = open(f, encoding="utf-8").read()
    i = s.find("<head>")
    if i == -1:
        continue
    j = i + len("<head>")
    if s[j:j + 40].lstrip().lower().startswith('<meta charset'):
        continue
    t = pat.sub("", s)
    i = t.find("<head>") + len("<head>")
    t = t[:i] + "\n" + META + t[i:]
    open(f, "w", encoding="utf-8").write(t); n += 1
print("fix_charset: moved charset to top of <head> on", n, "page(s)")
