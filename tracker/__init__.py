# tracker/__init__.py

# Initialization message when the package is imported
print("Tracker package initialized.")

# Import key components from app.py and utils.py to make them accessible at the package level
from .app import main  # Import the main Streamlit function
from .utils import fetch_content, check_appointment_status  # Import helper functions

# Optional metadata for your package
PACKAGE_VERSION = "1.0.0"

# You can also define a simple function that provides package info
def package_info():
    return f"Tracker Package - Version: {PACKAGE_VERSION}"

# If necessary, initialization code can go here
