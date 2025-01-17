# File: storage_server.py
from flask import Flask, jsonify
import sqlite3

storage_app = Flask(__name__)

@storage_app.route('/messages', methods=['GET'])
def get_messages():
    with sqlite3.connect('messages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, message FROM messages ORDER BY id DESC')
        messages = cursor.fetchall()
    return jsonify({'messages': [{'id': m[0], 'message': m[1]} for m in messages]})

if __name__ == '__main__':
    storage_app.run(port=5001)