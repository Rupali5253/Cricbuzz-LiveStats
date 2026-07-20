import streamlit as st
import plotly.express as px
import pandas as pd
from utils.footer import show_footer
from scheduler import run_scheduler_once

st.set_page_config(
    page_title="Home",
    page_icon="🏏",
    layout="wide"
)
from analytics.stats_queries import (
    get_match_status_distribution
)

from analytics.dashboard_queries import (
    get_total_matches,
    get_total_series,
    get_live_matches,
    get_total_teams,
    get_completed_matches,
    get_match_formats,
    get_highest_team_score,
    get_matches_by_venue
)
st.title("🏏 Cricbuzz Live Analytics Dashboard")
st.caption(
    "Real-Time Cricket Intelligence Platform | "
    "Live Scores • Upcoming Matches • Analytics • Match History"
)
st.info(
    "📌 This dashboard provides real-time cricket insights using the Cricbuzz API "
    "and PostgreSQL database."
)
col1, col2 = st.columns([8, 2])

with col2:

    if st.button("🔄 Sync Latest Cricket Data", use_container_width=True):

        with st.spinner("Synchronizing Cricket Data..."):

            try:

                run_scheduler_once()

                st.success("✅ Live, Upcoming & History Updated Successfully!")

                st.rerun()

            except Exception as e:

                st.error("❌ Data Synchronization Failed")

                st.exception(e)
st.divider()
st.subheader("📊 Dashboard Overview")

with st.container(border=True):

    col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🏏 Total Matches", get_total_matches())

with col2:
    st.metric("📺 Live Matches", get_live_matches())

with col3:
    st.metric("✅ Completed", get_completed_matches())

with col4:
    st.metric("👥 Teams", get_total_teams())

with col5:
    st.metric("🏆 Series", get_total_series())

st.divider()

left_col, right_col = st.columns(2)

with left_col:

    st.subheader("🏆 Highest Team Score")

    team, score = get_highest_team_score()

    st.metric(
        label="Highest Team Score",
        value=f"{score} Runs",
        delta=team
    )

with right_col:

    st.subheader("🏏 Match Format Distribution")

    formats = get_match_formats()

    df_formats = pd.DataFrame(
        formats,
        columns=["Match Format", "Total Matches"]
    )

    fig = px.bar(
        df_formats,
        x="Match Format",
        y="Total Matches",
        text="Total Matches",
        title="🏏 Match Format Distribution"
    )

    fig.update_layout(
        title=None,
        xaxis_title="Format",
        yaxis_title="Matches",
        height=380
    )

    st.plotly_chart(fig, use_container_width=True)
st.divider()

col1, col2 = st.columns(2)
with col1:

    st.subheader("📊 Match Status Distribution")

    status = get_match_status_distribution()

    df_status = pd.DataFrame(
        status,
        columns=[
            "Status",
            "Total Matches"
        ]
    )

    fig = px.pie(
        df_status,
        names="Status",
        values="Total Matches",
        hole=0.5
    )

    fig.update_traces(textposition="inside")

    fig.update_layout(
        title=None,
        height=380,
        legend_title="Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
with col2:

    st.subheader("🏟 Top Match Venues")
    st.info("Top venues based on available match records.")
    venues = get_matches_by_venue()

    df_venues = pd.DataFrame(
        venues,
        columns=[
            "Venue",
            "Matches"
        ]
    )

    st.dataframe(
        df_venues,
        use_container_width=True,
        hide_index=True,
        height=350
    )

show_footer()