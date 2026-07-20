from datetime import datetime


def parse_upcoming_matches(data):

    matches = []

    for type_match in data.get("typeMatches", []):

        for series in type_match.get("seriesMatches", []):

            wrapper = series.get("seriesAdWrapper")

            if not wrapper:
                continue

            for match in wrapper.get("matches", []):

                info = match.get("matchInfo", {})
                venue = info.get("venueInfo", {})

                start_date = None
                end_date = None

                if info.get("startDate"):
                    start_date = datetime.fromtimestamp(
                        int(info["startDate"]) / 1000
                    )

                if info.get("endDate"):
                    end_date = datetime.fromtimestamp(
                        int(info["endDate"]) / 1000
                    )

                matches.append({

                    "match_id": info.get("matchId"),

                    "series_id": info.get("seriesId"),
                    "series_name": info.get("seriesName"),

                    "match_desc": info.get("matchDesc"),
                    "match_format": info.get("matchFormat"),
                    "match_type": type_match.get("matchType"),

                    "start_date": start_date,
                    "end_date": end_date,

                    "state": info.get("state"),
                    "state_title": info.get("stateTitle"),
                    "status": info.get("status"),

                    "team1_id": info.get("team1", {}).get("teamId"),
                    "team1": info.get("team1", {}).get("teamName"),

                    "team2_id": info.get("team2", {}).get("teamId"),
                    "team2": info.get("team2", {}).get("teamName"),

                    "ground": venue.get("ground"),
                    "city": venue.get("city"),
                    "timezone": venue.get("timezone"),

                    "curr_bat_team_id": None,

                    "team1_runs": None,
                    "team1_wickets": None,
                    "team1_overs": None,

                    "team2_runs": None,
                    "team2_wickets": None,
                    "team2_overs": None

                })

    return matches