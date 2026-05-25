#!/usr/bin/env python3
"""Crypto Market Fetcher — CoinGecko free API, no key required."""

import argparse
import json
import sys
import urllib.request
from typing import Optional

API_BASE = "https://api.coingecko.com/api/v3/simple/price"
USER_AGENT = "DeepSeek-CryptoMarket-Skill/1.0"
TIMEOUT = 15

DEFAULT_COINS = [
    "bitcoin", "ethereum", "solana", "ripple", "cardano",
    "binancecoin", "dogecoin", "tron", "avalanche-2", "sui",
]

COIN_ALIASES = {
    "btc": "bitcoin", "eth": "ethereum", "sol": "solana",
    "xrp": "ripple", "ada": "cardano", "bnb": "binancecoin",
    "doge": "dogecoin", "trx": "tron", "avax": "avalanche-2",
}

def resolve_coins(raw: str) -> list[str]:
    ids = []
    for token in raw.split(","):
        token = token.strip().lower()
        if not token:
            continue
        ids.append(COIN_ALIASES.get(token, token))
    return ids or DEFAULT_COINS


def fetch(
    coins: list[str],
    vs: str,
    include_market_cap: bool,
    include_volume: bool,
    include_change: bool,
) -> dict:
    params = [
        f"ids={','.join(coins)}",
        f"vs_currencies={vs}",
    ]
    if include_market_cap:
        params.append("include_market_cap=true")
    if include_volume:
        params.append("include_24hr_vol=true")
    if include_change:
        params.append("include_24hr_change=true")

    url = f"{API_BASE}?{'&'.join(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:300]
        raise SystemExit(f"API HTTP {e.code}: {body}")
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error: {e.reason}")
    except json.JSONDecodeError:
        raise SystemExit("Invalid JSON from API")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch live crypto prices from CoinGecko (no API key needed)."
    )
    parser.add_argument(
        "--coins", default=",".join(DEFAULT_COINS),
        help="Comma-separated coin ids or aliases (btc,eth,sol,xrp,ada,bnb,doge,trx,avax,sui)"
    )
    parser.add_argument("--vs", default="usd,cny", help="VS currencies (default: usd,cny)")
    parser.add_argument("--include-market-cap", action="store_true", help="Include market cap")
    parser.add_argument("--include-volume", action="store_true", help="Include 24h volume")
    parser.add_argument("--include-change", action="store_true", help="Include 24h % change")

    args = parser.parse_args()

    # When run inside DeepSeek, always include all enrichments
    include_cap = args.include_market_cap or True
    include_vol = args.include_volume or True
    include_chg = args.include_change or True

    coins = resolve_coins(args.coins)
    data = fetch(coins, args.vs, include_cap, include_vol, include_chg)

    # Compact output — one line per coin for easy model parsing
    print(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    main()