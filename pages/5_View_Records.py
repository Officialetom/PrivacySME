import streamlit as st
import json
import os
from utils.encryptor import decrypt_data, encrypt_data

DATA_FILE = "data/sme_records.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "rb") as f:
         records = json.loads(decrypt_data(f.read()))
        df = pd.DataFrame(records)
        st.dataframe(df)
        st.download_button("Export as CSV", df.to_csv(index=False).encode(), "sme_records.csv", "text/csv")

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
    if not st.session_state.get("authenticated", False):
        st.warning("Please login first.")
        st.stop()

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
