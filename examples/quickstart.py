"""Run one Tavily Search call using a key from the environment.

Usage:
    export TAVILY_API_KEY=tvly-...   # copy the key from your Tavily dashboard
    python examples/quickstart.py "Who is Leo Messi?"

The call mirrors the official quickstart; only the key handling changes.
"""
import json
import os
import sys

from tavily import TavilyClient  # pip install tavily-python


def main() -> int:
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("TAVILY_API_KEY is not set. Copy a key from app.tavily.com first.", file=sys.stderr)
        return 1
    if not api_key.startswith("tvly-"):
        print("Warning: Tavily keys start with 'tvly-'; check the value you exported.", file=sys.stderr)

    query = sys.argv[1] if len(sys.argv) > 1 else "Who is Leo Messi?"
    client = TavilyClient(api_key=api_key)
    response = client.search(query)

    # The quickstart simply prints the response; pretty-printing makes the
    # structure easier to read the first time you see it.
    print(json.dumps(response, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
