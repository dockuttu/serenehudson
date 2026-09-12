#!/usr/bin/env bash
# build.sh — regenerate the entire Hudson site into bundle/site/
# Pure Python 3 stdlib, no external deps. Idempotent: safe to run repeatedly.
set -euo pipefail
cd "$(dirname "$0")"

echo "==> Building service pages"
python3 gen_pages.py
python3 build_cities.py

echo "==> Building section pages"
python3 build_pricing.py
python3 build_shop.py
# blog moved to blog.serenemedspas.com (repo sereneblog); old /blog/ URLs 301 via bundle/nginx.conf
rm -rf bundle/site/blog 2>/dev/null || true
python3 fix_blog_links.py
python3 build_gallery.py
python3 build_housecalls.py
python3 build_hydration.py
python3 build_rewards.py
# NOTE: build_peptides.py is intentionally NOT run — the peptides page stays
# hidden (noindex/unlinked) until LegitScript certification clears. To bring it
# back later, add:  python3 build_peptides.py

echo "==> SEO trim (titles <=60, descriptions <=155)"
python3 seo_trim.py

echo "==> Generating sitemap.xml (indexable pages only)"
python3 build_sitemap.py

echo "==> Cache-bust styles.css"
python3 cachebust.py

# Sanity gate: the homepage must exist and be non-trivial, or we refuse to ship.
if [ ! -s bundle/site/index.html ] || [ "$(wc -c < bundle/site/index.html)" -lt 2000 ]; then
  echo "!!! build sanity check FAILED: bundle/site/index.html missing or too small" >&2
  exit 1
fi

echo "==> Build complete: $(find bundle/site -type f | wc -l) files in bundle/site/"

echo "==> Google Ads tag"
python3 inject_gtag.py bundle/site

echo "==> Page guard (nav <-> built pages <-> deep links)"
python3 seo_polish.py bundle/site
python3 check_pages.py
