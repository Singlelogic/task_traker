import argparse
from views.cli import path_database, show_current, show_done
from views.commands import (
    add_task, del_task, find_task, help_task, print_task, quit_task
)


parser = argparse.ArgumentParser()

parser.add_argument('--show_current', action='store_true', help='Show all current not completed tasks')
parser.add_argument('--show_done', action='store_true', help='Show all current completed tasks')
parser.add_argument('--database', action='store_true', help='Path to the used database')

# Command line interface
if parser.parse_args().show_current:
    print(show_current())
elif parser.parse_args().show_done:
    print(show_done())
elif parser.parse_args().database:
    print(path_database())
# Task tracker commands
else:
    command = ''
    print("Enter 'StartApp' to start working with the task tracker ('Quit' - to exit):")

    while command != 'Quit':
        command = input('> ')

        if command == 'StartApp':
            print("Welcome to the task tracker!\nEnter 'Quit' to quit the task tracker. "
                  "For help enter 'Help'.")
            exit = False
            while not exit:
                commands = input('> ').strip().split('\n')
                for command in commands:
                    command = command.split()
                    if command:
                        if command[0] == 'Help':
                            print(help_task())

                        elif command[0] == 'Add':
                            print(add_task(command))

                        elif command[0] == 'Del':
                            print(del_task(command))

                        elif command[0] == 'Find':
                            print(find_task(command))

                        elif command[0] == 'Print':
                            print(print_task(command))

                        elif command[0] == 'Quit':
                            print(quit_task())
                            exit = True

                    if exit:
                        break
