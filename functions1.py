def get_todos():
    with open('todos_new.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


def put_todos(todos_local):
    with open('todos_new.txt', 'w') as file:
        file.writelines(todos_local)