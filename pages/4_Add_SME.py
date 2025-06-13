import streamlit as st
import json
import os
from utils.encryptor import encrypt_data, decrypt_data
from utils.logger import log_event

DATA_FILE = "data/sme_records.json"

st.title("Add SME Record check")

if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

business = st.text_input("Business Name")
owner = st.text_input("Owner")
email = st.text_input("Email")

if st.button("Save Record"):
    new_record = {"business": business, "owner": owner, "email": email}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            records = json.loads(decrypt_data(f.read()))
    else:
        records = []

    records.append(new_record)
    with open(DATA_FILE, "wb") as f:
        f.write(encrypt_data(json.dumps(records)))

    st.success("Record saved securely.")
    log_event(f"{st.session_state.username} added SME record")
