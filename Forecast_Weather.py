import tkinter as tk
import requests

def fetch_weather():
    city = city_entry.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Extracting weather information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed'] * 1.60934  # Convert mph to km/h
    rain = data.get('rain', {}).get('1h', 0)  # Rain in last hour, default to 0 if not available
    pressure = data['main']['pressure']
    
    # Convert temperature to Celsius
    temperature_celsius = (temperature - 32) * 5/9
    
    # Display weather information
    result_label.config(text=f"Temperature: {temperature_celsius:.2f} °C\n"
                              f"Humidity: {humidity}%\n"
                              f"Wind Speed: {wind_speed:.2f} km/h\n"
                              f"Rain (last hour): {rain} mm\n"
                              f"Pressure: {pressure} hPa")

# Creating the GUI
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("800x600")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
