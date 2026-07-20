import streamlit as st
import pandas as pd

from utils.footer import show_footer
from analytics.upcoming_queries import get_upcoming_matches

st.set_page_config(
    page_title="Upcoming Matches",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Upcoming Cricket Matches")
st.caption("Upcoming Cricket Fixtures Powered by Cricbuzz API")

st.divider()

matches = get_upcoming_matches()

if len(matches) == 0:

    st.info("📅 No Upcoming Matches Available.")

else:

    df = pd.DataFrame(

        matches,

        columns=[
            "Series",
            "Team 1",
            "Team 2",
            "Format",
            "Start Time",
            "Ground",
            "City",
            "Status"
        ]

    )

    df.index = range(1, len(df) + 1)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=False
    )

show_footer()