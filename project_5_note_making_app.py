notes = {}

print("Welcome to note taking app.")


def add_note(Note, note):
    Note[len(Note)+1] = note
    return Note


def display_notes(Note):
    if Note == {}:
        print("The folder is empty.")
    else:
        print('\nThe notes are: \n')
        for key in Note:
            print(f"{key}: {Note[key]}")


def delete_note(Note, number):
    if number in Note:
        Note.pop(number)
        values = [value for key,value in Note.items()]
        numbers = [x for x in range(1,len(Note)+1)]
        del Note
        Note = {key: val for key, val in zip(numbers, values)}
    else:
        print("\nThe given note number is not exist.")
    return Note


def edit_note(Note, number):
    if number in Note:
        Note[number] = input('\nEnter the note: ')
    else:
        print("The note number doesn't exit.")
    return Note


application_is_on = True

while application_is_on:
    print("\n1) for add a note.")
    print("2) for edit a note.")
    print("3) for delete a note.")
    print("4) for display all the notes")
    print("5) for exit the application.")

    choice = input('\nEnter any above choice: ')

    if choice == '5':
        print("The application is turned off.")
        application_is_on = False

    elif choice == '4':
        display_notes(Note=notes)

    elif choice == '3':
        if notes == {}:
            print("\nThe note is emtpy.")
            continue
        notes = delete_note(Note=notes, number=int(input('Enter the note number to delete: ')))

    elif choice == '2':
        notes = edit_note(Note=notes, number=int(input('Enter the note number to edit: ')) )

    elif choice == '1':
        notes = add_note(Note=notes, note=input('\nEnter the note to be store: '))

    else:
        print('\nEnter the correct choice.')
