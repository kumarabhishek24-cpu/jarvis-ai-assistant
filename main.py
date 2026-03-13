from listener import listen
from speak import speak
from automation import execute
from brain import ask_ai

speak("Jarvis activated")

while True:

    command = listen()

    if not command:
        continue

    command = command.lower()

    result = execute(command)

    if result is not None:
        speak(result)

    else:
        answer = ask_ai(command)

        if answer:
            speak(answer)

    if "stop" in command or "exit" in command:
        speak("Goodbye")
        break