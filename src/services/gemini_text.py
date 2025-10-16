import os
import google.generativeai as genai

# ✅ Configure Gemini API key once
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_script(topic: str, language: str) -> str:
    """
    Generates a podcast script (~1800–2000 words) using the Gemini model.

    Args:
        topic (str): The podcast topic or theme.
        language (str): The target language (e.g., 'English', 'Spanish').

    Returns:
        str: The generated podcast script text.
    """
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are a professional podcast host and storyteller.
    Write a compelling, 10–15 minute podcast script (around 1800–2000 words)
    in {language} about the topic: "{topic}".

    The script should include:
    1. An engaging introduction to hook listeners.
    2. 3–4 well-structured sections that explore different aspects of the topic.
    3. A conclusion that summarizes the key insights and ends memorably.
    4. Natural spoken tone (like a conversation).
    5. Avoid bullet points — write in flowing paragraphs.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Error generating script: {e}")
        return ""
