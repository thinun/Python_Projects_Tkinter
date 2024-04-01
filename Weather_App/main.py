import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pytz
import requests
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_weather():
    try:
        city = search_entry.get()
        geolocator = Nominatim(user_agent="main")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home).strftime("%I:%M %p")

        current_weather.configure(text='Current weather')
        current_time.configure(text=local_time)

        # getting weather info from Open weather api
        api_key = 'e60bc98bd30d1981b9c92c0c2b1839c2'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        json_data = requests.get(api_url).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']

        # displaying videos

        # home labels
        temp_home.configure(text=(str(temp) + "°"))
        condition_home.configure(text=condition + '| FEELS LIKE' + str(temp) + '°')

        # bottom bar labels
        w_label.configure(text=wind_speed)
        p_label.configure(text=pressure)
        h_label.configure(text=humidity)
        d_label.configure(text=description)
    except Exception as e:
        tk.messagebox.showerror('ERROR', f'Can\'t find this location!! {e}')


root = tk.Tk()
root.title("Weather Application")
root.geometry("500x600+450+100")
root.resizable(width=False, height=False)

root.configure(background="black")

# image resizing
original_image_2 = Image.open("sea_1.jpg")
resized_image_2_icon = original_image_2.resize((25, 24))
search_image_2 = ImageTk.PhotoImage(resized_image_2_icon)

original_logo_image = Image.open("logo.png")
resized_logo_image = original_logo_image.resize((400, 400))
logo_image = ImageTk.PhotoImage(resized_logo_image)

original_bottum_image = Image.open("bar.png")
resized_bottum_image = original_bottum_image.resize((450, 100))
bottum_image = ImageTk.PhotoImage(resized_bottum_image)

# image placement

logo_label = tk.Label(root, image=logo_image, bg='black')
logo_label.place(x=20, y=50)

bottum_label = tk.Label(root, image=bottum_image, bg='black')
bottum_label.place(x=25, y=440)

# search entry placement
search_entry = tk.Entry(root, width=20, font="poppins 14 bold", relief='groove', bg='black', fg='white', border=2)
search_entry.place(x=120, y=30)

# makes user type in the entry without click on it
search_entry.focus()

# placing search button image
search_icon_button = Button(image=search_image_2, border=2, background='black', cursor='hand2', command=get_weather)
search_icon_button.place(x=350, y=30)

# main window labels
current_weather = tk.Label(root, font='poppins 14 bold', fg='white', bg='black')
current_weather.place(x=10, y=70)

current_time = tk.Label(root, font='poppins 10 bold', fg='white', bg='black')
current_time.place(x=50, y=100)

temp_home = tk.Label(root, font='poppins 50 bold', bg='black', fg='red')
temp_home.place(x=370, y=80)

condition_home = tk.Label(root, font='poppins 10 bold', bg='black', fg='white')
condition_home.place(x=350, y=160)

# bottom image labels

wind_label = tk.Label(root, text='WIND', bg='#FFB117', font='poppins 10 bold')
wind_label.place(x=157, y=470)

humidity_label = tk.Label(root, text='HUMIDITY', bg='#FFB117', font='poppins 10 bold')
humidity_label.place(x=200, y=470)

description_label = tk.Label(root, text='DESCRIPTION', bg='#FFB117', font='poppins 10 bold')
description_label.place(x=270, y=470)

pressure_label = tk.Label(root, text='PRESSURE', bg='#FFB117', font='poppins 10 bold')
pressure_label.place(x=365, y=470)

w_label = tk.Label(root, bg='#FFB117', font='poppins 10 bold')
w_label.place(x=170, y=490)

h_label = tk.Label(root, bg='#FFB117', font='poppins 10 bold')
h_label.place(x=225, y=490)

d_label = tk.Label(root, bg='#FFB117', font='poppins 10 bold')
d_label.place(x=260, y=490)

p_label = tk.Label(root, bg='#FFB117', font='poppins 10 bold')
p_label.place(x=380, y=490)

root.mainloop()
