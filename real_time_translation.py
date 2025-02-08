import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
import os
import time

# Manually defined list of supported languages (language code: language name)
SUPPORTED_LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}

# Initialize the translator
translator = Translator()

# Function to handle text-to-speech with gTTS and play it using pygame.mixer
import os
import time
from gtts import gTTS
import pygame

# Function to handle text-to-speech with gTTS and play it using pygame.mixer
def speak_translated_text_with_gtts(text, lang_code):
    try:
        # Create a unique filename by appending a timestamp (seconds) to the file name
        timestamp = int(time.time())  # Get the current time in seconds
        filename = f"translated_audio_{timestamp}.mp3"  # Unique filename based on the timestamp

        # Generate speech using gTTS and save it with the unique filename
        tts = gTTS(text=text, lang=lang_code)
        tts.save(filename)

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Load and play the audio file
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # After playback, stop the music
        pygame.mixer.music.stop()

        # Prompt to re-listen to the audio
        while True:
            user_input = input("Do you want to hear the translated speech again? (y/n): ").strip().lower()
            if user_input == 'y':
                pygame.mixer.music.load(filename)  # Reload the same file
                pygame.mixer.music.play()  # Play again
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.music.stop()
            elif user_input == 'n':
                print("Exiting playback.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Cleanup: Delete the audio file after the user is done listening
        os.remove(filename)

        # Quit the pygame mixer to free up resources
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error occurred while speaking the translated text: {e}")
        # Ensure cleanup happens even if an error occurs
        pygame.mixer.quit()
        if os.path.exists(filename):
            os.remove(filename)


# Function to recognize speech from the microphone
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Listen to the speech input from the user
    with mic as source:
        print("Listening for your speech... (You have 4 seconds)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4)
        print("Recognizing speech...")

    # Recognize speech using Google Web Speech API
    try:
        speech_text = recognizer.recognize_google(audio)
        print(f"You said: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

# Function to detect the language of the input text
def detect_language(text):
    detected_lang = translator.detect(text).lang
    return detected_lang

# Function to show supported languages and let the user select one
def display_supported_languages():
    print("\nSupported Languages for Translation (Language Name and Code):")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"{name.capitalize()} ({code})")

# Function to get the language code or name from the user
def get_language_code_from_user():
    display_supported_languages()
    user_input = input("\nEnter the language code or name of your choice: ").strip().lower()

    # Handle user input for both language code and name
    if user_input in SUPPORTED_LANGUAGES:
        return user_input
    else:
        # If the user entered a language name, try to find the corresponding code
        for code, name in SUPPORTED_LANGUAGES.items():
            if name.lower() == user_input:
                return code
        print("Language not supported.")
        return ""

# Function to translate the text to the selected language
def translate_text(text, source_lang, target_lang):
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text

# Main function to handle user input and translation
def main():
    print("Welcome to the real-time translation system!")

    # Ask for input format choice (Voice or Text)
    input_choice = input("Choose input format:\n1. Voice Input\n2. Text Input\nEnter 1 for voice or 2 for text: ")

    if input_choice == '1':
        # Voice input logic
        text = recognize_speech_from_microphone()
    elif input_choice == '2':
        # Text input logic
        text = input("Enter text to translate: ")

    if not text:
        print("No valid input detected. Exiting...")
        return

    # Detect the language of the input text
    detected_lang = detect_language(text)
    print(f"Detected Language: {detected_lang}")

    # Show supported languages for translation
    target_lang = get_language_code_from_user()

    if not target_lang:
        print("Invalid language code entered. Exiting...")
        return

    # Translate the text to the selected language
    translated_text = translate_text(text, detected_lang, target_lang)
    print(f"Translated Text: {translated_text}")

    # Speak the translated text
    speak_translated_text_with_gtts(translated_text, target_lang)

    # Ask if the user wants to hear the translated speech again
    while True:
        replay = input("Do you want to hear the translated speech again? (y/n): ")
        if replay.lower() == 'y':
            speak_translated_text_with_gtts(translated_text, target_lang)
        else:
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()  
