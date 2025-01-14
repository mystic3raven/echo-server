from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    # Get current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get the raw data sent by the client
    data = request.get_json() or request.data.decode('utf-8') or "No data sent"

    # Print the received data with the timestamp
    print(f"[{timestamp}] Received: {data}")

    # Prepare the response
    response = {
        "timestamp": timestamp,
        "echo": data
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
