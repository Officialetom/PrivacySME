import streamlit as st

st.set_page_config(page_title="SME Secure System", layout="centered")

st.title("Welcome to SME Secure System")

st.sidebar.success("Use the sidebar to navigate")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.role = ""

if st.session_state.authenticated:
    st.write(f"You are logged in as **{st.session_state.username}** ({st.session_state.role})")
else:
    st.info("Go to Login or Register via the sidebar.")