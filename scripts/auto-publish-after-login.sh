#!/usr/bin/env bash
# Hands-off publishing, two steps and no further input:
#
#   1.  gh auth login --web          # device flow: paste the code at github.com/login/device
#   2.  ./scripts/auto-publish-after-login.sh &      # waits, then publishes by itself
#
# It polls the *API* (not `gh auth status`, which returns 0 even for a revoked token,
# and not `gh api` output, which prints an error body on stdout), then runs publish.sh,
# which builds dist/ from scratch, creates the repo, pushes and enables GitHub Pages.
# Progress lands in $LOG (default /tmp/publish.log).
#
# A device code is valid for ~15 minutes; if it expires, run step 1 again — this watcher
# keeps waiting for a valid token and will pick up whatever you authenticate next.
set -uo pipefail
cd "$(dirname "$0")/.."

LOG="${LOG:-/tmp/publish.log}"
MINUTES="${MINUTES:-45}"
: > "$LOG"

for _ in $(seq 1 $((MINUTES * 10))); do
  login="$(gh api user --jq .login 2>/dev/null | tr -d '\r\n')"
  case "$login" in
    ""|*[!A-Za-z0-9-]*) ;;                 # empty, error JSON, or otherwise not a login
    *)
      echo "== authenticated as $login at $(date -Iseconds)" | tee -a "$LOG"
      ./scripts/publish.sh >> "$LOG" 2>&1
      echo "== publish exit: $? at $(date -Iseconds)" >> "$LOG"
      REPO="$login/transport-atlas"
      sleep 90                              # let the first Actions run finish
      echo "== workflow runs ==" >> "$LOG"
      gh run list --repo "$REPO" --limit 5 >> "$LOG" 2>&1
      echo "== site http status ==" >> "$LOG"
      curl -s -o /dev/null -w '%{http_code}\n' \
        "https://${login,,}.github.io/transport-atlas/" >> "$LOG" 2>&1
      echo "== DONE — see $LOG" >> "$LOG"
      exit 0
      ;;
  esac
  sleep 6
done

echo "== gave up after ${MINUTES} min without a valid GitHub token" >> "$LOG"
