# Real-Time Language Translation using NMT: Bridging Language Barriers

This project performs **real-time translation of speech and text** using Neural Machine Translation (NMT). It enables users to communicate across languages using speech recognition, Google Translate, and speech synthesis.

## 🚀 Features

- 🎤 Real-Time **Speech Recognition** (Terminal)
- 📝 **Text Input** (Terminal + Web)
- 🔁 **Translation** using `googletrans` + NMT (`nmt_model.keras`)
- 🗣️ **Speech Output** via `gTTS` and `pygame`
- 💻 Web Interface using **Flask**
- ⚙️ **Built entirely using**: Python IDLE, CMD Prompt, Notepad, and Chrome — no IDEs!

## ⚙️ Input/Output Capabilities

| Mode          | Input Type       | Output Type             |
|---------------|------------------|-------------------------|
| **Terminal**  | ✅ Speech, ✅ Text | ✅ Text, ✅ Speech  |
| **Web App**   | ❌ Speech, ✅ Text | ✅ Text, ✅ Speech  |
--------------------------------------------------------------

## Tech Stack / Libraries Used
- **Python Libraries:** PyAudio, SpeechRecognition, gTTS, Pygame, Flask, os, sys, datetime, TensorFlow, Keras, numpy  
- **APIs:** Google Web Speech API, Google Translate API  
- **Frontend:** HTML, CSS  
- **Tools:** Python IDLE, Notepad, Chrome, CMD Prompt


## Setup Instructions

1. **Clone the repository:**  
  git clone https://github.com/Umakant051/Real_Time_Translation.git

2. Navigate to the project folder and create a virtual environment
  cd Real_Time_Translation
  python -m venv env

3. Activate the virtual environment: 
  env\Scripts\activate   # For Windows
  source env/bin/activate   # For Linux/Mac

4. Install the required dependencies: 
  pip install -r requirements.txt

5. Run Terminal (CMD) Mode: 
  python real_time_translation.py

6. Run Web Interface Mode: 
  cd Backend
  python app.py

      Open http://127.0.0.1:5000/ in a browser


## 🛠️ Requirements
Install all dependencies with:
```bash
pip install -r requirements.txt
