import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database.db_manager import DBManager  # Ensure this import is correct for your project structure
from ui.food_input import FoodInput  # Ensure this import is correct


class MainWindow(tk.Tk):
    def __init__(self, db_manager):
        super().__init__()

        self.db_manager = db_manager
        self.title("Goal Options")
        self.geometry("600x600")

        self.page = 1  # Current page
        self.gender = tk.StringVar()
        self.age = tk.StringVar()
        self.height_unit = tk.StringVar()
        self.height_value = tk.StringVar()
        self.weight = tk.StringVar()
        self.goal_weight = tk.StringVar()
        self.activity_level = tk.StringVar()
        self.goals = tk.StringVar()

        self.main_list = []
        
        self.inputs = {} # Dictionary to store the inputs from user. 

        self.frames = {}  # Dictionary to store frames for each page

        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 14))
        self.style.configure("TButton", font=("Arial", 14))
        self.style.configure("TEntry", font=("Arial", 14))

        self.navigation_frame = ttk.Frame(self)
        self.navigation_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        if self.page == 1:
            self.create_page1()
            self.show_next_button()
            self.hide_back_button()
            self.hide_submit_button()
        elif self.page == 2:
            self.create_page2()
            self.show_back_button()
            self.show_next_button()
            self.hide_submit_button()
        elif self.page == 3:
            self.create_page3()
            self.show_next_button()
            self.show_back_button()
            self.hide_submit_button()
        elif self.page == 4:
            self.create_page4()
            self.show_next_button()
            self.show_back_button()
            self.hide_submit_button()
        elif self.page == 5:
            self.create_page5()
            self.show_submit_button()
            self.show_back_button()
            self.hide_next_button()
        elif self.page == 6:
            self.create_page6()
            self.hide_next_button()
            self.show_back_button()
            self.show_create_button()

        self.update_navigation_buttons()


    def create_page1(self):
        self.frames[1] = ttk.Frame(self)
        self.frames[1].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        label = ttk.Label(self.frames[1], text="Let's Set a Goal!", font=("Arial", 19))
        label.grid(row=0, column=1, columnspan=3, padx=(0, 20), pady=(20, 5), sticky="e")

        label_subtitle = ttk.Label(self.frames[1], text="Choose the thing that is most important to you.",
                                font=("Arial", 13))
        label_subtitle.grid(row=1, column=0, columnspan=3, padx=10, pady=(5, 10))

        goals = [
            "Lose Weight",
            "Maintain Weight",
            "Gain Weight",
            "Muscle Training",
            "Modify Diet Menu"
        ]

        row_num = 2
        for idx, goal in enumerate(goals, start=1):  # Start indexing at 1 for easier understanding
            ttk.Radiobutton(self.frames[1], text=goal, variable=self.goals, value=goal).grid(
                row=row_num, column=0, sticky="w", padx=30, pady=5)
            row_num += 1

    def create_page2(self):
        self.frames[2] = ttk.Frame(self)
        self.frames[2].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        label_intro = ttk.Label(self.frames[2], text="Please let us know you a little more.", font=("Arial", 18))
        label_intro.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 5), sticky="ew")

        gender_description = ttk.Label(self.frames[2],
                                       text="Choose the gender and age to use when calculating your calorie needs",
                                       font=("Arial", 13))
        gender_description.grid(row=1, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="ew")

        label_gender = ttk.Label(self.frames[2], text="Select Gender:")
        label_gender.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        ttk.Radiobutton(self.frames[2], text="Male", variable=self.gender, value="Male").grid(row=2, column=1, padx=5,
                                                                                              pady=5)
        ttk.Radiobutton(self.frames[2], text="Female", variable=self.gender, value="Female").grid(row=2, column=2,
                                                                                                  padx=5, pady=5)

        age_label = ttk.Label(self.frames[2], text="Enter Age:")
        age_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        age_entry = ttk.Entry(self.frames[2], textvariable=self.age)
        age_entry.grid(row=3, column=1, padx=5, pady=5)
        age_entry.config(validate="key", validatecommand=(self.register(lambda P: self.validate_input(P, "age")), "%P"))

    def create_page3(self):
        self.frames[3] = ttk.Frame(self)
        self.frames[3].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        how_tall_label = ttk.Label(self.frames[3], text="How tall are you?", font=("Arial", 18))
        how_tall_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        label = ttk.Label(self.frames[3], text="Select Height Unit:")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        height_unit_combo = ttk.Combobox(self.frames[3], values=["Feet/Inches", "Centimeters"],
                                         textvariable=self.height_unit, state="readonly")
        height_unit_combo.grid(row=1, column=1, padx=5, pady=5)
        height_unit_combo.current(0)
        height_unit_combo.bind("<<ComboboxSelected>>", self.update_height_input)

        label = ttk.Label(self.frames[3], text="Enter Height:")
        label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        height_entry = ttk.Entry(self.frames[3], textvariable=self.height_value)
        height_entry.grid(row=2, column=1, padx=5, pady=5)
        height_entry.config(validate="key",
                            validatecommand=(self.register(lambda P: self.validate_input(P, "height")), "%P"))

    def create_page4(self):
        self.frames[4] = ttk.Frame(self)
        self.frames[4].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tell_weight_label = ttk.Label(self.frames[4], text="Tell your weight and target weight!", font=("Arial", 18))
        tell_weight_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        weight_label = ttk.Label(self.frames[4], text="Enter Weight (kg):")
        weight_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        weight_entry = ttk.Entry(self.frames[4], textvariable=self.weight)
        weight_entry.grid(row=1, column=1, padx=5, pady=5)
        weight_entry.config(validate="key",
                            validatecommand=(self.register(lambda P: self.validate_input(P, "weight")), "%P"))

        goal_weight_label = ttk.Label(self.frames[4], text="Enter Goal Weight (kg):")
        goal_weight_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        goal_weight_entry = ttk.Entry(self.frames[4], textvariable=self.goal_weight)
        goal_weight_entry.grid(row=2, column=1, padx=5, pady=5)
        goal_weight_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "goal weight")), "%P"))

    def create_page5(self):
        self.frames[5] = ttk.Frame(self)
        self.frames[5].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        activity_label = ttk.Label(self.frames[5], text="Select Activity Level:", font=("Arial", 18))
        activity_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        activity_options = ["Sedentary (little to no exercise)",
                            "Lightly active (light exercise/sports 1-3 days a week)",
                            "Moderately active (moderate exercise/sports 3-5 days a week)",
                            "Very active (hard exercise/sports 6-7 days a week)",
                            "Extra active (very hard exercise/sports & physical job or 2x training)"]

        for idx, option in enumerate(activity_options):
            ttk.Radiobutton(self.frames[5], text=option, variable=self.activity_level, value=option).grid(row=idx + 1, column=0, padx=5, pady=2, sticky="w")

    def create_page6(self):
        self.frames[6] = ttk.Frame(self)
        self.frames[6].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.get_inputs()

        goal_label = ttk.Label(self.frames[6], text="Your Daily Net Calories Result:", font=("Arial", 18))
        goal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        result_calories = self.save_user_info()
        result_label = ttk.Label(self.frames[6], text=f"You burn {result_calories} calories during a typical day", font=("Arial", 20))
        result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        paragraph_text = "Remember that this estimate is based on your body weight, height, age, gender, and your average level of activity. You can use this information to help you figure out how many calories you should be consuming to maintain your weight."
        paragraph_label = ttk.Label(self.frames[6], text=paragraph_text, font=("Arial", 14), wraplength=500, justify="left")
        paragraph_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


    def next_page(self):
        if self.page == 1:
            # Check if at least one goal is selected
            if not self.goals.get():
                messagebox.showwarning("No Goal Selected", "Please select at least one goal.")
                return
        elif self.page == 2:
            # Check if gender and age are selected
            if not self.gender.get() or not self.age.get():
                messagebox.showwarning("Missing Information", "Please select gender and enter age.")
                return
        elif self.page == 3:
            # Check if height unit and value are selected
            if not self.height_unit.get() or not self.height_value.get():
                messagebox.showwarning("Missing Information", "Please select height unit and enter height.")
                return
        elif self.page == 4:
            # Check if weight and goal weight are entered
            if not self.weight.get() or not self.goal_weight.get():
                messagebox.showwarning("Missing Information", "Please enter weight and goal weight.")
                return
        elif self.page == 5:
            # Check if activity level is selected
            if not self.activity_level.get():
                messagebox.showwarning("Missing Information", "Please select activity level.")
                return
            
        if self.page < 6:
            self.page += 1
            self.create_widgets()

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.create_widgets()

    def update_height_input(self, event):
        if self.height_unit.get() == "Feet/Inches":
            self.height_value.set("")
        else:
            self.height_value.set("")

    def validate_input(self, value, field):
        if value.isdigit() or value == "":
            return True
        else:
            messagebox.showwarning("Invalid Input", f"{field.capitalize()} should contain only numbers.")
            return False

    def update_navigation_buttons(self):
        if self.page == 5:
            self.next_button.config(state=tk.DISABLED)


    def hide_back_button(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Back":
                widget.grid_forget()
    
    def hide_submit_button(self):
         for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Submit":
                widget.grid_forget()
    
    def hide_next_button(self):
         for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Next":
                widget.grid_forget()
    
    def show_next_button(self): 
        self.next_button = ttk.Button(self.navigation_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

    def show_back_button(self):
        self.back_button = ttk.Button(self.navigation_frame, text="Back", command=self.prev_page)
        self.back_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    def show_submit_button(self):
        self.submit_button = ttk.Button(self.navigation_frame, text="Submit", command=self.get_inputs)
        self.submit_button.grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

    def show_create_button(self):
        self.submit_button = ttk.Button(self.navigation_frame, text="Create Food Logs", command=self.setup_food_log_entry)
        self.submit_button.grid(row=1, column=6, padx=10, pady=10, sticky="nsew")
    

    def get_inputs(self):
        self.next_page()
        self.inputs["gender"] = self.gender.get()
        self.inputs["age"] = float(self.age.get())
        self.inputs["height_unit"] = self.height_unit.get()
        if self.inputs["height_unit"] == "Feet/Inches":
            self.inputs["height_value"] = float(self.height_value.get()) * 2.54
        else:
            self.inputs["height_value"] = float(self.height_value.get())
        self.inputs["goals"] = self.goals.get()
        self.inputs["weight"] = float(self.weight.get())
        self.inputs["goal_weight"] = float(self.goal_weight.get())
        self.inputs["activity_level"] = self.activity_level.get()

        self.next_page()

    def save_user_info(self):
        gender = self.inputs["gender"]
        age = self.inputs["age"]
        weight = self.inputs["weight"]
        goal_weight = self.inputs["goal_weight"]
        height = self.inputs["height_value"]
        activity_level = self.inputs["activity_level"]
        goal = self.inputs["goals"]
        calories_per_day = self.calculate_calories(gender, age, weight, goal_weight, height, goal, activity_level)
        self.db_manager.save_user_info(gender, age, weight, goal_weight, height, goal, activity_level, calories_per_day)
        messagebox.showinfo("Info", "User information saved successfully.")
        return calories_per_day
    
    def calculate_calories(self, gender, age, weight, goal_weight, height, goal, activity_level):
        # BMR Calculation (simplified, consider adjusting for gender)
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:  # Female and Other
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        # Activity Level Multiplier
        activity_multiplier = {
            "Sedentary (little to no exercise)": 1.2,
            "Lightly active (light exercise/sports 1-3 days a week)": 1.375,
            "Moderately active (moderate exercise/sports 3-5 days a week)": 1.55,
            "Very active (hard exercise/sports 6-7 days a week)": 1.725,
            "Extra active (very hard exercise/sports & physical job or 2x training)": 1.9
        }.get(activity_level, 1.2)  # Default to sedentary if not found

        tdee = bmr * activity_multiplier

        # Goal Adjustment
        if goal == "Lose weight":
            calorie_goal = tdee - 500  # Create a deficit of 500 calories for weight loss
        elif goal == "Gain weight":
            calorie_goal = tdee + 500  # Add a surplus of 500 calories for weight gain
        elif goal == "Muscle training":
            calorie_goal = tdee + 300  # Adjust based on common recommendations for muscle gain
        else:  # Maintain weight
            calorie_goal = tdee

        return calorie_goal
        
    def setup_food_log_entry(self):
        # Launch Food_input dialog to collect detailed food log
        food_input_dialog = tk.Toplevel(self)
        food_input_dialog.title("Food Log Entry")

        # Initialize FoodInput with the Toplevel window as its master
        food_input_frame = FoodInput(food_input_dialog, self.db_manager)

        # You can adjust the size and position of the dialog window as needed
        food_input_dialog.geometry("400x400")  # Example size

        # If FoodInput is a frame, use pack or grid to display it within the Toplevel window
        food_input_frame.pack(fill="both", expand=True)
        self.master.withdraw()
        
    def save_food_log(self):
        food_name = self.food_name_field.get()
        calories = int(self.calorie_field.get())  # Ensure proper type conversion
        current_date = datetime.now().strftime("%Y-%m-%d")  # Use datetime to get the current date

        # Use DBManager to save the food log entry
        self.db_manager.add_food_log(current_date, food_name, calories)

        messagebox.showinfo("Success", "Food log entry saved successfully.")    
        # Consider what should happen next, e.g., clearing fields, showing another UI part, etc.