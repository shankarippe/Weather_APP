from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="sattenapalle"):
    

    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get current weather ***\n')

    city = input("\nPlease enter the city name: ")

    # check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "sattenapalle"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)