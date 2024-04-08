import sqlite3

def setup_database():
    conn = sqlite3.connect('fitness_app.db')
    c = conn.cursor()
    # Create tables with a UNIQUE constraint on some fields if necessary
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, weight REAL, height REAL, gender TEXT, goal TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS food_logs
                 (id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, food TEXT, calories INTEGER,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def add_user(name, age, weight, height, gender, goal):
    conn = sqlite3.connect('fitness_app.db')
    c = conn.cursor()
    # Ensure only one user record exists: method 1, using a fixed ID
    user_id = 1  # Assuming a single, static user ID
    c.execute('REPLACE INTO users (id, name, age, weight, height, gender, goal) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (user_id, name, age, weight, height, gender, goal))
    conn.commit()
    conn.close()

setup_database()
