import streamlit as st
from utils.auth import register

st.title("Register")

username = st.text_input("New Username")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["admin", "user"])

if st.button("Register"):
    result = register(username, password, role)
    st.info(result)