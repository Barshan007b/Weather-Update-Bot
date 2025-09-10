import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City not found. Please try again.")
            return

        # Extract details
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # Print formatted output
        print(f"\n🌍 Weather Update for {data['name']}, {data['sys']['country']}")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"☁️ Condition: {weather}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} m/s\n")

    except Exception as e:
        print(f"⚠️ Error fetching weather data: {e}")

if __name__ == "__main__":
    print("🌦️ Welcome to the Weather Updater Bot!")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("👋 Exiting Weather Bot. Stay safe!")
            break

        # If user didn’t add country code, default to India
        if "," not in city:
            city = city.strip() + ",IN"

        get_weather(city)
