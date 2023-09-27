# lib/cli.py

from models.exercise import Exercise

from helpers import (
    exit_program,
    helper_1,
    create_exercise,
    list_exercises,
    get_exercise_by_name_or_id,
    update_exercise_by_name_or_id,
    delete_exercise_by_name_or_id
)


def main():
    home_menu()
    while True:
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "1":
            user_menu()
            while True:
                choice = input("> ")
                if choice == "1":
                    print("My Info")
                elif choice == "2":
                    print("My Stats")
                elif choice == "3":
                    print("Workout History")
                elif choice == "x":
                    main()
                else:
                    print("Invalid choice user_menu")
        elif choice == "2":
            print("New User")
        elif choice == "3":
            exercise_menu()
            while True:
                choice = input("> ")
                if choice == "1":
                    list_exercises()
                elif choice == "2":
                    print("Exercise Stats")
                elif choice == "3":
                    get_exercise_by_name_or_id()
                elif choice == "4":
                    update_exercise_by_name_or_id()                    
                elif choice == "5":
                    delete_exercise_by_name_or_id()
                elif choice == "6":
                    create_exercise()
                elif choice == "x":
                    main()
                else:
                    print("Invalid choice exercise_menu")
        else:
            print("Invalid choice")

def home_menu():
    print("Please select an option:")
    print("[1] User Login")
    print("[2] New User")
    print("[3] Exercises")
    print("[x] Exit App")

def user_menu():
    print("Please select an option:")
    print("[1] My Info")
    print("[2] My Stats")
    print("[3] Workout History")
    print("[x] Log Out")

def exercise_menu():
    print("Please select an option:")
    print("[1] Exercises")
    print("[2] Exercise Stats")
    print("[3] Search for Exercise")
    print("[4] Update Exercise")  
    print("[5] Delete Exercise")      
    print("[6] Create Exercise")
    print("[x] Return to Home")

def exercise_search_menu():
    print("Please select an option:")
    print("[1] ID")
    print("[2] Name")
    print("[3] Time")
    print("[4] Category")
    print("[5] Intensity")
    print("[6] Calories Burned")
    print("[x] Return to Exercise Menu")

if __name__ == "__main__":
    print("Welcome to PyFit! Track your fitness journey to help you reach your goals.")
    main()



