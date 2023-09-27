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
        print(f"Success: {exercise.name} is now available!")
    except Exception as exc:
        print("Error creating new exercise: ", exc)

def list_exercises():
    exercises = Exercise.get_all()
    for exercise in exercises:
        print(exercise)

def get_exercise_by_name_or_id():
    name = input("Exercise or ID: ")
    try:
        id_ = int(name)
        exercise = Exercise.find_by_id(id_)
        print(exercise) if exercise else print(f"Exercise {name} not found")
    except:
        exercise = Exercise.find_by_name(name.title()) # .title() to allow for case insensitive
        print(exercise) if exercise else print(f"Exercise {name} not found")

def update_exercise_by_name_or_id():
    name = input("Exercise or ID: ")
    try:
        id_ = int(name)
        exercise = Exercise.find_by_id(id_)
        collect_updates(exercise)
    except:
        try:
            exercise = Exercise.find_by_name(name.title())
            collect_updates(exercise)
        except Exception as exc:
            print("Error updating exercise")

def collect_updates(exercise):
        # Update exercise instance
        name = input(f"{exercise.name} new name: ")
        exercise.name = name
        time = input(f"{exercise.name} new time: ")
        exercise.time = time
        category = input(f"{exercise.name} new category (Cardio = 1, Strength = 2): ")
        # exercise.category = category
        intensity = input(f"{exercise.name} new intensity (Beginner = 1, Intermediate = 2, Advanced = 3): ")
        # exercise.intensity = intensity
        cals_burned = input(f"{exercise.name} new calories burned: ")
        exercise.cals_burned = cals_burned

        # Allow choices to be numbers
        if category not in Exercise.CATEGORY and 0 < int(category) < len(Exercise.CATEGORY):
            exercise.category = Exercise.CATEGORY[int(category) - 1]
        if intensity not in Exercise.INTENSITY and 0 < int(intensity) < len(Exercise.INTENSITY):
            exercise.intensity = Exercise.INTENSITY[int(intensity) -1]        

        """ Exercise instance updated in database with .update() """
        exercise.update()
        print(f"{exercise.name} has been updated!") if exercise else print(f"Exercise {name} not found")

def delete_exercise_by_name_or_id():
    name_or_id = input("Exercise or ID: ")
    deleted_exercise = "deleted exercise"

    try:
        id_ = int(name_or_id)
        exercise = Exercise.find_by_id(id_)
        Exercise.delete(exercise)
        print(f"{exercise.name} has been deleted") if exercise else print(f"Exercise {exercise.name} not found")
    except:
        try:
            exercise = Exercise.find_by_name(name_or_id.title())
            Exercise.delete(exercise)
            print(f"{exercise.name} has been deleted") if exercise else print(f"Exercise {exercise.name} not found")
        except Exception as exc:
            print("Error deleting exercise")


def exit_program():
    print("See you next time for another workout!")
    exit()
