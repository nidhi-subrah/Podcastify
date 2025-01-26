from flask import Flask, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from transformers import pipeline
import requests
import base64
from flask_cors import CORS
import dotenv   

app = Flask(__name__)
CORS(app)

dotenv.load_dotenv()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf'}

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv("SPEECHIFY_API_KEY")
VOICE_ID = "george"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if not text.strip():
        return None  # Indicate failure to extract text
    return text

def summarize_text(text):
    max_chunk_size = 1000
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = [summarizer(chunk, max_length=min(150, len(chunk)//2), min_length=10, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)


def get_audio_from_speechify(text):
    url = f"{API_BASE_URL}/v1/audio/speech"
    payload = {
        "input": f"<speak>{text}</speak>",  # SSML
        "voice_id": VOICE_ID,
        "audio_format": "mp3",
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    if not response.ok:
        raise Exception(f"{response.status_code} {response.reason}\n{response.text}")
    response_data = response.json()
    decoded_audio_data = base64.b64decode(response_data["audio_data"])

    return decoded_audio_data

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        summary = summarize_text(text)

        audio = get_audio_from_speechify(summary)
        audio_file_path = os.path.join(UPLOAD_FOLDER, "podcast.mp3")
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(audio)

        return jsonify({"message": "Podcast generated", "audio_file": "/download/podcast.mp3"})

    return jsonify({"error": "Invalid file type"}), 400

@app.route("/download/podcast.mp3", methods=["GET"])
def download_podcast():
    audio_file = os.path.join(UPLOAD_FOLDER, "podcast.mp3")
    return send_file(audio_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
