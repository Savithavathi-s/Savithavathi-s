Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def main():
    contacts = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting contact book...")
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("\nContact Book Menu:")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Contact '{name}' added to the contact book.")

def search_contact(contacts):
    if not contacts:
        print("The contact book is empty.")
        return

    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]

    if not found_contacts:
        print("No contacts found.")
    else:
        print("\nFound contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact(contacts):
    if not contacts:
        print("The contact book is empty.")
        return

    name = input("Enter the name of the contact to update: ")
    found_contacts = [contact for contact in contacts if name.lower() in contact["name"].lower()]

    if not found_contacts:
        print("No contacts found.")
        return

    print("\nFound contacts:")
    for i, contact in enumerate(found_contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    choice = int(input("Enter the number of the contact to update: "))
...     if choice < 1 or choice > len(found_contacts):
...         print("Invalid choice.")
...         return
... 
...     updated_contact = found_contacts[choice - 1]
...     updated_contact["phone"] = input(f"Enter new phone number (current: {updated_contact['phone']}): ")
...     updated_contact["email"] = input(f"Enter new email address (current: {updated_contact['email']}): ")
...     print(f"Contact '{updated_contact['name']}' updated.")
... 
... def delete_contact(contacts):
...     if not contacts:
...         print("The contact book is empty.")
...         return
... 
...     name = input("Enter the name of the contact to delete: ")
...     found_contacts = [contact for contact in contacts if name.lower() in contact["name"].lower()]
... 
...     if not found_contacts:
...         print("No contacts found.")
...         return
... 
...     print("\nFound contacts:")
...     for i, contact in enumerate(found_contacts, start=1):
...         print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
... 
...     choice = int(input("Enter the number of the contact to delete: "))
...     if choice < 1 or choice > len(found_contacts):
...         print("Invalid choice.")
...         return
... 
...     deleted_contact = found_contacts[choice - 1]
...     contacts.remove(deleted_contact)
...     print(f"Contact '{deleted_contact['name']}' deleted.")
... 
... if __name__ == "__main__":
