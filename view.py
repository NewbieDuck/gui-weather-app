# view.py
import tkinter as tk
from tkinter import messagebox


class WeatherView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Weather App")
        self.my_menu = tk.Menu(self)
        self.geometry("500x400")
        self.config(menu=self.my_menu)

        self.city_label = tk.Label(self, text="Enter your city:")
        self.city_label.pack(pady=2)

        self.city_entry = tk.Entry(self)
        self.city_entry.pack(pady=2)

        self.check_weather_button = tk.Button(self, text="Check weather", command=self.controller.update_weather)
        self.forecast_weather_button = tk.Button(self, text="5 Day weather forecast", command=self.forecast_weather)
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)

        self.check_weather_button.pack(side='top', pady=2, anchor='center')
        self.forecast_weather_button.pack(side='top', pady=2, anchor='center')
        self.exit_button.pack(side='top', pady=2, anchor='center')

        # Dodaj label do wyświetlania wyników pogody
        self.weather_result_label = tk.Label(self, text="")
        self.weather_result_label.pack(pady=10)

    def forecast_weather(self):
        pass

    def display_weather_result(self, city, temperature, condition):
        # Zaktualizuj label z wynikami pogody
        result_text = f"Weather for {city}: Temperature: {temperature}°C, Condition: {condition}"
        self.weather_result_label.config(text=result_text)

    def display_error(self, error_message):
        messagebox.showerror("Error", error_message)  # Zmiana tej linii