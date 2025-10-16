import google.generativeai as genai, os, base64
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

text = "Hello! This is a test podcast in English."
model = genai.GenerativeModel("models/gemini-2.0-flash-tts")

response = model.generate_content(
    [text],
    generation_config={"response_mime_type": "audio/mpeg"}
)

audio_data = base64.b64decode(response.candidates[0].content[0].binary)
with open("test.mp3", "wb") as f:
    f.write(audio_data)

print("✅ Generated test.mp3 successfully")
