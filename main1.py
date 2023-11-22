from functions1 import get_todos,put_todos
while True:
    action = input("Type add,show,edit,complete or exit:")
    action = action.strip()
    if action.startswith('add'):
        new_todo = action[4:]

        if new_todo == "":
            print("You forgot to enter the todo \U0001F604")
        else:
            todos = get_todos()

            todos.append(new_todo+'\n')

            put_todos(todos)

            print(f'Successfully added "{new_todo}" to the list')

    elif action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            if len(todos) == 0:
                print("Todo is empty")
            else:
                item = item.strip('\n')
                print(f"{index + 1}-{item}")

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            new_todo = input("Enter the new todo :")
            todos = get_todos()

            todos[number - 1] = new_todo + '\n'

            put_todos(todos)
            print(f'Number {number} of your todo has been updated to "{new_todo}"')
        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            put_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith('exit'):
        break

    else:
        print("Invalid command")

print("Bye")