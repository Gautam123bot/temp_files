import os
import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1")
    while True:
        x = input("Enter what you want me to speak: ")
        if x=='q':
            break
        # command = f"echo {x}"
        # os.system(command)

        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)