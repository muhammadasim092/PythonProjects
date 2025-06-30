# Asim AI Voice Assistant
from time import strftime

# for voice speech_recognition
import speech_recognition as sr

# for speak lib
import pyttsx3

import webbrowser

import openai

import os

import datetime

from pyexpat import features


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"User said: {query}")
            say(query)
            return query
        except Exception:
            say("Sorry, can you speak again?")
            return ""


if __name__ == '__main__':
    say("Hello, I am Asim's AI")

    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.org"],["facebook", "https://www.facebook.com"],["google", "https://www.google.com"],["instagram", "https://www.instagram.com"], ]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} in your browser")
                webbrowser.open(site[1])

            # todo: open custom photo from your computer

            if "open photo" in query.lower():
                photoPath = r"D:\____2023-12-29_12822847488.jpg"
                say("Opening your photo")
                os.startfile(photoPath)

            # todo: add features to open video


            if "open video" in query.lower():
                videoPath = r"D:\dilmarapashkru.mp4"
                say("Opening your Video")
                os.startfile(videoPath)

            # todo: add features to open time


            if "the time" in query.lower():
                # videoPath = r"D:\dilmarapashkru.mp4"
                strfTime = datetime.datetime.now().strftime("%I:%M %S")
                say( f"Opening your time {strfTime}")

            # todo: add features to open notepad

            if "open notepad" in query.lower():
                say("Opening notepad")
                notepad_path = r"C:\Windows\System32\notepad.exe"
                os.startfile(notepad_path)

            # todo: add features to open whatsapp
            if "open whatsapp" in query.lower():
                os.system("start whatsapp:")

            elif "exit" in query.lower() or "quit" in query.lower():
                say("Goodbye!")
                break
