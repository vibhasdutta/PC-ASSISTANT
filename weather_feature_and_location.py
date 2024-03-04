import requests
from dotenv import load_dotenv
import os


load_dotenv()

weather_apikey = os.getenv("WEATHER_API")



def ask_for_city(cityname:str):  # * FUNCTION FOR CHECKING WEATHER FOR DIFFERRNT LOCATION
    
    if cityname:
        city = cityname
    # If cities list is not empty, use the first city from the list
    else:
        city = os.getenv("CITY_NAME")

    response = get_weather_info(city)
    temp_celsius = response["current"]["temp_c"]
    temp_fahrenhite = response["current"]["temp_f"]
    humidity = response["current"]["humidity"]
    pressure = response["current"]["pressure_in"]
    visibility = response["current"]["vis_km"]
    wind_speed = response["current"]["wind_kph"]
    weather = response["current"]["condition"]["text"]
    cloud = response["current"]["cloud"]
    uv = response["current"]["uv"]
    feelslike_C = response["current"]["feelslike_c"]
    feelslike_f = response["current"]["feelslike_f"]

    return (
        temp_celsius,
        temp_fahrenhite,
        humidity,
        pressure,
        visibility,
        wind_speed,
        weather,
        uv,
        city,
        cloud,
        feelslike_f,
        feelslike_C,
    )


def get_weather_info(default_city):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={weather_apikey}&q={default_city}"
    response = requests.get(base_url).json()
    return response
