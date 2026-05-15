import streamlit as st
import streamlit.components.v1 as components

# Configures the wide layout necessary for the dual-column dashboard
st.set_page_config(layout="wide")

# This CSS hides the Streamlit frame entirely so your clean application design takes over
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Loads your journal interface
try:
    with open("app.html", "r", encoding='utf-8') as f:
        journal_code = f.read()
    
    # Renders the application canvas (height set to 900px to accommodate the dashboard layout)
    components.html(journal_code, height=900, scrolling=True)
except FileNotFoundError:
    st.error("Please make sure your HTML file is named app.html inside your GitHub repository.")
