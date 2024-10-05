import os

# Define the project structure
folders = [
    "solar_management_app",
    "solar_management_app/pages"
]

files_content = {
    "solar_management_app/app.py": """
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
""",
    "solar_management_app/pages/1_Client_Management.py": """
import streamlit as st

st.set_page_config(page_title="Client Management", layout="wide")

# Page content
st.title("Client Management")
st.write("This is where you can manage your residential and commercial clients.")

# Placeholder for content
st.write("Coming soon: Add, edit, and remove clients. View their energy consumption and details.")
""",
    "solar_management_app/pages/2_Energy_Distribution.py": """
import streamlit as st

st.set_page_config(page_title="Energy Distribution", layout="wide")

# Page content
st.title("Energy Distribution Control")
st.write("Manage the energy distribution to clients and monitor solar system capacity.")

# Placeholder for content
st.write("Coming soon: Controls for energy allocation and system monitoring.")
""",
    "solar_management_app/pages/3_Billing_Management.py": """
import streamlit as st

st.set_page_config(page_title="Billing Management", layout="wide")

# Page content
st.title("Billing Management")
st.write("Manage billing cycles, rates, and view payment status for clients.")

# Placeholder for content
st.write("Coming soon: Invoices, billing schedules, and payment management.")
""",
    "solar_management_app/pages/4_Reports.py": """
import streamlit as st

st.set_page_config(page_title="Reports and Analytics", layout="wide")

# Page content
st.title("Usage Reports and Analytics")
st.write("View energy usage history, performance reports, and download data.")

# Placeholder for content
st.write("Coming soon: Data export, detailed reports on energy usage.")
""",
    "solar_management_app/pages/5_Settings.py": """
import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")

# Page content
st.title("Settings")
st.write("Configure app settings and user preferences.")

# Placeholder for content
st.write("Coming soon: Manage notifications, user accounts, and system settings.")
"""
}

# Create the folder structure
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")

# Create and populate the files
for file_path, content in files_content.items():
    with open(file_path, 'w') as file:
        file.write(content.strip())
        print(f"Created and populated file: {file_path}")

print("Project structure created successfully.")
