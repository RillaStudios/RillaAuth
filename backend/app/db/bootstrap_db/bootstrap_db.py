import sqlite3
from pathlib import Path

# Db path
DB_PATH = Path("db_settings.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS db_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                host TEXT NOT NULL,
                port INTEGER NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                db_name TEXT NOT NULL
            )
        ''')

        # Check if table is empty
        cursor.execute('SELECT COUNT(*) FROM db_settings')
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute('''
                INSERT INTO db_settings (host, port, username, password, db_name)
                VALUES (?, ?, ?, ?, ?)
            ''', (default_host, default_port, default_username, default_password, default_db_name))

        conn.commit()

def save_settings(host, port, username, password, db_name):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM db_settings')  # ensure only one record
        cursor.execute('''
            INSERT INTO db_settings (host, port, username, password, db_name)
            VALUES (?, ?, ?, ?, ?)
        ''', (host, port, username, password, db_name))
        conn.commit()

def load_db_settings():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT host, port, username, password, db_name FROM db_settings LIMIT 1')
        row = cursor.fetchone()
        if row:
            return {
                'host': row[0],
                'port': row[1],
                'username': row[2],
                'password': row[3],
                'db_name': row[4],
            }
        return None
