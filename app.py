import datetime
from CRUD import create_task, read_tasks, update_task, valid_statuses, taskArray, load_tasks

load_tasks()

while True:
    action = input('What do you want to do? (create task, read tasks, delete task, update task or quit): ')
    if action.lower() == 'quit':
        break

    if action.lower() == 'create task':
        name = input("Create new task or type 'quit' to exit: ")
        if name.lower() == 'quit':
            continue

        while True:
            status = input('Set task status (ToDo, In Progress, Done): ')
            if status in valid_statuses:
                break
            print("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")

        input_date = datetime.date.today()

        while True:
            due_date = input("Enter due date (DD.MM.YYYY): ")
            try:
                due_date_parsed = datetime.datetime.strptime(due_date, "%d.%m.%Y").date()
                break
            except ValueError:
                print("Invalid date format! Please use DD.MM.YYYY.")

        create_task(name, status, input_date, due_date_parsed)

    elif action.lower() == 'read tasks':
        read_tasks()

    elif action.lower() == 'update task':
        task_number = int(input("Enter the task number to edit: "))

        new_name = input("Edit task name: ")

        new_status = input("Set task status (ToDo, In Progress, Done): ")

        while True:
            new_task_due_date = input("Enter new due date (DD.MM.YYYY): ")
            try:
                new_task_due_date_parsed = datetime.datetime.strptime(new_task_due_date, "%d.%m.%Y").date()
                break
            except ValueError:
                print("Invalid date format! Please use DD.MM.YYYY.")

        update_task(task_number, new_name, new_status, new_task_due_date_parsed)
