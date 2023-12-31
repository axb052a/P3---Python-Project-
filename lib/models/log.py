from models.__init__ import CURSOR, CONN
from models.user import User
from models.exercise import Exercise
class Log:
    all = {}
    def __init__(self, user, exercise, date, id=None):
        self.id = id
        self.user = user
        self.exercise = exercise
        self.date = date
    def __repr__(self):
        return f"\033[35m {self.id} | User: {self.user.name} | Exercise: {self.exercise.name} | Date: {self.date}\033[0m"

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        if isinstance(user, User):
            self._user = user
        else:
            raise Exception("\033[31m Invalid user\033[0m")
    @property
    def exercise(self):
        return self._exercise
    @exercise.setter
    def exercise(self, exercise):
        if isinstance(exercise, Exercise):
            self._exercise = exercise
        else:
            raise Exception("\033[31m Invalid exercise\033[0m")
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        # Assuming date is a valid datetime object or string representation of a date
        self._date = date
    @classmethod
    def create_table(cls):
        """ Create a table to persist the attributes of Log instances """
        # sql = """
        #     CREATE TABLE IF NOT EXISTS logs (
        #     id INTEGER PRIMARY KEY,
        #     user_id TEXT,
        #     exercise_id TEXT,
        #     date INT,
        #     FOREIGN KEY (user_id) REFERENCES users(id),
        #     FOREIGN KEY (exercise_id) REFERENCES exercises(id))        
        # """

        sql = """
            CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            user TEXT,
            exercise_id TEXT,
            exercise TEXT,
            date INT
            )     
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Log instances """
        sql = """
            DROP TABLE IF EXISTS logs;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the log details for the current Log instance
         Update object id attribute using the primary key value of the new row.
          Save the object in the local dictionary using the table row's PK as the dictionary key """
        
        # sql = """
        #     INSERT INTO logs (user_id, exercise_id, date)
        #     VALUES (?, ?, ?)
        # """

        # CURSOR.execute(sql, (self.user.id, self.exercise.id, self.date))
        # CONN.commit()

        sql = """
            INSERT INTO logs (user_id, user, exercise_id, exercise, date)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.user.id, self.user.name, self.exercise.id, self.exercise.name, self.date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Log.all[self.id] = self
    
    @classmethod
    def create(cls, user, exercise, date):
        """ Initialize a new Log instance and save the object to the database """
        log = cls(user, exercise, date)
        log.save()
        return log
    
    def update(self):
        """ Update the table row corresponding to the current Log instance """
        sql = """
            UPDATE logs
            SET user_id = ?, exercise_id = ?, date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.user.id, self.exercise.id, self.date, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete the table row corresponding to the current Log instance, delete the dictionary entry, and reassign id attribute """
        sql = """
            DELETE FROM logs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del Log.all[self.id]
        # Set the id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Log object having the attribute values from the table row """
        # Check the dictionary for an existing instance using the row's primary key
        # log = Log.all.get(row[0])
        # if log:
        #     log.user = User.find_by_id(row[1])
        #     log.exercise = Exercise.find_by_id(row[2])
        #     log.date = row[3]
        # else:
        #     user = User.find_by_id(row[1])
        #     exercise = Exercise.find_by_id(row[2])
        #     log = Log(user, exercise, row[3])
        #     log.id = row[0]
        #     Log.all[log.id] = log
        # return log

        # Updated to reference additional table columns
        log = Log.all.get(row[0])
        if log:
            log.user = User.find_by_id(row[1])
            log.exercise = Exercise.find_by_id(row[3])
            log.date = row[5]
        else:
            user = User.find_by_id(row[1])
            exercise = Exercise.find_by_id(row[3])
            log = Log(user, exercise, row[5])
            log.id = row[0]
            Log.all[log.id] = log
        return log
    
    @classmethod
    def get_all(cls):
        """ Return a list containing a Log object per row in the table """
        sql = """
            SELECT *
            FROM logs
        """
        rows = CURSOR.execute(sql).fetchall()
        i = 0
        print("\033[35m ID | Date | User | Exercise \033[0m")
        while i < len(rows):
            print(f"{rows[i][0]} | {rows[i][5]} | {rows[i][2]} | {rows[i][4]}")
            i += 1

        # return [Log.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return a Log object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM logs
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id, )).fetchone()

        return Log.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """ Return a Log object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM logs
            WHERE user = ?
        """
        
#         rows = CURSOR.execute(sql, (name, )).fetchall()
        
#         i = 0
#         print("Date | User | Exercise")
#         while i < len(rows):
#             print(f"{rows[i][5]} | {rows[i][2]} | {rows[i][4]}")
#             i += 1
  
        row = CURSOR.execute(sql, (name, )).fetchall()

        return Log.instance_from_db(row) if row else None

    @classmethod
    def find_by_exercise(cls, exercise):
        """Return a list of logs associated with the given exercise."""
        sql = """
            SELECT *
            FROM logs
            WHERE exercise_id = ?
        """
        rows = CURSOR.execute(sql, (exercise.id,)).fetchall()
        return [Log.instance_from_db(row) for row in rows]

    
    @classmethod
    def find_by_user(cls, user):
        """Return a list of logs associated with the given user."""
        sql = """
            SELECT *
            FROM logs
            WHERE user_id = ?
        """
        rows = CURSOR.execute(sql, (user.id,)).fetchall()
        return [Log.instance_from_db(row) for row in rows]
