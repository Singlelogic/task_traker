import sqlite3


class Sqlite():
    """This class represents methods for working with the Sqlite3 database."""
    def __init__(self, name_db:str):
        self.conn = sqlite3.connect(name_db)
        self.cursor = self.conn.cursor()

    def create_table(self, name_table:str, fields:tuple):
        fields_table = "(" + ", ".join(f"'{i}'" for i in fields) + ")"
        # Formation of a string with fields depending on the number of fields in the tuple 'fields'
        self.cursor.execute(f"CREATE TABLE if not exists {name_table} {fields_table}")

    def insert_data(self, name_table:str, data:tuple):
        # Forming a string with data depending on the number of values in a tuple 'data'
        data = "(" + ",".join(f"'{i}'" for i in data) + ")"
        self.cursor.execute(f"INSERT INTO {name_table} VALUES {data}")
        self.conn.commit()
