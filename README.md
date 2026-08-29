# Serene Med Spa — Hudson site

Static site generator for **hudson.serenemedspas.com** (the Hudson, OH location).
Plain Python builds a set of HTML pages into `bundle/site/`, which is served by
nginx on the VPS. No framework, no build toolchain — just Python + HTML/CSS/JS.

## Layout

```
common.py            Shared nav (mega menu), footer, schema, engagement components
pages_data*.py       Service-page content (one dict per treatment page)
aftercare_data.py    Aftercare copy used by service pages
gen_pages.py         Builds all service pages from pages_data*.py + common.py
build_pricing.py     Builds /pricing/
build_shop.py        Builds /shop/
build_blog.py        Builds /blog/ and posts
build_gallery.py     Builds /before-after/
build_housecalls.py  Builds /house-calls/
build_hydration.py   Builds /hydration-bar/
build_peptides.py    Builds /peptides/ (currently noindex — hidden pending LegitScript)
cachebust.py         Appends ?v=<hash> to the styles.css link on every page
seo_trim.py          Trims <title> <=60 and meta description <=155 (idempotent)
gen_deploy3.py       Packages bundle/site into a self-verifying deploy-services.sh
bundle/site/         The actual built website (HTML, styles.css, /img, /popup.js, sitemap.xml, robots.txt)
```

## Build

```bash
python3 gen_pages.py          # service pages
python3 build_pricing.py      # + any build_*.py you changed
python3 build_shop.py
python3 build_blog.py
python3 build_gallery.py
python3 build_housecalls.py
python3 build_hydration.py
python3 seo_trim.py           # trim titles/descriptions (run after any page rebuild)
python3 cachebust.py          # only strictly needed when styles.css changed
```

Editing `common.py` changes the nav/footer for **newly generated** pages. Some
pages in `bundle/site/` are hand-maintained (e.g. the homepage `index.html`), so
site-wide nav/header changes are applied by a global find/replace across
`bundle/site/**/index.html` as well.

## Deploy (git-based — current)

Push to GitHub, then run one command on the VPS. The VPS pulls the repo,
rebuilds, and promotes the new site atomically.

**Every deploy (from your laptop):**

```bash
git add -A && git commit -m "your change" && git push
```

**Then on the VPS (one command):**

```bash
cd /root/hudson-src && ./deploy.sh
```

`deploy.sh` does: `git reset --hard origin/main` → `./build.sh` →
copy the freshly built `bundle/site` into `/root/hudson/site` (keeping the
previous copy as `site.old` for rollback) → `docker compose up -d`. The live
site is only replaced *after* a clean build + sanity check, so a bad push can
never leave a half-written site.

**Rollback** (if a deploy looks wrong):

```bash
rm -rf /root/hudson/site && mv /root/hudson/site.old /root/hudson/site \
  && cd /root/hudson && docker compose up -d --force-recreate
```

### One-time VPS setup

The live directory `/root/hudson` (with `docker-compose.yml` + `site/` +
traefik routing) already exists and is left untouched. We only add a clone
beside it:

```bash
cd /root
git clone https://github.com/<you>/<repo>.git hudson-src
cd hudson-src
git config --global --add safe.directory /root/hudson-src   # if git warns
chmod +x build.sh deploy.sh
./deploy.sh                                                  # first git deploy
```

After that, deploying is just `git push` (laptop) + `./deploy.sh` (VPS).

> **Optional — one-liner from the VPS that also pulls:** the whole thing is
> `cd /root/hudson-src && ./deploy.sh`. If you want push-button, add a shell
> alias on the VPS: `alias deploy='cd /root/hudson-src && ./deploy.sh'`.

### Old deploy (fallback, no longer needed)

`python3 gen_deploy3.py` still writes the self-verifying `deploy-services.sh`
used by the old Google-Drive relay. Kept only as a fallback if git is ever
unavailable on the VPS.

## Brand tokens (styles.css `:root`)

- rose `#e0698a` · rose-deep `#c94f74` · gold `#e0b25c` · mint `#57c9b6`
- blush `#fff4f1` · blush-deep `#ffe6df` · plum `#3f2b3d` · ink `#4a3f47`
- Fonts: Cormorant Garamond (headings) + Jost (body)
