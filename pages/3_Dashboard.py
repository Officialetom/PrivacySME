import streamlit as st
from utils.logger import log_event
from utils.backup import backup_db
from utils.auth import get_users

st.title("Dashboard")

if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

st.write(f"Welcome **{st.session_state.username}** ({st.session_state.role})")

if st.button("Add SME Record"):
    st.switch_page("pages/4_Add_SME.py")

if st.button("Backup Database"):
    result = backup_db()
    st.success(result)
    log_event(f"{st.session_state.username} performed a backup")

if st.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")

if st.session_state.role == "admin":
    st.subheader("User List")
    users = get_users()
    st.text("\n".join(users))