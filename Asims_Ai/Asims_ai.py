import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyboard
import speedtest



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
    
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

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
                
                elif "pause" in query:
                    pyautogui.press("k")
                    say("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    say("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    say("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    say("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard  import volumedown
                    say("Turning volume down, sir")
                    volumedown()
                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                    
                elif "shutdown the system" in query:
                    say("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    say(f"Wifi download speed is {download_net}")
                    say(f"Wifi Upload speed is {upload_net}")
    
                elif "google" in query:
                    from searchEngines import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchEngines import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchEngines import searchWikipedia
                    searchWikipedia(query)
                    
                    
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    say ("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    say("Done,sir")   
                                    
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
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    say("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    say("You told me " + remember.read()) 
