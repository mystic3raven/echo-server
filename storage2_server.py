import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database configuration
DB_PATH = "messages.db"

# Initialize the database
with sqlite3.connect(DB_PATH) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT)")
    conn.commit()

@app.route('/store', methods=['POST'])  # Changed from PUT to POST
@app.route('/echo', methods=['POST'])  # Changed from PUT to POST
def store():
    data = request.json
    if not data or 'message' not in data:
        return {"error": "Missing 'message' in request"}, 400

    # Store the message in the database
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO messages (message) VALUES (?)", (data['message'],))
            conn.commit()
        return {"status": "Message stored successfully"}, 200
    except Exception as e:
        return {"error": "Failed to store message", "details": str(e)}, 500

@app.route('/messages', methods=['GET'])
def get_messages():
    # Retrieve all messages from the database
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.execute("SELECT message FROM messages")
            messages = [row[0] for row in cursor.fetchall()]
        return jsonify(messages), 200
    except Exception as e:
        return {"error": "Failed to retrieve messages", "details": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

