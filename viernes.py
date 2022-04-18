
import speech_recognition as sr
import pyttsx3 as tt

listener = sr.Recognizer()
engine = tt.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices=[1].id)

engine.say("Buenos días")

try:
    with sr.Microphone() as source:
        print("Escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
except:
    pass