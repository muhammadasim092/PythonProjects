# main.py
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        say("Sorry, can you say again?")
        return ""

if __name__ == "__main__": 
    while True:
        query = takeCommand()
        
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand()
                
                if "go to sleep" in query:
                    say("Ok sir, I will sleep now")
                    break
                
                elif "hello" in query:
                    say("Hello sir, how are you today?")
                
                elif "i am fine" in query:
                    say("That's great sir, I am glad to hear that.")    
                
                elif "how are you" in query:
                    say("I am good sir, thanks for asking.")
                
                elif "what is your name" in query:
                    say("My name is Asim's AI sir, I am your personal assistant.")
                
                
                
                
                elif "google" in query:
                    from searchEngines import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchEngines import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchEngines import searchWikipedia
                    searchWikipedia(query)
                    
                    
                    
                    
                elif "temperature" in query:
                    search = "temperature in Gujrat"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    say(f"current{search} is {temp}")
                    
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    say(f"current{search} is {temp}")
                
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    say(f"Sir, the time is {strTime}")
                    
                elif "Good Bye" in query:
                    say("Going to sleep,sir")
                    exit()
