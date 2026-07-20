from database.database import get_connection


def execute_query(query, params=None):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def search_match(team_name):

    query = """
        SELECT
            match_id,
            team1,
            team2,
            match_format,
            state,
            ground,
            city
        FROM matches
        WHERE
            team1 ILIKE %s
            OR team2 ILIKE %s
        ORDER BY start_date DESC
    """

    return execute_query(
        query,
        (f"%{team_name}%", f"%{team_name}%")
    )


def get_all_matches():

    query = """
        SELECT
            match_id,
            series_name,
            team1,
            team2,
            match_format,
            state,
            ground,
            city,
            start_date
        FROM matches
        ORDER BY start_date DESC
    """

    return execute_query(query)


def get_filtered_matches(
    match_format="All",
    match_status="All",
    city="All",
    venue="All"
):

    query = """
        SELECT
            match_id,
            series_name,
            team1,
            team2,
            match_format,
            state,
            ground,
            city,
            start_date
        FROM matches
        WHERE 1=1
    """

    params = []

    if match_format != "All":
        query += " AND match_format = %s"
        params.append(match_format)

    if match_status != "All":
        query += " AND state = %s"
        params.append(match_status)

    if city != "All":
        query += " AND city = %s"
        params.append(city)

    if venue != "All":
        query += " AND ground = %s"
        params.append(venue)

    query += " ORDER BY start_date DESC"

    return execute_query(query, params)


def get_all_cities():

    query = """
        SELECT DISTINCT city
        FROM matches
        WHERE city IS NOT NULL
        ORDER BY city
    """

    result = execute_query(query)

    cities = ["All"]

    for row in result:
        cities.append(row[0])

    return cities


def get_all_venues():

    query = """
        SELECT DISTINCT ground
        FROM matches
        WHERE ground IS NOT NULL
        ORDER BY ground
    """

    result = execute_query(query)

    venues = ["All"]

    for row in result:
        venues.append(row[0])

    return venues