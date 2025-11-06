import streamlit as st
from services.gemini_text import generate_script
from services.tts import generate_audio

from dotenv import load_dotenv
import google.generativeai as genai
import os

# 🌿 Load environment variables
load_dotenv()

# 🔐 Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🎨 Streamlit UI setup
st.set_page_config(page_title="🎙️ AI Multilingual Podcast Generator", layout="wide")
st.title("🎧 AI Multilingual Podcast Generator")

st.markdown("""
Generate **10–15 minute podcasts** in your preferred language using **Gemini 2.5 Flash + TTS**.
""")

# 🎯 User input
topic = st.text_input("🎯 Enter Podcast Topic:")
language = st.selectbox(
    "🌍 Select Language:",
    ["English", "Spanish", "French", "German", "Hindi", "Bengali", "Japanese", "Korean"]
)

voice_name = st.selectbox("🗣️ Choose Voice:",
                          ["Fenrir", "Puck", "Charon", "Kore", "Artemis", "Achird"])

# 🎙️ Generate button
if st.button("🎙️ Generate Podcast"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic before generating.")
    else:
        try:
            # 🧠 Step 1: Generate script
            with st.spinner("🧠 Generating Podcast Script..."):
                script = generate_script(topic, language)

            if not script:
                st.error("❌ Script generation failed. Please try again.")
            else:
                st.success("✅ Script Generated Successfully!")
                st.subheader("📝 Podcast Script")
                st.text_area("Generated Script", script, height=300)

                # 🎤 Step 2: Generate audio
                with st.spinner("🎤 Generating Audio..."):
                    audio_path = generate_audio(script, language, topic, voice_name)

                if os.path.exists(audio_path):
                    st.audio(audio_path, format="audio/mp3")
                    with open(audio_path, "rb") as audio_file:
                        st.download_button(
                            "⬇️ Download Podcast",
                            data=audio_file,
                            file_name=os.path.basename(audio_path),
                            mime="audio/mpeg"
                        )
                    st.success("🎧 Podcast ready for playback and download!")
                else:
                    st.error("❌ Audio generation failed. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")