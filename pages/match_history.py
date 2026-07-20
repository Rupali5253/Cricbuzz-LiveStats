import streamlit as st
import pandas as pd
from utils.footer import show_footer

from analytics.history_queries import (
    get_filtered_history,
    get_all_history_teams
)

st.set_page_config(
    page_title="Match History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Match History")

st.caption("Complete Match Timeline Stored by Scheduler")

st.divider()

# ======================================
# Team Filter
# ======================================

col1, col2 = st.columns([3,7])

with col1:
    selected_team = st.selectbox(
        "🏏 Filter by Team",
        get_all_history_teams()
    )

# ======================================
# Fetch History
# ======================================

history = get_filtered_history(selected_team)

if not history:

    st.warning("No History Available")

else:

    df = pd.DataFrame(
        history,
        columns=[
            "Fetch Time",
            "Team 1",
            "Team 2",
            "Team 1 Runs",
            "Team 1 Wickets",
            "Team 1 Overs",
            "Team 2 Runs",
            "Team 2 Wickets",
            "Team 2 Overs",
            "Status"
        ]
    )

    st.metric(
        "📋 Records Found",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ======================================
    # Download CSV
    # ======================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Match History",
        data=csv,
        file_name="match_history.csv",
        mime="text/csv"
    )

show_footer()