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
        return None  # Return None if the request fails

def check_appointment_status(page_content):
    """Check if an appointment slot is available on the page."""
    if page_content is None:
        return False  # Return False if page content is None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_content, "html.parser")
    
    # Look for specific text or elements that indicate an available appointment
    # This selector might need to be adjusted based on the actual page structure
    appointment_text = soup.find("div", class_="appointment-status")  # Update this selector as needed
    if appointment_text and "available" in appointment_text.text.lower():
        return True  # Appointment is available
    
    return False  # No appointment available
