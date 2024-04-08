from ui.main_window import MainWindow
from ui.food_input import FoodInput  # Ensure this import is correct for your project structure
from database.db_manager import DBManager
import tkinter as tk

def main():
    # Initialize the database manager
    db_manager = DBManager()

    if db_manager.user_exists():
        # If a user exists, directly go to the food input interface
        root = tk.Tk()
        root.geometry("400x400")
        food_input = FoodInput(master=root, db_manager=db_manager)
        root.mainloop()
    else:
        # Otherwise, initialize and run the main application window
        app = MainWindow(db_manager=db_manager)
        app.mainloop()

if __name__ == "__main__":
    main()
