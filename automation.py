import webbrowser
import subprocess
import pywhatkit
from speak import speak
from listener import listen


def execute(command):

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open chrome" in command:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome"

    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    elif "send whatsapp message" in command or "send message" in command:

        speak("Who should I send the message to?")
        name = listen()

        speak("What message should I send?")
        message = listen()

        contacts = {
            "rishika": "+919123107354",
            "shiv": "+919123456789"
        }

        if name in contacts:
            phone = contacts[name]
            pywhatkit.sendwhatmsg_instantly(phone, message)
            return "Sending WhatsApp message"

        else:
            return "Contact not found"

    return None