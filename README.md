# Tavily API key examples

*Unofficial community examples for Tavily. Not affiliated with Tavily. All trademarks belong to their owners.*

Small, runnable scripts that show what to do once you have a Tavily API key: read it from the environment, make the first Search call in Python, JavaScript and cURL, and run a capped batch without burning the free monthly credits. Every endpoint, header and parameter used here comes from the official quickstart; the scripts only add key handling, error handling and output formatting.

> If the same agent needs to generate images, video or audio after it searches, [try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models, pay per run](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=tavily-api-key-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
| --- | --- |
| `examples/quickstart.py` | The four-line Python quickstart with the key read from `TAVILY_API_KEY` and the response pretty-printed |
| `examples/quickstart.js` | The same call with the `@tavily/core` package for Node |
| `examples/search.sh` | A raw HTTP POST to `https://api.tavily.com/search` with cURL and a Bearer header |
| `examples/batch_search.py` | Several queries from a file, a hard cap on calls, raw responses saved to JSONL |

## Setup

1. Get a key: sign in at [app.tavily.com](https://app.tavily.com) (email, Google, GitHub, LinkedIn or Microsoft), then copy one of the API keys on your dashboard. The quickstart says new accounts receive 1,000 free API credits per month with no credit card.
2. Export it: `export TAVILY_API_KEY=tvly-...` - real keys begin with `tvly-`.
3. Install what you need: `pip install tavily-python` for the Python scripts, `npm i @tavily/core` for the Node script. The shell script needs only cURL and Python 3 for JSON formatting.

No script in this repository contains a key. If you fork it, keep it that way.

## examples/quickstart.py

The official quickstart is four lines: import `TavilyClient`, construct it with `api_key`, call `search` with a query string, print the response. This script keeps those four lines and adds three things: it refuses to run if `TAVILY_API_KEY` is missing, warns if the value does not start with `tvly-`, and pretty-prints the response with `json.dumps` so the structure is readable the first time you see it. Pass a query as the first argument or fall back to the quickstart's own example.

## examples/quickstart.js

The Node version uses `require("@tavily/core")`, builds the client with `tavily({ apiKey })` and awaits `search(query)`, exactly as the JavaScript tab of the quickstart shows. It exits non-zero when the key is missing or the request throws, which makes it usable as a smoke test in CI.

## examples/search.sh

Some stacks have no SDK. The cURL tab of the quickstart is a POST to `https://api.tavily.com/search` with `Content-Type: application/json`, `Authorization: Bearer tvly-YOUR_API_KEY` and a body of `{"query": "..."}`. The script builds that body with Python so quotes inside the query are escaped safely, then pipes the response through `python3 -m json.tool`.

## examples/batch_search.py

The free tier is 1,000 credits per month. A loop that retries on every hiccup can drain that in an afternoon, so this script reads queries from a text file, applies a `--max-calls` cap, catches per-query exceptions instead of aborting, and appends `{query, response}` records to a JSONL file. Keeping the raw response next to the query means you can change your parsing later without spending credits again.

## Reading the response

The quickstart simply prints the response and points to the API reference for the details, so these examples do not assume any field names. Print the JSON once, look at the keys you actually get, and only then write parsing code; the response shape is documented on the Search endpoint page of the docs.

## When to use Synexa instead

Tavily answers "what is on the web about this". It does not make pictures, clips or audio. When the step after retrieval is generation - a hero image for the article your agent just researched, a short video from a script, a voiceover - [try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models, pay per run](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=tavily-api-key-examples&utm_content=readme-top&utm_term=tier-r). The pattern is the same as these scripts: one key in an environment variable, one client, one call.
