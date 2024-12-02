# tracker/app.py

import streamlit as st
from .utils import fetch_content, check_appointment_status
from playsound import playsound

# Main function that runs the Streamlit app
def main():
    # Title of the app
    st.title("Visa Appointment Tracker")

    # Input: URL for the German Visa appointment page
    url = st.text_input("Enter the URL for the appointment page:")

    # Input: Time interval (in seconds) to check the page
    interval = st.slider("Select time interval to check (in seconds):", min_value=5, max_value=60, value=15)

    # Button to start tracking
    if st.button("Start Tracking"):
        if url:
            st.write(f"Tracking URL: {url}")
            st.write(f"Checking every {interval} seconds.")
            check_appointments(url, interval)
        else:
            st.warning("Please enter a valid URL.")

# Function to check the appointment status
def check_appointments(url, interval):
    """Check if the appointment is available and notify the user."""
    # Simulating URL checking in intervals
    import time
    while True:
        # Fetch the page content
        page_content = fetch_content(url)
        
        # Check if an appointment is available
        appointment_open = check_appointment_status(page_content)
        
        if appointment_open:
            st.success("An appointment slot is now available!")
            playsound("alarm.mp3")  # Play alarm sound
            break
        else:
            st.warning("No appointment available yet. Checking again...")
        
        # Wait for the specified interval before checking again
        time.sleep(interval)
