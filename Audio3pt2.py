import random

import pyttsx3

def setup_tts():



    try:
        engine = pyttsx3.init() # Works on macOS
        # Set speed and volume
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        return engine

    except Exception as e:

        print("Error initializing TTS:", e)

        return None

def speak(engine, text):

    """Speak the given text."""

    engine.say(text)

    engine.runAndWait()

def get_samples():

    """Returns a list of fun phrases."""

    return [

    "Hello! I am your computer!",

    "Python is awesome!",

    "This is AI speaking!",

    "Welcome to the future!",

    "Artificial Intelligence is amazing!",

    "Have a wonderful day!"

    ]

def main():

    print("🤖 AI VOICE LAB")

    print("================")

    engine = setup_tts()

    if engine is None:

        return

    print("✅ Voice ready! Type something.")

    print("Type 'sample' for a random phrase.")

    print("Type 'exit' to quit.\n")

    speak(engine, "Hello! Type something for me to say!")

    while True:

        text = input("👤 You: ").strip()

        if text.lower() == "exit":

            speak(engine, "Goodbye! Have a nice day.")

            break

        elif text.lower() == "sample":

            phrase = random.choice(get_samples())

            print("🤖", phrase)

            speak(engine, phrase)

        elif text != "":

            speak(engine, text)

        else:

            print("⚠ Please type something.")

    engine.stop()

if __name__ == "__main__":
    main()