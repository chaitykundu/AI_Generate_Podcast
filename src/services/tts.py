import os
import wave
from google import genai
from google.genai import types
from services.utils import mix_with_background


def save_wave(filename: str, pcm_data: bytes, rate: int = 24000):
    """Save PCM data as a .wav file."""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(pcm_data)


def generate_audio(script_text: str, language: str, topic: str) -> str:
    """
    Generates podcast audio using Gemini 2.5 Flash Preview TTS,
    and mixes it with background music.
    """
    client = genai.Client()

    print("🎙️ Generating TTS with Gemini 2.5 Flash Preview...")

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=script_text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Puck")
                )
            ),
        ),
    )

    # ✅ Defensive extraction
    if not response.candidates:
        raise ValueError("❌ No candidates returned — check your API key and model access.")

    candidate = response.candidates[0]
    if not candidate.content or not getattr(candidate.content, "parts", None):
        raise ValueError(
            f"❌ No audio returned — got: {candidate.finish_reason or 'unknown reason'}"
        )

    audio_part = next(
        (p for p in candidate.content.parts if getattr(p, "inline_data", None)), None
    )
    if not audio_part:
        raise ValueError("❌ No inline audio data found in the response.")

    pcm_data = audio_part.inline_data.data

    # ✅ Save the audio as WAV
    output_dir = os.path.join("podcasts")
    os.makedirs(output_dir, exist_ok=True)
    safe_topic = topic.strip().replace(" ", "_")
    speech_path = os.path.join(output_dir, f"{safe_topic}_{language}.wav")

    save_wave(speech_path, pcm_data)
    print(f"✅ Raw speech saved: {speech_path}")

    # ✅ Mix with background
    music_path = os.path.join("assets", "music", "background1.mp3")
    output_path = speech_path.replace(".wav", "_with_music.mp3")
    final_path = mix_with_background(speech_path, music_path, output_path, music_volume_db=-15)

    print(f"✅ Final podcast (with music): {final_path}")
    return os.path.abspath(final_path)
