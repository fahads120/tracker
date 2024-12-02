import time
import hashlib
import logging
from urllib.error import URLError, HTTPError
from urllib.request import urlopen, Request
from playsound import playsound
import streamlit as st

# --- Configuration ---
ALARM_FILE = 'alarm.mp3'  # Alarm sound file
LOG_FILE = 'appointment_tracker.log'

# --- Logging Setup ---
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# --- Streamlit UI ---
st.title("Dynamic Appointment Tracker")
st.write("Monitor a website for changes and get notified.")

# --- User Inputs ---
url = st.text_input("Enter the URL to track:", "https://example.com")
tracking_interval = st.number_input("Enter time interval (seconds):", min_value=1, max_value=3600, value=5, step=1)
start_tracking = st.button("Start Tracker")

# --- Alarm Function ---
def play_alarm():
    """Play an alarm sound."""
    try:
        playsound(ALARM_FILE)
        logging.info("Alarm played successfully.")
        st.success("Alarm played!")
    except Exception as e:
        logging.error(f"Error playing alarm: {e}")
        st.error("Error playing alarm. Check logs for details.")

# --- Fetch Content Function ---
def fetch_website_content(url):
    """Fetch the content of the webpage."""
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(request).read()
        return hashlib.sha224(response).hexdigest()
    except HTTPError as e:
        logging.error(f"HTTP Error: {e.code} - {e.reason}")
        st.error(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except URLError as e:
        logging.error(f"URL Error: {e.reason}")
        st.error(f"URL Error: {e.reason}")
        return None
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        st.error(f"Unexpected Error: {e}")
        return None

# --- Main Tracking Logic ---
def track_appointments(url, interval):
    """Continuously track the website for changes."""
    st.write("Initializing tracker...")
    logging.info("Starting appointment tracker...")
    
    current_hash = fetch_website_content(url)
    if not current_hash:
        logging.error("Failed to fetch initial website content. Exiting...")
        st.error("Failed to fetch initial website content. Please check the URL or network connection.")
        return

    logging.info("Tracker is now monitoring the website for changes.")
    st.success("Tracker is now monitoring the website for changes.")

    # Initialize a counter
    cycle_count = 0

    while True:
        try:
            # Increment the counter
            cycle_count += 1
            st.write(f"Tracking Cycle: {cycle_count}")

            # Wait for the specified interval
            time.sleep(interval)

            # Fetch the new hash
            new_hash = fetch_website_content(url)

            if not new_hash:
                logging.warning("Failed to fetch website content. Skipping this cycle.")
                st.warning("Failed to fetch website content. Skipping this cycle.")
                continue

            # Compare the hashes
            if new_hash == current_hash:
                msg = f"Cycle {cycle_count}: No changes detected. Appointment NOT Opened."
                logging.info(msg)
                st.write(msg)
            else:
                msg = f"Cycle {cycle_count}: ******* Appointment Opened ******"
                logging.info(msg)
                st.write(msg)
                play_alarm()
                current_hash = new_hash  # Update hash after detecting a change

        except Exception as e:
            logging.error(f"Unexpected Error in main loop: {e}")
            st.error(f"Unexpected Error: {e}")
            break

# --- Run Tracker ---
if start_tracking:
    if url.strip():
        track_appointments(url, tracking_interval)
    else:
        st.error("Please enter a valid URL!")
