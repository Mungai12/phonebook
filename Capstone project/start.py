import phonebook_functions as pf
from os import system

"""The very first time you run the program, you have to choose option 5 to initialize the file storage.
Then after that never choose it again, or the program will not run. if you happen to choose it again,
delete the created file(contacts_list.json), choose option 5 again and never choose it again after that
"""


def menu():
    print("\t\t\t************** WELCOME TO THE MAIN MENU ***************\n\n")
    print("\t\t1. Add a new contact: \n")
    print("\t\t2. Edit a contact: \n")
    print("\t\t3. Delete a contact: \n")
    print("\t\t4: View all contacts: \n")
    print("\t\t5: initialize phonebook(Call this method only once): \n")

    choice = input("Enter a choice: ")

    if choice == '1':
        pf.add_contact()
        smart_exit()
    if choice == '2':
        pf.edit_contact()
        smart_exit()
    if choice == '3':
        pf.delete_contact()
        smart_exit()
    if choice == '4':
        pf.view_all_contacts()
        smart_exit()
    if choice == '5':
        pf.init_phonebook()


def smart_exit():
    choice = input("Enter 1 to return to main menu or 0 to exit: ")
    if choice == '1':
        system('cls')
        menu()
    elif choice == '0':
        exit("Thank you!")


menu()
