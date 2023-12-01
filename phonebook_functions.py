"""Module to host all methods of the program"""
import json
from contact import Contact

filename = 'contacts_list.json'


def init_phonebook():
    """Create the file and dump the empty list...should only be invoked once."""
    book = []
    with open(filename, 'a+') as f_obj:
        json.dump(book, f_obj)


def add_contact():
    """Add a new contact to the list after retrieving it from the file"""
    new = Contact()
    book = get_file()
    book.append(new.details)
    with open(filename, 'w') as f_obj:
        json.dump(book, f_obj)
        print("Contact added successfully! ")


def get_file():
    """Retrieve the list of dictionaries from the file"""
    with open(filename, 'r') as f:
        book = json.load(f)
        return book


def delete_contact():
    """Delete a specific contact dictionary."""
    book = get_file()
    person = input("Enter the contact name: ")
    for x in range(len(book)):
        if book[x]['name'] == person:
            del book[x]
            print("Contact deleted successfully")
            with open(filename, 'w') as f_obj:
                json.dump(book, f_obj)
                print("Contact deleted!")
            break


def view_all_contacts():
    """View all the dictionaries  well formatted."""
    book = get_file()
    for thing in book:
        for key, value in thing.items():
            print(key + ':' + value, "\n")

        print("\n\n")


def edit_contact():
    """Change a specific value in a contact  dictionary."""
    book = get_file()

    choice = input("Update by 1. name, 2.email, 3. Tel no :")
    if choice == '1':
        person = input("Enter name of the contact to edit: ")
        for x in range(len(book)):
            if book[x]['name'] == person:
                book[x]['name'] = input("Update name: ")
        with open(filename, 'w') as f_obj:
            json.dump(book, f_obj)
            print("Contact updated!")
    elif choice == '2':
        em = input("Enter current email: ")
        for x in range(len(book)):
            if book[x]['email'] == em:
                book[x]['email'] = input("Update email: ")
        with open(filename, 'w') as f_obj:
            json.dump(book, f_obj)
            print("Contact updated!")
    elif choice == '3':
        no = input("Enter number: ")
        for x in range(len(book)):
            if book[x]['Tel'] == no:
                book[x]['Tel'] = input("Update number: ")
        with open(filename, 'w') as f_obj:
            json.dump(book, f_obj)
            print("Contact updated!")

