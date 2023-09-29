# lib/helpers.py
from models.exercise import Exercise
from models.log import Log
from models.user import User
# from rich import print
# from rich.console import Console
# from rich.table import Table
logged_in_user_id = [0]
open = "\033[36m" ##blue
close = "\33[0m"
def create_exercise():
#  category not in Exercise.CATEGORY 
#  intensity not in Exercise.INTENSITY and 
    print(f"{open} Create Exercise {close}")
    name = input(f"{open} Enter Exercise: {close}")
    while not isinstance(name, str) or len(name) >= 20:
        print( "\033[31m Name must be greater than 0 and less than or equal to 20 characters.\33[0m")
        name = input(f"{open} Exercise: {close}")
    time = input(f"{open} Duration (in minutes):{close} ")
    try:
        time = int(time)
    except:
        print("\033[31m Duration must be a number \33[0m")
        time = input(f"{open} Duration (in minutes): {close}")
    category = input(f"{open} Choose a category [1] Cardio, [2] Strength: {close}")
    try:
        if int(category) not in range(1, len(Exercise.CATEGORY)+1):
            print("\033[31m  Enter a number that represents the exercise category \033[0m")
            category = input(f"{open} Choose a category [1] Cardio, [2] Strength: {close}")
    except ValueError:
        print("\033[31m  Enter a number the represents the exercise category \033[0m")
        category = input(f"{open} Choose a category [1] Cardio, [2] Strength: {close}")
    intensity = input(f"{open} Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): {close}")
    while int(intensity) not in range(1, len(Exercise.INTENSITY)+1):
        print("\033[31m Enter a number that represents the exercise intensity \033[0m")
        intensity = input(f"{open} Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): {close}")
    cals_burned = input(f"{open} Calories Burned: {close}")
    try:
        cals_burned = int(cals_burned)
    except:
        print("\033[31m Enter a number for calories burned \033[0m")
        cals_burned = input(f" {open} Calories Burned: {close}")
    # Allow choices to be numbers
    if category not in Exercise.CATEGORY and 0 < int(category) <=len(Exercise.CATEGORY):
        category = Exercise.CATEGORY[int(category) - 1]
    if intensity not in Exercise.INTENSITY and 0 < int(intensity) <= len(Exercise.INTENSITY):
        intensity = Exercise.INTENSITY[int(intensity) -1]
    try:
        exercise = Exercise.create(name, time, category, intensity, cals_burned)
        print(f"\033[32m Success: {exercise.name} is now available!\033[0m 🏃🏻‍♂️")
    except Exception as exc:
        print("\033[31m Error creating new exercise: \033[0m", exc)

def list_exercises():
    print("\033[34m Exercises \033[0m")
    print("\033[35m ID | Exercise | Duration | Category | Intensity | Calories Burned \033[0m")
    exercises = Exercise.get_all()
    for exercise in exercises:
        print(exercise)
    exercise_names = []
    for exercise in exercises:
        exercise_names.append(exercise.name)
def get_exercise_by_name_or_id():
    print(f"{open} Search for Exercise {close}")
    name = input(f"{open} Exercise or ID: {close}")
    try:
        id_ = int(name)
        exercise = Exercise.find_by_id(id_)
        print(f"{open} ID | Exercise | Duration | Category | Intensity | Calories Burned\n{exercise}{close}") if exercise else print(f"\033[31m Exercise {name} not found \033[0m")
    except:
        exercise = Exercise.find_by_name(name.title()) # .title() to allow for case insensitive
        print(f"{open} ID | Exercise | Duration | Category | Intensity | Calories Burned\n{exercise}{close}") if exercise else print(f"\033[31m Exercise {name} not found \033[0m")
def update_exercise_by_name_or_id():
    print(f"{open}Update Exercise{close}")
    name = input(f"{open}Exercise or ID:{close}")
    try:
        id_ = int(name)
        exercise = Exercise.find_by_id(id_)
        collect_updates(exercise)
    except:
        try:
            exercise = Exercise.find_by_name(name.title())
            collect_updates(exercise)
        except Exception as exc:
            print("\033[31m Error updating exercise \033[0m", exc)
def collect_updates(exercise):
        # Update exercise instance
        name = input(f"\033[33m{exercise.name} new name: \033[0m")
        exercise.name = name
        time = input(f"\033[33m{exercise.name} new time: \033[0m")
        exercise.time = time
        category = input(f"\033[33m{exercise.name} new category (Cardio = 1, Strength = 2): \033[0m")
        # exercise.category = category
        intensity = input(f"\033[33m{exercise.name} new intensity (Beginner = 1, Intermediate = 2, Advanced = 3): \033[0m")
        # exercise.intensity = intensity
        cals_burned = input(f"\033[33m{exercise.name} new calories burned: \033[0m")
        exercise.cals_burned = cals_burned
        # Allow choices to be numbers
        if category not in Exercise.CATEGORY and 0 < int(category) <= len(Exercise.CATEGORY):
            exercise.category = Exercise.CATEGORY[int(category) - 1]
        if intensity not in Exercise.INTENSITY and 0 < int(intensity) <= len(Exercise.INTENSITY):
            exercise.intensity = Exercise.INTENSITY[int(intensity) -1]        
        """ Exercise instance updated in database with .update() """
        exercise.update()
        print(f"\033[32m{exercise.name} has been updated!\033[0m") if exercise else print(f"\033[31mExercise {name} not found\033[0m")
