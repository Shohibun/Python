import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Jack")

MASTER = "Shohibun"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#Speak
def Speak(text):
    engine.say(text)
    engine.runAndWait()

#Function 
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        Speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        Speak("good Afternoon" + MASTER)
    else:
        Speak("Good Evening" + MASTER)
        Speak("")

#Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please....")
        query = None

    return query

#Main Start Here
Speak("Hello my name is Jack, I can help you!")
wishMe()
query = takeCommand()

def menu():
    if "wikipedia" in query.lower():
        to_wikipedia()
    elif "open youtube" in query.lower():
        to_youtube()
    elif "open google" in query.lower():
        to_google()
    elif "play music" in query.lower():
        to_music()
    elif "the time" in query.lower():
        to_thetime()
    elif "Thank you Jack" in query.lower():
        to_exit()
    else:
        back_to_menu()

def back_to_menu():
    menu()

def to_wikipedia():
    Speak("searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    Speak(results)
    back_to_menu()

def to_youtube():
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    back_to_menu()

def to_google():
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    back_to_menu()

def to_music():
    songs_dir = "C:\\Users\\User\\Music\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
    back_to_menu()

def to_thetime():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(f"{MASTER} the time is {strtime}")
    back_to_menu()

def to_exit():
    Speak("You are welcome sir")

if __name__ == "__main__":
    menu()
