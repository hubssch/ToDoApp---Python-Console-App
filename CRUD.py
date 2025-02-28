import datetime

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]

def createTask(name: str, status: str, taskDueDate: str):
    if status not in valid_statuses:
        raise ValueError("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")
    
    try:
        taskDueDate = datetime.datetime.strptime(taskDueDate, "%d.%m.%Y").date()
        if taskDueDate < datetime.date.today():
            raise ValueError("Due date cannot be in the past!")
    except ValueError:
        raise ValueError("Invalid date format! Use DD.MM.YYYY.")
    
    taskInputDate = datetime.date.today()
    
    task = {
        'name': name,
        'status': status,
        'taskInputDate': taskInputDate.strftime('%d.%m.%Y'),
        'taskDueDate': taskDueDate.strftime('%d.%m.%Y')
    }
    
    taskArray.append(task)
    
    with open('./ToDo.txt', 'a') as file:
        file.write(f"\n- {task['name']} [{task['status']}] Created: {task['taskInputDate']} | Due: {task['taskDueDate']}")
    
    return task

# def deleteTask(task_name: str):
#     global taskArray
#     taskArray = [task for task in taskArray if task['name'] != task_name]
    
#     with open('./ToDo.txt', 'r') as file:
#         lines = file.readlines()
    
#     with open('./ToDo.txt', 'w') as file:
#         for line in lines:
#             if not line.strip().startswith(f"- {task_name} "):
#                 file.write(line)

def deleteTask(name):
    