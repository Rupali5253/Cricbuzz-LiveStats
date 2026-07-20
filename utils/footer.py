import streamlit as st

def show_footer():
    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:gray; font-size:14px;">
            © 2026 Cricbuzz Live Analytics Dashboard | Developed by <b>Rupali Rathore</b><br>
            Python • SQLite • Streamlit • RapidAPI
        </div>
        """,
        unsafe_allow_html=True
    )