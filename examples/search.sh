#!/usr/bin/env bash
# Call the Tavily Search endpoint directly with cURL.
#
#   export TAVILY_API_KEY=tvly-...
#   bash examples/search.sh "Who is Leo Messi?"
#
# Endpoint, headers and body match the cURL tab of the official quickstart.
set -euo pipefail

if [[ -z "${TAVILY_API_KEY:-}" ]]; then
  echo "TAVILY_API_KEY is not set. Copy a key from app.tavily.com first." >&2
  exit 1
fi

QUERY="${1:-Who is Leo Messi?}"

# Build the JSON body with Python so quotes inside the query are escaped safely.
BODY=$(python3 -c 'import json, sys; print(json.dumps({"query": sys.argv[1]}))' "$QUERY")

curl -sS -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${TAVILY_API_KEY}" \
  -d "${BODY}" | python3 -m json.tool
