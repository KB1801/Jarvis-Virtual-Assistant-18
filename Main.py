import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import difflib
import os
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
newsapi = "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"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def processcommand(command):
    command = command.lower()
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com")  
    elif "open instagram" in command:
        speak("Opening insta")  
        webbrowser.open("https://www.instagram.com")  
    elif command.lower().startswith("play"):
        song = command.lower().replace("play", "").strip()
        matches = difflib.get_close_matches(song, musiclibrary.music.keys(), n=1, cutoff=0.6)
        if matches:
            best_match = matches[0]
            speak(f"Playing {best_match}")
            webbrowser.open(musiclibrary.music[best_match])
        else:
            speak(f"Sorry, I don’t know the song {song}")

    elif "news" in command: 
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()    

            articles = data.get('articles',[])

            if not articles:
                speak("Sorry, I couldn't find any news right now.")
            else:
                for article in articles[:5]:  # read only first 5
                    title = article.get("title", "No title available")
                    speak(title)
                    print(title)
        else:
            speak("Sorry, I couldn't fetch the news.")    

    else:    
        # let Openai handle the request
        pass

    
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        

         

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening!!")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("You said:", word)
            if(word.lower() == "jarvis"):
                speak("Yes, Kartik")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))

    