def delete_exercise_by_name_or_id():
    print(f"{open}Delete Exercise{close}")
    name_or_id = input(f"{open} Exercise or ID: {close}")
    deleted_exercise = "deleted exercise"
    try:
        id_ = int(name_or_id)
        exercise = Exercise.find_by_id(id_)
        Exercise.delete(exercise)
        print(f"\033[32m{exercise.name} has been deleted\033[0m") if exercise else print(f"\033[31mExercise {exercise.name} not found\033[0m")
    except:
        try:
            exercise = Exercise.find_by_name(name_or_id.title())
            Exercise.delete(exercise)
            print(f"\033[32m{exercise.name} has been deleted\033[0m") if exercise else print(f"\033[31mExercise {exercise.name} not found\033[0m")
        except Exception as exc:
            print("\033[31mError deleting exercise\033[0m")
            
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
    print(f"{open}The most popular exercise is: {most_popular_exercise} with {exercise_popularity[most_popular_exercise]} log entries.{close}")
    print(f"{open}The least popular exercise is: {least_popular_exercise} with {exercise_popularity[least_popular_exercise]} log entries.{close}")
    
def create_log():
    print(f"{open} New Workout Entry{close}")
    try:
        user_id = input(f"{open} User ID: {close}")
        exercise_id = input(f"{open} Exercise ID: {close}")
        date = input(f"{open} Date (YYYY-MM-DD): {close}")
        user_instance = User.find_by_id(user_id)
        exercise_instance = Exercise.find_by_id(exercise_id)
        log = Log.create(user_instance, exercise_instance, date)
        print("\033[32mLog created successfully.\033[0m")
    except Exception as exc:
        print("\033[31mError creating new log: \033[0m", exc)
def list_logs():
    print(f"{open}Logs{close}")
    # logs = Log.get_all()
    # for log in logs:
    #     print(log)
    Log.get_all()
def get_log_by_id():
    print(f"{open} Get Log by ID {close}")
    log_id = input(f"{open} Log ID: {close}")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        print(f"\033[35mDate | User | Exercise\n{log.date} | {log.user.name} | {log.exercise.name}\033[0m") if log else print(f"\033[31mLog with ID {log_id} not found\033[0m")
    except:
        print(f"\033[31mInvalid Log ID: {log_id}\033[0m")
def update_log_by_id():
    print(f"{open} Update Log Date by ID{close}")
    log_id = input(f"{open}Log ID: {close}")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        if log:
            collect_log_updates(log)
        else:
            print(f"\033[31mLog with ID {log_id} not found\033[0m")
    except:
        print(f"\033[31mInvalid Log ID: {log_id}\033[0m")
def collect_log_updates(log):
    try:
        date = input(f"{open}New date for Log ID {log.id} (YYYY-MM-DD): {close}")
        log.date = date
        log.update()
        print(f"\033[32mLog entry updated successfully for Log ID {log.id}.\033[0m")
    except Exception as exc:
        print(f"\033[31mError updating log entry: {exc}\033[0m")
def delete_log_by_id():
    print(f"{open}Delete Log by ID{close}")
    log_id = input(f"{open}Log ID: {close}")
    try:
        id_ = int(log_id)
        log = Log.find_by_id(id_)
        if log:
            Log.delete(log)
            print(f"\033[32mLog entry with ID {log_id} deleted successfully.\033[0m")
        else:
            print(f"\033[31mLog with ID {log_id} not found\033[0m")
    except:
        print(f"\033[31mInvalid Log ID: {log_id}\033[0m")

def exit_program():
    print("\033[37mSee you next time for another workout!\033[0m")
    exit()
def show_popular():
    Exercise.most_popular()
def least_popular():
    Exercise.least_popular()
def list_users():
    print(f"{open}Users{close}")
    print("\033[35mID | User | Height | Weight (lbs)\033[0m")
    users = User.get_all()
    for user in users:
        print(user)
def create_user():
    print(f"{open}Register new user{close}")
    name = input(f"{open}Name: {close}")
    
    try:
        search_for_user = User.find_by_name(name)
        if search_for_user.name == name:
            print(f"\033[31mError creating new user. User already exists.\033[0m \033[37m\nWelcome back, {search_for_user.name}!\033[0m ")
            logged_in_user_id[0] = search_for_user.id
    except:
        height = input(f"{open}Height (inches): {close}")
        weight = input(f"{open}Weight (lbs): {close}")
        # Convert height to feet and inches
        height = int(height)
        height_ft = round(height/12)
        height_inches = height - height_ft * 12
        weight = int(weight)
        try:
            
            user = User.create_user(name, height_ft, height_inches, weight)
            print(f"\033[37mWelcome to PyFit, {user.name}!\033[0m")
            logged_in_user_id[0] = user.id
        except Exception as exc:
            print("\033[31mError creating new user: \033[0m", exc)
def login_user():
    print(f"{open}Login User{close}")
    user_status = input(f"{open}New User? [y/n] {close}")
    if user_status == "y":
        create_user()
    elif user_status == "n":
        name = input(f"{open}Name: {close}")
        try:
            user = User.find_by_name(name)
            logged_in_user_id[0] = user.id
            print(f"\033[37mWelcome back, {user.name}!\033[0m")
        except:
            raise Exception("\033[31mUnable to find user. Please try again.\033[0m")
    else:
        print("\033[31mInvalid menu selection\033[0m")
def get_user_logs():
    print(f"{open}Get User Logs{close}")
    name = input(f"{open}Name: {close}")
    try:
        log = Log.find_by_name(name)
        print(f"\033[35mDate | User | Exercise\n{log.date} | {log.user.name} | {log.exercise.name}\033[0m") if log else print(f"\033[31mLogs for {name} not found\033[0m")
    except:
        print(f"\033[31mInvalid name\033[0m")
def get_my_info():
    print(f"{open}My Info{close}")
    my_info = User.find_by_id(logged_in_user_id[0])
    print("\033[35mID | User | Height | Weight (lbs)\033[0m")
    print(my_info)
