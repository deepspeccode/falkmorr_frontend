import streamlit as st

# Set up the main page title and sidebar navigation
st.set_page_config(page_title="Solar Management Dashboard", layout="wide")

# Sidebar Menu for Navigation
st.sidebar.title("Navigation")
st.sidebar.info("Select a page from below:")

# Display dashboard content here
st.title("Solar Energy Management Dashboard")
st.write("Welcome to the Solar Energy Management System.")

# This can be your main dashboard
st.write("Here you can view overall statistics and system status.")

# Placeholder for future content
st.write("Coming soon: Statistics, alerts, and quick insights.")