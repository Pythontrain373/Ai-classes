import speech_recognition as sr

import pyttsx3

from googletrans import Translator 
def speak(text, language='en'): 
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)
    voices=engine.getProperty('voices')
    if language == 'en':
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)  

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English...")
        audio=recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text=recognizer.recognize_google(audio, language='en-US')
        print("You said :", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def display_language_options():
    print("Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Bengali (bn)")
    print("4. Urdu (ur)")
    print("5. Punjabi (pa)")
    print("6. Gujarati (gu)")
    print("7. Marathi (mr)")
    print("8. Telugu (te)")

    choice=input("Enter the number corresponding to your choice (1-8): ")

    language_dict={
        '1': 'hi',
        '2': 'ta',
        '3': 'bn',
        '4': 'ur',
        '5': 'pa',
        '6': 'gu',
        '7': 'mr',
        '8': 'te'
    }

    return language_dict.get(choice, 'es')

def main():
    target_language=display_language_options()
    orginal_text=speech_to_text()
    if orginal_text:
        translated_text=translate_text(orginal_text, target_language)
        speak(translated_text, target_language="en")
        print("Translation spoken out")

if __name__=="__main__":
    main()