# File: init_db.py
import sqlite3

def init_db():
    with sqlite3.connect('messages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            message TEXT NOT NULL
                          )''')
        conn.commit()

if __name__ == '__main__':
    init_db()
