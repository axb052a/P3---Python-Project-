# lib/models/exercise.py
from models.__init__ import CURSOR, CONN

class Exercise:

    all = {}

    INTENSITY = ["Beginner", "Intermediate", "Advanced"]
    CATEGORY = ["Cardio", "Strength"]

    def __init__(self, name, time, category, intensity= "Beginner", cals_burned = 0, id=None):
        self.id = id
        self.name = name
        self.time = time
        self.category = category
        self.intensity = intensity
        self.cals_burned = cals_burned
        Exercise.all.append(self)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.time}, {self.category}, {self.intensity}, {self.cals_burned}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise Exception("Invalid name")

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        if isinstance(time, int) and 0 < time:
            self._time = time
        else:
            raise Exception("Invalid time")
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category in Exercise.CATEGORY:
            self._category = category
        else:
            raise Exception("Invalid category")

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, intensity):
        if intensity in Exercise.INTENSITY:
            self._intensity = intensity
        else:
            raise Exception("Invalid intensity")

    @property
    def cals_burned(self):
        return self._cals_burned

    @cals_burned.setter
    def cals_burned(self, cals_burned):
        if isinstance(cals_burned, int) and 0 < cals_burned:
            self._cals_burned = cals_burned
        else:
            raise Exception("Invalid calories")

    @classmethod
    def create_table(cls):
        """ Create a table to persist the attributes of Exercise instances """
        sql = """
            CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            name TEXT,
            time INT,
            category TEXT,
            intensity TEXT,
            cals_burned INT
            )        
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Exercise instances """
        sql = """
            DROP TABLE IF EXISTS exercises;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the exercise details for current Exercise instance
         Update object id attribute using the primary key value of new row.
          Save the object in local dictionary using table row's PK as dictionary key """
        
        sql = """
            INSERT INTO exercises (name, time, category, intensity, cals_burned)
            values (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.time, self.category, self.intensity, self.cals_burned))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Exercise.all[self.id] = self
    
    @classmethod
    def create(cls, name, time, category, intensity, cals_burned):
        """ Initialize a new Exercise instance and save the object to the database """
        exercise = cls(name, time, category, intensity, cals_burned)
        exercise.save()
        return exercise
    
    def update(self):
        """ Update the table row corresponding to the current Exercise instance """
        sql = """
            UPDATE exercises
            SET name = ?, time = ?, category = ?, intensity = ?, cals_burned = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.time, self.category, self.intensity, self.cals_burned, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete the table row corresponding to the current Exercise instance, delete the dictionary entry, and reassign id attribute """
        sql = """
            DELETE FROM exercises
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del Exercise.all[self.id]

        # Set the id to None
        self.id = None