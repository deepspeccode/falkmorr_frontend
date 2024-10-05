import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Energy Distribution", layout="wide")

# Page content
st.title("Energy Distribution Control")
st.write("Manage the energy distribution to clients and monitor solar system capacity.")

# Dummy energy distribution data
data = {
    'Client': ['John Doe', 'Jane Smith', 'Acme Corp', 'Global Inc', 'Solaris Energy'],
    'Energy Allocated (kWh)': [1300, 1000, 4600, 3500, 5300]
}

df_distribution = pd.DataFrame(data)
st.subheader("Energy Allocation Summary")
st.dataframe(df_distribution, use_container_width=True)

# Plot energy distribution
st.subheader("Energy Distribution Graph")
fig, ax = plt.subplots()
df_distribution.plot(kind='bar', x='Client', y='Energy Allocated (kWh)', ax=ax, color='orange')
st.pyplot(fig)
