import json
import requests
import win32com.client as wincom

city = input("Enter city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=a642ba80b034409fb8b113930230807&q={city}"

r = requests.get(url)
new_dict = json.loads(r.text)

condition = new_dict["current"]["condition"]["text"]
text = f"The weather condition of {city} is {condition}"
print(text)
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(text)