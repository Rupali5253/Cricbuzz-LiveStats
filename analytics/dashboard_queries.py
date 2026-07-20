from database.database import get_connection

def execute_query(query, params=None):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def get_total_matches():

    query = """
        SELECT COUNT(*)
        FROM matches
    """

    result = execute_query(query)

    return result[0][0]

def get_total_series():

    query = """
        SELECT COUNT(DISTINCT series_name)
        FROM matches
    """

    result = execute_query(query)

    return result[0][0]
def get_live_matches():

    query = """
        SELECT COUNT(*)
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

    result = execute_query(query)

    return result[0][0]

def get_total_teams():

    query = """
        SELECT COUNT(*)
        FROM (
            SELECT team1 AS team FROM matches
            UNION
            SELECT team2 AS team FROM matches
        ) AS teams
    """

    result = execute_query(query)

    return result[0][0]

def get_completed_matches():

    query = """
        SELECT COUNT(*)
        FROM matches
        WHERE state = 'Complete'
    """

    result = execute_query(query)

    return result[0][0]

def get_match_formats():

    query = """
        SELECT
            match_format,
            COUNT(*)
        FROM matches
        GROUP BY match_format
        ORDER BY COUNT(*) DESC
    """

    result = execute_query(query)

    return result

def get_highest_team_score():

    query = """
        SELECT
            team1,
            team1_runs
        FROM matches
        WHERE team1_runs IS NOT NULL

        UNION ALL

        SELECT
            team2,
            team2_runs
        FROM matches
        WHERE team2_runs IS NOT NULL

        ORDER BY team1_runs DESC
        LIMIT 1
    """

    result = execute_query(query)

    return result[0]

def get_matches_by_venue():

    query = """
        SELECT
            ground,
            COUNT(*) AS total_matches
        FROM matches
        WHERE ground IS NOT NULL
        GROUP BY ground
        ORDER BY total_matches DESC
    """

    result = execute_query(query)

    return result