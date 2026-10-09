import requests
from weather_codes import wmo

















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
    print("City not found")
else: 
    lat, lon = coordinates
    temperature_2m, weather_code = get_current_weather(lat, lon)
    weather_code = wmo.get()
    print(f"city: {city}")
    print(f"temperature: {temperature_2m} and code: {weather_code}")