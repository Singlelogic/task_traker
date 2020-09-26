from db import Sqlite


class Task:
    __tablename__ = 'tasks'

    def __init__(self, name_db: str, name_table: str):
        self.db = Sqlite(name_db)
        self.db.create_table(self.__tablename__, ('date TEXT', 'task TEXT', 'done TEXT'))

    def __str__(self):
        pass

    def add_task(self, date: str, event: str, done: str = 'no'):
        data = (date, event, done)
        self.db.insert_data(self.__tablename__, data)

    def find_task(self, date: str):
        field = 'date'
        return self.db.select_data(self.__tablename__, field, date)

    def find_all_tasks(self):
        return self.db.select_data(self.__tablename__)

    def change_status_task(self, date: str, event: str = '', done: str = 'yes'):
        """Change the status of the specified task to complete."""
        _set = f"done='{done}'"
        where = f"date='{date}' and task='{event}'"
        self.db.update_data(self.__tablename__, _set, where)

    def change_status_all_task(self, date: str, done: str = 'yes'):
        """Change the status of tasks to completed on the specified date."""
        _set = f"done='{done}'"
        where = f"date='{date}'"
        self.db.update_data(self.__tablename__, _set, where)
