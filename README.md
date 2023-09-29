# Pyfit Fitness Tracker

## Summary

Pyfit is a CLI application fitness tracker. A user can pick from various exercises that range from beginner to advanced intensity. Each workout displays its name, duration, intensity, calories burned and will either be a Strength or Cardio type. Users are able to add workouts and even check their workout history. Pyfit is meant to guide and help you reach your Fitness Goals. 

---

## Requirements

- Python 3.x 
- SQLlite

## Installation

To run the Program, the following commands must be entered:  

1. In the Project directory:
```
 pipenv install 
 pipenv shell    
```
2. Once the shell has been run: 
```
 python lib/seed.py 
 python lib/cli.py 
```
## Usage  
Once started, the program will greet you and display a Menu displaying Users, Exercises and Logs. Navigation is made easy by entering in numbers to move between selections.

From the main menu:
- Users: Users will login or create a new user. After logging in, the user can see their info, stats, workout history and view all users.
- Exercises: The user can see a list of exercises, stats, search, create, update or delete an exercise.
- Logs: User can view the app's log history, search, create, update, and delete a log
- Exit App: Closes application

## File Structure

[cli.py](https://github.com/axb052a/P3---Python-Project-/blob/main/lib/cli.py)

Menu lists and options for navigating the app

[helpers.py](https://github.com/axb052a/P3---Python-Project-/blob/main/lib/helpers.py)

Helper functions are accessed through the menu based on selection. They will retrieve information from the database and output the result to the terminal.

[models](https://github.com/axb052a/P3---Python-Project-/tree/main/lib/models)

ORM model classes that lay the foundation for the app. Classes: User, Exercise, and Log. CRUD functions are built out for each class along with additional methods to make SQL queries and calculations.

[seed.py](https://github.com/axb052a/P3---Python-Project-/blob/main/lib/seed.py)

Starter data to help fill in SQL database tables

## Resources

- [Github repo: Pyfit](https://github.com/axb052a/P3---Python-Project-)
