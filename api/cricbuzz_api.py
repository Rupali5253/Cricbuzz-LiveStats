import os
import json
import requests
from dotenv import load_dotenv

from utils.parser import parse_matches
from database.match_queries import save_matches
from database.history_queries import save_history

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}


def fetch_live_matches():

    response = requests.get(URL, headers=HEADERS)

    print("Status Code:", response.status_code)

    data = response.json()

    with open("data/live_matches.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ Data saved successfully.")

    matches = parse_matches(data)

    save_matches(matches)
        
    live_matches = []

    LIVE_STATES = [
        "In Progress",
        "Stumps",
        "Lunch",
        "Tea",
        "Drinks",
        "Innings Break"
    ]

    for match in matches:

        if match["state"] in LIVE_STATES:
            live_matches.append(match)

    if live_matches:
        save_history(live_matches)
        print("✅ History table updated.")

    else:
        print("ℹ️ No live matches available. History not updated.")

print("✅ Latest table updated.")


if __name__ == "__main__":

    fetch_live_matches()
