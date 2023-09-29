# lib/cli.py
from models.exercise import Exercise
from models.log import Log
from helpers import (
    exit_program,
    create_exercise,
    list_exercises,
    get_exercise_by_name_or_id,
    update_exercise_by_name_or_id,
    delete_exercise_by_name_or_id,
    delete_exercise_with_logs,
    create_log, 
    list_logs,
    get_log_by_id,
    update_log_by_id,
    delete_log_by_id,
    show_popular,
    least_popular,
    list_users,
    create_user,
    login_user,
    # get_user_logs,
    get_user_recent_workout,
    get_user_workout_history,
    get_my_info
)

def main():
    while True:
        print("HOME\nPlease select an option:")
        print("[1] Users")
        print("[2] Exercises")
        print("[3] Logs")
        print("[x] Exit App")
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "1":
            login()
        elif choice == "2":
            exercise_menu()
        elif choice == "3":
            log_menu()
        else:
            print("Invalid choice")

def login():
    print("Login User")
    new_user = input("New User? [y/n] ")
    if new_user == "y":
        create_user()
        main()
    elif new_user == "n":
        login_user()
        user_menu()
    elif new_user == "x" or "0":
        main()

def user_menu():
    while True:
        print("USER\nPlease select an option:")
        print("[1] My Info")
        print("[2] My Stats")
        print("[3] Create workout log")
        print("[4] Workout History")
        print("[5] All Users")
        print("[6] Update Info")
        print("[7] Delete User")
        print("[x] Log Out")
        choice = input("> ")
        if choice == "1":
            get_my_info()
        elif choice == "2":
            get_user_recent_workout()
        elif choice == "3":
            create_log()
        elif choice == "4":
            # get_user_logs()
            get_user_workout_history()
        elif choice == "5":
            print("All Users")
            list_users()
        elif choice == "6":
            update_user()
        elif choice == "7":
            print("Delete User")
        elif choice == "0" or "x":
            main()
        else:
            print("Invalid user menu option")

def exercise_menu():
    while True:
        print("EXERCISE\nPlease select an option:")
        print("[1] Exercises")
        print("[2] Exercise Stats")
        print("[3] Search for Exercise")
        print("[4] Update Exercise")  
        print("[5] Delete Exercise")      
        print("[6] Create Exercise")
        print("[x] Return to Home")
        choice = input("> ")
        if choice == "1":
            list_exercises()
        elif choice == "2":
            print("Exercise Stats")
            show_popular()
            least_popular()
        elif choice == "3":
            get_exercise_by_name_or_id()
        elif choice == "4":
            update_exercise_by_name_or_id()                    
        elif choice == "5":
            delete_exercise_by_name_or_id()
        elif choice == "6":
            create_exercise()
        elif choice == "0" or "x":
            main()
        else:
            print("Invalid exercise menu option")
            
    
def log_menu():
    while True:
        print("LOG\nPlease select an option:")
        print("[1] Log History")
        print("[2] Search for Log")
        print("[3] Update Log")  
        print("[4] Delete Log")      
        print("[5] Create Log")
        print("[x] Return to Home")
        choice = input("> ")
        if choice == "1":
            list_logs()
        elif choice == "2":
            get_log_by_id() 
        elif choice == "3":
            update_log_by_id() 
        elif choice == "4":
            delete_log_by_id()      
        elif choice == "5":
            create_log()
        elif choice == "0" or "x":
            main()
        else:
            print("Invalid log menu option")

runner = """
                         .7Y5Y7.       
                       :#@@@@@#^      
                       ?@@@@@@@7      
                 ^J5GB#&@@@@&B?       
                :&@@#@@@@@B:.         
                G@@55@@@@@B^^~^       
               .G#GG@@P?@@@@@@@~      
                 !B@@@! !?77!!^       
               .Y@@&&@@P^             
     :5P5YJ7!^!B@@P::Y&@@5:           
     ?@@&&@@@@@@&7    :5@@&7          
      ^^..:^~!77:       ~&@@J         
                         ^B@@G?.      
                          .P@@&:      
                            ~7:  
                            """

if __name__ == "__main__":
    print("\033[37mWelcome to PyFit! Track your fitness journey to help you reach your goals.\033[0m")
    print(runner)
    main()
