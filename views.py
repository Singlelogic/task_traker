from model.task import Task


def help_task():
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
    if len(command) >= 3:
        if validate_date(command[1]):
            event = ' '.join(command[2:])
            newtask = Task(command[1], event)
            newtask.save()
            return "Task added successfully."
        else:
            return "Invalid date entered. The date format is YYYY-MM-DD. Try again."
    else:
        return "Incorrect command entered. Try again."

def quit_task():
    message = """The task tracker has ended. To re-enter, enter 'StartApp'.\nTo exit the program, enter 'Quit'."""
    return message

def validate_date(msg: str):
    """Check if the given string is a date."""
    msg = msg.split('-')
    if len(msg) == 3:
        if (len(msg[0]) == 4) and (len(msg[1]) == 2) and (len(msg[2]) == 2):
            if (int(msg[1]) <= 12) and (int(msg[2]) <= 31):
                return ''.join(msg).isdecimal()
