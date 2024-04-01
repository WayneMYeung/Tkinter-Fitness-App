def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_tdee(bmr, activity_level):
    if activity_level == 'sedentary':
        return bmr * 1.2
    elif activity_level == 'lightly active':
        return bmr * 1.375
    elif activity_level == 'moderately active':
        return bmr * 1.55
    elif activity_level == 'very active':
        return bmr * 1.725
    else:
        return bmr * 1.9

def adjust_calories_for_goal(tdee, goal):
    if goal == 'lose weight':
        return tdee - 500  # Create a deficit of 500 calories for weight loss
    elif goal == 'gain weight':
        return tdee + 500  # Add 500 calories for weight gain
    else:
        return tdee  # Maintain current weight
