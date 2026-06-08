import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    if not city:
        messagebox.showwarning("Warning", "Enter a city name")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result.config(
            text=f"City: {city}\n"
                 f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {weather.title()}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

title = tk.Label(root, text="Weather App", font=("Arial", 18))
title.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=5)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.mainloop()