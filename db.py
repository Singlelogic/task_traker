import sqlite3


class Sqlite():
    """This class represents methods for working with the Sqlite3 database."""
    def __init__(self, name_db: str):
        self.conn = sqlite3.connect(name_db)
        self.cursor = self.conn.cursor()

    def create_table(self, name_table: str, fields: tuple):
        """Create table in database.

        Formation of a string with fields depending on the number of fields
        in the tuple 'fields'.
        """
        fields_table = "(" + ", ".join(fields) + ")"
        self.cursor.execute(f"CREATE TABLE if not exists {name_table} {fields_table}")

    def insert_data(self, name_table: str, data: tuple):
        """Insert data into database.

        Forming a string with data depending on the number of values in a tuple 'data'.
        """
        data = "(" + ",".join(f"'{i}'" for i in data) + ")"
        self.cursor.execute(f"INSERT INTO {name_table} VALUES {data}")
        self.conn.commit()

    def select_data(self, name_table: str, field: str = '', data: str = ''):
        """Select data from database.

        Selects data by the specified field and the value of this field,
        if no field or field value is specified, all data from the table is fetched.
        """
        if field and data:
            return self.cursor.execute(f"SELECT * FROM {name_table} WHERE {field}=('{data}')")
        else:
            return self.cursor.execute(f"SELECT * FROM {name_table}")

    def update_data(self, name_table: str, _set: str, where: str = ''):
        """Updating data in the database."""
        query_update = f"UPDATE {name_table} SET {_set} WHERE {where}"
        self.cursor.execute(query_update)
        self.conn.commit()
