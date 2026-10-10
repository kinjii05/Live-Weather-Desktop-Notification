import requests
from weather_codes import wmo
from plyer import notification
import time
















city = input("For which City would you like to know the Weather? ")

def get_coordinates(city):
    
    params = {
        "name" : city,
        "count" : 1
    }


    response = requests.get("https://geocoding-api.open-meteo.com/v1/search", timeout=10,
        params = params
    ) 

    response.raise_for_status()
    
    data = response.json()

    if "results" not in data:
        return None

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    return latitude, longitude


def get_current_weather(lat, lon):

    params = {
        "latitude" : lat,
        "longitude" : lon,
        "current" : "temperature_2m,weather_code"
    }
    
    
    response = requests.get("https://api.open-meteo.com/v1/forecast", timeout=10,
        params = params
    ) 

    response.raise_for_status()

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    weather_code = data["current"]["weather_code"]
    return temperature, weather_code


coordinates = get_coordinates(city)

if coordinates is None:
    notification.notify(
        title = "City couldn't be found",
        message = f"Are you sure you searched for {city}?",
        timeout = 5
    )
else: 
    lat, lon = coordinates
    try:
        while True:
            temperature_2m, weather_code = get_current_weather(lat, lon)
            weather_str = wmo.get(weather_code, "Unknown")
            notification.notify(
                title = f"Weather in {city}",
                message = f"Current condition: {temperature_2m} °C, {weather_str}",
                timeout = 5
            ) 
            time.sleep(1800)
    except KeyboardInterrupt:
        print("Stopped")