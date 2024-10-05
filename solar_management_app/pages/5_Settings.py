import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")

# Page content
st.title("Settings")
st.write("Configure app settings and user preferences.")

# Dummy settings controls
st.subheader("User Preferences")
st.checkbox("Receive email notifications")
st.checkbox("Enable dark mode")
st.selectbox("Select language", ["English", "Zulu", "Xhosa", "Sotho"])
st.slider("Notification frequency (days)", 1, 30, 7)
