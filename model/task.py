import sqlite3


class Task:
    """This class is used for adding tasks, changing their state,
    and searching for."""
    __tablename__ = 'tasks'

    def __init__(self, date: str, event: str, done: str = 'no'):
        self.__date = date
        self.__event = event
        self.__done = done

    def __str__(self):
        return f"Date: {self.__date} - {self.__event}; Done: {self.__done}"

    def save(self) -> None:
        """Method for saving an object in the database"""
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        query_insert = f"INSERT INTO {self.__tablename__} VALUES(NULL, ?, ?, ?)"
        cur.execute(query_insert, (self.__date, self.__event, self.__done))

        conn.commit()
        conn.close()

    @classmethod
    def find_task(cls, date: str = '', done: str = 'no') -> list:
        """To find the tasks from the database.

        Incomplete tasks are selected by default.
        If a date is specified, it returns data for that date.
        If no date is specified, it returns all tasks.
        """
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        if date:
            query_select = f"SELECT * FROM {cls.__tablename__} WHERE date='{date}' and done='{done}'"
        else:
            query_select = f"SELECT * FROM {cls.__tablename__} WHERE done='{done}'"
        tasks = []
        for row in cur.execute(query_select):
            tasks.append(cls(row[1], row[2], row[3]))
        conn.close()
        return tasks

    @classmethod
    def change_status_task(cls, date: str, event: str = '', done: str = 'yes') -> None:
        """Changing the task status.

        By default, the task status changes to completed.
        If no task is specified, this changes the status of all tasks for
        the specified date.
        """
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        if event:
            query_update = f"UPDATE {cls.__tablename__} SET done=? WHERE date=? and task=?"
            cur.execute(query_update, (done, date, event))
        else:
            query_update = f"UPDATE {cls.__tablename__} SET done=? WHERE date=?"
            cur.execute(query_update, (done, date))

        conn.commit()
        conn.close()
