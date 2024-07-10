import speech_recognition as speech 
import pyttsx3

# CREATING A RECOGNIZER OBJECT 
recognizer = speech.Recognizer()

while True :
    try :
        with speech.Microphone() as mic :
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_whisper(audio)
            text = text.lower()
            print(f"BOT : {text}")

    except speech.UnknownValueError() : 
        recognizer = speech.Recognizer()
        continue