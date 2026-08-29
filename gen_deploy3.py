import os, hashlib, base64

BUNDLE = "/home/claude/hudson-site/bundle"
OUT = "/home/claude/hudson-site/deploy-services.sh"

# separate compose from site files
compose_path = os.path.join(BUNDLE, "docker-compose.yml")
compose_data = open(compose_path, "rb").read()

site_files = []
site_root = os.path.join(BUNDLE, "site")
for root, dirs, fnames in os.walk(site_root):
    dirs.sort()
    for fn in sorted(fnames):
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, site_root)  # relative to site/
        site_files.append((rel, open(full, "rb").read()))

def heredoc(target, data):
    # text files -> plain heredoc; binaries (images) -> base64 heredoc
    try:
        text = data.decode("utf-8")
        delim = "SERENE_EOF"
        assert delim not in text
        return "cat > %s <<'%s'\n%s\n%s\n" % (target, delim, text.rstrip("\n"), delim)
    except UnicodeDecodeError:
        b64 = base64.b64encode(data).decode("ascii")
        lines = "\n".join(b64[i:i+76] for i in range(0, len(b64), 76))
        return "base64 -d > %s <<'B64EOF'\n%s\nB64EOF\n" % (target, lines)

L = []
L.append("#!/bin/bash")
L.append("set -e")
L.append("# Serene Med Spa (Hudson) - deploy 4 service pages + shared CSS + SEO")
L.append("# Stages files, verifies checksums, then promotes atomically. Live site")
L.append("# stays untouched unless every file verifies.")
L.append('cd /root/hudson')
L.append('rm -rf site.new; mkdir -p site.new')
L.append('echo "Writing staged files..."')
L.append('')
# compose to a staged name at root
L.append(heredoc("docker-compose.yml.new", compose_data))
# site files into site.new/
for rel, data in site_files:
    d = os.path.dirname(rel)
    if d:
        L.append('mkdir -p site.new/%s' % d)
    L.append(heredoc("site.new/" + rel, data))

# verify
L.append('echo "Verifying checksums..."')
L.append('FAIL=0')
checks = [("docker-compose.yml.new", compose_data)] + [("site.new/"+r, d) for r,d in site_files]
for path, data in checks:
    sha = hashlib.sha256(data).hexdigest()
    L.append('GOT=$(sha256sum %s | cut -d" " -f1)' % path)
    L.append('if [ "$GOT" != "%s" ]; then echo "  MISMATCH %s"; FAIL=1; else echo "  ok %s"; fi' % (sha, path, path))
L.append('')
L.append('if [ "$FAIL" != "0" ]; then')
L.append('  echo "!!! Transfer corrupted - ABORTING. Live site untouched."')
L.append('  rm -rf site.new docker-compose.yml.new')
L.append('  exit 1')
L.append('fi')
L.append('')
L.append('echo "All verified. Promoting to live..."')
L.append('rm -rf site')
L.append('mv site.new site')
L.append('mv -f docker-compose.yml.new docker-compose.yml')
L.append('docker compose up -d --force-recreate --remove-orphans')
L.append('echo "=== DONE - live at hudson.serenemedspas.com ==="')
L.append("docker ps --format 'table {{.Names}}\\t{{.Status}}'")
L.append('')

script = "\n".join(L)
open(OUT, "w").write(script)
print("Wrote", len(script), "bytes")
