# AI_Generate_Podcast
🎙️ AI Multilingual Podcast Generator

Generate 10–15 minute podcasts in any language using Google Gemini 2.5 Flash + TTS.
This project automatically creates a full podcast script and converts it into high-quality AI-generated speech, complete with background music and voice selection options.

✨ Features

✅ Multilingual Support — Generate podcasts in English, Spanish, Bengali, Hindi, French, Japanese, and more.
✅ AI Script Generation — Automatically creates 10–15 minute engaging podcast scripts using Gemini 2.5 Flash.
✅ Text-to-Speech (TTS) — Converts the script into natural human-like speech using Gemini 2.5 Flash Preview TTS.
✅ Voice Selection — Choose from multiple AI voices (Fenrir, Puck, Charon, Kore, Artemis, Achird).
✅ Background Music Mixing — Adds soft background music to make podcasts sound professional.
✅ Streamlit Frontend — Simple and beautiful web interface for users to enter topics and download podcasts.
✅ Automatic File Management — Generated podcasts are saved locally in /podcasts/.

🧠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	  Python
AI Model	Gemini 2.5 Flash + Flash TTS
Audio Mixing	PyDub (FFmpeg)
Environment Management	python-dotenv

🔑 Environment Setup

Create a .env file in the root folder and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/yourusername/podcast-ai-generator.git
cd podcast-ai-generator


2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate   # (Windows)


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Install FFmpeg

Download from https://www.gyan.dev/ffmpeg/builds/

Extract it to C:\ffmpeg\

Add C:\ffmpeg\bin to your PATH

Or manually set ffmpeg in code:

from pydub import AudioSegment
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"

🚀 Run the App
streamlit run src/app.py


Then open the browser link (usually http://localhost:8501) to access your app.

🎧 How It Works

1️⃣ Enter a podcast topic and select a language.
2️⃣ The AI generates a 10–15 minute podcast script using Gemini 2.5 Flash.
3️⃣ Select your preferred voice (e.g. Fenrir, Puck, Artemis).
4️⃣ The system converts the script to speech using Gemini 2.5 Flash TTS.
5️⃣ Background music is added for a professional sound.
6️⃣ Download your final MP3 podcast.
