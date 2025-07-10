from flask import Flask, request, jsonify
from utils import download_audio
from transcribe import transcribe_audio
from summarize import summarize_text
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    youtube_url = data.get("url")

    audio_path = download_audio(youtube_url)
    if not audio_path:
        return jsonify({"error": "Audio download failed"}), 500

    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)

    # Save summary to a file
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    # Clean up audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(port=5000)