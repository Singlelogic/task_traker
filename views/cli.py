from model.task import Task


def show_current():
    return Task.formatted_tasks_output()

def show_done():
    return Task.formatted_tasks_output(done='yes')

def path_database():
    print('Running path database')