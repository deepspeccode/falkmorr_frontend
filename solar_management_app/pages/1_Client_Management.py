import streamlit as st
import pandas as pd

st.set_page_config(page_title="Client Management", layout="wide")

# Page content
st.title("Client Management")
st.write("This is where you can manage your residential and commercial clients.")

# Dummy client data
data = {
    'Client Name': ['John Doe', 'Jane Smith', 'Acme Corp', 'Global Inc', 'Solaris Energy'],
    'Type': ['Residential', 'Residential', 'Commercial', 'Commercial', 'Commercial'],
    'Energy Usage (kWh)': [1200, 950, 4500, 3400, 5200]
}

df_clients = pd.DataFrame(data)
st.subheader("Client List")
st.dataframe(df_clients, use_container_width=True)
