from views import (
    add_task, help_task, quit_task, del_task, find_task,
)


command = ''
print("Enter 'StartApp' to start working with the task tracker ('Quit' - to exit):")

while command != 'Quit':
    command = input('> ')

    if command == 'StartApp':
        print("Welcome to the task tracker!\nEnter 'Quit' to quit the task tracker. "
              "For help enter 'Help'.")
        while True:
            command = input('> ').strip().split()
            if command:
                if command[0] == 'Help':
                    print(help_task())

                elif command[0] == 'Add':
                    print(add_task(command))

                elif command[0] == 'Del':
                    print(del_task(command))

                elif command[0] == 'Find':
                    print(find_task(command))

                elif command[0] == 'Quit':
                    print(quit_task())
                    break

