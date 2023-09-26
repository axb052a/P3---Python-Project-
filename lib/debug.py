#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.exercise import Exercise
# from models.log import Log
# from models.user import User
import ipdb

def reset_database():

    # Delete existing tables
    Exercise.drop_table()
    # Log.drop_table()
    # User.drop_table()

    # Create new tables
    Exercise.create_table()
    # Log.create_table()
    # User.create_table()

    # Create seed data
    treadmill = Exercise.create("Treadmill", 15, "Cardio", "Advanced", 200)
    weights = Exercise.create("Weights", 30, "Strength", "Intermediate", 150)
    walking = Exercise.create("Walking", 30, "Cardio", "Beginner", 100)
    jump_rope = Exercise.create("Jump Rope", 5, "Cardio", "Beginner", 100)
    push_ups = Exercise.create("Push Ups", 5, "Strength", "Beginner", 25)

reset_database()
ipdb.set_trace()
