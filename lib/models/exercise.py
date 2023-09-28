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

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.time} min | {self.category} | {self.intensity} | {self.cals_burned} cals"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 20:
            self._name = name
        else:
            raise Exception("Invalid name. Name must be a string greater than 0 and less than 20 characters.")

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        time = int(time)
        if isinstance(time, int) and 0 < time:
            self._time = time
        else:
            raise Exception("Invalid duration. Duration must be a number greater than 0.")
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category in Exercise.CATEGORY:
            self._category = category
        else:
            raise Exception("Invalid category. Please select between Cardio or Strength.")

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, intensity):
        if intensity in Exercise.INTENSITY:
            self._intensity = intensity
        else:
            raise Exception("Invalid intensity. Please select either Beginner, Intermediate, Advanced.")

    @property
    def cals_burned(self):
        return self._cals_burned

    @cals_burned.setter
    def cals_burned(self, cals_burned):
        cals_burned = int(cals_burned)
        if isinstance(cals_burned, int) and 0 < cals_burned:
            self._cals_burned = cals_burned
        else:
            raise Exception("Invalid calories. Calories must be a number greater than 0.")

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
            cals_burned INT)        
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
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del Exercise.all[self.id]

        # Set the id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return an Exercise object having the attribute values from the table row """

        # Check the dictionary for an existing instance using the row's primary key
        exercise = Exercise.all.get(row[0])
        if exercise:
            exercise.name = row[1]
            exercise.time = row[2]
            exercise.category = row[3]
            exercise.intensity = row[4]
            exercise.cals_burned = row[5]
        else:
            exercise = Exercise(row[1], row[2], row[3], row[4], row[5])
            exercise.id = row[0]
            Exercise.all[exercise.id] = exercise
        return exercise

    @classmethod
    def get_all(cls):
        """ Return a list containing an Exercise object per row in the table """
        sql = """
            SELECT *
            FROM exercises
        """
        rows = CURSOR.execute(sql).fetchall()

        return [Exercise.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return an Exercise object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM exercises
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id, )).fetchone()
        return Exercise.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return an Exercise object corresponding to the table row matching the name """
        sql = """
            SELECT *
            FROM exercises
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
        return Exercise.instance_from_db(row) if row else None
    
    def users(self):
        """ Return list of users associated with Exercise instance """
        from models.log import Log
        sql = """
            SELECT *
            FROM log
            WHERE exercise_id = ?
        """
        CURSOR.execute(sql, (self.id, ),)

        rows = CURSOR.fetchall()
        return [Exercise.instance_from_db(row) for row in rows]
    
    @classmethod
    def most_popular(cls):
        """ Return a list containing an Exercise object per row in the table """
        sql = """
            SELECT exercise_id, count(*) as exercise_id
            FROM logs
            GROUP BY exercise_id
            ORDER BY count(*) desc
        """
        
        most_used = CURSOR.execute(sql).fetchall()
        num_time = most_used[0][1]
        
        i = 0
        most_used_list = []
        while i < len(most_used):
            if most_used[i][1] == num_time:
                most_used_exercise = Exercise.find_by_id(most_used[i][0])
                most_used_list.append(most_used_exercise)
            i += 1
    
        print("Most popular exercises:")
        for exercise in most_used_list:
            print(f"- {exercise.name} completed {num_time} times!")
    
    @classmethod
    def least_popular(cls):
        """ Return a list containing an Exercise object per row in the table """
        sql = """
            SELECT exercise_id, count(*) as exercise_id
            FROM logs
            GROUP BY exercise_id
            ORDER BY count(*) asc
        """
        
        least_used = CURSOR.execute(sql).fetchall()
        num_time = least_used[0][1]
        
        i = 0
        least_used_list = []
        while i < len(least_used):
            if least_used[i][1] == num_time:
                least_used_exercise = Exercise.find_by_id(least_used[i][0])
                least_used_list.append(least_used_exercise)
            i += 1
    
        print("Least popular exercises:")
        for exercise in least_used_list:
            print(f"- {exercise.name} completed only {num_time} times!")
    


    
