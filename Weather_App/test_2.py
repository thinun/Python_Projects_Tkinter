import tkinter as tk
from tkinter import ttk
import pygame
import requests
import os

# Initialize pygame
pygame.init()

# Create the Tkinter window
root = tk.Tk()
root.title("Weather App")

# Weather data
city = 'London'  # Replace with the desired city
api_key = 'e60bc98bd30d1981b9c92c0c2b1839c2'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

try:
    json_data = requests.get(api_url).json()
    condition = json_data['weather'][0]['main']
except requests.RequestException as e:
    condition = 'Unknown'
except KeyError as e:
    condition = 'Unknown'

# Weather condition mapping to video clips
video_mapping = {
    'Clear': 'Animation - 1711982149838.mp4',
    'Clouds': 'Animation - 1711982135070.mp4',
    'Rain': 'Animation - 1711981871478.mp4',
    'Snow': 'Animation - 1711982135070.mp4',
    'Thunderstorm': 'Animation - 1711981871478.mp4',
    'Unknown': 'Animation - 1711981389365.mp4'
}

# Load video clip
video_file = video_mapping.get(condition, 'Animation - 1711981389365.mp4')
video_path = os.path.join(os.getcwd(), video_file)

# Create a label to display weather information
weather_label = ttk.Label(root, text=f'Weather Condition: {condition}')
weather_label.pack(pady=20)

# Create a Canvas widget to display video
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Initialize pygame display
pygame.display.init()

# Load and play video clip
movie = pygame.movie.Movie(video_path)
movie_screen = pygame.Surface((640, 480))
movie.set_display(movie_screen)
movie.play()

# Convert pygame Surface to Tkinter PhotoImage and display on Canvas
movie_surface = pygame.image.tostring(movie_screen, 'RGB')
photo = tk.PhotoImage(data=movie_surface, width=640, height=480)
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Tkinter main loop
root.mainloop()
