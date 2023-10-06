import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    
    try:
        print("Wait for Few Moments...")
        
        query=r.recognize_google(audio, language='en-in')
        print(f"You just said:{query}\n")
        
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query=""
    return query    

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning BOSS")
        speak("Good Morining BOSS")
    elif hour>=12 and hour<17:
        print("Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour>=17 and hour<21:
        print("Good Evening BOSS")
        speak("Good Evening BOSS") 
    else:
        print("Good Night BOSS")
        speak("Good Night BOSS")     
        
if __name__ =="__main__":
    wishings()
    query=commands().lower()  
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir,the time is {strTime}")
        
    elif 'Open microsoft' in query:
        speak("Opening Microsoft edge Application sir...")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        
    elif 'wikipedia'in query:
        speak("searching in Wikipedia...")
        try:
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
        except:
            speak("No results found..")
            print("No results found..")
            
            
    elif 'play'in query:
        query=query.replace('play','')
        speak('playing '+ query)
        pywhatkit.playonyt(query)
                
    elif 'type'in query:
        speak("Please tell me what should i write")
        
        while True:
            
            writeInNotepad=commands()
            if writeInNotepad=='exit typing':
                speak("Done sir")
            else:
                pyautogui.write(writeInNotepad)  
                
    elif 'joke'in query:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)   
            
    elif 'exit program' in query:
        speak("I'm Leaving Sir, BYE!")
        quit()                        
                    