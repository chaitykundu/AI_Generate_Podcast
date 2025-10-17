from pydub import AudioSegment
import os

def mix_with_background(speech_path: str, music_path: str, output_path: str, music_volume_db: float = -15):
    """
    Mixes a voice/speech audio file with background music.

    Args:
        speech_path (str): Path to the speech audio file (WAV or MP3).
        music_path (str): Path to the background music file.
        output_path (str): Path to save the final mixed audio.
        music_volume_db (float): Volume reduction in dB for background music.

    Returns:
        str: The path to the mixed audio file.
    """

     # ✅ Add this so Pydub always knows where ffmpeg is
    AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
    AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
    AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"
    
    # Load both audio files
    speech = AudioSegment.from_file(speech_path)
    music = AudioSegment.from_file(music_path)

    # Match duration (loop or trim the background)
    if len(music) < len(speech):
        loops = int(len(speech) / len(music)) + 1
        music = music * loops
    music = music[:len(speech)]

    # Lower background music volume
    music = music + music_volume_db  # reduce volume (negative dB)

    # Mix tracks together
    combined = music.overlay(speech)

    # Export mixed result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    combined.export(output_path, format="mp3")

    print(f"✅ Mixed audio saved: {output_path}")
    return output_path
