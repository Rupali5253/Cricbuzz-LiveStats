from psycopg2.extras import execute_values
from database.database import get_connection


def insert_match(matches):

    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO matches (

        match_id,
        series_id,
        series_name,
        match_desc,
        match_format,
        match_type,

        start_date,
        end_date,

        state,
        state_title,
        status,

        team1_id,
        team1,

        team2_id,
        team2,

        ground,
        city,
        timezone,

        curr_bat_team_id,

        team1_runs,
        team1_wickets,
        team1_overs,

        team2_runs,
        team2_wickets,
        team2_overs

    )

    VALUES %s

    ON CONFLICT (match_id)

    DO UPDATE SET

        series_id = EXCLUDED.series_id,
        series_name = EXCLUDED.series_name,
        match_desc = EXCLUDED.match_desc,
        match_format = EXCLUDED.match_format,
        match_type = EXCLUDED.match_type,

        start_date = EXCLUDED.start_date,
        end_date = EXCLUDED.end_date,

        state = EXCLUDED.state,
        state_title = EXCLUDED.state_title,
        status = EXCLUDED.status,

        team1_id = EXCLUDED.team1_id,
        team1 = EXCLUDED.team1,

        team2_id = EXCLUDED.team2_id,
        team2 = EXCLUDED.team2,

        ground = EXCLUDED.ground,
        city = EXCLUDED.city,
        timezone = EXCLUDED.timezone,

        curr_bat_team_id = EXCLUDED.curr_bat_team_id,

        team1_runs = EXCLUDED.team1_runs,
        team1_wickets = EXCLUDED.team1_wickets,
        team1_overs = EXCLUDED.team1_overs,

        team2_runs = EXCLUDED.team2_runs,
        team2_wickets = EXCLUDED.team2_wickets,
        team2_overs = EXCLUDED.team2_overs;
    """

    values = [

        (

            match["match_id"],
            match["series_id"],
            match["series_name"],
            match["match_desc"],
            match["match_format"],
            match["match_type"],

            match["start_date"],
            match["end_date"],

            match["state"],
            match["state_title"],
            match["status"],

            match["team1_id"],
            match["team1"],

            match["team2_id"],
            match["team2"],

            match["ground"],
            match["city"],
            match["timezone"],

            match["curr_bat_team_id"],

            match["team1_runs"],
            match["team1_wickets"],
            match["team1_overs"],

            match["team2_runs"],
            match["team2_wickets"],
            match["team2_overs"]

        )

        for match in matches

    ]

    execute_values(cursor, query, values)

    connection.commit()

    cursor.close()
    connection.close()

def reset_live_matches():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE matches
        SET
            state = 'Complete',
            state_title = 'Complete'
        WHERE state IN (
            'In Progress',
            'Stumps',
            'Lunch',
            'Tea',
            'Drinks',
            'Innings Break'
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()

def save_matches(matches):

    reset_live_matches()

    insert_match(matches)