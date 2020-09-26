from task import Task


task = Task('db.sqlite3', 'tasks')
# task.add_task("2020-09-17", "First_task")
# task.add_task("2020-09-18", "Second_task")
# task.add_task("2020-09-19", "Third_task")
# task.add_task("2020-09-17", "Fourth_task")

for row in task.find_task("2020-09-17"):
    print(row)

print("#########################")
for row in task.find_all_tasks():
    print(row)

task.change_status_task("2020-09-17", "First_task")
task.change_status_all_task("2020-09-17")
