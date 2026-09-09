#!/usr/bin/env bash
# deploy.sh — git-based deploy for hudson.serenemedspas.com
#
# Runs ON THE VPS from the cloned repo (default: /root/hudson-src).
# It pulls the latest commit, rebuilds the site, promotes it atomically into
# the live directory (/root/hudson/site), and restarts the nginx container.
# The live site is only touched AFTER a clean build + sanity check, so a bad
# push can never leave a half-written site.
#
# Usage on the VPS:
#     cd /root/hudson-src && ./deploy.sh
#
# One-time setup lives in README.md ("Git-based deploy").
set -euo pipefail

# --- config (override with env vars if your paths differ) ---
SRC="${SRC:-/root/hudson-src}"      # the git clone (this repo)
LIVE="${LIVE:-/root/hudson}"        # where docker-compose.yml + live site/ live
BRANCH="${BRANCH:-main}"

cd "$SRC"

echo "==> Pulling latest ($BRANCH)"
git fetch --all --quiet
git reset --hard "origin/$BRANCH"
echo "    now at: $(git rev-parse --short HEAD) — $(git log -1 --pretty=%s)"

echo "==> Building"
./build.sh

echo "==> Promoting to live ($LIVE/site) atomically"
rm -rf "$LIVE/site.new"
cp -a bundle/site "$LIVE/site.new"
# swap: keep the previous site as site.old for one-command rollback
rm -rf "$LIVE/site.old"
[ -d "$LIVE/site" ] && mv "$LIVE/site" "$LIVE/site.old"
mv "$LIVE/site.new" "$LIVE/site"

# keep the compose file in sync if it changed in the repo
cp -f bundle/docker-compose.yml "$LIVE/docker-compose.yml"
cp -f bundle/nginx.conf "$LIVE/nginx.conf"

echo "==> Restarting container"
cd "$LIVE"
docker compose up -d --force-recreate --remove-orphans

echo "==> Live containers:"
docker ps --format 'table {{.Names}}\t{{.Status}}' | grep -E 'NAMES|hudson' || true
echo "==> Deploy complete. Rollback if needed:  rm -rf $LIVE/site && mv $LIVE/site.old $LIVE/site && cd $LIVE && docker compose up -d --force-recreate"
