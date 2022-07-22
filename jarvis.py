import pyttsx3 #for audio
import datetime
import speech_recognition as sr


engine = pyttsx3.init("sapi5")  #sapi5 is used for opening audio
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[1].id) #helps in selection audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morling")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may i help you")

def takecommand():
    ''' '''
    r= sr.Recognizer() #helps in recognising the voice
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio= r.listen(source)

    try:# used if erro occur .. mainly error handling
        print("Reconising....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that agin please")
        return "None"
    return query


#
speak("hello shiv")
takecommand()