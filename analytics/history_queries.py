from database.database import get_connection


def execute_query(query, params=None):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_match_history():

    query = """
        SELECT
            fetch_time,
            team1,
            team2,
            team1_runs,
            team1_wickets,
            team1_overs,
            team2_runs,
            team2_wickets,
            team2_overs,
            status
        FROM match_history
        ORDER BY fetch_time DESC
    """

    return execute_query(query)


def get_all_history_teams():

    query = """
        SELECT DISTINCT team1
        FROM match_history

        UNION

        SELECT DISTINCT team2
        FROM match_history

        ORDER BY team1
    """

    result = execute_query(query)

    teams = ["All"]

    for row in result:

        if row[0]:
            teams.append(row[0])

    return teams


def get_filtered_history(team="All"):

    query = """
        SELECT
            fetch_time,
            team1,
            team2,
            team1_runs,
            team1_wickets,
            team1_overs,
            team2_runs,
            team2_wickets,
            team2_overs,
            status
        FROM match_history
        WHERE 1=1
    """

    params = []

    if team != "All":

        query += " AND (team1=%s OR team2=%s)"
        params.extend([team, team])

    query += " ORDER BY fetch_time DESC"

    return execute_query(query, params)