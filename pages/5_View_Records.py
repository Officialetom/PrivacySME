import streamlit as st
import json
import os
from utils.encryptor import decrypt_data, encrypt_data
import pandas as pd

DATA_FILE = "data/sme_records.json"

st.title("View SME Records")

# Check if user is logged in
if not st.session_state.get("authenticated", False):
    st.warning("Please login first.")
    st.stop()

# Check if user is admin
is_admin = st.session_state.get("role") == "admin"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        records = json.loads(decrypt_data(f.read()))
    
    df = pd.DataFrame(records)

    st.dataframe(df)

    st.download_button("Export as CSV", df.to_csv(index=False).encode(), "sme_records.csv", "text/csv")

    if is_admin:
        st.subheader("Admin: Delete a Record")

        # Allow deletion by selecting index
        if len(df) > 0:
            selected_index = st.selectbox("Select record to delete (by index)", df.index)

            if st.button("Delete Record"):
                del records[selected_index]  # Remove from the list
                # Encrypt and save updated records
                with open(DATA_FILE, "wb") as f:
                    f.write(encrypt_data(json.dumps(records)))
                st.success("Record deleted successfully.")
                st.experimental_rerun()
        else:
            st.info("No records available to delete.")
else:
    st.warning("No records found.")
