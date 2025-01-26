import requests
import json


# Define the URL for the Voiceflow API
VOICEFLOW_API_URL = 'https://general-runtime.voiceflow.com/state/'  # Replace with your actual User ID
API_KEY = 'VF.DM.679594ed6d87d3a9603037e4.10JUDaosX2mzlAVC'  # Replace with your actual API Key


# Function to send input to the Voiceflow API and get a response
def query_voiceflow(user_input, user_state):
    # Set headers for the request
    headers = {
        'Authorization': f'Bearer {API_KEY}',  # Authorization header
        'Content-Type': 'application/json'     # JSON content type
    }


    # Construct the payload (message to send to the API)
    payload = {
        "action": "send_message",  # This could be different depending on the action you want
        "data": {
            "message": user_input  # The message from the user
        },
        "state": user_state  # User state to maintain context (use empty state initially)
    }


    # Make the POST request to Voiceflow API
    response = requests.post(VOICEFLOW_API_URL, json=payload, headers=headers)


    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response from the API
    else:
        print(f"Error: {response.status_code}")
        return {"error": "Failed to get response from Voiceflow"}


# Main function to interact with the user
def chat():
    print("Chatbot (type 'exit' to quit)")
    user_state = {}  # This will store user-specific information across requests (you can expand this to store the state in a database)
    
    while True:
        # Get the user input
        user_input = input("You: ")


        if user_input.lower() == 'exit':  # Exit condition
            print("Goodbye!")
            break


        # Send the user input to the Voiceflow API and get the response
        voiceflow_response = query_voiceflow(user_input, user_state)


        # Handle error if the response failed
        if 'error' in voiceflow_response:
            print(f"Error: {voiceflow_response['error']}")
        else:
            # Extract and print the chatbot's response from the API
            print(f"Chatbot: {voiceflow_response.get('response', {}).get('text', 'No response available')}")
            
            # You can update the user_state here based on the Voiceflow response
            # For example, Voiceflow might return a new state in its response, and you can store it


# Run the chat function to start the interaction
if __name__ == "__main__":
    chat()
