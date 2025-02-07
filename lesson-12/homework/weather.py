import requests


API_KEY = "1ef102d7efc654774c9d3bb536bac87a"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()


if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    
    
    print(f"🌤 Weather in {CITY}:")
    print(f"🌡 Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"☁ Condition: {weather_description.capitalize()}")
else:
    print("Error fetching weather data:", data.get("message", "Unknown error"))