from CRUD import createTask

taskArray = []


while True:
    action = input('What do you want to do? (create task, read tasks, delete task, update task or quit)')
    if action.lower() == 'quit':
        break
    while True:
        if action == 'create task':
            createTask()
    # elif action == 'read tasks':
