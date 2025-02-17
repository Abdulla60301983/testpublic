import requests

# Define the API endpoint and parameters
API_KEY = "e120ef0b631bc9ade12cf5d3f0b75965"  # Replace this with your actual API key
CITY = "London"
BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

# Set up the parameters with the city name
params = {
    "q": CITY,
    "limit": 5,  # Limit the number of results returned
    "appid": API_KEY
}

try:
    # Make the GET request
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    geolocation_data = response.json()

    # Print the geolocation data for London
    if geolocation_data:
        print("Geolocation for London:")
        for location in geolocation_data:
            print(f"Name: {location['name']}")
            print(f"Latitude: {location['lat']}")
            print(f"Longitude: {location['lon']}")
            print("-" * 30)
    else:
        print("No data found for the city.")

except requests.exceptions.RequestException as e:
    print("Error fetching geolocation data:", e)
