import os
import json
import requests
from dotenv import load_dotenv

from utils.upcoming_parser import parse_upcoming_matches
from database.match_queries import save_matches

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}


def fetch_upcoming_matches():

    response = requests.get(URL, headers=HEADERS)

    print("Status Code:", response.status_code)

    # ==========================
    # No Content Available
    # ==========================
    if response.status_code == 204:
        print("ℹ️ No Upcoming Matches Available.")
        return

    # ==========================
    # API Error
    # ==========================
    if response.status_code != 200:
        print(f"❌ API Error : {response.status_code}")
        print(response.text)
        return

    # ==========================
    # Convert Response to JSON
    # ==========================
    try:
        data = response.json()

    except Exception as e:
        print("❌ Invalid JSON Response")
        print("Error:", e)
        print(response.text)
        return

    # ==========================
    # Save JSON Backup
    # ==========================
    with open("data/upcoming_matches.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ Upcoming JSON Saved Successfully")

    # ==========================
    # Parse Data
    # ==========================
    matches = parse_upcoming_matches(data)

    # ==========================
    # Save Database
    # ==========================
    save_matches(matches)

    print(f"✅ {len(matches)} Upcoming Matches Saved in PostgreSQL")


if __name__ == "__main__":
    fetch_upcoming_matches()