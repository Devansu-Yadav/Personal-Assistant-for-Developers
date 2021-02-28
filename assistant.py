import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # Taking voice commands from user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......")
        r.pause_threshold = 1.5   # No of seconds of non-speaking audio after which a phrase is considered.
        r.energy_threshold = 400
        audio = r.listen(source) #Listen audio from source which is a an input voice stream 
    
    try:
        print("Recognizing .....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    
    except Exception as e:
        print(e)
        print("Can you say that agin please......")
        return "None"
    
    return query


def process():
    speak('I am Bot')
    while True:
        query = takeCommand().lower()
        # Tasks to execute using this query
        if "wikipedia" in query:
            speak("Searching Wikipedia.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play music" in query:
            # Something will be done
            pass
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
        
        elif "open vs code" in query:
            code_path = 'C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)
