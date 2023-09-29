# lib/helpers.py

from models.exercise import Exercise
from models.log import Log
from models.user import User

# from rich import print
# from rich.console import Console
# from rich.table import Table

logged_in_user_id = [0]
open = "\033[34m"
close = "\33[0m"

def create_exercise():
#  category not in Exercise.CATEGORY 
#  intensity not in Exercise.INTENSITY and 
    print("Create Exercise")
    name = input(f"{open} Enter Exercise: {close}")
    while not isinstance(name, str) or len(name) >= 20:
        print("Name must be greater than 0 and less than or equal to 20 characters.")
        name = input("Exercise: ")
    time = input("Duration (in minutes): ")
    try:
        time = int(time)
    except:
        print("Duration must be a number")
        time = input("Duration (in minutes): ")
    category = input("Choose a category [1] Cardio, [2] Strength: ")
    try:
        if int(category) not in range(1, len(Exercise.CATEGORY)+1):
            print("Enter a number the represents the exercise category")
            category = input("Choose a category [1] Cardio, [2] Strength: ")
    except ValueError:
        print("Enter a number the represents the exercise category")
        category = input("Choose a category [1] Cardio, [2] Strength: ")
    intensity = input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): ")
    while int(intensity) not in range(1, len(Exercise.INTENSITY)+1):
        print("Enter a number that represents the exercise intensity")
        intensity = input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): ")
    cals_burned = input("Calories Burned: ")
    try:
        cals_burned = int(cals_burned)
    except:
        print("Enter a number for calories burned")
        cals_burned = input("Calories Burned: ")

    # Allow choices to be numbers
    if category not in Exercise.CATEGORY and 0 < int(category) <=len(Exercise.CATEGORY):
        category = Exercise.CATEGORY[int(category) - 1]
    if intensity not in Exercise.INTENSITY and 0 < int(intensity) <= len(Exercise.INTENSITY):
        intensity = Exercise.INTENSITY[int(intensity) -1]

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
        if category not in Exercise.CATEGORY and 0 < int(category) <= len(Exercise.CATEGORY):
            exercise.category = Exercise.CATEGORY[int(category) - 1]
        if intensity not in Exercise.INTENSITY and 0 < int(intensity) <= len(Exercise.INTENSITY):
            exercise.intensity = Exercise.INTENSITY[int(intensity) -1]        

        """ Exercise instance updated in database with .update() """
        exercise.update()
        print(f"{exercise.name} has been updated!") if exercise else print(f"Exercise {name} not found")

# def delete_exercise_by_name_or_id():
#     print("Delete Exercise")
#     name_or_id = input("Exercise or ID: ")
#     deleted_exercise = "deleted exercise"

#     try:
#         id_ = int(name_or_id)
#         exercise = Exercise.find_by_id(id_)
#         Exercise.delete(exercise)
#         print(f"{exercise.name} has been deleted") if exercise else print(f"Exercise {exercise.name} not found")
#     except:
#         try:
#             exercise = Exercise.find_by_name(name_or_id.title())
#             Exercise.delete(exercise)
#             print(f"{exercise.name} has been deleted") if exercise else print(f"Exercise {exercise.name} not found")
#         except Exception as exc:
#             print("Error deleting exercise")
            
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
    
def delete_exercise_with_logs():
    print("Delete Exercise with Logs")
    name_or_id = input("Exercise or ID: ")

    try:
        id_ = int(name_or_id)
        exercise = Exercise.find_by_id(id_)
    except ValueError:
        exercise = Exercise.find_by_name(name_or_id.title())

    if exercise:
        # Find and delete logs associated with the exercise
        logs = Log.find_by_exercise(exercise)
        for log in logs:
            Log.delete(log)

        # Delete the exercise itself
        Exercise.delete(exercise)
        print(f"{exercise.name} and its associated logs have been deleted")
    else:
        print(f"Exercise {name_or_id} not found")
    
def create_log():
    print("New Workout Entry")
    try:
        user_id = input("User ID: ")
        exercise_identifier = input("Exercise ID or Name: ")
        date = input("Date (YYYY-MM-DD): ")

        user_instance = User.find_by_id(user_id)

        # Check if the exercise exists either by ID or name
        exercise_instance = Exercise.find_by_id(exercise_identifier)
        if not exercise_instance:
            exercise_instance = Exercise.find_by_name(exercise_identifier.title())

        if not exercise_instance:
            print("Invalid exercise. Please enter a valid exercise ID or name.")
        else:
            # Create the log with the valid exercise
            log = Log.create(user_instance, exercise_instance, date)
            print(f"{log} created successfully.")
    except Exception as exc:
        print("Error creating new log:", exc)

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

