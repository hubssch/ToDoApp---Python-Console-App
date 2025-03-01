from CRUD import create_task, read_tasks, update_task, valid_statuses, taskArray
import datetime

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

            inputDate = datetime.date.today()
            dueDate = input("Enter due date (DD.MM.YYYY): ")

            create_task(name, status, inputDate, dueDate)
            break

    elif action.lower() == 'read tasks':
        read_tasks()

    elif action.lower() == 'update task':
        task_number = int(input("Enter the task number to edit: "))

        new_name = input("Edit task name: ")

        new_status = input("Set task status (ToDo, In Progress, Done): ")

        new_task_due_date = input("Enter new due date (DD.MM.YYYY): ")

        update_task(task_number, new_name, new_status, new_task_due_date)