# Made By Dhyey Dave
# We first import all the modules and libraries required

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):  # This function enables to speak audio
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # This function enables enables the A.I to wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis A.I. How may I help")


def takeCommand():  # This function takes the command from the user and either recognizes and returns the word or tries again
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__ == '__main__':  # We put all the functions and give results based on the keyword said by user
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open dps' in query:
            webbrowser.open("website.dpssharjah.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\dhyey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)