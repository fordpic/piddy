import csv
import requests
import json
import os
import pygsheets
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
GOOGLE_CREDS = os.getenv("GOOGLE_CREDS")

creds = pygsheets.authorize(service_file=GOOGLE_CREDS)

SUBGRAPH_ENDPOINTS = {
    "ethereum": "https://api.thegraph.com/subgraphs/name/sushiswap/master-chefv2",
}


def fetch_pids():
    pid_query = """
    query pidQuery {
        pools(orderBy: id, orderDirection: asc, first: 1000) {
            id
            pair
        }
    }
"""
    pids_n_pairs = {}

    response = requests.post(
        SUBGRAPH_ENDPOINTS["ethereum"],
        json={"query": pid_query},
    )

    if response.status_code == 200:
        data = json.loads(response.text)

        for pool in data["data"]["pools"]:
            pid = pool["id"]
            pair_addy = pool["pair"]
            pids_n_pairs[pid] = pair_addy

        # convert to csv
        with open("eth_pids.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Pool ID", "Pair Addy"])

            for pid, pair_addy in pids_n_pairs.items():
                writer.writerow([pid, pair_addy])

        # convert to df
        df = pd.read_csv("eth_pids.csv")

        # send to g sheets
        sheet = creds.open("PIDS N PAIRS")
        db = sheet[2]

        db.set_dataframe(df, (1, 1))

        print("\nData pulled from ETH and ported successfully")

    else:
        print(f"Failed to fetch data: {response.text}")


fetch_pids()
