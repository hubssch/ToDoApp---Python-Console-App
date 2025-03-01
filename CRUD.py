import datetime

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]


def create_task(name: str, status: str, task_input_date: datetime, task_due_date: datetime):
    task = {
        'name': name,
        'status': status,
        'task_input_date': task_input_date,
        'task_due_date': task_due_date
    }
    taskArray.append(task)

def read_tasks():
    for task in taskArray:
        print(f"- {task['name']} [{task['status']}] Created: {task['task_input_date']} | Due: {task['task_due_date']}")

def update_task():
