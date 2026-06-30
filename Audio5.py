import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.9)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print("API error: ",e)

    return ""

def respond_to_commands(command):
    if "Hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "your name" in command:
        speak("I am your AI assistant.")
    elif "exit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I do not know how to respond to that.")

def main():
    speak("Voice assistant is ready. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_commands(command):
            break

if __name__ == "__main__":
    main()
    