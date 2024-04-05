import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

 
class Food_input(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Your Food Logs")
        self.geometry("560x330")
        self.page = 1  # Current page
        self.breakfast_protein_food_var = tk.StringVar()
        self.breakfast_vegetable_var = tk.StringVar()
        self.breakfast_main_var = tk.StringVar()
        self.breakfast_protein_amount = tk.StringVar()
        self.breakfast_vegetable_amount = tk.StringVar()
        self.breakfast_main_amount = tk.StringVar()
        self.lunch_protein_food_var = tk.StringVar()
        self.lunch_vegetable_var = tk.StringVar()
        self.lunch_main_var = tk.StringVar()
        self.lunch_protein_amount = tk.StringVar()
        self.lunch_vegetable_amount = tk.StringVar()
        self.lunch_main_amount = tk.StringVar()
        self.dinner_protein_food_var = tk.StringVar()
        self.dinner_vegetable_var = tk.StringVar()
        self.dinner_main_var = tk.StringVar()
        self.dinner_protein_amount = tk.StringVar()
        self.dinner_vegetable_amount = tk.StringVar()
        self.dinner_main_amount = tk.StringVar()
        self.inputs = {}
        self.foods = {
            "protein_list": 
            ["N/A",
            "Chicken breast", 
            "Chicken thigh", 
            "Beef", 
            "Steak",
            "Pork", 
            "Pork belly", 
            "Fish", 
            "Eggs", 
            "Tofu", 
            "Milk", 
            "Soy milk", 
            "Yogurt", 
            "Nut and seeds", 
            "Whey protein powder", 
            "Cheese"],

            "veggtable_list" : 
            [ "N/A",
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
            "Sunchoke"],

            "main_list" :[
            "N/A",
            "Rice",
            "Pasta",
            "Bread",
            "Potatoes",
            "Noodles",
            "Quinoa",
            "Couscous",
            "Barley",
            "Millet",
            "Bulgar",
            "Buckwheat",
            "Tortillas",
            "Polenta",
            "Oats",
            "Cornmeal"]
        }

        self.frames = {}
        self.inputs = {} # Dictionary to store the inputs from user. 

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
            elif self.page == 2:
                self.create_page2()
                self.show_next_button()
                self.show_back_button()
            elif self.page == 3:
                self.create_page3()
                self.hide_next_button()
                self.show_submit_button()
                self.show_back_button()
            elif self.page == 4:
                self.create_page4()
                self.hide_next_button()
                self.hide_submit_button()
                self.show_back_button()
            

    def create_page1(self):
        self.frames[1] = ttk.Frame(self)
        self.frames[1].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        goal_label = ttk.Label(self.frames[1], text="What is your breakfast intake?", font=("Arial", 18))
        goal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        protein_label = ttk.Label(self.frames[1], text="Select Protein:", font=("Arial", 16))
        protein_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        protein_combo = ttk.Combobox(self.frames[1], values=self.foods["protein_list"],textvariable=self.breakfast_protein_food_var, state="readonly")
        protein_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        protein_amount_label = ttk.Label(self.frames[1], text="How much did you eat (g):", font=("Arial", 16))
        protein_amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        protein_amout_entry = ttk.Entry(self.frames[1], textvariable=self.breakfast_protein_amount)
        protein_amout_entry.grid(row=2, column=1, padx=5, pady=5)
        protein_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        vegetable_label = ttk.Label(self.frames[1], text="Select Vegetable:", font=("Arial", 16))
        vegetable_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        vegetable_combo = ttk.Combobox(self.frames[1], textvariable=self.breakfast_vegetable_var, values=self.foods["veggtable_list"], state="readonly")
        vegetable_combo.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[1], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        vegetable_amout_entry = ttk.Entry(self.frames[1], textvariable=self.breakfast_vegetable_amount)
        vegetable_amout_entry.grid(row=4, column=1, padx=5, pady=5)
        vegetable_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        main_label = ttk.Label(self.frames[1], text="Select Main:", font=("Arial", 16))
        main_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        main_combo = ttk.Combobox(self.frames[1], textvariable=self.breakfast_main_var, values=self.foods["main_list"], state="readonly")
        main_combo.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[1], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        main_amout_entry = ttk.Entry(self.frames[1], textvariable=self.breakfast_main_amount)
        main_amout_entry.grid(row=6, column=1, padx=5, pady=5)
        main_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))
        protein_combo.current(0)
        vegetable_combo.current(0)
        main_combo.current(0)
        
    def create_page2(self):
        self.frames[2] = ttk.Frame(self)
        self.frames[2].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        goal_label = ttk.Label(self.frames[2], text="What is your Lunch intake?", font=("Arial", 18))
        goal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        protein_label = ttk.Label(self.frames[2], text="Select Protein:", font=("Arial", 16))
        protein_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        protein_combo = ttk.Combobox(self.frames[2], values=self.foods["protein_list"],textvariable=self.lunch_protein_food_var, state="readonly")
        protein_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        protein_amount_label = ttk.Label(self.frames[2], text="How much did you eat (g):", font=("Arial", 16))
        protein_amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        protein_amout_entry = ttk.Entry(self.frames[2], textvariable=self.lunch_protein_amount)
        protein_amout_entry.grid(row=2, column=1, padx=5, pady=5)
        protein_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        vegetable_label = ttk.Label(self.frames[2], text="Select Vegetable:", font=("Arial", 16))
        vegetable_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        vegetable_combo = ttk.Combobox(self.frames[2], textvariable=self.lunch_vegetable_var, values=self.foods["veggtable_list"], state="readonly")
        vegetable_combo.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[2], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        vegetable_amout_entry = ttk.Entry(self.frames[2], textvariable=self.lunch_vegetable_amount)
        vegetable_amout_entry.grid(row=4, column=1, padx=5, pady=5)
        vegetable_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        main_label = ttk.Label(self.frames[2], text="Select Main:", font=("Arial", 16))
        main_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        main_combo = ttk.Combobox(self.frames[2], textvariable=self.lunch_main_var, values=self.foods["main_list"], state="readonly")
        main_combo.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[2], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        main_amout_entry = ttk.Entry(self.frames[2], textvariable=self.lunch_main_amount)
        main_amout_entry.grid(row=6, column=1, padx=5, pady=5)
        main_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))
        
        protein_combo.current(0)
        vegetable_combo.current(0)
        main_combo.current(0)
    
    def create_page3(self):
        self.frames[3] = ttk.Frame(self)
        self.frames[3].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        goal_label = ttk.Label(self.frames[3], text="What is your Dinner intake?", font=("Arial", 18))
        goal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        protein_label = ttk.Label(self.frames[3], text="Select Protein:", font=("Arial", 16))
        protein_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        protein_combo = ttk.Combobox(self.frames[3], values=self.foods["protein_list"],textvariable=self.dinner_protein_food_var, state="readonly")
        protein_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        protein_amount_label = ttk.Label(self.frames[3], text="How much did you eat (g):", font=("Arial", 16))
        protein_amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        protein_amout_entry = ttk.Entry(self.frames[3], textvariable=self.dinner_protein_amount)
        protein_amout_entry.grid(row=2, column=1, padx=5, pady=5)
        protein_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        vegetable_label = ttk.Label(self.frames[3], text="Select Vegetable:", font=("Arial", 16))
        vegetable_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        vegetable_combo = ttk.Combobox(self.frames[3], textvariable=self.dinner_vegetable_var, values=self.foods["veggtable_list"], state="readonly")
        vegetable_combo.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[3], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        vegetable_amout_entry = ttk.Entry(self.frames[3], textvariable=self.dinner_vegetable_amount)
        vegetable_amout_entry.grid(row=4, column=1, padx=5, pady=5)
        vegetable_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))

        main_label = ttk.Label(self.frames[3], text="Select Main:", font=("Arial", 16))
        main_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        main_combo = ttk.Combobox(self.frames[3], textvariable=self.dinner_main_var, values=self.foods["main_list"], state="readonly")
        main_combo.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        vegetable_amount_label = ttk.Label(self.frames[3], text="How much did you eat (g):", font=("Arial", 16))
        vegetable_amount_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        main_amout_entry = ttk.Entry(self.frames[3], textvariable=self.dinner_main_amount)
        main_amout_entry.grid(row=6, column=1, padx=5, pady=5)
        main_amout_entry.config(validate="key",
                                 validatecommand=(self.register(lambda P: self.validate_input(P, "food amount")), "%P"))
        
        protein_combo.current(0)
        vegetable_combo.current(0)
        main_combo.current(0)

    
    def create_page4(self):
        self.frames[4] = ttk.Frame(self)
        self.frames[4].grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        intake_label = ttk.Label(self.frames[4], text="Your Today calorie intake:", font=("Arial", 18))
        intake_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        result_intake = self.calories_intake()
        result_intake = ttk.Label(self.frames[4], text=f"You consumed {result_intake} calories today.", font=("Arial", 20))
        result_intake.grid(row=1, column=0, padx=5, pady=5, sticky="w")


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

    def hide_next_button(self):
         for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Next":
                widget.grid_forget()
    
    def hide_submit_button(self):
         for widget in self.winfo_children():
            if isinstance(widget, ttk.Button) and widget["text"] == "Submit":
                widget.grid_forget()

    def show_next_button(self): 
        self.next_button = ttk.Button(self.navigation_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

    def show_back_button(self):
        self.back_button = ttk.Button(self.navigation_frame, text="Back", command=self.prev_page)
        self.back_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def show_submit_button(self):
        self.submit_button = ttk.Button(self.navigation_frame, text="Submit", command=self.next_page)
        self.submit_button.grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

    def next_page(self):
        if self.page == 1:
            if not self.breakfast_protein_amount.get() or not self.breakfast_vegetable_amount.get() or not self.breakfast_main_amount.get():
                messagebox.showwarning("Some food categories missing", "Please make sure to fill all the amount.")
                return
        elif self.page == 2:
            if not self.lunch_protein_amount.get() or not self.lunch_vegetable_amount.get() or not self.lunch_main_amount.get():
                messagebox.showwarning("Some food categories missing", "Please make sure to fill all the amount.")
                return
        elif self.page == 3:
            if not self.dinner_protein_amount.get() or not self.dinner_vegetable_amount.get() or not self.dinner_main_amount.get():
                messagebox.showwarning("Some food categories missing", "Please make sure to fill all the amount.")
                return
        self.page += 1
        self.create_widgets()

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.create_widgets()
    
    def calories_intake(self):
        # Calories calculation formula here
        pass

    def save_data(self):
        self.inputs["breakfast_protein"] = self.breakfast_protein_food_var.get()
        self.inputs["breakfast_vegetable"] = self.breakfast_vegetable_var.get()
        self.inputs["breakfast_main"] = self.breakfast_main_var.get()
        self.inputs["breakfast_protein_amount"] = int(self.breakfast_protein_amount.get())
        self.inputs["breakfast_vegetable_amount"] = int(self.breakfast_vegetable_amount.get())
        self.inputs["breakfast_main_amount"] = int(self.breakfast_main_amount.get())
        self.inputs["lunch_protein_food"] = self.lunch_protein_food_var.get()
        self.inputs["lunch_vegetable"] = self.lunch_vegetable_var.get()
        self.inputs["lunch_main_var"] = self.lunch_main_var.get()
        self.inputs["lunch_protein_amount"] = int(self.lunch_protein_amount.get())
        self.inputs["lunch_vegetable_amount"] = int(self.lunch_vegetable_amount.get())
        self.inputs["lunch_main_amount"] = int(self.lunch_main_amount.get())
        self.inputs["dinner_protein_food"] = self.dinner_protein_food_var.get()
        self.inputs["dinner_vegetable"] = self.dinner_vegetable_var.get()
        self.inputs["dinner_main_var"] = self.dinner_main_var.get()
        self.inputs["dinner_protein_amount"] = int(self.dinner_protein_amount.get())
        self.inputs["dinner_vegetable_amount"] = int(self.dinner_vegetable_amount.get())
        self.inputs["dinner_main_amount"] = int(self.dinner_main_amount.get())


if __name__ == "__main__":
    app = Food_input()
    app.mainloop()