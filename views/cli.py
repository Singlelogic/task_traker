import os
from model.task import Task


def show_current():
    """The method returns a formatted string of not completed tasks,
    in the date: task format, one event per line.
    """
    tasks = Task.formatted_tasks_output()
    if tasks:
        return tasks
    else:
        return "Incomplete tasks not found"


def show_done():
    """The method returns a formatted string of completed tasks,
    in the date: task format, one event per line
    """
    tasks = Task.formatted_tasks_output(done='yes')
    if tasks:
        return tasks
    else:
        return "Complete tasks not found"


def path_database():
    """Checks if the database exists, and return the absolute path if it exists."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_db = base_dir + '/db.sqlite3'
    if os.path.exists(path_db):
        return path_db
    else:
        return "Database does not exist."
