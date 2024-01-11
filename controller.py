# controller.py
from model import WeatherData
from view import WeatherView




class WeatherController:
    def __init__(self):
        self.model = WeatherData('')
        self.view = WeatherView(self)
        if self.view.name_city_label.cget('text'):
            self.update_forecast(self.view.name_city_label.cget('text'))



    def update_forecast(self, c=None):
        flag = False
        city = self.view.city_entry.get()
        if c:
            city = c
        if not city:
            self.view.display_error("Please enter a city name.")
            return
        self.model.connection(city)
        if self.model.flag_no_internet_connection:
            self.view.display_error("No internet connection. Please check your connection and try again.")
        elif self.model.flag_incorrect_city_name:
            self.view.display_error("Incorrect city name. Please try again.")
        else:
            forecast_data = self.model.get_data_forecast()
            self.view.display_forecast_result(city, forecast_data, flag, city)

    def update_forecast_from_history(self, city):
        flag = True
        self.model.connection(city)
        forecast_data = self.model.get_data_forecast()
        self.view.display_forecast_result(city, forecast_data, flag, city)

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    controller = WeatherController()
    controller.run()
