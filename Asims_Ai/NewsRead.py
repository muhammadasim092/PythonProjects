import requests
import json
import pyttsx3



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=47bcff6d011049a482048087b132da52",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=47bcff6d011049a482048087b132da52",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=47bcff6d011049a482048087b132da52",
            "science" :"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=47bcff6d011049a482048087b132da52",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=47bcff6d011049a482048087b132da52",
            "technology" :"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=47bcff6d011049a482048087b132da52"
}

    content = None
    url = None
    say("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    say("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        say(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    say("thats all")