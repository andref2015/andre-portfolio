import requests

def get_location():
  with open("templates/weather-header.html", "r") as f:
    header = f.read()
  with open("templates/get-location.html", "r") as f:
    location = f.read()
  return header + location

def get_weather_description(code):
  weather_codes = {
    0: 'Clear sky 🌞',
    1: 'Mainly clear, partly cloudy, and overcast ☁️',
    2: 'Mainly clear, partly cloudy, and overcast ☁️',
    3: 'Mainly clear, partly cloudy, and overcast ☁️',
    45: 'Fog and depositing rime fog 🌫️',
    48: 'Fog and depositing rime fog 🌫️',
    51: 'Drizzle: Light, moderate, and dense intensity 🌧️',
    53: 'Drizzle: Light, moderate, and dense intensity 🌧️',
    55: 'Drizzle: Light, moderate, and dense intensity 🌧️',
    56: 'Freezing Drizzle: Light and dense intensity ❄️🌧️',
    57: 'Freezing Drizzle: Light and dense intensity ❄️🌧️',
    61: 'Rain: Slight, moderate and heavy intensity 🌧️',
    63: 'Rain: Slight, moderate and heavy intensity 🌧️',
    65: 'Rain: Slight, moderate and heavy intensity 🌧️',
    66: 'Freezing Rain: Light and heavy intensity ❄️🌧️',
    67: 'Freezing Rain: Light and heavy intensity ❄️🌧️',
    71: 'Snow fall: Slight, moderate, and heavy intensity 🌨️',
    73: 'Snow fall: Slight, moderate, and heavy intensity 🌨️',
    75: 'Snow fall: Slight, moderate, and heavy intensity 🌨️',
    77: 'Snow grains 🌨️',
    80: 'Rain showers: Slight, moderate , and violent 🌧️',
    81: 'Rain showers: Slight, moderate , and violent 🌧️',
    82: 'Rain showers: Slight, moderate , and violent 🌧️',
    85: 'Snow showers 🌨️',
    86: 'Snow showers 🌨️',
    95: 'Thunderstorm: Slight or moderate ⛈️',
    96: 'Thunderstorm with slight and heavy hail ⛈️🧊',
    99: 'Thunderstorm with slight and heavy hail ⛈️🧊'
  }
  return weather_codes.get(code, 'Unknown weather code')

def get_weather(latitude, longitude):
  with open("templates/weather-header.html", "r") as f:
    header = f.read()

  api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto"
  response = requests.get(api_url)
  weather_data = response.json()
  
  timezone_city = weather_data['timezone']
  max_temp_today = weather_data["daily"]["temperature_2m_max"][0]
  min_temp_today = weather_data["daily"]["temperature_2m_min"][0]
  weather_code_today = weather_data["daily"]["weathercode"][0]
  weather_description = get_weather_description(weather_code_today)
  
  page_content = f"""
    <br>
    <p>Forecast for today in {timezone_city}:</p>
    <p>{weather_description}</p>
    <ul>
      <li>Max: {max_temp_today}°C</li>
      <li>Min: {min_temp_today}°C</li>
    </ul>
    <br><br>
    <a href="/">Go back</a>
    </body>
    </html>
    """
  return header + page_content
