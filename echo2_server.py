# echo_server.py
from flask import Flask, request
import requests

app = Flask(__name__)

# Configuration for storage server
STORAGE_SERVER_URL = "http://localhost:5002"

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    if not data or 'message' not in data:
        return {"error": "Missing 'message' in request"}, 400

    # Call the storage server to store the message
    try:
        response = requests.put(f"{STORAGE_SERVER_URL}/store", json={"message": data['message']})
        if response.status_code == 200:
            return {"message": data['message'], "status": "Stored successfully"}, 200
        else:
            return {"error": "Failed to store message", "details": response.json()}, response.status_code
    except Exception as e:
        return {"error": "Failed to connect to storage server", "details": str(e)}, 500

@app.route('/messages', methods=['GET'])
def get_messages():
    # Call the storage server to fetch all messages
    try:
        response = requests.get(f"{STORAGE_SERVER_URL}/messages")
        if response.status_code == 200:
            return response.json(), 200
        else:
            return {"error": "Failed to fetch messages", "details": response.json()}, response.status_code
    except Exception as e:
        return {"error": "Failed to connect to storage server", "details": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)