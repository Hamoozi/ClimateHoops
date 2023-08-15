import tkinter as tk
import requests
import time
import os
from tkVideoPlayer import TkinterVideo



#Loops through cities entered and displays them on GUI
#Will add option for images
def getWeather(canvas):
    #city = textField.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?appid=API&q=Amherst"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))


    final_info = condition + "\nTemperature: " + str(temp) + "°C" 
    final_data = "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + \
    "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    if wind < 2:
        videoplayer.load(r"basket.gif")
        videoplayer.pack(expand=True)
    else:
        videoplayer.load(r"home.gif")
        videoplayer.pack(expand=True, fill="both")
        


root = tk.Tk()


videoplayer = TkinterVideo(master=root, scaled=True)
getWeather(videoplayer)

videoplayer.play() # play the video

root.mainloop()