import speech_recognition as sr
from translate import Translator
import gtts
import pyttsx3
# from playsound import playsound
translator= Translator(to_lang="es")
r = sr.Recognizer()

with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source,duration=1) 
    print("say something")
    audio = r.listen(source)       
try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
    translation = translator.translate(text)
    print("translated :",translation)
    text = r.recognize_google(audio)

    # tts = gtts.gTTS(translation)
    # tts.save("hola.mp3")
    # playsound("hola.mp3")
    engine = pyttsx3.init()
    text = "Python is a great programming language"
    engine.say(text)
    engine.runAndWait()
except:
    print("Sorry could not recognize your voice")