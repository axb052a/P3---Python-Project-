# Pyfit Fitness Tracker

## Summary

Pyfit is a CLI application fitness tracker. A user can pick from various exercises that range from beginner to advanced intensity. Each workout displays it's name, duration, intensity, calories burned and will either be a Strength or Cardio type. Users are able to add workouts and even check their workout history. Pyfit is meant to guide and help you reach your Fitness Goals.

---

## Requirements
- Python 3.x
-SQLlite


---

## Installation

To run the Program, the following commands must be entered:

1. In the Project directory: 

```console
pipenv install
pipenv shell


2. Once the shell has been run:
python lib/seed.py
python lib/cli.py

```

## Usage

Once started, the program will greet you and display a Menu displaying Users, Exercises and Logs. Navigate into Users by selecting "1", here you will be able to add your name as well as your height and weight. Once you've been added you can navigate back to the main menu by pressing "x". From here you are ready to jump into Exercises. Pressing "2" will navigate you into the Exercises menu, here you can view a list of exercises, thier stats, search for an exercise, update, create and delete and exercise. 
