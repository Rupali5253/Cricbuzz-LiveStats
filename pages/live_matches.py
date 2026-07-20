import streamlit as st
from datetime import datetime
from utils.footer import show_footer
from analytics.live_queries import get_live_match_details

st.set_page_config(
    page_title="Live Matches",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Live Cricket Matches")
st.caption("Real-Time Cricket Scores Powered by Cricbuzz API")
st.divider()

live_matches = get_live_match_details()
st.caption("Last Updated : " + datetime.now().strftime("%H:%M:%S"))

if not live_matches:
    st.warning("⚠️ No Live Matches Available")

else:

    for match in live_matches:

        (
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
        ) = match

        with st.container(border=True):

            st.subheader(f"🏏 {team1} 🆚 {team2}")

            col1, col2 = st.columns(2)

            with col1:

                team1_score = "Yet to Bat"

                if team1_runs is not None:
                    wickets = team1_wickets if team1_wickets is not None else 0
                    overs = team1_overs if team1_overs is not None else 0
                    team1_score = f"{team1_runs}/{wickets} ({overs})"

                st.markdown(f"### {team1}")
                st.markdown(f"## {team1_score}")

            with col2:

                team2_score = "Yet to Bat"

                if team2_runs is not None:
                    wickets = team2_wickets if team2_wickets is not None else 0
                    overs = team2_overs if team2_overs is not None else 0
                    team2_score = f"{team2_runs}/{wickets} ({overs})"

                st.markdown(f"### {team2}")
                st.markdown(f"## {team2_score}")

            st.success(f"🟢 LIVE • {status}")

            st.markdown(f"📍 **{ground}, {city}**")

            st.write("")

show_footer()