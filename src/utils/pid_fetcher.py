import csv
import requests
import json

SUBGRAPH_ENDPOINTS = {
    "arbitrum": "https://api.thegraph.com/subgraphs/name/sushiswap/arbitrum-minichef",
}

fields = [""]


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

    for pid in pids:
        result = requests.post(
            SUBGRAPH_ENDPOINTS["arbitrum"],
            json={"query": pid_query},
        )

        data = json.loads(result.text)
        print(data)

        return pids
