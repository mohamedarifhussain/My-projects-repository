todo_list = []

print("Welcome to 'todo' list app.")

while True:
    print("\n1)Enter 'a' for add a todo.")
    print("2)Enter 'd' for delete a todo.")
    print("3)Enter 'dp' for display all the todo.")
    print("4)Enter 'e' for edit a todo.")
    print("5)Enter 'off' to exit")
    choice = input("\nEnter your choice: ")
    if choice.lower() == 'a':
        todo_list.append(input('\nEnter a todo for add: '))
    elif choice.lower() == 'd':
        todo_list.remove(input('\nEnter a todo for delete: '))
    elif choice.lower() == 'dp':
        if todo_list == []:
            print("\nNothing in todolist.")
        else:
            for todo in todo_list:
                print(f"{todo_list.index(todo)+1}) {todo}")
    elif choice.lower() == 'e':
        edit = int(input('\nEnter the number of the todo to edit:'))
        if len(todo_list)>=edit:
            todo_list[edit-1]=input("\nEnter the todo here: ")
        else:
            print("\nThe todo number doesn't exist!")
    elif choice.lower() == 'off':
        print("\nThe program is turned off.")
        break