# def create_user():
#     print("Register new user")
#     name = input("Name: ")
    
#     try:
#         search_for_user = User.find_by_name(name)
#         if search_for_user.name == name:
#             print(f"Error creating new user. User already exists.\nWelcome back, {search_for_user.name}!")
#             logged_in_user_id[0] = search_for_user.id

#     except:
#         height = input("Height (inches): ")
#         weight = input("Weight (lbs): ")
#         # Convert height to feet and inches
#         height = int(height)
#         height_ft = round(height/12)
#         height_inches = height - height_ft * 12

#         weight = int(weight)

#         try:
            
#             user = User.create_user(name, height_ft, height_inches, weight)
#             print(f"Welcome to PyFit, {user.name}!")
#             logged_in_user_id[0] = user.id
#         except Exception as exc:
#             print("Error creating new user: ", exc)

def create_user():
    print("Register new user")
    name = input("Name: ")
    height_ft = input("Height (feet): ")
    height_inches = input("Height (inches): ")
    weight = input("Weight (lbs): ")

    try:
        # Convert height to feet and inches
        height_ft = int(height_ft)
        height_inches = int(height_inches)

        user = User.create_user(name, height_ft, height_inches, weight)
        print(f"Welcome to PyFit, {user.name}!")
        logged_in_user_id[0] = user.id
    except Exception as exc:
        print("Error creating new user: ", exc)


def login_user():
    print("Login User")
    user_status = input("New User? [y/n] ")
    if user_status == "y":
        create_user()
    elif user_status == "n":
        name = input("Name: ")
        try:
            user = User.find_by_name(name)
            logged_in_user_id[0] = user.id
            print(f"Welcome back, {user.name}!")
        except:
            raise Exception("Unable to find user. Please try again.")
    else:
        print("Invalid menu selection")

# def get_user_logs():
#     print("Get User Logs")
#     name = input("Name: ")
#     try:
#         log = Log.find_by_name(name)
#         print(f"Date | User | Exercise\n{log.date} | {log.user.name} | {log.exercise.name}") if log else print(f"Logs for {name} not found")
#     except:
#         print(f"Invalid name")

# def get_my_info():
#     print("My Info")
#     my_info = User.find_by_id(logged_in_user_id[0])
#     print("ID | User | Height | Weight (lbs)")
#     print(my_info)

def get_my_info():
    print("My Info")
    my_info = User.find_by_id(logged_in_user_id[0])
    print("ID | User | Height | Weight (lbs)")
    print(my_info)

    # Display the most recent workout for the user
    get_user_recent_workout(my_info)
    
def get_user_workout_history():
    print("Get User Workout History")
    user_name_or_id = input("Enter user's name or ID: ")

    try:
        # Try to convert the input to an integer; if successful, it's an ID.
        user_identifier = int(user_name_or_id)

        user = User.find_by_id(user_identifier)
        if user:
            logs = Log.find_by_user(user)
            if logs:
                print(f"Workout History for {user.name}")
                print("Date | Exercise")
                for log in logs:
                    print(f"{log.date} | {log.exercise.name}")
            else:
                print(f"No workout history found for {user.name}")
        else:
            print(f"User with ID {user_identifier} not found")
    except ValueError:
        # If the input couldn't be converted to an integer, assume it's a name.
        user = User.find_by_name(user_name_or_id)
        if user:
            logs = Log.find_by_user(user)
            if logs:
                print(f"Workout History for {user.name}")
                print("Date | Exercise")
                for log in logs:
                    print(f"{log.date} | {log.exercise.name}")
            else:
                print(f"No workout history found for {user.name}")
        else:
            print(f"User '{user_name_or_id}' not found")
    except Exception as exc:
        print("Error getting workout history:", exc)
        
def get_user_recent_workout(user):
    print(f"Most Recent Workout for {user.name}")
    
    # Find the most recent workout log for the user
    recent_log = None
    recent_date = None
    
    for log in Log.find_by_user(user):
        if recent_date is None or log.date > recent_date:
            recent_log = log
            recent_date = log.date
    
    if recent_log:
        print(f"Date: {recent_log.date}")
        print(f"Exercise: {recent_log.exercise.name}")
    else:
        print("No workout history found for this user.")


    
