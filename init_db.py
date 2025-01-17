import sqlite3
import os

DB_PATH = './data/messages.db'  # Ensure this matches the volume mapping

def init_db():
    os.makedirs('./data', exist_ok=True)  # Create directory if it doesn't exist
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()

if __name__ == '__main__':
    init_db()

