# File: echo_server.py
from flask import Flask, request, jsonify
import sqlite3

echo_app = Flask(__name__)

@echo_app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    message = data.get('message', '')
    
    # Store message in SQLite database
    with sqlite3.connect('messages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
        conn.commit()
    
    return jsonify({'echo': message})

if __name__ == '__main__':
    echo_app.run(port=5000)