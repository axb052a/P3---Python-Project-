import sqlite3

from models.__init__ import CURSOR, CONN

# Establish a connection to the SQLite database (create if not exists)
# conn = sqlite3.connect('fitness_tracker.db')

class User:

    all = {}

    def __init__(self, name, height_ft, height_inches, weight, id=None):
        self.id = id
        self.name = name
        self.height_ft = height_ft
        self.height_inches = height_inches
        self.weight = weight
        self.workouts = []
    
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.height_ft}\'{self.height_inches}\" | {self.weight}"

    # def get_all_users(conn):
    #     cursor = conn.execute('SELECT * FROM Users')
    #     return cursor.fetchall()

    @classmethod
    def get_all(cls):
        """ Return a list containing User object per row in the table """
        sql = """
            SELECT *
            FROM users
        """
        rows = CURSOR.execute(sql).fetchall()

        return [User.instance_from_db(row) for row in rows]

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 25:  
                self._name = new_name
        else:
            raise Exception("Name must be a string with a length between 2 and 25 characters.")
    @property
    def height_ft(self):
        return self._height_ft
    @height_ft.setter
    def height_ft(self, new_height_ft):
        self._height_ft = new_height_ft
        
    @property
    def height_inches(self):
        return self._height_inches

    @height_inches.setter
    def height_inches(self, new_height_inches):
        self._height_inches = new_height_inches
        
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight
        
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


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of User instances """
        sql = """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                height_ft INT,
                height_inches INT,
                weight INT)
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        """ DROP the table that persists User instances"""
        sql = """
            DROP TABLE IF EXISTS  users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current User instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO users (name, height_ft, height_inches, weight)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.height_ft, self.height_inches, self.weight))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        User.all[self.id] = self

    @classmethod
    def create_user(cls, name, height_ft, height_inches, weight):
        """ Initialize a new User instance and save the object to the database """
        user = cls(name, height_ft, height_inches, weight)
        user.save()
        return user

    def update(self):
            """Update the table row corresponding to the current User instance."""
            sql = """
                UPDATE user
                SET name = ?, height_ft = ?, height_inches = ?, weight = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.height_ft, self.height_inches, self.weight, self.id))
            CONN.commit()

    def delete(self):
            """Delete the table row corresponding to the current User instance"""
            sql = """
                DELETE FROM users
                WHERE id = ?
            """

            CURSOR.execute(sql, (self.id,))
            CONN.commit()

            del User.all[self.id]

            self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return User object having the attribute values from the table row """

        # Check the dictionary for an existing instance using the row's primary key
        user = User.all.get(row[0])
        if user:
            user.name = row[1]
            user.height_ft = row[2]
            user.height_inches = row[3]
            user.weight = row[4]
        else:
            user = User(row[1], row[2], row[3], row[4])
            user.id = row[0]
            User.all[user.id] = user
        return user
    
    @classmethod
    def find_by_id(cls, id):
        """ Return User object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id, )).fetchone()
        return User.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        """ Return a list containing an Exercise object per row in the table """
        sql = """
            SELECT *
            FROM users
        """
        rows = CURSOR.execute(sql).fetchall()

        return [User.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """ Return an Exercise object corresponding to the table row matching the name """
        sql = """
            SELECT *
            FROM users
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
        return User.instance_from_db(row) if row else None
