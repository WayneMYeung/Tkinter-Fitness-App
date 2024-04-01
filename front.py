import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

 
class GoalSettingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Goal Options")
        self.geometry("560x300")

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

        self.frames = {}  # Dictionary to store frames for each page

        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 14))
        self.style.configure("TButton", font=("Arial", 14))
        self.style.configure("TEntry", font=("Arial", 14))

        if self.page == 1:
            self.create_page1()
            next_button = ttk.Button(self, text="Next", command=self.next_page)
            next_button.grid(row=1, column=1, padx=5, pady=10, sticky="e")
            self.hide_back_button()
        elif self.page == 2:
            self.create_page2()
            self.show_back_button()
        elif self.page == 3:
            self.create_page3()
            self.show_back_button()
        elif self.page == 4:
            self.create_page4()
            self.show_back_button()
        elif self.page == 5:
            self.create_page5()
            self.show_back_button()

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

    def next_page(self):
        if self.page < 5:
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

    def hide_back_button(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Back":
                widget.grid_forget()

    def show_back_button(self):
        back_button = ttk.Button(self, text="Back", command=self.prev_page)
        back_button.grid(row=1, column=0, padx=5, pady=10, sticky="w")


if __name__ == "__main__":
    app = GoalSettingApp()
    app.mainloop()
