from task import Task


task = Task('db.sqlite3', 'tasks')
# print(task)
task.add("tasks", "2020-09-17", "First_task")
# print(task)
task.add("tasks", "2020-09-18", "Second_task")
# print(task)
task.add("tasks", "2020-09-19", "Third_task")
