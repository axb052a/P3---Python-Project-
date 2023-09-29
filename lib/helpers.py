# lib/helpers.py

from models.exercise import Exercise
from models.log import Log
from models.user import User

logged_in_user_id = [0]
open = "\033[34m"
close = "\33[0m"

def create_exercise():
    print("Create Exercise")
    while True:
        try:
            name = input(f"{open} Enter Exercise: {close}")
            if isinstance(name, str) and 0 < len(name) <= 20:
                name.title()
                break
        except:
            raise Exception("Name must be greater than 0 and less than or equal to 20 characters.")   
    while True:
        try:
            time = int(input("Duration (in minutes): "))
            if 0 < time:
                time
                break
        except ValueError:
            print("Duration must be a number")   
    while True:
        try:
            category = int(input("Choose a category [1] Cardio, [2] Strength: "))
            if category in range(1, len(Exercise.CATEGORY) +1):
                category = Exercise.CATEGORY[category - 1]
                break
        except ValueError:
            print("Enter a number that corresponds to the exercise category")
    while True:
        try:
            intensity = int(input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): "))
            if intensity in range(1, len(Exercise.INTENSITY) +1):
                intensity = Exercise.INTENSITY[intensity -1]
                break
        except ValueError:
            print("Enter a number that corresponds to the exercise intensity")
    while True:
        try:
            cals_burned = int(input("Calories Burned: "))
            if 0 < cals_burned:
                cals_burned
                break
        except ValueError:
            print("Calories burned must be a number") 

    try:
        exercise = Exercise.create(name, time, category, intensity, cals_burned)
        print(f"Success: {exercise.name} is now available! 🏃🏻‍♂️")
    except Exception as exc:
        print("Error creating new exercise: ", exc)


def list_exercises():
    print("Exercises")
    print("ID | Exercise | Duration | Category | Intensity | Calories Burned")
    exercises = Exercise.get_all()
    for exercise in exercises:
        print(exercise)

    exercise_names = []
    for exercise in exercises:
        exercise_names.append(exercise.name)

def get_exercise_by_name_or_id():
    print("Search for Exercise")
    name = input("Exercise or ID: ")
    try:
        id_ = int(name)
        exercise = Exercise.find_by_id(id_)
        print(f"ID | Exercise | Duration | Category | Intensity | Calories Burned\n{exercise}") if exercise else print(f"Exercise {name} not found")
    except:
        exercise = Exercise.find_by_name(name.title()) # .title() to allow for case insensitive
        print(f"ID | Exercise | Duration | Category | Intensity | Calories Burned\n{exercise}") if exercise else print(f"Exercise {name} not found")

def update_exercise_by_name_or_id():
    print("Update Exercise")
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
    while True:
        try:
            name = input(f"{open} Update {exercise.name}: {close}")
            if isinstance(name, str) and 0 < len(name) <= 20:
                exercise.name = name.title()
                break
        except:
            raise Exception("Name must be greater than 0 and less than or equal to 20 characters.")   
    while True:
        try:
            time = int(input("Duration (in minutes): "))
            if 0 < time:
                exercise.time = time
                break
        except ValueError:
            print("Duration must be a number")   
    while True:
        try:
            category = int(input("Choose a category [1] Cardio, [2] Strength: "))
            if category in range(1, len(Exercise.CATEGORY) +1):
                exercise.category = Exercise.CATEGORY[category - 1]
                break
        except ValueError:
            print("Enter a number that corresponds to the exercise category")
    while True:
        try:
            intensity = int(input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): "))
            if intensity in range(1, len(Exercise.INTENSITY) +1):
                exercise.intensity = Exercise.INTENSITY[intensity - 1]
                break
        except ValueError:
            print("Enter a number that corresponds to the exercise intensity")
    while True:
        try:
            cals_burned = int(input("Calories Burned: "))
            if 0 < cals_burned:
                exercise.cals_burned = cals_burned
                break
        except ValueError:
            print("Calories burned must be a number")     

    """ Exercise instance updated in database with .update() """
    exercise.update()
    print(f"{exercise.name} has been updated!") if exercise else print(f"Exercise {name} not found")

def delete_exercise_by_name_or_id():
    print("Delete Exercise")
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
        log_entries = Log.find_by_id(exercise)
        exercise_popularity[exercise.name] = len(log_entries)

    # Find the most and least popular exercises
    most_popular_exercise = max(exercise_popularity, key=exercise_popularity.get)
    least_popular_exercise = min(exercise_popularity, key=exercise_popularity.get)

    print(f"The most popular exercise is: {most_popular_exercise} with {exercise_popularity[most_popular_exercise]} log entries.")
    print(f"The least popular exercise is: {least_popular_exercise} with {exercise_popularity[least_popular_exercise]} log entries.")
    
def create_log():
    print("New Workout Entry")
    try:
        user_id = input("User ID: ")
        exercise_id = input("Exercise ID: ")
        date = input("Date (YYYY-MM-DD): ")

        user_instance = User.find_by_id(user_id)
        exercise_instance = Exercise.find_by_id(exercise_id)

        log = Log.create(user_instance, exercise_instance, date)
        print("Log created successfully.")

    except Exception as exc:
        print("Error creating new log: ", exc)

def list_logs():
    print("Logs")
    # logs = Log.get_all()
    # for log in logs:
    #     print(log)
    Log.get_all()

def get_log_by_id():
    print("Get Log by ID")
    log_id = input("Log ID: ")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        print(f"Date | User | Exercise\n{log.date} | {log.user.name} | {log.exercise.name}") if log else print(f"Log with ID {log_id} not found")
    except:
        print(f"Invalid Log ID: {log_id}")

def update_log_by_id():
    print("Update Log Date by ID")
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
    print("Delete Log by ID")
    log_id = input("Log ID: ")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        if log:
            Log.delete(log)
            print(f"Log entry with ID {log_id} deleted successfully.")
        else:
            print(f"Log with ID {log_id} not found")
    except:
        print(f"Invalid Log ID: {log_id}")


def exit_program():
    print("See you next time for another workout!")
    exit()

def show_popular():
    Exercise.most_popular()

def least_popular():
    Exercise.least_popular()

def list_users():
    print("Users")
    print("ID | User | Height | Weight (lbs)")
    users = User.get_all()
    for user in users:
        print(user)

def create_user():
    print("Register new user")
    name = input("Name: ")
    
    try:
        search_for_user = User.find_by_name(name)
        if search_for_user.name == name:
            print(f"Error creating new user. User already exists.")
            logged_in_user_id[0] = search_for_user.id

    except:
        height = input("Height (inches): ")
        weight = input("Weight (lbs): ")
        # Convert height to feet and inches
        height = int(height)
        height_ft = round(height/12)
        height_inches = height - height_ft * 12

        weight = int(weight)

        try:
            user = User.create_user(name, height_ft, height_inches, weight)
            print(f"Welcome to PyFit, {user.name}!")
            logged_in_user_id[0] = user.id
        except Exception as exc:
            print("Error creating new user: ", exc)

def login_user():
    name = input("Name: ")
    user = User.find_by_name(name)
    if user == None:
        print("Unable to find user. [x] Return to Home")
    else:
        logged_in_user_id[0] = user.id
        print(f"Welcome back, {user.name} (ID: {user.id})!")

def get_user_logs():
    print("Get User Logs")
    user = User.find_by_id(logged_in_user_id[0])
    try:
        Log.find_by_name(user.name)
    except:
        print(f"Invalid name")

def get_my_info():
    print("My Info")
    my_info = User.find_by_id(logged_in_user_id[0])
    print("ID | User | Height | Weight (lbs)")
    print(my_info)
