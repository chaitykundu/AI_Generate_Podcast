import os
import wave
from google import genai
from google.genai import types


def save_wave(filename: str, pcm_data: bytes, rate: int = 24000):
    """Utility to save PCM data as a .wav file."""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(pcm_data)


def generate_audio(script_text: str, language: str, topic: str) -> str:
    """
    Generates an audio file (WAV) using Gemini 2.5 Flash TTS model.
    
    Args:
        script_text (str): The text content to be converted to speech.
        language (str): The language name (for file naming).
        topic (str): The topic of the podcast (for file naming).

    Returns:
        str: The absolute path to the generated WAV file.
    """
    # ✅ Initialize Gemini client (ensure GOOGLE_API_KEY is set in .env)
    client = genai.Client()

    # ✅ Generate TTS audio
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=script_text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="achird"  # You can use "Artemis", "Fenrir", etc.
                    )
                )
            )
        ),
    )

    # ✅ Extract PCM audio data
    try:
        pcm_data = response.candidates[0].content.parts[0].inline_data.data
    except Exception as e:
        raise ValueError(f"❌ Failed to extract audio data: {e}")

    # ✅ Prepare output folder
    output_dir = os.path.join("podcasts")
    os.makedirs(output_dir, exist_ok=True)

    safe_topic = topic.strip().replace(" ", "_")
    file_path = os.path.join(output_dir, f"{safe_topic}_{language}.wav")

    # ✅ Save audio as WAV
    save_wave(file_path, pcm_data)
    print(f"✅ Podcast generated successfully: {file_path}")

    return os.path.abspath(file_path)
