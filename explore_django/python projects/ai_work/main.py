import speech_recognition as sr
import os
import win32com.client as wincom

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1           # pause_thresold provides a virtual environment to us
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query

if __name__ == '__main__':
    print('vscode')
    text = f"Hello I am Jarvis AI"
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.speak(text)
    print("Listening...")
    txt = takeCommand()
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.speak(txt)