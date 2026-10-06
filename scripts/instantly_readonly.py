#!/usr/bin/env python3
"""Letture in sola lettura sul workspace Instantly di Fluffy (API v2).

Usa solo la variabile INSTANTLY_API_KEY_FLUFFY. Fa solo richieste GET.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://api.instantly.ai/api/v2"
KEY_ENV = "INSTANTLY_API_KEY_FLUFFY"

CAMPAIGN_STATUS = {
    0: "bozza",
    1: "attiva",
    2: "in pausa",
    3: "completata",
    4: "subsequence",
    -1: "account non sani",
    -2: "bounce protection",
    -99: "sospesa",
}


def get_all(path, api_key, limit=100):
    """Scarica tutte le pagine di un endpoint di lista v2."""
    items, cursor = [], None
    while True:
        params = {"limit": limit}
        if cursor:
            params["starting_after"] = cursor
        url = f"{BASE_URL}{path}?{urllib.parse.urlencode(params)}"
        # Senza User-Agent Cloudflare risponde 403 (error code 1010).
        headers = {"Authorization": f"Bearer {api_key}", "User-Agent": "instantly-readonly/1.0"}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
        except urllib.error.HTTPError as e:
            sys.exit(f"Errore HTTP {e.code} su {path}: {e.read().decode(errors='replace')[:300]}")
        items.extend(data.get("items", []))
        cursor = data.get("next_starting_after")
        if not cursor:
            return items


def print_campaigns(items):
    for c in sorted(items, key=lambda c: (c.get("status") != 1, c.get("name", ""))):
        status = CAMPAIGN_STATUS.get(c.get("status"), str(c.get("status")))
        print(f"{status:<18} {c.get('name', '')}  ({c.get('id')})")
    print(f"\nTotale campagne: {len(items)}")


def print_accounts(items):
    for a in sorted(items, key=lambda a: a.get("email", "")):
        print(f"{a.get('email', ''):<45} status={a.get('status')}  warmup={a.get('warmup_status')}")
    print(f"\nTotale account: {len(items)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("what", choices=["campaigns", "accounts"])
    parser.add_argument("--json", action="store_true", help="stampa il JSON grezzo")
    args = parser.parse_args()

    api_key = os.environ.get(KEY_ENV)
    if not api_key:
        sys.exit(f"Variabile {KEY_ENV} non impostata: impostala con la chiave del workspace Fluffy.")

    items = get_all(f"/{args.what}", api_key)
    if args.json:
        print(json.dumps(items, indent=2, ensure_ascii=False))
    elif args.what == "campaigns":
        print_campaigns(items)
    else:
        print_accounts(items)


if __name__ == "__main__":
    main()
