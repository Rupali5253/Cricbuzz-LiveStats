from datetime import datetime
from database.database import get_connection
from decimal import Decimal

def is_history_changed(match):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            team1_runs,
            team1_wickets,
            team1_overs,
            team2_runs,
            team2_wickets,
            team2_overs,
            status

        FROM match_history

        WHERE match_id = %s

        ORDER BY history_id DESC

        LIMIT 1
        """,

        (match["match_id"],)

    )

    last_record = cursor.fetchone()

    cursor.close()
    connection.close()

    if last_record is None:
        return True

    current_record = (

        match["team1_runs"],
        match["team1_wickets"],
        Decimal(str(match["team1_overs"])) if match["team1_overs"] is not None else None,

        match["team2_runs"],
        match["team2_wickets"],
        Decimal(str(match["team2_overs"])) if match["team2_overs"] is not None else None,

        match["status"]

    )
    
    return current_record != last_record

def insert_history(match):

    connection = get_connection()
    cursor = connection.cursor()

    fetch_time = datetime.now()

    cursor.execute(
        """
        INSERT INTO match_history (

            fetch_time,
            match_id,

            team1,
            team2,

            team1_runs,
            team1_wickets,
            team1_overs,

            team2_runs,
            team2_wickets,
            team2_overs,

            status

        )

        VALUES (

            %s,%s,%s,%s,
            %s,%s,%s,
            %s,%s,%s,
            %s

        )
        """,

        (

            fetch_time,
            match["match_id"],

            match["team1"],
            match["team2"],

            match["team1_runs"],
            match["team1_wickets"],
            match["team1_overs"],

            match["team2_runs"],
            match["team2_wickets"],
            match["team2_overs"],

            match["status"]

        )

    )

    connection.commit()

    cursor.close()
    connection.close()

def save_history(matches):

    for match in matches:

        if is_history_changed(match):

            insert_history(match)

            print(
                f"✅ History Updated : {match['team1']} vs {match['team2']}"
            )

        else:

            print(
                f"⏭️ No Change : {match['team1']} vs {match['team2']}"
            )