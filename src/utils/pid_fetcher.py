import csv
import requests
import json

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
    pids_n_pairs = {}

    response = requests.post(
        SUBGRAPH_ENDPOINTS["arbitrum"],
        json={"query": pid_query},
    )

    if response.status_code == 200:
        data = json.loads(response.text)

        for pool in data["data"]["pools"]:
            pid = pool["id"]
            pair_addy = pool["pair"]
            pids_n_pairs[pid] = pair_addy

        print(pids_n_pairs)

        # write to csv
        # TO DO: port to G Sheets
        with open("arbitrum_pids.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Pool ID", "Pair Addy"])

            for pid, pair_addy in pids_n_pairs.items():
                writer.writerow([pid, pair_addy])

    else:
        print(f"Failed to fetch: {response.text}")


fetch_pids()
