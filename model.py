# model.py
import requests

API_KEY = 'fe6ab4450179af5c9c34da5ffd6dacc9'

class WeatherData:
    def __init__(self, location):
        self.weather_data = {}
        self.flag_incorrect_city_name = False
        self.flag_no_internet_connection = False
        self.connection(location)

    def set_weather(self):
        pass

    def get_location_temp(self):
        return str(self.weather_data['main']['temp']) if 'main' in self.weather_data else ''

    def connection(self, location):
        self.flag_incorrect_city_name = False
        self.flag_no_internet_connection = False
        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            response.raise_for_status()
            self.weather_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            if isinstance(e, requests.exceptions.HTTPError):
                if response.status_code == 404:
                    self.flag_incorrect_city_name = True
                else:
                    self.flag_no_internet_connection = True
            else:
                self.flag_no_internet_connection = True
