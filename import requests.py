import requests
import socket

def get_ip_from_ipify():
    """Fetches public IP address using the ipify API."""
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Raise an error for non-200 status codes
        return response.text
    except requests.exceptions.RequestException as error:
        print("Error fetching IP from ipify:", error)
        return None

def get_ip_from_socket():
    """Gets local IP address using socket module."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to a reliable server
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error as error:
        print("Error fetching IP from socket:", error)
        return None

def get_location_info(ip_address):
    """Gets location information using the ipapi API."""
    try:
        url = f"https://ipapi.co/{ip_address}/json/"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print("Error fetching location info:", error)
        return None

# Main logic
ip = get_ip_from_ipify()  # Prefer external IP, but fallback to local if needed
if not ip:
    ip = get_ip_from_socket()

if ip:
    print("Your IP address is:", ip)
    location_info = get_location_info(ip)
    if location_info:
        print("Location information:")
        for key, value in location_info.items():
            print(f"{key}: {value}")
else:
    print("Failed to retrieve IP address.")

