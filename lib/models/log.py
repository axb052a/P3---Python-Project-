from models.__init__ import CURSOR, CONN
from models.user import User
from models.exercise import Exercise

class Log:
    def __init__(self): 
        self.entries = [] # An empty list that will store the exercise log entries

    def create_log_entry(self, user, exercise, date):
        if not isinstance(user, User):
            raise ValueError("Invalid user object provided.")
        if not isinstance(exercise, Exercise):
            raise ValueError("Invalid exercise object provided.")

        sql = """
            INSERT INTO logs (user_id, exercise_id, date)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (user.id, exercise.id, date))
        CONN.commit()

    @classmethod
    def read_log_entries(cls):
        sql = """
            SELECT logs.id, users.name, exercises.name, logs.date
            FROM logs
            INNER JOIN users ON logs.user_id = users.id
            INNER JOIN exercises ON logs.exercise_id = exercises.id
        """

        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        entries = []
        for row in rows:
            entry = {
                "id": row[0],
                "user": row[1],
                "exercise": row[2],
                "date": row[3]
            }
            entries.append(entry)

        return entries

    @classmethod
    def find_entry_by_id(cls, entry_id):
        sql = """
            SELECT logs.id, users.name, exercises.name, logs.date
            FROM logs
            INNER JOIN users ON logs.user_id = users.id
            INNER JOIN exercises ON logs.exercise_id = exercises.id
            WHERE logs.id = ?
        """

        CURSOR.execute(sql, (entry_id,))
        row = CURSOR.fetchone()

        if row:
            entry = {
                "id": row[0],
                "user": row[1],
                "exercise": row[2],
                "date": row[3]
            }
            return entry
        else:
            return None

    @classmethod
    def update_log_entry(cls, entry_id, user=None, exercise=None, date=None):
        sql = """
            UPDATE logs
            SET user_id = COALESCE(?, user_id), exercise_id = COALESCE(?, exercise_id), date = COALESCE(?, date)
            WHERE id = ?
        """

        CURSOR.execute(sql, (user.id if user else None, exercise.id if exercise else None, date, entry_id))
        CONN.commit()

    @classmethod
    def delete_log_entry(cls, entry_id):
        sql = """
            DELETE FROM logs
            WHERE id = ?
        """

        CURSOR.execute(sql, (entry_id,))
        CONN.commit()

    def __str__(self):
        return f"Log with {len(self.entries)} entries"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                exercise_id TEXT,
                date INT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS logs;
        """
        CURSOR.execute(sql)
        CONN.commit()
