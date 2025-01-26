# storage_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for messages
storage = []

@app.route('/store', methods=['PUT'])
def store():
    data = request.json
    if not data or 'message' not in data:
        return {"error": "Missing 'message' in request"}, 400

    # Store the message
    storage.append(data['message'])
    return {"status": "Message stored successfully"}, 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(storage), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
