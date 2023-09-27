import sqlite3

CONN = sqlite3.connect('fitness_tracker.db')
CURSOR = CONN.cursor()
