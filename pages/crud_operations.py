import streamlit as st
import pandas as pd
from utils.footer import show_footer

from analytics.crud_queries import (
    search_match,
    get_filtered_matches,
    get_all_cities,
    get_all_venues
)

st.set_page_config(
    page_title="CRUD Operations",
    page_icon="🗂",
    layout="wide"
)

st.title("🗂 CRUD Operations")

st.caption("Manage Cricket Match Records")

st.divider()

# ==========================
# Search Team
# ==========================
st.subheader("🔍 Search Matches")
team_name = st.text_input(
    "🔍 Search Team",
    placeholder="Enter Team Name (Example: India)"
)

if team_name:

    matches = search_match(team_name)

    if matches:

        df = pd.DataFrame(
            matches,
            columns=[
                "Match ID",
                "Team 1",
                "Team 2",
                "Format",
                "Status",
                "Ground",
                "City"
            ]
        )

        st.subheader("🔎 Search Result")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning("No Match Found.")

st.divider()

# ==========================
# Filters
# ==========================
st.subheader("🎯 Filter Matches")
col1, col2, col3, col4 = st.columns(4)

with col1:

    selected_format = st.selectbox(
        "🏏 Format",
        ["All","TEST","ODI","T20","T20I"]
    )

with col2:

    selected_status = st.selectbox(
        "📊 Status",
        ["All","In Progress","Complete","Preview"]
    )

with col3:

    selected_city = st.selectbox(
        "🏙 City",
        get_all_cities()
    )
with col4:

    selected_venue = st.selectbox(
        "🏟 Venue",
        get_all_venues()
    )

# ==========================
# All Match Records
# ==========================

st.subheader("📋 All Match Records")

matches = get_filtered_matches(
    selected_format,
    selected_status,
    selected_city,
    selected_venue
)

df = pd.DataFrame(
    matches,
    columns=[
        "Match ID",
        "Series",
        "Team 1",
        "Team 2",
        "Format",
        "Status",
        "Ground",
        "City",
        "Start Date"
    ]
)

# -----------------------------
# Convert Timestamp to Date
# -----------------------------
if not df.empty:

    df["Start Date"] = pd.to_datetime(
        df["Start Date"],
        errors="coerce"
    )

    df["Start Date"] = df["Start Date"].dt.strftime(
        "%d %b %Y %I:%M %p"
    )

if df.empty:

    st.warning("⚠️ No Match Records Found.")

else:

    st.metric(
        "📋 Total Records",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.write("")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Match Data (CSV)",
        data=csv,
        file_name="cricket_matches.csv",
        mime="text/csv"
    )
show_footer()