import pyttsx3
import datetime
import os 



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            say("Alarm ringing,sir")
            os.startfile("D:\Introduction to Programming with Python\PythonProjects\Asims_Ai\music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)