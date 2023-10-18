import speech_recognition as sr
from googletrans import Translator
from langdetect import detect
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recognizing...")

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return ""

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"  # Default to English if language detection fails

def start_translation(selected_language):
    recognized_text = recognize_speech()
    if recognized_text:
        detected_language = detect_language(recognized_text)
        print(f"Detected Language: {detected_language}")
        
        if selected_language == "English":
            target_language_code = "en"
            voice_language = "en-us"
        elif selected_language == "French":
            target_language_code = "fr"
            voice_language = "fr-fr"
        elif selected_language == "Hindi":
            target_language_code = "hi"
            voice_language = "hi-IN"
        elif selected_language == "Italian":
            target_language_code = "it"
            voice_language = "it-IT"
        elif selected_language == "German":
            target_language_code = "it"
            voice_language = "it-IT"

        # Add more language cases as needed
        
        translated_text = translate_text(recognized_text, target_language_code)
        print(f"Translated text: {translated_text}")

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Set voice properties for Hindi and Marathi
        engine.setProperty('voice', voice_language)
        
        engine.say(translated_text)
        engine.runAndWait()

if __name__ == "__main__":
    print("Select the target language:")
    print("1. English")
    print("2. French")
    print("3. Hindi")
    print("4. Italian")
    print("5. German")
    # Add more language options as needed
    
    choice = input("Enter the number corresponding to your choice: ")
    
    if choice == "1":
        selected_language = "English"
    elif choice == "2":
        selected_language = "French"
    elif choice == "3":
        selected_language = "Hindi"
    elif choice == "4":
        selected_language = "Italian"
    elif choice == "5":
        selected_language = "German"
    # Add more language cases as needed
    
    start_translation(selected_language)
