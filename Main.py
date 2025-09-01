import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("ya")
        except Exception as e:
            print("Error; {0}".format(e))

