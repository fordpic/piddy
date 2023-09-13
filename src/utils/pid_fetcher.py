import csv
import requests
import json

# Need to figure out:
# Why requests won't load
# Why my script won't print

SUBGRAPH_ENDPOINTS = {
    "arbitrum": "https://api.thegraph.com/subgraphs/name/sushiswap/arbitrum-minichef",
}


def fetch_pids():
    pid_query = """
    query pidQuery {
        pools {
            id
            pair
        }
    }
"""
    pids = {}

    result = requests.post(
        SUBGRAPH_ENDPOINTS["arbitrum"],
        json={"query": pid_query},
    )

    if result.status_code == 200:
        data = json.loads(result.text)
        print(data)

    else:
        print(f"Failed to fetch: {result.text}")
