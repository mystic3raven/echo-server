from flask import Flask, request, jsonify
import sqlite3

DB_PATH = '/data/messages.db'

echo_app = Flask(__name__)

@echo_app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    message = data.get('message', '')

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
        conn.commit()
    
    return jsonify({'echo': message})

if __name__ == '__main__':
    echo_app.run(host='0.0.0.0', port=5001)

