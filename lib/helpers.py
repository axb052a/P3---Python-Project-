# lib/helpers.py
from models.exercise import Exercise
from models.log import Log
from models.user import User

logged_in_user_id = [0]
open = "\033[36m" ##blue
close = "\33[0m"
cardio_emoji = "🏃🏻‍♂️"
strength_emoji = "🏋🏻‍♂️"
congrats_emoji = "🎉"
waving_emoji = "👋"

def create_exercise():
    print("Create Exercise")
    while True:
        try:
            name = input(f"{open}Enter Exercise: {close}")
            if isinstance(name, str) and 0 < len(name) <= 20:
                name = name.title()
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
            category = input("Choose a category [1] Cardio, [2] Strength: ")
            if category.title() in Exercise.CATEGORY:
                category = category.title()
                break
            elif int(category) in range(1, len(Exercise.CATEGORY) +1):
                category = Exercise.CATEGORY[int(category) - 1]
                break
        except ValueError:
            print("Enter a number or choose category that corresponds to the exercise category")  
    while True:
        try:
            intensity = input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): ")
            if intensity.title() in Exercise.INTENSITY:
                intensity = intensity.title()
                break
            elif int(intensity) in range(1, len(Exercise.INTENSITY) +1):
                intensity = Exercise.INTENSITY[int(intensity) -1]
                break
        except ValueError:
            print("Enter a number or choose level that corresponds to the exercise intensity")
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
        if exercise.category == "Cardio":
            print(f"Success: {exercise.name} is now available! {cardio_emoji}")
        elif exercise.category == "Strength":
            print(f"Success: {exercise.name} is now available! {strength_emoji}")
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
    while True:
        try:
            name = input(f"{open}Update {exercise.name}: {close}")
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
            category = input("Choose a category [1] Cardio, [2] Strength: ")
            if category.title() in Exercise.CATEGORY:
                exercise.category = category.title()
                break
            elif int(category) in range(1, len(Exercise.CATEGORY) +1):
                exercise.category = Exercise.CATEGORY[int(category) - 1]
                break
        except ValueError:
            print("Enter a number or choose category that corresponds to the exercise category")  
    while True:
        try:
            intensity = input("Choose an intensity [1] Beginner, [2] Intermediate, [3] Advanced): ")
            if intensity.title() in Exercise.INTENSITY:
                exercise.intensity = intensity.title()
                break
            elif int(intensity) in range(1, len(Exercise.INTENSITY) +1):
                exercise.intensity = Exercise.INTENSITY[int(intensity) -1]
                break
        except ValueError:
            print("Enter a number or choose level that corresponds to the exercise intensity")
    while True:
        try:
            cals_burned = int(input("Calories Burned: "))
            if 0 < cals_burned:
                exercise.cals_burned = cals_burned
                break
        except ValueError:
            print("Calories burned must be a number")     

    """ Exercise instance updated in database with .update() """
    Exercise.update(exercise)
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
    print(f"{open}The most popular exercise is: {most_popular_exercise} with {exercise_popularity[most_popular_exercise]} log entries.{close}")
    print(f"{open}The least popular exercise is: {least_popular_exercise} with {exercise_popularity[least_popular_exercise]} log entries.{close}")
    
def delete_exercise_with_logs():
    print(f"{open}Delete Exercise with Logs{close}")
    name_or_id = input(f"{open}Exercise or ID: {close}")

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
        print(f"\033[32m{exercise.name} and its associated logs have been deleted\033[0m")
    else:
        print(f"\033[31mExercise {name_or_id} not found\033[0m")
    
def create_log():
    print(f"{open} New Workout Entry{close}")
    try:
        user_id = input(f"{open} User ID: {close}")
        exercise_id = input(f"{open} Exercise ID or Name: {close}")
        date = input(f"{open} Date (YYYY-MM-DD): {close}")

        user_instance = User.find_by_id(user_id)

 # Something might need to be updated
        log = Log.create(user_instance, exercise_instance, date)
        print(f"Log created successfully. {congrats_emoji}")

        # Check if the exercise exists either by ID or name
        exercise_instance = Exercise.find_by_id(exercise_identifier)
        if not exercise_instance:
            exercise_instance = Exercise.find_by_name(exercise_identifier.title())


        if not exercise_instance:
            print("\033[31mInvalid exercise. Please enter a valid exercise ID or name.\033[0m")
        else:
            # Create the log with the valid exercise
            log = Log.create(user_instance, exercise_instance, date)
            print("\033[32m{log} created successfully.\033[0m")
    except Exception as exc:
        print("\033[31mError creating new log: \033[0m", exc)

def list_logs():
    print(f"{open}Logs{close}")
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
    print("\033[37mSee you next time for another workout! {waving_emoji} \033[0m")
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
    height_ft = input(f"{open}Height (feet): {close}")
    height_inches = input(f"{open}Height (inches): {close}")
    weight = input(f"{open}Weight (lbs): {close}")

    try:
        # Convert height to feet and inches
        height_ft = int(height_ft)
        height_inches = int(height_inches)

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

def get_my_info():
    print(f"{open}My Info{close}")
    my_info = User.find_by_id(logged_in_user_id[0])
    print("\033[35mID | User | Height | Weight (lbs)\033[0m")
    print(my_info)

    # Display the most recent workout for the user
    get_user_recent_workout(my_info)
    
def get_user_workout_history():
    print(f"{open}Get User Workout History{close}")
    user_name_or_id = input(f"{open}Enter user's name or ID: {close}")

    try:
        # Try to convert the input to an integer; if successful, it's an ID.
        user_identifier = int(user_name_or_id)

        user = User.find_by_id(user_identifier)
        if user:
            logs = Log.find_by_user(user)
            if logs:
                print(f"{open}Workout History for {user.name}{close}")
                print("\033[35mDate | Exercise\033[0m")
                for log in logs:
                    print(f"\033[35m{log.date} | {log.exercise.name}\033[0m")
            else:
                print(f"\033[31mNo workout history found for {user.name}\033[0m")
        else:
            print(f"\033[31mUser with ID {user_identifier} not found\033[0m")
    except ValueError:
        # If the input couldn't be converted to an integer, assume it's a name.
        user = User.find_by_name(user_name_or_id)
        if user:
            logs = Log.find_by_user(user)
            if logs:
                print(f"{open}Workout History for {user.name}{close}")
                print("\033[35mDate | Exercise\033[0m")
                for log in logs:
                    print(f"\033[35m{log.date} | {log.exercise.name}\033[0m")
            else:
                print(f"\033[31mNo workout history found for {user.name}\033[0m")
        else:
            print(f"\033[31mUser '{user_name_or_id}' not found\033[0m")
    except Exception as exc:
        print("\033[31mError getting workout history:\033[0m", exc)
        
def get_user_recent_workout(user):
    print(f"{open}Most Recent Workout for {user.name}{close}")
    
    # Find the most recent workout log for the user
    recent_log = None
    recent_date = None
    
    for log in Log.find_by_user(user):
        if recent_date is None or log.date > recent_date:
            recent_log = log
            recent_date = log.date
    
    if recent_log:
        print(f"{open}Date: {recent_log.date}{close}")
        print(f"{open}Exercise: {recent_log.exercise.name}{close}")
    else:
        print("\033[31mNo workout history found for this user.\033[0m")

