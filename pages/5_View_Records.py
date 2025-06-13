import streamlit as st
import json
import os
from utils.encryptor import decrypt_data
import pandas as pd

DATA_FILE = "data/sme_records.json"

st.title("View SME Records")

if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        records = json.loads(decrypt_data(f.read()))
        df = pd.DataFrame(records)
        st.dataframe(df)
        st.download_button("Export as CSV", df.to_csv(index=False).encode(), "sme_records.csv", "text/csv")
else:
    st.warning("No records found.")