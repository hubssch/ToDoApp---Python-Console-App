import datetime
import os

taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]
file_path = './ToDo.txt'

# def load_tasks():
#     """Wczytuje istniejące zadania z pliku do taskArray."""
#     if not os.path.exists(file_path):
#         return  # Jeśli plik nie istnieje, nie rób nic

#     with open(file_path, 'r') as file:
#         for line in file:
#             parts = line.strip().split(' | ')
#             if len(parts) == 3:
#                 name_status = parts[0].split(' ', 1)
#                 if len(name_status) < 2:
#                     continue
                
#                 name = name_status[1].split('[')[0].strip()
#                 status = name_status[1].split('[')[-1].replace(']', '').strip()
#                 created_date = parts[1].split(': ')[-1].strip()
#                 due_date = parts[2].split(': ')[-1].strip()

#                 taskArray.append({
#                     'name': name,
#                     'status': status,
#                     'task_input_date': created_date,
#                     'task_due_date': due_date
#                 })

def create_task(name: str, status: str, task_input_date: datetime.date, task_due_date: datetime.date):
    
    new_task = {
        'name': name,
        'status': status,
        'task_input_date': task_input_date,
        'task_due_date': task_due_date
    }
    
    taskArray.append(new_task)
    save_tasks()  # Zapisujemy zadania po dodaniu nowego

def save_tasks():
    with open(file_path, 'w') as file:
        for index, task in enumerate(taskArray, start=1):
            file.write(f"- {index}. {task['name']} [{task['status']}] | Created: {task['task_input_date']} | Due: {task['task_due_date']}\n")

def update_task(task_number: int, new_name: str, new_status: str, new_task_due_date: datetime.date):
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

def read_tasks():
    with open(file_path, 'r') as file:
        print(file.read())
