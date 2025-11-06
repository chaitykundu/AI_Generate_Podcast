# app.py
from flask import Flask, request, jsonify, send_file, render_template_string
import os
from services.gemini_text import generate_script
from services.tts import generate_audio

app = Flask(__name__)

# ----------------------
# Root page with a simple form for testing
# ----------------------
@app.route("/", methods=["GET"])
def index():
    html = """
    <h1>🎧 AI Podcast Generator</h1>
    <form method="POST" action="/generate_audio_form">
        Topic: <input type="text" name="topic" required><br>
        Language: <input type="text" name="language" value="English"><br>
        Voice: <input type="text" name="voice_name" value="Fenrir"><br>
        <input type="submit" value="Generate Podcast">
    </form>
    """
    return render_template_string(html)

@app.route("/generate_audio_form", methods=["POST"])
def generate_audio_form():
    topic = request.form.get("topic")
    language = request.form.get("language", "English")
    voice_name = request.form.get("voice_name", "Fenrir")

    try:
        script = generate_script(topic, language)
        audio_path = generate_audio(script, language, topic, voice_name)
        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        return f"❌ Error: {e}", 500

# ----------------------
# API: Generate script (JSON)
# ----------------------
@app.route("/generate_script", methods=["POST"])
def generate_script_route():
    data = request.json
    topic = data.get("topic")
    language = data.get("language", "English")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    try:
        script = generate_script(topic, language)
        return jsonify({"script": script})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# API: Generate audio (JSON)
# ----------------------
@app.route("/generate_audio", methods=["POST"])
def generate_audio_route():
    data = request.json
    script = data.get("script")
    language = data.get("language", "English")
    topic = data.get("topic")
    voice_name = data.get("voice_name", "Fenrir")

    if not script or not topic:
        return jsonify({"error": "Script and topic are required"}), 400

    try:
        audio_path = generate_audio(script, language, topic, voice_name)
        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
