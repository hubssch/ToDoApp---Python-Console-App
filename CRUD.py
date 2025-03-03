import datetime
import os

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]
file_path = './ToDo.txt'

def load_tasks():

    if not os.path.exists(file_path):
        return  # Jeśli plik nie istnieje, nie rób nic

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' | ')
            if len(parts) != 3:
                continue

            name_status = parts[0].split(' ', 1)
            if len(name_status) < 2:
                continue

            name = name_status[1].split('[')[0].strip()
            status = name_status[1].split('[')[-1].replace(']', '').strip()
            created_date = parts[1].split(': ')[-1].strip()
            due_date = parts[2].split(': ')[-1].strip()

            try:
                created_date_parsed = datetime.datetime.strptime(created_date, "%Y-%m-%d").date()
            except ValueError:
                created_date_parsed = datetime.datetime.strptime(created_date, "%d.%m.%Y").date()

            try:
                due_date_parsed = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                due_date_parsed = datetime.datetime.strptime(due_date, "%d.%m.%Y").date()

            taskArray.append({
                'name': name,
                'status': status,
                'task_input_date': created_date_parsed,
                'task_due_date': due_date_parsed
            })


def create_task(name: str, status: str, task_input_date: datetime.date, task_due_date: datetime.date):
    new_task = {
        'name': name,
        'status': status,
        'task_input_date': task_input_date,
        'task_due_date': task_due_date
    }

    taskArray.append(new_task)
    save_tasks()  

def save_tasks():

    with open(file_path, 'w') as file:
        for index, task in enumerate(taskArray, start=1):
            file.write(f"- {index}. {task['name']} [{task['status']}] | Created: {task['task_input_date'].strftime('%d.%m.%Y')} | Due: {task['task_due_date'].strftime('%d.%m.%Y')}\n")

def update_task(task_number: int, new_name: str, new_status: str, new_task_due_date: datetime.date):
    index = task_number - 1
    if 0 <= index < len(taskArray):
        if new_name:
            taskArray[index]['name'] = new_name
        if new_status:
            taskArray[index]['status'] = new_status
        if new_task_due_date:
            taskArray[index]['task_due_date'] = new_task_due_date

        save_tasks()
        print(f"Task {task_number} updated successfully!")
    else:
        print("Invalid task number!")

def read_tasks():

    if not os.path.exists(file_path):
        print("No tasks found.")
        return

    with open(file_path, 'r') as file:
        print(file.read())
