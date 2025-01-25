import requests
import base64


API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = "kO5--wtLz2h-R9NJ-B2S3p0pVFjhFlaBy8hXeWgEfo0="
VOICE_ID = "george"


def get_audio(text):
    url = f"{API_BASE_URL}/v1/audio/speech"
    payload = {
        "input": f"<speak>{text}</speak>",
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

def main():
    # Read text from a file
    input_file = "input.txt"
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Generate audio from the text
    audio = get_audio(text)

    # Save the audio as an MP3 file
    output_file = "speech.mp3"
    with open(output_file, "wb") as file:
        file.write(audio)


    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    main()