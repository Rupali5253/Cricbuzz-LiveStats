from database.database import get_connection


def execute_query(query, params=None):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_live_match_details():

    query = """
        SELECT
            team1,
            team2,
            team1_runs,
            team1_wickets,
            team1_overs,
            team2_runs,
            team2_wickets,
            team2_overs,
            status,
            ground,
            city
        FROM matches
        WHERE state IN (
            'In Progress',
            'Stumps',
            'Lunch',
            'Tea',
            'Drinks',
            'Innings Break'
        )
    """

    return execute_query(query)