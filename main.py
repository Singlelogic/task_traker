from model.task import Task


print("Enter 'StartApp' to start working with the task tracker:")

command = input('> ')

if command == 'StartApp':
    print("Welcome to the task tracker!\nEnter 'Quit' to quit the task tracker. "
          "For help enter 'Help'.")
    while command[0] != 'Quit':
        command = input('> ')
        command = command.strip().split()

        if command[0] == 'Help':
            print("Date format: YYYY-MM-DD")
            print("Options are:")
            print("   Add Date Task  - Add event.")
            print("   Del Date Event - Delete event")
            print("   Del Date       - Delete all events for a specific date")
            print("   Find Date      - Search for events for a specific date")
            print("   Print          - Print all events for all dates")
            print("   StartApp       - Command to start working with the task tracker")
            print("   Quit           - Сommand to exit the task tracker")

        elif command[0] == 'Add':
            task = Task(command[1], ' '.join(command[2:]))
            task.save()
