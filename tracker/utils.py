# tracker/utils.py

import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    """Fetch the content of the page."""
    try:
        # Send a request to the URL and get the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text  # Return the raw HTML content
    except requests.RequestException as e:
        print(f"Error fetching the content from {url}: {e}")
        return None

def check_appointment_status(page_content):
    """Check if an appointment slot is available on the page."""
    if page_content is None:
        return False

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_content, "html.parser")
    
    # Look for specific text or elements that indicate an available appointment
    # This will depend on the structure of the page you're scraping
    appointment_text = soup.find("div", class_="appointment-status")  # Example: you need to adjust this to your page structure
    if appointment_text and "available" in appointment_text.text.lower():
        return True  # Appointment is available
    
    return False  # No appointment available
