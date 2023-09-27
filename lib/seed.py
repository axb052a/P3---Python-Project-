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

   # Create seed data for exercises
    treadmill = Exercise.create("Treadmill", 15, "Cardio", "Advanced", 200)
    weights = Exercise.create("Weights", 30, "Strength", "Intermediate", 150)
    walking = Exercise.create("Walking", 30, "Cardio", "Beginner", 100)
    jump_rope = Exercise.create("Jump Rope", 5, "Cardio", "Beginner", 100)
    push_ups = Exercise.create("Push Ups", 5, "Strength", "Beginner", 25)

    # Create seed data for users
    user1 = User.create("User1", 5, 10, 150)
    user2 = User.create("User2", 6, 2, 180)
    user3 = User.create("User3", 5, 8, 160)

    # Create seed data for logs
    log1 = Log.create(user3, treadmill, "2023-09-27")
    log2 = Log.create(user2, weights, "2023-09-28")
    log3 = Log.create(user3, walking, "2023-09-29")
    log4 = Log.create(user1, jump_rope, "2023-09-29")
    log5 = Log.create(user2, push_ups, "2023-09-25")

seed_database()
print("Seeded database")
