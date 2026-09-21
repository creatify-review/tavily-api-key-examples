"""Run a small batch of Tavily searches and save raw responses as JSONL.

    export TAVILY_API_KEY=tvly-...
    python examples/batch_search.py queries.txt out.jsonl --max-calls 20

Why the cap: the free tier is 1,000 credits per month, and a loop that
retries on every hiccup can drain it in an afternoon.
"""
import argparse
import json
import os
import sys

from tavily import TavilyClient  # pip install tavily-python


def main() -> int:
    parser = argparse.ArgumentParser(description="capped batch of Tavily searches")
    parser.add_argument("queries", help="text file, one query per line")
    parser.add_argument("out", help="output JSONL path (appended to)")
    parser.add_argument("--max-calls", type=int, default=20, help="hard cap on API calls")
    args = parser.parse_args()

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("TAVILY_API_KEY is not set.", file=sys.stderr)
        return 1
    client = TavilyClient(api_key=api_key)

    with open(args.queries, encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]
    queries = queries[: args.max_calls]

    calls = 0
    with open(args.out, "a", encoding="utf-8") as out:
        for q in queries:
            try:
                response = client.search(q)
            except Exception as exc:  # keep the raw error next to the query
                response = {"error": str(exc)}
            calls += 1
            out.write(json.dumps({"query": q, "response": response}, ensure_ascii=False) + "\n")
            print(f"[{calls}/{len(queries)}] {q}")

    print(f"done: {calls} calls written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
