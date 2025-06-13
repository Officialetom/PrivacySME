import streamlit as st
import json
import os
from utils.session import is_logged_in
from utils.crypto import decrypt_data, encrypt_data

DATA_FILE = "sme_records.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "rb") as f:
        return json.loads(decrypt_data(f.read()))

def save_data(data):
    with open(DATA_FILE, "wb") as f:
        f.write(encrypt_data(json.dumps(data)))

def delete_record(index):
    data = load_data()
    if 0 <= index < len(data):
        del data[index]
        save_data(data)
        return True
    return False

def app():
    if not is_logged_in():
        st.error("You must be logged in to view this page.")
        return

    st.title("View & Manage SME Records")
    data = load_data()

    if not data:
        st.info("No records available.")
        return

    for i, record in enumerate(data):
        st.write(f"### Record {i+1}")
        st.json(record)
        if st.button(f"🗑️ Delete Record {i+1}", key=f"del_{i}"):
            if delete_record(i):
                st.success("Record deleted successfully.")
                st.experimental_rerun()
