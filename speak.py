import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 165)
engine.setProperty('volume', 1)

def speak(text):
    if not text:
        return

    text = str(text)

    print("Jarvis:", text)

    engine.stop()
    engine.say(text)
    engine.runAndWait()