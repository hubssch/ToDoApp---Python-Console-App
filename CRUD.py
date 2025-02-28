taskArray = []
valid_statuses = ["ToDo", "In Progress", "Done"]


def createTask():
    while True:
        name = input('Type task name or quit: ')
        if name.lower() == 'quit':
            break
        while True:
            status = input('Set task status (ToDo, In Progress, Done): ')
            # taskArray.append(name)
            # return print(taskArray)
            break