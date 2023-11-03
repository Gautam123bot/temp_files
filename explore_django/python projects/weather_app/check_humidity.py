import requests
import json
import win32com.client as wincom

city = input("Enter city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=a642ba80b034409fb8b113930230807&q={city}"

r = requests.get(url)
newdict = json.loads(r.text)
h = newdict["current"]["humidity"]

text = f"Current Humidity in {city} is {h}"

speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(text)