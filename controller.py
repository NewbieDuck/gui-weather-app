# controller.py
from model import WeatherData
from view import WeatherView


class WeatherController:
    def __init__(self):
        self.model = WeatherData('')
        self.view = WeatherView(self)

    def update_weather(self):
        city = self.view.city_entry.get()
        self.model.connection(city)
        temperature = self.model.get_location_temp()

        if self.model.flag_no_internet_connection:
            self.view.display_error("No internet connection. Please check your connection and try again.")
        elif self.model.flag_incorrect_city_name:
            self.view.display_error("Incorrect city name. Please try again.")
        else:
            condition = "Sunny"  # Tutaj możesz pobierać rzeczywiste warunki pogodowe
            # self.model.set_weather(temperature, condition)
            self.view.display_weather_result(city, temperature, condition)

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    controller = WeatherController()
    controller.run()
