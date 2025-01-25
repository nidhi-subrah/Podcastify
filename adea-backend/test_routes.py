import os
import pytest
import io
from io import BytesIO
from fpdf import FPDF
from app import app  # Ensure this correctly imports your Flask app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    client = app.test_client()
    yield client  # Provide the test client

@pytest.fixture
def sample_pdf():
    """Provide a file-like object for test.pdf."""
    return io.BytesIO(open("test.pdf", "rb").read())  # Convert bytes into a file-like object


def test_upload_pdf(client, sample_pdf):
    """Test if the upload route accepts a real PDF file."""
    data = {
        'file': (sample_pdf, "test.pdf")  # Ensure correct tuple structure
    }
    response = client.post("/upload", content_type='multipart/form-data', data=data)
    
    assert response.status_code == 200  # Ensure the request was successful
    assert "audio_file" in response.json  # Check if the response contains the expected key


def test_upload_invalid_file(client):
    """Test if the upload route rejects non-PDF files."""
    data = {
        'file': (BytesIO(b"Dummy text content"), "test.txt")
    }
    response = client.post("/upload", content_type='multipart/form-data', data=data)
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_download_podcast(client):
    """Test if the download route serves the podcast file."""
    file_path = os.path.join("uploads", "podcast.mp3")

    # Ensure the uploads directory exists
    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(b"Dummy audio content")

    response = client.get("/download/podcast.mp3")
    assert response.status_code == 200
    assert response.mimetype == "audio/mpeg"

    # Ensure file is properly closed before removing
    for _ in range(5):  # Try up to 5 times
        try:
            os.remove(file_path)
            break  # Exit loop if deletion succeeds
        except PermissionError:
            import time
            time.sleep(1)  # Wait briefly before retrying



