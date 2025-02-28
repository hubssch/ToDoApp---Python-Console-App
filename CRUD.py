import datetime

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]


def createTask(name: str, status: str, taskInputDate: datetime, taskDueDate: datetime):
    task = {
        'name': name,
        'status': status,
        'taskInputDate': taskInputDate,
        'taskDueDate': taskDueDate
    }
    taskArray.append(task)
    for task in taskArray:
        print(f"- {task['name']} [{task['status']}] Created: {task['taskInputDate']} | Due: {task['taskDueDate']}")

def readTasks():
    for task in taskArray:
        print(f"- {task['name']} [{task['status']}] Created: {task['taskInputDate']} | Due: {task['taskDueDate']}")