from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Voiceflow API key
API_KEY = "VF.DM.6795c19d12f08bcbb5f778d8.O9aqxLFyvDwdACM8"

# Interact with Voiceflow API
def interact_with_voiceflow(user_id, user_input):
    try:
        response = requests.post(
            f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
            headers={"Authorization": API_KEY, "Content-Type": "application/json"},
            json={"request": {"type": "text", "payload": user_input}}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id", "default_user")
    user_input = data.get("input", "")


    # Communicate with Voiceflow API
    traces = interact_with_voiceflow(user_id, user_input)
    responses = []


    for trace in traces:
        if trace["type"] in ["speak", "text"]:
            responses.append({"sender": "bot", "text": trace["payload"]["message"]})
        elif trace["type"] == "end":
            responses.append({"sender": "bot", "text": "The conversation has ended."})
    
    return jsonify({"messages": responses})

if __name__ == "__main__":
    app.run(debug=True)