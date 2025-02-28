from CRUD import createTask, readTasks, valid_statuses
import datetime

while True:
    action = input('What do you want to do? (create task, read tasks, delete task, update task or quit): ')
    if action.lower() == 'quit':
        break
    while True:
        name = input("Create new task or type 'quit' to exit: ")
        if name.lower() == 'quit':
            break

        status = input('Set task status (ToDo, In Progress, Done): ')
        if status not in valid_statuses:
             raise ValueError("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")
        
        inputDate = datetime.date.today()

        dueDate = input("Enter due date (DD.MM.YYYY): ")
        break

    createTask(name, status, inputDate, dueDate)