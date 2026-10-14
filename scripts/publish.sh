#!/usr/bin/env bash
# Build the atlas and publish it free on GitHub Pages.
#
#   ./scripts/publish.sh                      # uses gh (must be logged in: gh auth login)
#   REPO=user/name ./scripts/publish.sh       # publish to an explicit repo
#
# The site itself is produced by build.py; CI (.github/workflows/pages.yml) rebuilds and
# redeploys it on every push, so the link stays current.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== building =="
rm -rf dist                      # always publish a site built from scratch — no stale pages
python3 build.py --levels --standalone
touch dist/.nojekyll

REPO="${REPO:-}"
if [ -z "$REPO" ]; then
  # NOTE: `gh auth status` exits 0 with a revoked token, and `gh api` prints an error body on
  # stdout — so validate the *shape* of the login, not just that something came back.
  LOGIN="$(gh api user --jq .login 2>/dev/null | tr -d '\r\n')"
  case "$LOGIN" in
    ""|*[!A-Za-z0-9-]*)
      cat <<'EOF'
gh is not authenticated (or its token has been revoked), so the repo cannot be created
automatically.
Either:
   gh auth login                          # then re-run: ./scripts/publish.sh
or:
   REPO=youruser/transport-atlas ./scripts/publish.sh
No upload is needed for sharing in the meantime: dist/atlas-standalone.html is one
self-contained file (~10 MB) that works offline and can be emailed or dropped on any host.
EOF
      exit 1
      ;;
  esac
  REPO="$LOGIN/transport-atlas"
fi
echo "== publishing to $REPO =="

if [ ! -d .git ]; then
  git init -q
  git add -A
  git commit -qm "Transport Atlas: layered notes + site"
fi
git remote remove origin >/dev/null 2>&1 || true
git remote add origin "https://github.com/$REPO.git"
git branch -M main

if gh repo view "$REPO" >/dev/null 2>&1; then
  git push -u origin main
else
  gh repo create "$REPO" --public --source . --push \
     --description "Panta Rhei — a layered atlas of transport phenomena: 122 notes, 14 parts, one balance law"
fi

# enable Pages with the GitHub Actions source (the workflow in .github/workflows does the rest)
gh api -X POST "repos/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 \
  || gh api -X PUT "repos/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 \
  || echo "(enable Pages manually: Settings → Pages → Source: GitHub Actions)"

OWNER="${REPO%%/*}"; NAME="${REPO##*/}"
echo
echo "site (live after the first workflow run, ~1 min):"
echo "   https://${OWNER,,}.github.io/${NAME}/"
echo "single-file edition (no server, no internet):"
echo "   dist/atlas-standalone.html"
