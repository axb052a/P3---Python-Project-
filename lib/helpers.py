# lib/helpers.py

from models.exercise import Exercise
from models.log import Log

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
            print("Error updating exercise", exc)

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
            
def find_most_and_least_popular_exercises():
    # Get a list of all exercises
    all_exercises = Exercise.get_all()

    # Initialize dictionaries to store exercise popularity counts
    exercise_popularity = {}
    
    # Count the popularity of each exercise based on log entries
    for exercise in all_exercises:
        log_entries = Log.find_by_exercise(exercise)
        exercise_popularity[exercise.name] = len(log_entries)

    # Find the most and least popular exercises
    most_popular_exercise = max(exercise_popularity, key=exercise_popularity.get)
    least_popular_exercise = min(exercise_popularity, key=exercise_popularity.get)

    print(f"The most popular exercise is: {most_popular_exercise} with {exercise_popularity[most_popular_exercise]} log entries.")
    print(f"The least popular exercise is: {least_popular_exercise} with {exercise_popularity[least_popular_exercise]} log entries.")
    
def create_log():
    try:
        user = input("User ID: ")
        exercise = input("Exercise ID: ")
        date = input("Date (YYYY-MM-DD): ")

        log = Log.create(user, exercise, date)
        print("Log created successfully.")
    except Exception as exc:
        print("Error creating new log: ", exc)

def list_logs():
    logs = Log.get_all()
    for log in logs:
        print(log)

def get_log_by_id():
    log_id = input("Log ID: ")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        print(log) if log else print(f"Log with ID {log_id} not found")
    except:
        print(f"Invalid Log ID: {log_id}")

def update_log_by_id():
    log_id = input("Log ID: ")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        if log:
            collect_log_updates(log)
        else:
            print(f"Log with ID {log_id} not found")
    except:
        print(f"Invalid Log ID: {log_id}")

def collect_log_updates(log):
    try:
        date = input(f"New date for Log ID {log.id} (YYYY-MM-DD): ")
        log.date = date
        log.update()
        print(f"Log entry updated successfully for Log ID {log.id}.")
    except Exception as exc:
        print(f"Error updating log entry: {exc}")

def delete_log_by_id():
    log_id = input("Log ID: ")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        if log:
            Log.delete(log)
            print(f"Log entry with ID {log.id} deleted successfully.")
        else:
            print(f"Log with ID {log_id} not found")
    except:
        print(f"Invalid Log ID: {log_id}")


def exit_program():
    print("See you next time for another workout!")
    exit()
