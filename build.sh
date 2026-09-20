#!/usr/bin/env bash
# build.sh — regenerate the entire Hudson site into bundle/site/
# Pure Python 3 stdlib, no external deps. Idempotent: safe to run repeatedly.
set -euo pipefail
cd "$(dirname "$0")"

echo "==> Building service pages"
python3 gen_pages.py
python3 build_cities.py
python3 build_aftercare.py        # /aftercare/ hub + 25 per-treatment post-care pages
python3 build_service_cities.py   # service+city landing pages (Search Console gap: ranked ~30, zero clicks)

echo "==> Building section pages"
python3 build_pricing.py
python3 build_obagi_shop.py   # Obagi store: /shop/, /shop/<product>/, /cart/, /obagi/, shop.js (old build_shop.py retired)
# blog moved to blog.serenemedspas.com (repo sereneblog); old /blog/ URLs 301 via bundle/nginx.conf
rm -rf bundle/site/blog 2>/dev/null || true
python3 fix_blog_links.py
python3 build_gallery.py
python3 build_housecalls.py
python3 build_hydration.py
python3 build_rewards.py
python3 build_easypay.py    # /easy-pay/ (Cherry + CareCredit) + Easy Pay styles
python3 build_labs.py        # /labs/ test guide pages
# NOTE: build_peptides.py is intentionally NOT run — the peptides page stays
# hidden (noindex/unlinked) until LegitScript certification clears. To bring it
# back later, add:  python3 build_peptides.py

echo "==> SEO trim (titles <=60, descriptions <=155)"
python3 seo_trim.py

echo "==> Generating sitemap.xml (indexable pages only)"
python3 build_thankyou.py
python3 patch_static_consult.py   # hand-built pages + popup.js -> Zoho form
python3 build_sitemap.py

echo "==> SEO targeting (final titles/descriptions for search)"
python3 seo_targeting.py bundle/site

echo "==> ABIM board-certification badge in every footer"
python3 abim_badge.py bundle/site
