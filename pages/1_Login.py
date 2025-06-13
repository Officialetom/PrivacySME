import streamlit as st
from utils.auth import login

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    role = login(username, password)
    if role:
        st.session_state.authenticated = True
        st.session_state.username = username
        st.session_state.role = role
        st.success(f"Welcome {username} ({role})")
    else:
        st.error("Invalid username or password")