# Phase 3 (Sep 23, 2026): served at serenemedspas.com/hudson/

The last build step, `v2_merge.py`, prefixes every URL with `/hudson`, rewrites the old host to
`https://serenemedspas.com/hudson/`, swaps the header/footer for the main site's v2 shell (imported from the
serenemain checkout: `$SERENEMAIN_SRC`, `/root/serenemain-src`, or `../serenemain`) and writes `v2.css` / `v2-shell.js`.

The MAIN nginx container (repo serenemain) bind-mounts `/root/hudson` and serves `/root/hudson/site`
at `/hudson/` (see serenemain/bundle/nginx.conf + docker-compose.yml).

`bundle/nginx.conf` for hudson.serenemedspas.com is redirect-only (301 to the new URLs). Keep the container
and its certificate for 12+ months so old links, Google Ads final URLs, GBP and printed material keep working.

Design tokens/colors now come from serenemain/site_lib.py; edit page CONTENT in this repo as before.
Rollback: restore the previous bundle/nginx.conf and remove the v2_merge line from build.sh.
