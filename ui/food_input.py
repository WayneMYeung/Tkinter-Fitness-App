import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import DBManager
from datetime import datetime
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk
# Essie. (n.d.). Variety HD transparent, black and white variety of food, black vector, food vector, vector diagram PNG image for free download. Pngtree. https://pngtree.com/freepng/black-and-white-variety-of-food_3319164.html

class FoodInput:
    def __init__(self, master, db_manager):
        self.master = master
        self.db_manager = db_manager
        self.setup_ui(master)


    def setup_ui(self, master):
        # Load the background image
        original_img = Image.open('background.png')  # Load the image with Pillow
        # Essie. (n.d.). Variety HD transparent, black and white variety of food, black vector, food vector, vector diagram PNG image for free download. Pngtree. https://pngtree.com/freepng/black-and-white-variety-of-food_3319164.html
        resized_img = original_img.resize((400, 400))
        self.bg_image = ImageTk.PhotoImage(resized_img)
        bg_label = Label(master, image=self.bg_image)
        top_padding = 50
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.lower()  # Ensure it's behind other widgets

        # Define a consistent font and padding
        font = ('Arial', 10)
        pad_x, pad_y = 10, 5
        
        # Configure Styles
        style = ttk.Style()
        style.configure('TLabel', background='light grey', foreground='black', font=font, padding=(pad_x, pad_y))
        style.configure('TEntry', padding=(pad_x, pad_y))
        style.configure('TButton', font=('Arial', 10, 'bold'), borderwidth=1)
        style.map('TButton', foreground=[('pressed', 'red'), ('active', 'blue')],
                   background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        
        # UI elements for logging food and displaying remaining calories
        
        top_padding = 30
        self.food_name_label = ttk.Label(master, text="Food Name:", font=font)
        
        self.food_name_entry = ttk.Entry(master, font=font)
        self.food_calories_label = ttk.Label(master, text="Calories:", font=font)
        self.food_calories_entry = ttk.Entry(master, font=font)
        self.log_button = ttk.Button(master, text="Log Food", command=self.log_food, style='Accent.TButton')
        self.remaining_calories_label = ttk.Label(master, text="Remaining Calories: Calculating...", font=font)
        
        # Layout with padding
        self.food_name_label.grid(row=0, column=0, padx=pad_x, pady=(top_padding,pad_y), sticky="W")
        self.food_name_entry.grid(row=0, column=1, padx=pad_x, pady=(top_padding,pad_y), sticky="EW")
        self.food_calories_label.grid(row=1, column=0, padx=pad_x, pady=pad_y, sticky="W")
        self.food_calories_entry.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky="EW")
        self.log_button.grid(row=2, column=0, columnspan=2, padx=pad_x, pady=pad_y)
        self.remaining_calories_label.grid(row=3, column=0, columnspan=2, padx=pad_x, pady=pad_y)

        # Make the entry widgets expand to fill the column
        master.columnconfigure(1, weight=1)


        # Initially update the remaining calories
        self.update_remaining_calories()

    def log_food(self):
        # Method to log food to the database and update UI
        food_name = self.food_name_entry.get()
        food_calories = self.food_calories_entry.get()
        if not food_name or not food_calories.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid food name and calorie count.")
            return

        # Assuming a table structure for food logging, adjust as necessary
        self.db_manager.add_food_log(datetime.now().date(), food_name, int(food_calories))
        self.food_name_entry.delete(0, tk.END)
        self.food_calories_entry.delete(0, tk.END)
        self.update_remaining_calories()

    def update_remaining_calories(self):
        # Calculate and display remaining calories for the day
        daily_goal = self.db_manager.get_calories_per_day() # This could be dynamically set or retrieved from the database
        consumed_calories = self.db_manager.get_total_calories_for_today()
        remaining = daily_goal - consumed_calories
        self.remaining_calories_label.config(text=f"Remaining Calories: {remaining}")
