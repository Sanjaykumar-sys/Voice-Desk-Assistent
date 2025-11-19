import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet.")
        return ""

def perform_task(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don't know how to do that yet.")

def main():
    speak("Hello! I am your desk assistant. How can I help you?")
    while True:
        command = listen_command()
        if command:
            perform_task(command)

if __name__ == "__main__":
    main()
    
