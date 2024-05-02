import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_current_weather(location):
    """Get the current weather in a given location"""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={OPENWEATHER_API_KEY}&q={location}"
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        return weather, round(temperature, 2)
    else:
        return "Data Fetch Error", "N/A"

# Streamlit app
st.title('Weather Checker App')
city = st.text_input('Enter a city name:', 'San Francisco')

if st.button('Get Weather'):
    weather, temperature = get_current_weather(city)
    if weather != "Data Fetch Error":
        st.success(f"The current weather in {city} is {weather} with a temperature of {temperature}°C.")
    else:
        st.error("Failed to fetch weather data.")
