import requests

# Example of using OpenWeatherMap API for weather data
api_key = 'your_api_key'  # Replace with your API key
city_name = 'city_name'  # Replace with the city name you're interested in
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

# Extract rainfall forecast data
rain_data = [entry['rain']['3h'] if 'rain' in entry else 0 for entry in data['list']]  # 3-hour rainfall data

print(rain_data)
