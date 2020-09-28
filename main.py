from model.task import Task


# task1 = Task('2020-09-17', 'First_task')
# task1.save()
#
# task2 = Task('2020-09-17', 'Second_task')
# task2.save()
#
# task3 = Task('2020-09-18', 'Third_task')
# task3.save()
#
# task4 = Task('2020-09-17', 'Fourth_task')
# task4.save()


all_tasks = Task.find_task()
for task in all_tasks:
    print(task)

print("##########################################")
task = Task.find_task("2020-09-18")
for task in task:
    print(task)

Task.change_status_task('2020-09-17', 'First_task')

print("##########################################")
all_tasks = Task.find_task()
for task in all_tasks:
    print(task)

Task.change_status_task('2020-09-17')

print("##########################################")
all_tasks = Task.find_task()
for task in all_tasks:
    print(task)