# lib/helpers.py

from models.exercise import Exercise

def helper_1():
    print("Performing useful function#1.")

def create_exercise():
    name = input("Exercise: ")
    time = input("Duration (in minutes): ")
    category = input("Category (Cardio or Strength): ")
    intensity = input("Intensity (Beginner, Intermediate, Advanced): ")
    cals_burned = input("Calories Burned: ")
    try:
        Exercise.create_table()
        exercise = Exercise.create(name, time, category, intensity, cals_burned)
        print(f"Success: {exercise} is now available!")
    except Exception as exc:
        print("Error creating new exercise: ", exc)

# def create_exercise():
#     name = input("Exercise: ")
#     time = input("Duration (in minutes): ")
#     category = input("Category (Cardio or Strength): ")
#     intensity = input("Intensity (Beginner, Intermediate, Advanced): ")
#     cals_burned = input("Calories Burned: ")
#     try:
#         Exercise.create_table()
#         exercise = Exercise.create(name, time, category, intensity, cals_burned)
#         print(f"Success: {exercise} is now available!")
#     except Exception as exc:
#         print("Error creating new exercise: ", exc)

def list_exercises():
    exercises = Exercise.get_all()
    for exercise in exercises:
        print(exercise)


def exit_program():
    print("Goodbye!")
    exit()
