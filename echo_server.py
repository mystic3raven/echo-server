from flask import Flask, request, jsonify
import sqlite3

# Path to the SQLite database
DB_PATH = '/data/messages.db'

# Initialize Flask application
echo_app = Flask(__name__)

# Define the /echo endpoint
@echo_app.route('/echo', methods=['POST'])
def echo():
    data = request.json  # Get the JSON payload
    if not data or 'message' not in data:
        return jsonify({'error': 'Message field is required'}), 400
    
    message = data.get('message', '')

    # Insert the message into the database
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
        cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
        conn.commit()

    # Return the echoed message
    return jsonify({'echo': message})

# Define the /messages endpoint
@echo_app.route('/messages', methods=['GET'])
def get_messages():
    # Fetch all messages from the database
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')  # Ensure table exists
        cursor.execute('SELECT * FROM messages')
        rows = cursor.fetchall()

    # Format the messages as a list of dictionaries
    messages = [{'id': row[0], 'message': row[1]} for row in rows]

    # Return the messages as a JSON response
    return jsonify(messages)

if __name__ == '__main__':
    echo_app.run(host='0.0.0.0', port=5000)

