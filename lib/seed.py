#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.exercise import Exercise
from models.log import Log
from models.user import User

def seed_database():

    # Delete existing tables
    Exercise.drop_table()
    Log.drop_table()
    User.drop_table()

    # Create new tables
    Exercise.create_table()
    Log.create_table()
    User.create_table()

    # Create seed data
    # Exercise instances
    treadmill = Exercise.create("Treadmill", 15, "Cardio", "Advanced", 200)
    weights = Exercise.create("Weights", 30, "Strength", "Intermediate", 150)
    walking = Exercise.create("Walking", 30, "Cardio", "Beginner", 100)
    jump_rope = Exercise.create("Jump Rope", 5, "Cardio", "Beginner", 100)
    push_ups = Exercise.create("Push Ups", 5, "Strength", "Beginner", 25)

    # User instances
    john = User.create_user("John Cena", 6, 1, 200)
    alicia = User.create_user("Alicia Keys", 5, 6, 120)
    bob = User.create_user("Bob Mackey", 6, 1, 175)
    adam = User.create_user("Adam Brody", 5, 11, 170)
    charlie = User.create_user("Charlie Brown", 4, 2, 75)

    # Log instances
    Log.create(john, treadmill, "2023-09-28")
    Log.create(alicia, weights, "2023-09-28")
    Log.create(bob, walking, "2023-09-27")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(charlie, push_ups, "2023-09-26")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(adam, jump_rope, "2023-09-27")
    Log.create(charlie, push_ups, "2023-09-26")
    Log.create(charlie, push_ups, "2023-09-26")
    Log.create(charlie, push_ups, "2023-09-26")
    Log.create(charlie, push_ups, "2023-09-26")
    Log.create(charlie, push_ups, "2023-09-26")

seed_database()
print("Seeded database")