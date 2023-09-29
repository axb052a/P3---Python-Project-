# lib/cli.py

from models.exercise import Exercise
from models.log import Log

from helpers import (
    exit_program,
    create_exercise,
    list_exercises,
    get_exercise_by_name_or_id,
    update_exercise_by_name_or_id,
    # delete_exercise_by_name_or_id,
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
    home_menu()
    while True:
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "1":
            try:
                login_user()
                user_menu()
            except:
                print("Login error. Please try again.\n[x] Return to menu")
            while True:
                choice = input("> ")
                if choice == "1":
                    get_my_info()
                elif choice == "2":
                    print("My Stats")
                    get_user_recent_workout()
                elif choice == "3":
                    # get_user_logs()
                    get_user_workout_history()
                elif choice == "4":
                    print("All Users")
                    list_users()
                elif choice == "0" or "x":
                    main()
                else:
                    print("Invalid choice user_menu")
        elif choice == "2":
            exercise_menu()
            while True:
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
                    # delete_exercise_by_name_or_id()
                    delete_exercise_with_logs()
                elif choice == "6":
                    create_exercise()
                elif choice == "x":
                    main()
                else:
                    print("Invalid choice exercise_menu")
        elif choice == "3":
            log_menu()  
            while True:
                choice = input("> ")
                if choice == "1":
                    list_logs()
                elif choice == "2":
                    # log_id = input("Enter the log ID: ")
                    # get_log_by_id(log_id) 
                    get_log_by_id() 
                elif choice == "3":
                    update_log_by_id() 
                elif choice == "4":
                    delete_log_by_id()      
                elif choice == "5":
                    create_log()
                elif choice == "x":
                    main()
                else:
                    print("Invalid choice log_menu")
        else:
            print("Invalid choice")

def home_menu():
    print("Please select an option:")
    print("[1] Users")
    print("[2] Exercises")
    print("[3] Logs")
    print("[x] Exit App")

def user_menu():
    print("Please select an option:")
    print("[1] My Info")
    print("[2] My Stats")
    print("[3] Workout History")
    print("[4] All Users")
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
    
def log_menu():
    print("Please select an option:")
    print("[1] Log History")
    print("[2] Search for Log")
    print("[3] Update Log")  
    print("[4] Delete Log")      
    print("[5] Create Log")
    print("[x] Return to Home")

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
    print("Welcome to PyFit! Track your fitness journey to help you reach your goals.")
    print(runner)
    main()


