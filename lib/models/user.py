import sqlite3

from models.__init__ import CURSOR, CONN

# Establish a connection to the SQLite database (create if not exists)
# conn = sqlite3.connect('fitness_tracker.db')

class User:
    def __init__(self, name, height_ft, height_inches, weight):
        self.name = name
        self.height_ft = height_ft
        self.height_inches = height_inches
        self.weight = weight
        self.workouts = []
        
    @classmethod
    def find_by_id(cls, user_id):
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (user_id,)).fetchone()
        return User.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        if row:
            user_id = row  # Extract data from the database row
            return cls(user_id)  # Create a User instance

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of User instances """
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            height_ft INTEGER,
            height_inches INTEGER,
            weight INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ DROP the table that persists User instances """
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current User instance.
        Update object id attribute using the primary key value of the new row.
        """
        sql = """
            INSERT INTO users (name, height_ft, height_inches, weight)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.height_ft, self.height_inches, self.weight))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, height_ft, height_inches, weight):
        """ Initialize a new User instance and save the object to the database """
        user = cls(name, height_ft, height_inches, weight)
        user.save()
        return user

    def update(self):
        """ Update the table row corresponding to the current User instance. """
        sql = """
            UPDATE users
            SET name = ?, height_ft = ?, height_inches = ?, weight = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.height_ft, self.height_inches, self.weight, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current User instance """
        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 25:
            self._name = new_name
        else:
            raise Exception("Name must be a string with a length between 2 and 25 characters.")

    # Similar properties and setters for height_ft, height_inches, and weight

    def add_height(self, new_height_ft, new_height_inches):
        # Validate inputs for height
        if not isinstance(new_height_ft, int) or not isinstance(new_height_inches, int):
            raise Exception("Height values must be integers.")

        if new_height_ft < 0 or new_height_ft > 10 or new_height_inches < 0 or new_height_inches >= 12:
            raise Exception("Invalid height values. Height must be within the range of 0-10 feet and 0-11 inches.")

        self.height_ft = new_height_ft
        self.height_inches = new_height_inches

    def add_weight(self, new_weight):
        # Validate input for weight
        if not isinstance(new_weight, (float, int)):
            raise Exception("Weight must be a float or integer.")

        if new_weight <= 0:
            raise ValueError("Weight must be greater than 0.")

        self.weight = new_weight

def get_all_users(conn):
    cursor = conn.execute('SELECT * FROM users')
    return cursor.fetchall()
