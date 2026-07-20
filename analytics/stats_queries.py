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

    return execute_query(query)[0][0]

def get_total_series():

    query = """
        SELECT COUNT(DISTINCT series_name)
        FROM matches
    """

    return execute_query(query)[0][0]

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

    return execute_query(query)[0][0]

def get_total_teams():

    query = """
        SELECT COUNT(*)
        FROM (
            SELECT team1 AS team FROM matches
            UNION
            SELECT team2 AS team FROM matches
        ) AS teams
    """

    return execute_query(query)[0][0]

def get_completed_matches():

    query = """
        SELECT COUNT(*)
        FROM matches
        WHERE state = 'Complete'
    """

    return execute_query(query)[0][0]

def get_top_teams():

    query = """
        SELECT
            team,
            COUNT(*) AS total_matches
        FROM
        (
            SELECT team1 AS team FROM matches

            UNION ALL

            SELECT team2 AS team FROM matches
        ) AS teams

        GROUP BY team

        ORDER BY total_matches DESC
    """

    return execute_query(query)

def get_match_status_distribution():

    query = """
        SELECT
            state,
            COUNT(*) AS total_matches
        FROM matches
        GROUP BY state
        ORDER BY total_matches DESC
    """

    return execute_query(query)

def get_top_venues():

    query = """
        SELECT
            ground,
            COUNT(*) AS total_matches
        FROM matches
        WHERE ground IS NOT NULL
        GROUP BY ground
        ORDER BY total_matches DESC
    """

    return execute_query(query)

def get_match_format_distribution():

    query = """
        SELECT
            match_format,
            COUNT(*) AS total_matches
        FROM matches
        GROUP BY match_format
        ORDER BY total_matches DESC
    """

    return execute_query(query)
def get_top_cities():

    query = """
        SELECT
            city,
            COUNT(*) AS total_matches
        FROM matches
        WHERE city IS NOT NULL
        GROUP BY city
        ORDER BY total_matches DESC
    """

    return execute_query(query)

def get_highest_team_scores():

    query = """
        SELECT
            team,
            runs
        FROM
        (
            SELECT
                team1 AS team,
                team1_runs AS runs
            FROM matches
            WHERE team1_runs IS NOT NULL

            UNION ALL

            SELECT
                team2 AS team,
                team2_runs AS runs
            FROM matches
            WHERE team2_runs IS NOT NULL
        ) AS scores

        ORDER BY runs DESC
        LIMIT 10
    """

    return execute_query(query)

