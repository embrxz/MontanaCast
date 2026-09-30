import requests

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,precipitation",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch"
    }

    response = requests.get(url, params=parameters)

    data = response.json()

    current = data["current"]

    weather = {
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "precipitation": current["precipitation"]
    }

    return weather