
while True:
    action = input("Type add,show,edit,complete or exit:")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # method 1 to strip newline(for loop)
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # method 2 to strip new line(list comprehensions)
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}-{item}")

        case 'edit':
            number = int(input("Enter the number of the todo to edit:"))
            # if number > len(todos):
            #     print("Invalid number")
            new_todo = input("Enter the new todo :")

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos[number-1] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(f'Number {number} of your todo has been updated to "{new_todo}"')

        case 'complete':
            number = int(input("Enter the number of todo which has been completed:"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")

        case 'exit':
            break
print("Bye")