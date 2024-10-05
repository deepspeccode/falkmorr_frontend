import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reports and Analytics", layout="wide")

# Page content
st.title("Usage Reports and Analytics")
st.write("View energy usage history, performance reports, and download data.")

# Dummy historical usage data
dates = pd.date_range('2024-09-01', periods=30)
usage_data = {
    'Date': dates,
    'Energy Usage (kWh)': [1400, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 
                           1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400,
                           2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900]
}

df_usage = pd.DataFrame(usage_data)

# Plot usage over time
st.subheader("Historical Energy Usage")
fig, ax = plt.subplots()
ax.plot(df_usage['Date'], df_usage['Energy Usage (kWh)'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Energy Usage (kWh)")
st.pyplot(fig)

# Table Summary
st.subheader("Energy Usage Summary")
st.write(df_usage.describe())
