import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WeatherDataVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Data Visualizer")
        
        # Create and configure the main frame
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # City entry
        self.city_label = ttk.Label(self.frame, text="Enter City Name:")
        self.city_label.grid(row=0, column=0, padx=5, pady=5)

        self.city_entry = ttk.Entry(self.frame)
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)

        # Fetch weather button
        self.fetch_btn = ttk.Button(self.frame, text="Fetch Weather Data", command=self.fetch_weather_data)
        self.fetch_btn.grid(row=0, column=2, padx=5, pady=5)

        # Matplotlib Figure
        self.figure = plt.Figure(figsize=(8, 5), dpi=100)
        self.ax1 = self.figure.add_subplot(211)  # Temperature plot
        self.ax2 = self.figure.add_subplot(212)  # Humidity plot

        # Canvas for Matplotlib
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)

        self.api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API Key

    def fetch_weather_data(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                raise ValueError(data.get("message", "Error fetching data."))

            self.display_weather_data(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_weather_data(self, data):
        # Extracting relevant data
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        # Prepare data for visualization
        metrics = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
        values = [temperature, humidity, wind_speed]

        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()

        # Plotting temperature and humidity
        self.ax1.bar(metrics[:2], values[:2], color=['blue', 'orange'])
        self.ax1.set_title(f'Weather in {city}')
        self.ax1.set_ylabel('Value')
        
        self.ax2.bar(['Wind Speed (m/s)'], [wind_speed], color='green')
        self.ax2.set_title('Wind Speed')
        self.ax2.set_ylabel('Value')

        self.canvas.draw()

        # Display additional information
        messagebox.showinfo("Weather Info", f"{city}\nTemperature: {temperature} °C\n"
                                              f"Humidity: {humidity} %\n"
                                              f"Wind Speed: {wind_speed} m/s\n"
                                              f"Description: {weather_description.capitalize()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDataVisualizerApp(root)
    root.mainloop()
