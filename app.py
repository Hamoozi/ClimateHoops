import tkinter as tk
import requests
import time
import os
from dotenv import load_dotenv

#Hides API key for safety
def configure():
    load_dotenv()

def getWeather(canvas):
    configure()
    city = textField.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('apikey')}"

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


    if wind > 5:
        label3.config(text = "Weather not optimable for Basketball")
    else:
        label3.config(text = "Go shoot some hoops")


    final_info = condition + "\nTemperature: " + str(temp) + "°C" 
    final_data = "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + \
    "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    

    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 15, "bold")
z = ("poppins", 20, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
label3 = tk.Label(canvas, font=z)
label3.pack()
canvas.mainloop()