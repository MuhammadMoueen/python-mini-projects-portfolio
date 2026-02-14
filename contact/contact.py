import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def show_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n--- CONTACT LIST ---")
    for name, number in contacts.items():
        print(f"{name} : {number}")


def add_contact(contacts):
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    save_contacts(contacts)
    print("Contact added!")


def edit_contact(contacts):
    name = input("Enter contact name to edit: ")

    if name in contacts:
        contacts[name] = input("Enter new number: ")
        save_contacts(contacts)
        print("Contact updated!")
    else:
        print("Contact not found!")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted!")
    else:
        print("Contact not found!")


def search_contact(contacts):
    name = input("Search name: ")

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Not found!")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


main()
