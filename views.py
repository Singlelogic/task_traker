from model.task import Task


def help_task():
    """This function returns a list of available task tracker commands."""
    message = """Date format: YYYY-MM-DD\nOptions are: 
        Add Date Task  - Add event
        Del Date Event - Delete event
        Del Date       - Delete all events for a specific date
        Find Date      - Search for events for a specific date
        Print          - Print all events for all dates
        StartApp       - Command to start working with the task tracker
        Quit           - Сommand to exit the task tracker
        """
    return message

def add_task(command):
    """Add a new task.

    If the same task already exists on this date, the answer is returned that
    this task already exists in the database.
    """
    if len(command) >= 3:
        if validate_date(command[1]):
            event = ' '.join(command[2:])
            if not Task.is_exist_task(command[1], event):
                newtask = Task(command[1], event)
                newtask.save()
                return "Task added successfully."
            else:
                return "This task already exists in the database."
        else:
            return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    else:
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
                if Task.is_exist_task(command[1], event):
                    Task.change_status_task(command[1], event)
                    return "Deleted successfully"
                else:
                    return "Event not found"
            else:
                amount_task_found = len(Task.find_task(command[1]))
                Task.change_status_task(command[1])
                if amount_task_found > 1:
                    end_word_event = 's'
                else:
                    end_word_event = ''
                return f"Deleted {amount_task_found} event{end_word_event}"
        else:
            return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    else:
        return "Incorrect command entered. Try again."

def find_task(command):
    """This function displays all outstanding tasks for the specified date."""
    if len(command) == 2:
        if validate_date(command[1]):
            tasks_from_db = Task.find_task(command[1])
            tasks = []
            for task in tasks_from_db:
                tasks.append(task.get_event())
            if tasks:
                return '\n'.join(sorted(tasks))
            else:
                return "No events found for this date."

        return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    else:
        return "Incorrect command entered. Try again."

def quit_task():
    """This function returns a message when the task tracker is finished."""
    message = """The task tracker has ended. To re-enter, enter 'StartApp'.\nTo exit the program, enter 'Quit'."""
    return message

def validate_date(msg: str):
    """Check if the given string is a date."""
    msg = msg.split('-')
    if len(msg) == 3:
        if (len(msg[0]) == 4) and (len(msg[1]) == 2) and (len(msg[2]) == 2):
            if (int(msg[1]) <= 12) and (int(msg[2]) <= 31):
                return ''.join(msg).isdecimal()
