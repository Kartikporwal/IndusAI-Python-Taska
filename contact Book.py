import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {
            'phone': phone,
            'email': email
        }
        self.save_contacts()

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 20)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Deleted contact: {name}")
        else:
            print("Contact not found.")

def main():
    book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
