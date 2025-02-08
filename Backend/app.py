from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data['text']
        target_language = data['target_language']
        
        # Translate the text
        translated_text = translator.translate(text, dest=target_language).text

        # Convert translated text to speech
        tts = gTTS(text=translated_text, lang=target_language)
        audio_file = "static/output.mp3"
        tts.save(audio_file)

        return jsonify({'translated_text': translated_text, 'audio_url': audio_file})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
