import streamlit as st
from services.gemini_text import generate_script
from services.tts import generate_audio

from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="🎙️ AI Multilingual Podcast Generator", layout="wide")
st.title("🎧 AI Multilingual Podcast Generator")

st.markdown("Generate 10–15 minute podcasts in any language using Gemini 2.5 + Flash TTS.")

topic = st.text_input("🎯 Enter Podcast Topic:")
language = st.selectbox("🌍 Select Language:", 
    ["English","Spanish","French","German","Hindi","Bengali","Japanese","Korean"])

if st.button("🎙️ Generate Podcast"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("🧠 Generating Podcast Script..."):
            script = generate_script(topic, language)

        st.success("✅ Script Generated Successfully!")
        st.subheader("📝 Podcast Script")
        st.write(script)

        with st.spinner("🎤 Generating Audio..."):
            audio_path = generate_audio(script, language, topic)

        st.audio(audio_path, format="audio/mp3")
        st.download_button("⬇️ Download Podcast", open(audio_path, "rb"), file_name=audio_path)
