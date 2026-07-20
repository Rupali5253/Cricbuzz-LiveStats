import streamlit as st
import pandas as pd
import plotly.express as px
from utils.footer import show_footer

from analytics.stats_queries import (
    get_total_matches,
    get_live_matches,
    get_completed_matches,
    get_total_teams,
    get_total_series,
    get_match_status_distribution,
    get_top_teams,
    get_top_venues,
    get_match_format_distribution,
    get_top_cities,
    get_highest_team_scores
)

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Cricket Analytics Dashboard")

st.caption("Analytics generated from Cricbuzz Live Data")

st.divider()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("🏏 Matches", get_total_matches())
col2.metric("🟢 Live", get_live_matches())
col3.metric("✅ Completed", get_completed_matches())
col4.metric("👥 Teams", get_total_teams())
col5.metric("🏆 Series", get_total_series())

st.divider()
st.subheader("📈 Overall Statistics")
col1, col2 = st.columns(2)
with col1:

    st.subheader("🥧 Match Status")

    status_data = get_match_status_distribution()

    df = pd.DataFrame(
        status_data,
        columns=["Match Status", "Total Matches"]
    )

    fig = px.pie(
        df,
        names="Match Status",
        values="Total Matches",
        hole=0.5
    )

    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        showlegend=True
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
    
with col2:

    st.subheader("🏏 Top Teams")

    team_data = get_top_teams()

    team_df = pd.DataFrame(
        team_data,
        columns=["Team", "Matches"]
    )

    fig = px.bar(
        team_df,
        x="Team",
        y="Matches",
        text="Matches"
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=30, b=20)
    )
    fig.update_traces(
        textposition="outside"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            team_df,
            use_container_width=True,
            hide_index=True
        )
st.divider()

col1, col2 = st.columns(2)
with col1:

    st.subheader("🏟 Top Venues")

    venue_data = get_top_venues()

    venue_df = pd.DataFrame(
        venue_data,
        columns=["Venue", "Matches"]
    )

    fig = px.bar(
        venue_df,
        x="Venue",
        y="Matches",
        text="Matches"
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=30, b=20)
    )
    fig.update_traces(
        textposition="outside"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            venue_df,
            use_container_width=True,
            hide_index=True
        )
with col2:

    st.subheader("🏏 Match Formats")

    format_data = get_match_format_distribution()

    format_df = pd.DataFrame(
        format_data,
        columns=["Format", "Matches"]
    )

    fig = px.pie(
        format_df,
        names="Format",
        values="Matches",
        hole=0.5
    )

    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        showlegend=True
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            format_df,
            use_container_width=True,
            hide_index=True
        )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📍 Top Cities")

    city_data = get_top_cities()

    city_df = pd.DataFrame(
        city_data,
        columns=["City", "Matches"]
    )

    fig = px.bar(
        city_df,
        x="City",
        y="Matches",
        text="Matches"
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=30, b=20)
    )
    fig.update_traces(
        textposition="outside"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            city_df,
            use_container_width=True,
            hide_index=True
        )

with col2:

    st.subheader("🏆 Highest Team Scores")

    score_data = get_highest_team_scores()

    score_df = pd.DataFrame(
        score_data,
        columns=["Team", "Runs"]
    )

    fig = px.bar(
        score_df,
        x="Team",
        y="Runs",
        text="Runs"
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=30, b=20)
    )
    fig.update_traces(
        textposition="outside"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📋 View SQL Result"):
        st.dataframe(
            score_df,
            use_container_width=True,
            hide_index=True
        )

st.success(
    "✔ Analytics Generated Successfully "
    f"({get_total_matches()} Matches Analysed)"
)
show_footer()
