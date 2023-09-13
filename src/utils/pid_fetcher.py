import csv
import requests
import json

SUBGRAPH_ENDPOINTS = {
    "arbitrum": "https://api.thegraph.com/subgraphs/name/sushiswap/arbitrum-minichef",
}

def fetch_pids():
    pid_query = """
    query pidQuery {
        pools(first: 100) {
            id
        }
    }
"""
