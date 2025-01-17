from flask import Flask, jsonify
import sqlite3

DB_PATH = '/data/messages.db'

storage_app = Flask(__name__)

@storage_app.route('/messages', methods=['GET'])
def get_messages():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, message FROM messages ORDER BY id DESC')
        messages = cursor.fetchall()
    return jsonify({'messages': [{'id': m[0], 'message': m[1]} for m in messages]})

if __name__ == '__main__':
    storage_app.run(host='0.0.0.0', port=5002)

