from db import Sqlite


class Task:
    def __init__(self, name_db:str, name_table:str):
        self.db = Sqlite(name_db)
        self.db.create_table(name_table, ('date text', 'task text', 'done text'))

    def __str__(self):
        pass

    def add(self, name_table:str, date:str, event:str, done:str='no'):
        data = (date, event, done)
        self.db.insert_data(name_table, data)
