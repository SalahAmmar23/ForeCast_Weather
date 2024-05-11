import tkinter as tk
import requests

def get_weather(api_key, city):
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

def display_weather_info(city):
    """
    Displays weather information for the specified city.

    Args:
        city (str): The name of the city.
    """
    weather_data = get_weather(api_key, city)

    if weather_data['cod'] == '404':
        result_label.config(text="No City Found")
    else:
        weather = weather_data['weather'][0]['main']
        temp_fahrenheit = weather_data['main']['temp']
        temp_celsius = round((temp_fahrenheit - 32) * 5/9)  # Convert Fahrenheit to Celsius
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']  # hPa
        wind_speed = weather_data['wind']['speed']  # meters/second

        result_label.config(text=f"The weather in {city} is: {weather}\n"
                                  f"The temperature in {city} is: {temp_celsius}ºC\n"  # Display temperature in Celsius
                                  f"Humidity: {humidity}%\n"
                                  f"Pressure: {pressure} hPa\n"
                                  f"Wind Speed: {wind_speed} m/s")  # You can convert m/s to other units if needed

def on_submit():
    city = city_entry.get()
    display_weather_info(city)

# Set up GUI window
root = tk.Tk()
root.title("Weather Information")
root.geometry("800x600")  # Set window size to 800x600

# API key
api_key = '30d4741c779ba94c470ca1f63045390a'

# City input
city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=on_submit)
submit_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
