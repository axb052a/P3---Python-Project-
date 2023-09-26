# lib/cli.py

import time
import sys
from models.exercise import Exercise

from helpers import (
    exit_program,
    helper_1,
    create_exercise,
    list_exercises
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            create_exercise()
        elif choice == "3":
            print("Exercise List:")
            list_exercises()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Create exercise")
    print("3. Show Exercises")

def welcome_menu():
    print("User Login")
    print("New User")
    print("Exit App")


if __name__ == "__main__":
    print("Welcome to PyFit! Track your fitness journey to help you reach your goals.")
    main()



