from tkinter import *
import requests

root = Tk()
root.title("SunBreaker : Weather Application")
root.geometry('500x400')
root.configure(background = "powderblue")

#Defining Early Variables
global theWeather, theDescription, theTemperature
theWeather =  StringVar()
theDescription = StringVar()
theTemperature = IntVar()

# Making Frames
titleFrame = Frame(root, width = 500, height = 100, relief = "raise", bg = "powderblue")
titleFrame.pack(side = TOP)

inputFrame = Frame(root, width = 500, height = 100, relief = "raise", bg = "powderblue")
inputFrame.pack(side = TOP)

detailFrame = Frame(root, width = 500, height = 200, relief = "raise", bg = "powderblue")
detailFrame.pack(side = TOP)


### MAIN PROGRAMMING FOR THE WEATHER API ###

def thisClimate(event):
    address =  "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    place = location.get().title()

    url = address + place

    data = requests.get(url).json()

    getWeather = data['weather'][0]['main'].title()
    getDescription = data['weather'][0]['description'].title()
    getTemperature = data['main']['temp']

    temp_in_celsius = getTemperature - 273.15

    theWeather.set(getWeather)
    theDescription.set(getDescription)
    theTemperature.set(str(temp_in_celsius) + " °C")

### END OF PROGRAMMING FOR THE WEATHER API ###


# Adding items to titleFrame
title = Label(titleFrame, text = "SunBreaker", font = ("Arial", 48), fg = "orange", bg = "powderblue")
title.grid(row = 0, column = 0)

# Adding items to the inputFrame
global location
location = Entry(inputFrame, bd = 5, width = 20, font = "Arial 18")
location.grid(row = 0, column = 0)
location.insert(0, "Enter Location")

# Adding items to the detail Frame
spacer = Label(detailFrame, text ='', height = 5, bg = "powderblue")
spacer.grid(row = 0, column = 0)

weather = Entry(detailFrame, textvariable = theWeather, bd = 2, width = 20, font = "Arial 18", fg = "gray48")
weather.grid(row = 1, column = 0, pady = 10)
weather.insert(0, "Weather Display")

description = Entry(detailFrame, textvariable = theDescription, bd = 2, width = 20, font = "Arial 18", fg = "gray48")
description.grid(row = 2, column = 0, pady = 10)
description.insert(0, "Description Display")

temperature = Entry(detailFrame, textvariable = theTemperature, bd = 2, width = 20, font = "Arial 18", fg = "gray48")
temperature.grid(row = 3, column = 0, pady = 10)
temperature.insert(0, "Temperature Display")

root.bind('<Return>', thisClimate)

root.mainloop()
