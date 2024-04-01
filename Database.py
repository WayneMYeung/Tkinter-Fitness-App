import sqlite3

def setup_database():
    conn = sqlite3.connect('fitness_app.db')
    c = conn.cursor()
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, weight REAL, height REAL, gender TEXT, goal TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS food_logs
                 (id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, food TEXT, calories INTEGER)''')
    conn.commit()
    conn.close()
    
def add_user(name, age, weight, height, gender, goal):
    conn = sqlite3.connect('fitness_app.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name, age, weight, height, gender, goal) VALUES (?, ?, ?, ?, ?, ?)',
              (name, age, weight, height, gender, goal))
    conn.commit()
    conn.close()

setup_database()