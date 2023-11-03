import requests
import json
import win32com.client as wincom
# import os


city = input("Enter the name of city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=a642ba80b034409fb8b113930230807&q={city}"

r = requests.get(url)
# print(r.text)

w_dict = json.loads(r.text)
w = w_dict["current"]["temp_c"]

text = f" The current weather in {city} is {w} degrees "
# os.system(text)
speak = wincom.Dispatch("SAPI.SpVoice")         # take syntax from internet as we use text to speech in python search on google
speak.Speak(text)