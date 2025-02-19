taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]

while True:
    name = input("Add new task (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    while True:
        status = input("Set task status (ToDo, In Progress, Done): ")
        if status in valid_statuses:
            break
        print("Invalid status! Please enter 'ToDo', 'In Progress' or 'Done'.")

    task = {'name': name, 'status': status}
    taskArray.append(task)


print("\nYour tasks:")
for task in taskArray:
    print(f"- {task['name']} [{task['status']}]")  # Formatowane wyświetlanie listy

