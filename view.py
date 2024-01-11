import tkinter as tk
from tkinter import messagebox
import json


bg_color = '#9900ff'
custom_font = ('Verdana', 15, 'bold')
city_font = ("Helvetica", 56, "bold")
flag = False
forecast_frame_bg_color = '#4675c0'
left_frame_bg_color = '#19335a'
middle_frame_bg_color = '#8fc8eb'


class WeatherView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Weather App")
        self.my_menu = tk.Menu(self)
        self.geometry("1200x675")
        self.minsize(1200, 675)
        self.maxsize(1200, 675)
        self.config(bg=left_frame_bg_color)
        self.city_list = []
        self.forecast_data = [[]]
        self.first_open = False
        with open('forecast.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                self.forecast_data.extend(data)
        with open('cities.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cities = [line.strip() for line in lines]
            self.city_list.extend(cities)
            print(self.city_list)
        self.name_city_label = tk.Label()
        if self.city_list:
            self.name_city_label.config(text=self.city_list[-1])

        # frames
        self.left_frame = tk.Frame(self, width=240, height=675, bg=left_frame_bg_color)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.left_frame_history_1 = tk.Frame(self.left_frame, width=240, height=105, bg=left_frame_bg_color)
        self.left_frame_history_2 = tk.Frame(self.left_frame, width=240, height=105, bg=left_frame_bg_color)
        self.left_frame_history_3 = tk.Frame(self.left_frame, width=240, height=105, bg=left_frame_bg_color)
        self.left_frame_history_4 = tk.Frame(self.left_frame, width=240, height=105, bg=left_frame_bg_color)
        self.left_frame_history_5 = tk.Frame(self.left_frame, width=240, height=105, bg=left_frame_bg_color)

        self.left_frame_history_1.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.left_frame_history_2.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.left_frame_history_3.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.left_frame_history_4.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.left_frame_history_5.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.middle_frame = tk.Frame(self, width=960, height=675, bg=middle_frame_bg_color)
        self.middle_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.forecast_frame = tk.Frame(self.middle_frame, width=960, height=300, bg=forecast_frame_bg_color)
        self.forecast_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.main_forecast_frame = tk.Frame(self.middle_frame, width=960, height=155, bg=middle_frame_bg_color)
        self.main_forecast_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.main_forecast_frame_bottom = tk.Frame(self.middle_frame, width=960, height=220, bg=middle_frame_bg_color)
        self.main_forecast_frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # icons day
        self.icon_storm = tk.PhotoImage(file='icons/storm.png')
        self.icon_clouds = tk.PhotoImage(file='icons/clouds.png')
        self.icon_raining = tk.PhotoImage(file='icons/raining.png')
        self.icon_snow = tk.PhotoImage(file='icons/snow.png')
        self.icon_sun = tk.PhotoImage(file='icons/sun.png')
        # icons night
        self.icon_storm_night = tk.PhotoImage(file='icons/thunder-night.png')
        self.icon_clouds_night = tk.PhotoImage(file='icons/cloudy-night.png')
        self.icon_raining_night = tk.PhotoImage(file='icons/heavy-rain.png')
        self.icon_snow_night = tk.PhotoImage(file='icons/cloud-moon-snow.png')
        self.icon_moon = tk.PhotoImage(file='icons/half-moon.png')
        # app icon
        self.app_icon = tk.PhotoImage(file='icons/app_icon.png')
        self.iconphoto(False, self.app_icon)
        # icon resize
        self.icon_storm_res = self.icon_storm.subsample(3, 3)
        self.icon_clouds_res = self.icon_clouds.subsample(3, 3)
        self.icon_raining_res = self.icon_raining.subsample(3, 3)
        self.icon_snow_res = self.icon_snow.subsample(3, 3)
        self.icon_sun_res = self.icon_sun.subsample(3, 3)
        self.icon_storm_night_res = self.icon_storm_night.subsample(3, 3)
        self.icon_clouds_night_res = self.icon_clouds_night.subsample(3, 3)
        self.icon_raining_night_res = self.icon_raining_night.subsample(3, 3)
        self.icon_snow_night_res = self.icon_snow_night.subsample(3, 3)
        self.icon_moon_res = self.icon_moon.subsample(3, 3)

        self.icon_storm_sub = self.icon_storm.subsample(5, 5)
        self.icon_clouds_sub = self.icon_clouds.subsample(5, 5)
        self.icon_raining_sub = self.icon_raining.subsample(5, 5)
        self.icon_snow_sub = self.icon_snow.subsample(5, 5)
        self.icon_sun_sub = self.icon_sun.subsample(5, 5)
        self.icon_storm_night_sub = self.icon_storm_night.subsample(5, 5)
        self.icon_clouds_night_sub = self.icon_clouds_night.subsample(5, 5)
        self.icon_raining_night_sub = self.icon_raining_night.subsample(5, 5)
        self.icon_snow_night_sub = self.icon_snow_night.subsample(5, 5)
        self.icon_moon_sub = self.icon_moon.subsample(5, 5)

        self.city_label = tk.Label(self.left_frame, text="Search city:", bg=left_frame_bg_color, fg='white',
                                   font=custom_font)
        self.city_label.pack(pady=2)

        self.city_entry = tk.Entry(self.left_frame, bg=left_frame_bg_color, fg='white', font=custom_font)
        self.city_entry.pack(pady=2)

        # button images
        self.button_forecast_image = tk.PhotoImage(file='buttons/check_weather_button.png')

        self.forecast_weather_button = tk.Button(self.left_frame, image=self.button_forecast_image,
                                                 command=self.controller.update_forecast, border=0,
                                                 bg=left_frame_bg_color)
        self.forecast_weather_button.pack(side='top', pady=10, anchor='center')



    def history(self, parent, city):
        parent.pack_propagate(False)
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        button = tk.Button(parent, text=city, command=lambda c=city: self.controller.update_forecast_from_history(c),
                           border=0, bg=left_frame_bg_color, font=custom_font, fg='white')
        button.pack(side="top", fill="both", expand=True)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def display_forecast_result(self, city, forecast_data, from_history, city_name):
        if from_history == False:
            if len(self.city_list) >= 5:
               self.city_list.pop(0)

            if city in self.city_list:
                print("")
            else:
                self.city_list.append(city)
            if len(self.city_list) == 1:
                parent = self.left_frame_history_5
            elif len(self.city_list) == 2:
                parent = self.left_frame_history_5
                self.history(self.left_frame_history_4, self.city_list[0])
            elif len(self.city_list) == 3:
                parent = self.left_frame_history_5
                self.history(self.left_frame_history_3, self.city_list[0])
                self.history(self.left_frame_history_4, self.city_list[1])
            elif len(self.city_list) == 4:
                parent = self.left_frame_history_5
                self.history(self.left_frame_history_2, self.city_list[0])
                self.history(self.left_frame_history_3, self.city_list[1])
                self.history(self.left_frame_history_4, self.city_list[2])
            else:
                parent = self.left_frame_history_5
                self.history(self.left_frame_history_1, self.city_list[0])
                self.history(self.left_frame_history_2, self.city_list[1])
                self.history(self.left_frame_history_3, self.city_list[2])
                self.history(self.left_frame_history_4, self.city_list[3])

            if parent is not None:
                self.history(parent, city)

            with open('cities.txt', 'w', encoding='utf-8') as file:
                for city in self.city_list:
                    file.write(f"{city}\n")

            with open('forecast.txt', 'w', encoding='utf-8') as file:
                json.dump(forecast_data, file)

        flag = False
        row_index = 1
        column_index = 1
        for index, data in enumerate(forecast_data):
            if index == 0:
                frame = self.create_forecast_first_frame(self.main_forecast_frame, data, city_name)
            else:
                frame = self.create_forecast_frame(self.forecast_frame, data, column_index)
                column_index += 1

    def create_forecast_first_frame(self, parent, data, city_name):
        parent.pack_propagate(False)
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
        for widget in self.main_forecast_frame_bottom.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        labels = ["Temperature", "Description", "Date", "Humidity", "Pressure", "Visibility"]

        for i, text in enumerate(labels):
            label = tk.Label(self.main_forecast_frame_bottom, text=text, bg=middle_frame_bg_color, fg='white',
                             font=custom_font)
            label.grid(row=i, column=0, pady=2)

        city_label = tk.Label(parent, text=city_name, bg=middle_frame_bg_color, fg='white', font=city_font)
        city_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        temp_text = f"{data[0]} °C"
        desc_text = f"{data[1]}"
        time_text = f"{data[2].split()[0]}"
        humidity_text = f"{data[3]} %"
        pressure_text = f" {data[4]} hPa"
        visibility_text = f"{data[5]} meters"
        img = self.get_icon_first_frame(data)

        labels = [temp_text, desc_text, time_text, humidity_text, pressure_text, visibility_text]
        for i, text in enumerate(labels):
            label = tk.Label(self.main_forecast_frame_bottom, text=text, bg=middle_frame_bg_color, fg='white',
                             font=custom_font)
            label.grid(row=i, column=1, pady=2)

        for i, text in enumerate(labels):
            label = tk.Label(self.main_forecast_frame_bottom, text=text, bg=middle_frame_bg_color, fg='white',
                             font=custom_font)
            label.grid(row=i, column=1, pady=2, sticky='s')

        icon = tk.Label(self.main_forecast_frame_bottom, image=img, border=0, bg=middle_frame_bg_color)
        icon.place(relx=0.8, rely=0.5, anchor=tk.E)

    def create_forecast_frame(self, parent, data, column_index):
        frame = tk.Frame(parent, bg=forecast_frame_bg_color, width=240, height=300)
        frame.grid(row=0, column=column_index, sticky='n', columnspan=1)
        temp_text = f"{data[0]} °C"
        time_text = f"{data[2].split()[0]}"
        img = self.get_icon(data)

        label_temp = tk.Label(frame, text=temp_text, fg='white', font=custom_font, bg=forecast_frame_bg_color)
        label_temp.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        icon = tk.Label(frame, image=img, border=0, bg=forecast_frame_bg_color)
        icon.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        label_time = tk.Label(frame, text=time_text, fg='white', font=custom_font, bg=forecast_frame_bg_color)
        label_time.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        return frame

    def display_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def get_icon(self, data):
        if 'd' in data[6]:
            if "thunderstorm" in data[1]:
                return self.icon_storm_sub
            elif "rain" in data[1]:
                return self.icon_raining_sub
            elif "cloud" in data[1]:
                return self.icon_clouds_sub
            elif "clear" in data[1]:
                return self.icon_sun_sub
            elif "snow" in data[1]:
                return self.icon_snow_sub
        else:
            if "thunderstorm" in data[1]:
                return self.icon_storm_night_sub
            elif "rain" in data[1]:
                return self.icon_raining_night_sub
            elif "cloud" in data[1]:
                return self.icon_clouds_night_sub
            elif "clear" in data[1]:
                return self.icon_moon_sub
            elif "snow" in data[1]:
                return self.icon_snow_night_sub

    def get_icon_first_frame(self, data):
        if 'd' in data[6]:
            if "thunderstorm" in data[1]:
                return self.icon_storm_res
            elif "rain" in data[1]:
                return self.icon_raining_res
            elif "cloud" in data[1]:
                return self.icon_clouds_res
            elif "clear" in data[1]:
                return self.icon_sun_res
            elif "snow" in data[1]:
                return self.icon_snow_res
        else:
            if "thunderstorm" in data[1]:
                return self.icon_storm_night_res
            elif "rain" in data[1]:
                return self.icon_raining_night_res
            elif "cloud" in data[1]:
                return self.icon_clouds_night_res
            elif "clear" in data[1]:
                return self.icon_moon_res
            elif "snow" in data[1]:
                return self.icon_snow_night_res
