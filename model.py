# model.py
import requests
from datetime import datetime

API_KEY = ''


class WeatherData:
    def __init__(self, location):
        self.weather_data = {}
        self.flag_incorrect_city_name = False
        self.flag_no_internet_connection = False
        self.connection(location)

    def set_weather(self):
        pass

    def get_temp(self):
        return str(self.weather_data['list'][0]['main']['temp']) if 'list' in self.weather_data else ''

    def get_data_forecast(self):
        self.weather_list = []
        time_rn = self.weather_data['list'][0]['dt_txt'].split()[1]
        time_rn = time_rn[:2]
        avg_temp = 0
        if time_rn[0] == '0':
            time_rn = time_rn[1:]
        for day in self.weather_data['list']:
            temp = str(day['main']['temp'])
            desc = str(day['weather'][0]['description'])
            time = str(day['dt_txt'])
            humidity = str(day['main']['humidity'])
            pressure = str(day['main']['pressure'])
            visibility = str(day['visibility'])
            icon = str(day['weather'][0]['icon'])
            time_object = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            hour = time_object.hour
            avg_temp += float(temp)
            if str(hour) == str(time_rn):
                self.weather_list.append([temp, desc, time, humidity, pressure, visibility, icon])

        avg_temp = round(avg_temp / 40, 2)
        return self.weather_list

    def get_description(self):
        return str(self.weather_data['list'][0]['weather'][0]['description']) if 'list' in self.weather_data else ''

    def get_min_temp(self):
        return str(self.weather_data['list'][0]['main']['temp_min']) if 'list' in self.weather_data else ''

    def get_max_temp(self):
        return str(self.weather_data['list'][0]['main']['temp_max']) if 'list' in self.weather_data else ''

    def get_humidity(self):
        return str(self.weather_data['list'][0]['main']['humidity']) if 'list' in self.weather_data else ''

    def get_visibility(self):
        return str(self.weather_data['list'][0]['visibility']) if 'list' in self.weather_data else ''

    def get_pressure(self):
        return str(self.weather_data['list'][0]['main']['pressure']) if 'list' in self.weather_data else ''

    def get_day(self):
        icon = str(self.weather_data['list'][0]['weather'][0]['icon']) if 'list' in self.weather_data else ''
        if 'd' in icon:
            return True
        return False

    def get_icon(self):
        return str(self.weather_data['list'][0]['weather'][0]['icon']) if 'list' in self.weather_data else ''

    def connection(self, location):
        self.flag_no_internet_connection = False
        self.flag_incorrect_city_name = False
        try:
            url_forecast = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric'
            response = requests.get(url_forecast)
            response.raise_for_status()
            self.weather_data = response.json()
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.HTTPError):
                if response.status_code == 404:
                    self.flag_incorrect_city_name = True
                else:
                    self.flag_no_internet_connection = True
            else:
                self.flag_no_internet_connection = True
