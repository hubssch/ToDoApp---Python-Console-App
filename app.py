import datetime
from CRUD import create_task, read_tasks, update_task, valid_statuses, taskArray

while True:
    action = input('What do you want to do? (create task, read tasks, delete task, update task or quit): ')
    if action.lower() == 'quit':
        break

    if action.lower() == 'create task':
        while True:
            name = input("Create new task or type 'quit' to exit: ")
            if name.lower() == 'quit':
                break

            status = input('Set task status (ToDo, In Progress, Done): ')
            if status not in valid_statuses:
                print("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")
                continue 

            input_date = datetime.date.today()
            
            due_date = input("Enter due date (DD.MM.YYYY): ")
            try:
                due_date_parsed = datetime.datetime.strptime(due_date, "%d.%m.%Y").date()
            except ValueError:
                print("Invalid date format! Please use DD.MM.YYYY.")
                continue  

            create_task(name, status, input_date, due_date_parsed)
            break

    elif action.lower() == 'read tasks':
        read_tasks()

    elif action.lower() == 'update task':
        task_number = int(input("Enter the task number to edit: "))

        new_name = input("Edit task name: ")

        new_status = input("Set task status (ToDo, In Progress, Done): ")

        new_task_due_date = input("Enter new due date (DD.MM.YYYY): ")
        try:
            new_task_due_date_parsed = datetime.datetime.strptime(new_task_due_date, "%d.%m.%Y").date()
        except ValueError:
            print("Invalid date format! Please use DD.MM.YYYY.")
            continue

        update_task(task_number, new_name, new_status, new_task_due_date_parsed)
