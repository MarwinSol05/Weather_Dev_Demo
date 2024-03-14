import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the Menu 👋")

st.sidebar.success("Select an option above.")

st.markdown(
    """
    For info, please contact msolomon@hartreepartners.com
"""
)
