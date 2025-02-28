import datetime
from CRUD import createTask

taskArray = []

while True:
    name = input("Add new task (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    while True:
        status = input("Set task status (ToDo, In Progress, Done): ")
        if status in ["ToDo", "In Progress", "Done"]:
            break
        print("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")

    while True:
        taskDueDate = input("Enter due date (DD.MM.YYYY): ")
        try:
            datetime.datetime.strptime(taskDueDate, "%d.%m.%Y").date()
            break
        except ValueError:
            print("Invalid date format! Use DD.MM.YYYY.")

    task = createTask(name, status, taskDueDate)
    taskArray.append(task)

with open('./ToDo.txt', 'r') as readFile:
    print(f"\nYour tasks:{readFile.read()}")

print('\nNew task added:')
for task in taskArray:
    print(f"- {task['name']} [{task['status']}] Created: {task['taskInputDate']} | Due: {task['taskDueDate']}")
