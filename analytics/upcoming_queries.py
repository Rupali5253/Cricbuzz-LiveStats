from database.database import get_connection


def get_upcoming_matches():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            series_name,
            team1,
            team2,
            match_format,
            start_date,
            ground,
            city,
            status
        FROM matches

        WHERE state = 'Preview'

        ORDER BY start_date ASC
    """)

    matches = cursor.fetchall()

    cursor.close()
    connection.close()

    return matches

