import time

from api.cricbuzz_api import fetch_live_matches
from api.upcoming_api import fetch_upcoming_matches


def run_scheduler_once():

    print("🔄 Synchronizing Cricket Data...")

    try:

        # Live Matches
        fetch_live_matches()

        # Upcoming Matches
        fetch_upcoming_matches()

        print("✅ Live + Upcoming + History Updated")

        return True

    except Exception as e:

        print(f"❌ Scheduler Error : {e}")

        return False


if __name__ == "__main__":

    print("🏏 Cricket Scheduler Started...")

    while True:

        run_scheduler_once()

        print("Waiting for 5 minutes...\n")

        time.sleep(300)