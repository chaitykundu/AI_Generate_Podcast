import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_script(topic: str, language: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    You are a podcast host. Write an engaging 10–15 minute script (~1800–2000 words)
    in {language} about "{topic}" with intro, 3–4 sections, and closing summary.
    """
    response = model.generate_content(prompt)
    return response.text
