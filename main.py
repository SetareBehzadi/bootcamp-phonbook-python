import re
import json
import sys

FILE_NAME = 'contact.json'


def load_contacts():
    try:
        with open(FILE_NAME, 'r') as file:  # Open the file in read mode
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist
    except json.JSONDecodeError:
        return {}  # Return an empty dictionary if the file is empty or not a valid JSON


def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def validate_phone(phone):
    pattern = r"^\+?\d{8}$"
    return re.match(pattern, phone) is not None


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def add_contact(contacts):
    name = input("name: ").strip()
    if not name:
        print("Invalid name.")
        return
    phone = input("phone(without city code and must be 8 digits like 88888888): ").strip()
    if not validate_phone(phone):
        print("Invalid phone number format. must be 8 number:")
        return
    email = input("email: ").strip()
    if not validate_email(email):
        print("Invalid email address format.")
        return

    contacts[name] = {'name': name, 'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")


def edit_contact(contacts):
    name = input("Enter Name to Edit: ").strip()
    if name not in contacts:
        raise ValueError("User Not Found")
    phone = input("new phone number(Empty if you not to change, and must 8 number): ").strip()
    if phone:
        if not validate_phone(phone):
            print("Invalid phone number format. must be 8 number:")
            return
    contacts[name]['phone'] = phone
    email = input("new email(Empty if you not to change): ").strip()
    if email and not validate_email(email):
        print("Invalid email address format.")
        return
    contacts[name]['email'] = email
    save_contacts(contacts)
    print(f"Contact {name} edited successfully!")


def display_contacts(contacts):
    if not contacts:
        print("The List is Empty")
        return
    for name, info in contacts.items():
        print(f"name: {name}")
        print(f"phone: {info['phone']}")
        print(f"email: {info['email']}")
        print("-----")


def delete_contact(contacts):
    name_to_delete = input("Enter Name to Remove: ")
    found = False
    contact_list = list(contacts.items())

    for i, (name, info) in enumerate(contact_list):
        if name == name_to_delete:
            found = True
            contacts.pop(name)
            print(f"Contact {name} deleted successfully!")
            save_contacts(contacts)
            break

    if not found:
        print(f"Contact {name} Not Found!")


def sort_contacts(contacts):
    contact_list = list(contacts.items())
    n = len(contact_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if contact_list[j][0] < contact_list[min_index][0]:
                min_index = j
        contact_list[i], contact_list[min_index] = contact_list[min_index], contact_list[i]

    sorted_contacts = dict(contact_list)
    print("Ordering User Successfully")
    for name, info in sorted_contacts.items():
        print(f"name: {name}")
        print(f"phone: {info['phone']}")
        print(f"email: {info['email']}")
        print("-----")
    return sorted_contacts


def main():
    contacts = load_contacts()
    try:
        while True:
            print('''
Welcome to the Phone Directory
------------------------------
1) Add New Contact
2) Update Contact
3) Delete Contact
4) Show All Contacts
5) Sort Contact
6) Quit
''')

            choice = input("Select any one of the option above:\t").strip()

            if choice == '1':
                add_contact(contacts)
            elif choice == '2':
                edit_contact(contacts)
            elif choice == '3':
                delete_contact(contacts)
            elif choice == '4':
                display_contacts(contacts)
            elif choice == '5':
                contacts = sort_contacts(contacts)
                save_contacts(contacts)
            elif choice == '6':
                print("Exit...")
                sys.exit()
            else:
                print("Try again... You choose wrong number!")

    except Exception as e:
        print(f"Unknown exception occured: {e}")


if __name__ == "__main__":
    main()
