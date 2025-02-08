import time
import speech_recognition as sr
from googletrans import Translator

# Recognize speech from the microphone
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized Speech: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Sorry, the speech service is down.")
        return None

# Translate text to selected language
def translate_text(text, target_language):
    translator = Translator()
    start_time = time.time()
    translated = translator.translate(text, dest=target_language)
    latency = time.time() - start_time
    return translated.text, latency

def main():
    print("Welcome to the real-time translation system!")
    print("Choose input format:")
    print("1. Voice Input")
    print("2. Text Input")
    input_choice = input("Enter 1 for voice or 2 for text: ")

    if input_choice == '1':
        recognized_text = recognize_speech_from_microphone()
        if recognized_text:
            text_to_translate = recognized_text
    elif input_choice == '2':
        text_to_translate = input("Enter text to translate: ")
    else:
        print("Invalid choice, exiting...")
        return

    # Language selection
    language_options = {
        '1': ('en', 'English'),
        '2': ('es', 'Spanish'),
        '3': ('fr', 'French'),
        '4': ('de', 'German'),
        '5': ('it', 'Italian'),
        '6': ('hi', 'Hindi'),
        '7': ('zh-CN', 'Chinese'),
        '8': ('ja', 'Japanese'),
        '9': ('kn', 'Kannada'),
        '10': ('te', 'Telugu'),
        '11': ('ta', 'Tamil'),
        '12': ('ml', 'Malayalam')
    }

    print("\nChoose the target language:")
    for key, (code, name) in language_options.items():
        print(f"{key}. {name}")

    language_choice = input("Enter the number corresponding to the target language: ")

    if language_choice not in language_options:
        print("Invalid language choice, exiting...")
        return

    target_language_code, target_language_name = language_options[language_choice]

    # Translate the text to the selected language
    translated_text, latency = translate_text(text_to_translate, target_language_code)

    # Display translation and latency
    print(f"\nTranslated Text in {target_language_name}: {translated_text}")
    print(f"Latency for translation: {latency:.2f} seconds")

if __name__ == "__main__":
    main()
