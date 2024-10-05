import streamlit as st
import pandas as pd

st.set_page_config(page_title="Billing Management", layout="wide")

# Page content
st.title("Billing Management")
st.write("Manage billing cycles, rates, and view payment status for clients.")

# Dummy billing data
data = {
    'Client Name': ['John Doe', 'Jane Smith', 'Acme Corp', 'Global Inc', 'Solaris Energy'],
    'Invoice Amount ($)': [150, 120, 980, 750, 1100],
    'Due Date': ['2024-10-10', '2024-10-12', '2024-10-15', '2024-10-20', '2024-10-25'],
    'Status': ['Paid', 'Unpaid', 'Paid', 'Unpaid', 'Paid']
}

df_billing = pd.DataFrame(data)
st.subheader("Billing Summary")
st.dataframe(df_billing, use_container_width=True)

# Summary Stats
st.write("### Total Revenue from Paid Invoices: $2230")
st.write("### Outstanding Amount: $870")
