"""A personal task recorder that communicates with the user via standard I/O streams."""
import click
from views.cli import path_database, cli_show_current, cli_show_done
from views.commands import (
    add_task, del_task, find_task, help_task, print_task, quit_task
)


def task_tracker_commands():
    """Task tracker commands."""
    command = ''
    print("Enter 'StartApp' to start working with the task tracker ('Quit' - to exit):")

    while command != 'Quit':
        command = input('> ')

        if command == 'StartApp':
            print("Welcome to the task tracker!\nEnter 'Quit' to quit the task tracker. "
                  "For help enter 'Help'.")
            _exit = False
            while not _exit:
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
                            _exit = True

                    if _exit:
                        break


@click.command()
@click.option('--show_current', is_flag=True, help='Show all current not completed tasks')
@click.option('--show_done', is_flag=True, help='Show all current completed tasks')
@click.option('--database', is_flag=True, help='Path to the used database')
def main(show_current, show_done, database):
    """A personal task recorder that communicates with the user via standard I/O streams."""
    # Command line interface
    if show_current:
        print(cli_show_current())
    elif show_done:
        print(cli_show_done())
    elif database:
        print(path_database())
    else:
        # Task tracker commands
        task_tracker_commands()


if __name__ == "__main__":
    main()
