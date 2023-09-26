# lib/helpers.py

from models.exercise import Exercise

def helper_1():
    print("Performing useful function#1.")

def create_exercise():
    name = input("Exercise: ")
    time = input("Duration (in minutes): ")
    category = input("Choose a category (Cardio = 1, Strength = 2): ")
    intensity = input("Choose an intensity (Beginner = 1, Intermediate = 2, Advanced = 3): ")
    cals_burned = input("Calories Burned: ")

    # Allow choices to be numbers
    if category not in Exercise.CATEGORY and 0 < int(category) < len(Exercise.CATEGORY):
        category = Exercise.CATEGORY[int(category) - 1]
    if intensity not in Exercise.INTENSITY and 0 < int(intensity) < len(Exercise.INTENSITY):
        intensity = Exercise.INTENSITY[int(intensity) -1]
    
    try:
        # Exercise.create_table()
        exercise = Exercise.create(name, time, category, intensity, cals_burned)
        print(f"Success: {exercise} is now available!")
    except Exception as exc:
        print("Error creating new exercise: ", exc)

def list_exercises():
    exercises = Exercise.get_all()
    for exercise in exercises:
        print(exercise)


def exit_program():
    print("See you next time for another workout!")
    exit()
