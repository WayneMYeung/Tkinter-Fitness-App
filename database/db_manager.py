import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name='fitness_app.db'):
        self.db_name = db_name
        self.setup_database()

    def setup_database(self):
        """Create the database tables if they don't already exist."""
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            # Create tables
            c.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY, gender TEXT, age INTEGER, weight REAL, goal_weight REAL, height REAL, goal TEXT, activity_level TEXT, calories_per_day REAL)''')
            c.execute('''CREATE TABLE IF NOT EXISTS food_log 
                      (id INTEGER PRIMARY KEY, food_name TEXT NOT NULL, calories INTEGER NOT NULL, logged_at DATE NOT NULL)''')
            conn.commit()
            
    def user_exists(self):
        """Check if there is at least one user in the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            return count > 0
        

    def save_user_info(self, gender, age, weight, goal_weight, height, goal, activity_level, calories_per_day):
        """Add or update the single user in the database."""
        user_id = 1  # Static user ID for the single user scenario
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''REPLACE INTO users (id, gender, age, weight, goal_weight, height, goal, activity_level, calories_per_day)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (user_id, gender, age, weight, goal_weight, height, goal, activity_level, calories_per_day))
            conn.commit()
    
    def get_calories_per_day(self):
        """Retrieve the daily calorie goal for the user."""
        user_id = 1
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''SELECT calories_per_day FROM users WHERE id = ?''', (user_id,))
            result = c.fetchone()
            return result[0] if result is not None else 0
            
    def get_total_calories_for_today(self):
        """Retrieve the total calories consumed for the current day."""
        today = datetime.now().date()
        query = """
        SELECT SUM(calories) FROM food_log
        WHERE date(logged_at) = date(?)
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (today,))
            result = cursor.fetchone()
            total_calories = result[0] if result[0] is not None else 0
            return total_calories

    def add_food_log(self, date, food, calories):
        """Add a new food log entry for the user."""
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO food_log (logged_at, food_name, calories)
                         VALUES (?, ?, ?)''',
                      (date, food, calories))
            conn.commit()

    def get_all_food_logs(self):
        """Retrieve all food log entries for the user."""
        user_id = 1  # Static user ID for the single user scenario
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''SELECT date, food, calories FROM food_logs WHERE user_id = ?''', (user_id,))
            return c.fetchall()

# Example usage
if __name__ == '__main__':
    db_manager = DBManager()
    db_manager.add_or_update_user('John Doe', 30, 70, 175, 'Male', 'Lose weight')
    db_manager.add_food_log('2024-04-07', 'Apple', 95)
    logs = db_manager.get_all_food_logs()
    for log in logs:
        print(log)
