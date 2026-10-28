# Live-Weather-Desktop-Notification

The script fetches the live weather and displays it as a desktop notification.


## How it works

- The script asks for a city then `get_coordinates` proceeds to return the latitude and longitude of the city for the next function
- Now the function `get_current_weather` takes the lat and lon values and returns the temperature and the weather code
- The weather codes turn into text by fetching the description from `weather_codes.py`
- At the end the script shows the weather condition as a desktop notification and repeats every 30 minutes


## How to run

1. Install dependencies: `pip install -r requirements.txt`

2. Run the script: `python weather.py`

3. To stop the script press: `Ctrl+C`