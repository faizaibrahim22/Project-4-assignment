import requests


API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # Celsius
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    wind = data['wind']['speed']

    print(f"\nWeather in {city} 🌍:")
    print(f"Temperature: {temp}°C 🌡️")
    print(f"Condition: {weather} ☁️")
    print(f"Wind Speed: {wind} m/s 🌬️")
else:
    print("City not found or API issue 😓")
