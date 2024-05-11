import requests

def get_weather_data(api_key, city):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        city (str): The name of the city for which to fetch weather data.

    Returns:
        dict: Weather data for the specified city.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    response = requests.get(url)
    return response.json()

def display_weather_info(weather_data, city):
    """
    Displays weather information for the specified city.

    Args:
        weather_data (dict): Weather data for the city.
        city (str): The name of the city.
    """
    if weather_data['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data['weather'][0]['main']
        temperature = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']  # hPa
        wind_speed = weather_data['wind']['speed']  # meters/second

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temperature}ºF")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")  # You can convert m/s to other units if needed

def main():
    api_key = '30d4741c779ba94c470ca1f63045390a'
    city = input("Enter city: ")
    weather_data = get_weather_data(api_key, city)
    display_weather_info(weather_data, city)

if __name__ == "__main__":
    main()
