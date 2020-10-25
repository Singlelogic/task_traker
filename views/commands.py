"""This module contents internal commands."""
from collections import defaultdict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.task import Task


engine = create_engine('sqlite:///db.sqlite3')
session = sessionmaker(bind=engine)()


def validate_date(msg: str):
    """Check if the given string is a date."""
    msg = msg.split('-')
    if len(msg) == 3:
        if (len(msg[0]) == 4) and (len(msg[1]) == 2) and (len(msg[2]) == 2):
            if (int(msg[1]) <= 12) and (int(msg[2]) <= 31):
                return ''.join(msg).isdecimal()
    return False


def is_exist_task(date: str, event: str) -> bool:
    """Check if a task exists on a given date in the database."""
    query = session.query(Task).filter_by(date=date, event=event)
    if query.first():
        return True
    return False


def formatted_tasks_output(done: str = 'No') -> str:
    """The method returns a formatted string of date events, one event per line.
    Returns all uncompleted tasks by default.
    """
    query = session.query(Task).filter_by(done=done)
    tasks = defaultdict(list)
    for task_object in query.all():
        tasks[task_object.date].append(task_object.event)

    # Formation of a string to display each event with a date.
    response_form = ''
    for date in sorted(tasks):
        for task in sorted(tasks[date]):
            response_form += f"{date}: {task}\n"
    return response_form.rstrip()


def help_task():
    """This function returns a list of available task tracker commands."""
    message = """Date format: YYYY-MM-DD\nOptions are:
        Add Date Task  - Add event
        Del Date Event - Delete event
        Del Date       - Delete all events for a specific date
        Find Date      - Search for events for a specific date
        Print          - Print all events for all dates
        StartApp       - Command to start working with the task tracker
        Quit           - Command to exit the task tracker"""
    return message


def add_task(command):
    """Add a new task.

    If the same task already exists on this date, the answer is returned that
    this task already exists in the database.
    """
    if len(command) >= 3:
        if validate_date(command[1]):
            event = ' '.join(command[2:])
            if not is_exist_task(command[1], event):
                new_task = Task(date=command[1], event=event, done='No')
                session.add(new_task)
                session.commit()
                return "Task added successfully."
            return "This task already exists in the database."
        return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    return "Incorrect command entered. Try again."


def del_task(command):
    """A function to mark a task as completed.

    If no specific task is specified, all tasks for the specified date
    are marked as completed.
    """
    if len(command) >= 2:
        if validate_date(command[1]):
            if len(command) > 2:
                event = ' '.join(command[2:])
                if is_exist_task(command[1], event):
                    query = session.query(Task).filter_by(date=command[1], event=event)
                    task = query.first()
                    task.done = 'Yes'
                    session.commit()
                    return "Deleted successfully"
                return "Event not found"
            query = session.query(Task).filter_by(date=command[1], done='No')
            query_count = query.count()
            for one_task in query.all():
                one_task.done = 'Yes'
            session.commit()
            if query_count > 1:
                end_word_event = 's'
            else:
                end_word_event = ''
            return f"Deleted {query_count} event{end_word_event}"
        return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    return "Incorrect command entered. Try again."


def find_task(command):
    """This function displays all outstanding tasks for the specified date."""
    if len(command) == 2:
        if validate_date(command[1]):
            query = session.query(Task).filter_by(date=command[1], done='No')
            tasks = []
            for task in query.all():
                tasks.append(task.event)
            if tasks:
                return '\n'.join(sorted(tasks))
            return "No events found for this date."
        return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    return "Incorrect command entered. Try again."


def print_task(command):
    """Returns all unfinished tasks for all dates."""
    if len(command) == 1:
        tasks = formatted_tasks_output()
        if tasks:
            return tasks
        return "Incomplete tasks not found"
    return "Incorrect command entered. Try again."


def quit_task():
    """This function returns a message when the task tracker is finished."""
    message = "The task tracker has ended. To re-enter, enter 'StartApp'." + \
              "\nTo exit the program, enter 'Quit'."
    return message
