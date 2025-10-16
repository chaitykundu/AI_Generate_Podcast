import google.generativeai as genai
import base64, os

def generate_audio(script_text: str, language: str, topic: str) -> str:
    model = genai.GenerativeModel("models/gemini-2.5-flash-tts")
    response = model.generate_content(
        [script_text],
        generation_config={"response_mime_type": "audio/mpeg"}
    )

    audio_bytes = base64.b64decode(response.candidates[0].content[0].binary)
    os.makedirs("src/outputs/podcasts", exist_ok=True)
    file_path = f"src/outputs/podcasts/{topic.replace(' ', '_')}_{language}.mp3"

    with open(file_path, "wb") as f:
        f.write(audio_bytes)
    return file_path
