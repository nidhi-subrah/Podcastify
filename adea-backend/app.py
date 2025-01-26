from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
import dotenv
from podcastify import convert_pdf_to_text, summarize_text_spacy, generate_podcast_script, get_audio
import io
app = Flask(__name__)
CORS(app)

dotenv.load_dotenv()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Convert PDF to text
        pdf_text = convert_pdf_to_text(file_path)
        if not pdf_text:
            return jsonify({"error": "Failed to extract text from PDF"}), 400
        
        # Summarize and generate podcast script
        summary = summarize_text_spacy(pdf_text)
        podcast_script = generate_podcast_script(pdf_text, summary)
        
        # Generate audio
        audio = get_audio(podcast_script)
        audio_file_path = os.path.join(UPLOAD_FOLDER, "podcast.mp3")
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(audio)
        
        # Return JSON response with audio file path
        return jsonify({"message": summary, "audio_file": "/uploads/podcast.mp3"})
    
    return jsonify({"error": "Invalid file type"}), 400

# Route to serve uploaded files dynamically
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/audio", methods=["POST"])
def generate_audio():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    audio = get_audio(text)
    return send_file(
        io.BytesIO(audio),
        mimetype="audio/mpeg",
        as_attachment=True,
        attachment_filename="podcast.mp3"
    )

if __name__ == "__main__":
    app.run(debug=True)
