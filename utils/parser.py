from datetime import datetime
def parse_matches(data):

    matches = []

    type_matches = data.get("typeMatches", [])

    for match_type in type_matches:

        series_matches = match_type.get("seriesMatches", [])

        for series in series_matches:

            series_wrapper = series.get("seriesAdWrapper", {})

            if not series_wrapper:
                continue

            match_list = series_wrapper.get("matches", [])

            for match in match_list:

                match_info = match.get("matchInfo", {})
                match_score = match.get("matchScore", {})
                venue_info = match_info.get("venueInfo", {})
                team1 = match_info.get("team1", {})
                team2 = match_info.get("team2", {})

                match_data = {

                    # Match Details
                    "match_id": match_info.get("matchId"),
                    "series_id": match_info.get("seriesId"),
                    "series_name": match_info.get("seriesName"),
                    "match_desc": match_info.get("matchDesc"),
                    "match_format": match_info.get("matchFormat"),
                    "match_type": match_type.get("matchType"),
                    "start_date": (
                        datetime.fromtimestamp(
                            int(match_info.get("startDate")) / 1000
                        ).strftime("%Y-%m-%d %H:%M:%S")
                        if match_info.get("startDate")
                        else None
                    ),

                    "end_date": (
                        datetime.fromtimestamp(
                            int(match_info.get("endDate")) / 1000
                        ).strftime("%Y-%m-%d %H:%M:%S")
                        if match_info.get("endDate")
                        else None
                    ),

                    # Match Status
                    "state": match_info.get("state"),
                    "state_title": match_info.get("stateTitle"),
                    "status": match_info.get("status"),

                    # Teams
                    "team1_id": team1.get("teamId"),
                    "team1": team1.get("teamName"),

                    "team2_id": team2.get("teamId"),
                    "team2": team2.get("teamName"),

                    # Venue
                    "ground": venue_info.get("ground"),
                    "city": venue_info.get("city"),
                    "timezone": venue_info.get("timezone"),

                    # Current Batting Team
                    "curr_bat_team_id": match_info.get("currBatTeamId"),

                    # Score
                    "team1_runs": match_score.get("team1Score", {}).get("inngs1", {}).get("runs"),
                    "team1_wickets": match_score.get("team1Score", {}).get("inngs1", {}).get("wickets"),
                    "team1_overs": match_score.get("team1Score", {}).get("inngs1", {}).get("overs"),

                    "team2_runs": match_score.get("team2Score", {}).get("inngs1", {}).get("runs"),
                    "team2_wickets": match_score.get("team2Score", {}).get("inngs1", {}).get("wickets"),
                    "team2_overs": match_score.get("team2Score", {}).get("inngs1", {}).get("overs"),
                }

                matches.append(match_data)

    return matches