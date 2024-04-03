import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

 
class GoalSettingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Goal Options")
        self.geometry("560x320")

        self.page = 1  # Current page
        self.gender = tk.StringVar()
        self.age = tk.StringVar()
        self.height_unit = tk.StringVar()
        self.height_value = tk.StringVar()
        self.weight = tk.StringVar()
        self.goal_weight = tk.StringVar()
        self.activity_level = tk.StringVar()
        self.goals = {
            "Lose Weight": tk.BooleanVar(),
            "Maintain Weight": tk.BooleanVar(),
            "Gain Weight": tk.BooleanVar(),
            "Muscle Training": tk.BooleanVar(),
            "Modify Diet Menu": tk.BooleanVar()
        }

        self.protein_list = ["chicken breast", 
                             "chicken thigh", 
                             "beef", 
                             "steak",
                             "pork", 
                             "pork belly", 
                             "fish", 
                             "eggs", 
                             "tofu", 
                             "milk", 
                             "soy milk", 
                             "yogurt", 
                             "nut and seeds", 
                             "Whey protein powder", 
                             "cheese" ]
        self.veggtable_list = [ 
            "Spinach",
            "Broccoli",
            "Carrots",
            "Tomatoes",
            "Bell peppers",
            "Cucumbers",
            "Lettuce",
            "Onions",
            "Garlic",
            "Potatoes",
            "Sweet potatoes",
            "Zucchini",
            "Eggplant",
            "Mushrooms",
            "Celery",
            "Cabbage",
            "Radishes",
            "Beets",
            "Corn",
            "Green peas",
            "Green beans",
            "Brussels sprouts",
            "Asparagus",
            "Artichokes",
            "Cauliflower",
            "Kale",
            "Chard",
            "Pumpkin",
            "Squash",
            "Okra",
            "Turnips",
            "Rutabagas",
            "Fennel",
            "Bok choy",
            "Leeks",
            "Scallions",
            "Watercress",
            "Soybeans",
            "Snap peas",
            "Bean sprouts",
            "Jicama",
            "Kohlrabi",
            "Yuca",
            "Parsnips",
            "Turnip greens",
            "Collard greens",
            "Mustard greens",
            "Swiss chard",
            "Radish greens",
            "Endive",
            "Arugula",
            "Dandelion greens",
            "Chicory",
            "Broccoli rabe",
            "Sprouts",
            "Lotus root",
            "Taro",
            "Cassava",
            "Chayote",
            "Bamboo shoots",
            "Hearts of palm",
            "Bitter melon",
            "Winter melon",
            "Daikon",
            "Burdock root",
            "Jerusalem artichoke",
            "Fiddlehead ferns",
            "Samphire",
            "Lotus root",
            "Water chestnuts",
            "Rhubarb",
            "Tamarind",
            "Plantains",
            "Yams",
            "Cassava",
            "Yucca",
            "Arrowroot",
            "Chicory root",
            "Ginger",
            "Turmeric",
            "Horseradish",
            "Wasabi",
            "Salsify",
            "Skirret",
            "Yacon",
            "Chinese artichoke",
            "Crosne",
            "Oca",
            "Maca",
            "Chicory root",
            "Sunchoke"
                    ]
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
            self.hide_submit_button()
            self.show_next_button()
            self.show_back_button()
        
        self.update_navigation_buttons()


    def create_page1(self):
        self.frames[1] = ttk.Frame(self)
        self.frames[1].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        label = ttk.Label(self.frames[1], text="Let's Set a Goal!", font=("Arial", 19))
        label.grid(row=0, column=1, columnspan=3, padx=(0, 20), pady=(20, 5), sticky="e")

        label_subtitle = ttk.Label(self.frames[1], text="Choose the things that are most important to you.",
                                   font=("Arial", 13))
        label_subtitle.grid(row=1, column=0, columnspan=3, padx=10, pady=(5, 10))

        row_num = 2
        for goal, var in self.goals.items():
            ttk.Checkbutton(self.frames[1], text=goal, variable=var).grid(row=row_num, column=0, sticky="w", padx=30,
                                                                          pady=5)
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

        result_calories = self.cal_calories_goal()
        result_label = ttk.Label(self.frames[6], text=f"You burn {result_calories} calories during a typical day", font=("Arial", 20))
        result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        paragraph_text = "Remember that this estimate is based on your body weight, height, age, gender, and your average level of activity. You can use this information to help you figure out how many calories you should be consuming to maintain your weight."
        paragraph_label = ttk.Label(self.frames[6], text=paragraph_text, font=("Arial", 14), wraplength=500, justify="left")
        paragraph_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    def create_page7(self):
        self.frames[7] = ttk.Frame(self)
        self.frames[7].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        goal_label = ttk.Label(self.frames[7], text="What is your breakfast intake", font=("Arial", 18))
        goal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        
        breakfast_protein = ttk.Combobox(self.frames[7], values=["Feet/Inches", "Centimeters"],
                                         textvariable=self.height_unit, state="readonly")




    def next_page(self):
        if self.page == 1:
            # Check if at least one goal is selected
            if not any(var.get() for var in self.goals.values()):
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

    def get_inputs(self):
        self.next_page()
        self.inputs["gender"] = app.gender.get()
        self.inputs["age"] = float(app.age.get())
        self.inputs["height_unit"] = app.height_unit.get()
        if self.inputs["height_unit"] == "Feet/Inches":
            self.inputs["height_value"] = float(app.height_value.get()) * 2.54
        else:
            self.inputs["height_value"] = float(app.height_value.get())
        self.inputs["weight"] = float(app.weight.get())
        self.inputs["goal_weight"] = float(app.goal_weight.get())
        self.inputs["activity_level"] = app.activity_level.get()

        self.next_page()

    def cal_calories_goal(self):
        calories = 0
        if self.inputs["gender"] == "Female":
            calories = 65.51 + (9.563 * self.inputs["weight"]) + (1.850 * self.inputs["height_value"]) - (4.676 * self.inputs["age"])
        elif self.inputs["gender"] == "Male":
            calories = 66.47 + (13.75 * self.inputs["weight"]) + (5.003 * self.inputs["height_value"]) - (6.755 * self.inputs["age"])

        if self.inputs["activity_level"] == "Sedentary (little to no exercise)":
            calories *= 1.2
        elif self.inputs["activity_level"] == "Lightly active (light exercise/sports 1-3 days a week)":
            calories *=1.375
        elif self.inputs["activity_level"] == "Moderately active (moderate exercise/sports 3-5 days a week)":
            calories *= 1.55
        elif self.inputs["activity_level"] == "Very active (hard exercise/sports 6-7 days a week)":
            calories *= 1.725
        elif self.inputs["activity_level"] == "Extra active (very hard exercise/sports & physical job or 2x training)":
            calories *= 1.9
        return calories

if __name__ == "__main__":
    app = GoalSettingApp()
    app.mainloop()

