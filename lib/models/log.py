from models.__init__ import CURSOR, CONN
from user import User
from exercise import Exercise 

import datetime # Allows us to work with dates and times

class Log:
    def __init__(self): 
        self.entries = [] # An empty list that will store the exercise log entries

    def create_log_entry(self, user, exercise, date): # Creates a new log entry + checks the type of object
        if not isinstance(user, User):
            raise ValueError("Invalid user object provided.")
        if not isinstance(exercise, Exercise):
            raise ValueError("Invalid exercise object provided.")
        if not isinstance(date, datetime.datetime):
            raise ValueError("Invalid date object provided.")

        log_entry = {"user": user, "exercise": exercise, "date": date} # Creates a dict to contain the user, exercise and date
        self.entries.append(log_entry) # Appends the dict to the "entries" list

    def read_log_entries(self): # Returns the list of long entries 
        return self.entries

    def find_entry_by_id(self, entry_id): # Returns a matching entry by its Id
        for entry in self.entries:
            if entry.get("id") == entry_id:
                return entry
        return None

    def update_log_entry(self, index, user=None, exercise=None, date=None): # To update an entry 
        if index < 0 or index >= len(self.entries):
            raise IndexError("Index out of range.")

        log_entry = self.entries[index]

        if user is not None:
            if not isinstance(user, User):
                raise ValueError("Invalid user object provided.")
            log_entry["user"] = user

        if exercise is not None:
            if not isinstance(exercise, Exercise):
                raise ValueError("Invalid exercise object provided.")
            log_entry["exercise"] = exercise

        if date is not None:
            if not isinstance(date, datetime.datetime):
                raise ValueError("Invalid date object provided.")
            log_entry["date"] = date

    def delete_log_entry(self, index): # Delete a log entry
        if index < 0 or index >= len(self.entries):
            raise IndexError("Index out of range.")

        del self.entries[index]

    def __str__(self): # Returns the string "Exercise Log"
        return "Exercise Log"
