import requests

API_TOKEN = "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"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
} 

# Generate podcast script from input text using Hugging Face Inference API
def generate_podcast_script(input_text):
    # Define the API endpoint for the GPT-2 model
    API_URL = "https://api-inference.huggingface.co/models/gpt2"

    # Generalized prompt: Asking the model to generate a podcast script or summary
    prompt = f"Generate a conversational and engaging podcast script based on the following content. The script should summarize the input text and present it in a fun, informative way as if it's a podcast episode:\n\n{input_text}\n\nPlease make sure the tone is friendly, informative, and entertaining."

    # Payload with the input text and parameters for generating podcast script
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300,
            "num_return_sequences": 1,
            "temperature": 0.8,
            "top_p": 0.9
        }
    }

    # Send the POST request to the API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the response is successful
    if response.status_code == 200:
        result = response.json()
        print("API Response:", result)  # Print the entire response to see its structure
        return result[0].get('generated_text', "No generated text found")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Read the content from the input file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Specify the input file path
input_file_path = 'input.txt'

# Read the content from the file
input_text = read_input_file(input_file_path)

# Generate the podcast script directly from the input text
podcast_script = generate_podcast_script(input_text)

if podcast_script:
    print("\nPodcast Script:\n", podcast_script)
