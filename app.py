import datetime

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]
file = open('ToDo.txt', 'a')

while True:
    name = input("Add new task (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    while True:
        status = input("Set task status (ToDo, In Progress, Done): ")
        if status in valid_statuses:
            break
        print("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")

    while True:
        taskDueDate = input("Enter due date (DD.MM.YYYY): ")
        try:
            taskDueDate = datetime.datetime.strptime(taskDueDate, "%d.%m.%Y").date()
            if taskDueDate < datetime.date.today():
                print("Due date cannot be in the past! Try again.")
            else:
                break
        except ValueError:
            print("Invalid date format! Use DD.MM.YYYY.")

    taskInputDate = datetime.date.today()  # Data utworzenia zadania

    task = {
        'name': name,
        'status': status,
        'taskInputDate': taskInputDate.strftime('%d.%m.%Y'),  # Zmieniony format
        'taskDueDate': taskDueDate.strftime('%d.%m.%Y')  # Zmieniony format
    }
    taskArray.append(task)
    file.write(str(f'\n{task}'))
    # file.close()
    

print("\nYour tasks:")
for task in taskArray:
    print(f"- {task['name']} [{task['status']}] Created: {task['taskInputDate']} | Due: {task['taskDueDate']}")
