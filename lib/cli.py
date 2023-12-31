# lib/cli.py
from models.exercise import Exercise
from models.log import Log
from helpers import (
    exit_program,
    create_exercise,
    list_exercises,
    get_exercise_by_name_or_id,
    update_exercise_by_name_or_id,
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
    display_recent_workout,
    get_user_workout_history,
    update_user_info_and_logs,
    delete_user_with_logs,
    get_my_info
)

                
def main():
    while True:
        print("\033[36mPlease select an option:\033[0m")
        print("\033[36m[1] Users\033[0m")
        print("\033[36m[2] Exercises\033[0m")
        print("\033[36m[3] Logs\033[0m")
        print("\033[36m[x] Exit App\033[0m")
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
        print("\033[36mPlease select an option:\033[0m")
        print("\033[36m[1] My Info\033[0m")
        print("\033[36m[2] My Stats\033[0m")
        print("\033[36m[3] Workout History\033[0m")
        print("\033[36m[4] All Users\033[0m")
        print("\033[36m[5] Update an User\033[0m")
        print("\033[36m[6] Delete an User\033[0m")
        print("\033[36m[x] Log Out\033[0m")
        choice = input("> ")
        if choice == "1":
            get_my_info()
        elif choice == "2":
            display_recent_workout()
        elif choice == "3":
            get_user_workout_history()
        elif choice == "4":
            print("All Users")
            list_users()
        elif choice == "5":
            update_user_info_and_logs()
        elif choice == "6":
            print("Delete User")
            delete_user_with_logs()
        elif choice == "0" or "x":
            main()
        else:
            print("Invalid user menu option")


def exercise_menu():
    while True:
        print("\033[36mPlease select an option:\033[0m")
        print("\033[36m[1] Exercises\033[0m")
        print("\033[36m[2] Exercise Stats\033[0m")
        print("\033[36m[3] Search for Exercise\033[0m")
        print("\033[36m[4] Update Exercise\033[0m")  
        print("\033[36m[5] Delete Exercise\033[0m")      
        print("\033[36m[6] Create Exercise\033[0m")
        print("\033[36m[x] Return to Home\033[0m")
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
            delete_exercise_with_logs()
        elif choice == "6":
            create_exercise()
        elif choice == "0" or "x":
            main()
        else:
            print("Invalid exercise menu option")
    
def log_menu():
    while True:
        print("\033[36mPlease select an option:\033[0m")
        print("\033[36m[1] Log History\033[0m")
        print("\033[36m[2] Search for Log\033[0m")
        print("\033[36m[3] Update Log\033[0m")  
        print("\033[36m[4] Delete Log\033[0m")      
        print("\033[36m[5] Create Log\033[0m")
        print("\033[36m[x] Return to Home\033[0m")
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
