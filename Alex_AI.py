# //////  Modules Required  ////
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser as wb

# //////  Initialising Speech instance  ////
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)

# //////  Creating Speak Function  ////
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# //////  Creating a wish me function  ////
def wish_me():
    time=datetime.datetime.now()
    if time.hour>=00 and time.hour<12:
        speak("Good Morning Sir")
    elif time.hour>=12 and time.hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir ")
    speak('I am Alex sir how may i help you')

# //////  Function to take commands that are to be performed  ////
def take_command():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        rec.pause_threshold = 1
        print('Listening........')
        audio=rec.listen(source)
        try:
            query = rec.recognize_google(audio, language='en-in')
            print('Recognizing......')
            print(f'User Said : {query}')
        except Exception as e:
            print("Unable to understand,please say that again")
            return 'None'
    return query

# //////  An infinite loop to performance tasks  ////
count=0
wish_me()
while(count<3):
    query=take_command().lower()
    if 'stop' in query:
        break
    elif query=='none':
        count+=1
    elif query!='none':
        count=0
        if 'who are you' in query:
            speak('My name is Alex sir')
        elif 'time' in query:
            time=datetime.datetime.now()
            Time=datetime.time(time.hour,time.minute)
            speak(Time)
        elif 'wikipedia' in query:
            speak('searching wikipedia......')
            query=query.replace('wikipedia','')
            try:
                result=wikipedia.summary(query,sentences=3)
                speak('According to wikipedia....')
                speak(result)
            except Exception as e:
                print(f"Unable to find about {query} in wikipedia")
        elif 'open google' in query:
            wb.open('http://www.google.com')
        elif 'youtube' in query:
            if 'codewithharry' in query:
                wb.open('http://www.youtube.com/codewithharry')
            else:
                wb.open('http://www.youtube.com')
        elif 'facebook' in query:
            wb.open('http://www.facebook.com')
        elif 'whatsapp' in query:
            wb.open('https://web.whatsapp.com/')
        elif 'instagram' in query:
            wb.open('https://www.instagram.com/')
        elif 'open code blocks' in query:
            path = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(path)
        elif 'open visual studio code' in query:
            path="C:\\Users\\nikhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
speak("Thank you sir signing off")