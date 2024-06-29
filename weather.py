import os
import json
from dotenv import load_dotenv
import requests
import streamlit as st

# Load environment variables
load_dotenv()

# Retrieve API keys from environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Function to get current weather
def get_current_weather(location):
    """Get the current weather in a given location"""
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={OPENWEATHER_API_KEY}&q={location}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        return {
            "city": location,
            "weather_description": weather_description,
            "temperature": round(temperature, 2),
            "humidity": humidity,
            "pressure": pressure,
            "wind_speed": wind_speed
        }
    else:
        return {
            "city": location,
            "weather_description": "Data Fetch Error",
            "temperature": "N/A",
            "humidity": "N/A",
            "pressure": "N/A",
            "wind_speed": "N/A"
        }

# Streamlit UI
st.title("Weather App")
st.write("Enter a city name to get the current weather information.")

city = st.text_input("City Name")

if st.button("Get Weather"):
    if city:
        weather_info = get_current_weather(city)
        st.write(f"**City:** {weather_info['city']}")
        st.write(f"**Weather Description:** {weather_info['weather_description']}")
        st.write(f"**Temperature:** {weather_info['temperature']} °C")
        st.write(f"**Humidity:** {weather_info['humidity']} %")
        st.write(f"**Pressure:** {weather_info['pressure']} hPa")
        st.write(f"**Wind Speed:** {weather_info['wind_speed']} m/s")
    else:
        st.write("Please enter a city name.")
