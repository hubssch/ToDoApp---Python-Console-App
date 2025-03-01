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
    for index, task in enumerate(taskArray, start = 1):
        print(f"- {index}. {task['name']} [{task['status']}] Created: {task['task_input_date']} | Due: {task['task_due_date']}")

def update_task(task_number: int, new_name: str, new_status: str, new_task_due_date: datetime):
    index = task_number - 1
    if 0 <= index < len(taskArray):
        if new_name:
            taskArray[index]['name'] = new_name
        if new_status:
            taskArray[index]['status'] = new_status
        if new_task_due_date:
            taskArray[index]['task_due_date'] = new_task_due_date
        print(f"Task {task_number} updated successfully!")
    else:
        print("Invalid task number!")
