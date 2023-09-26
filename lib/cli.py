# lib/cli.py

from models.exercise import Exercise

from helpers import (
    exit_program,
    helper_1,
    create_exercise,
    list_exercises
)


def main():
    while True:
        home_menu()
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "1":
            while True:
                user_menu()
                choice = input("> ")
                if choice == "1":
                    print("My Info")
                if choice == "2":
                    print("My Stats")
                if choice == "3":
                    print("Workout History")
                if choice == "x":
                    main()
                else:
                    print("Invalid choice user_menu")
        elif choice == "2":
            print("New User")
        elif choice == "3":
            while True:
                exercise_menu()
                choice = input("> ")
                if choice == "1":
                    list_exercises()
                if choice == "2":
                    print("Exercise Stats")
                if choice == "3":
                    create_exercise()
                if choice == "x":
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
    print("[3] Create Exercise")
    print("[x] Return to Home")


if __name__ == "__main__":
    print("Welcome to PyFit! Track your fitness journey to help you reach your goals.")
    main()



