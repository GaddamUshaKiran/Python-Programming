class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name}: {contact.phone}")

    def delete_contact(self, contact_number):
        try:
            del self.contacts[contact_number - 1]
        except IndexError:
            print("Invalid contact number.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add contact")
        print("2. Display contacts")
        print("3. Delete contact")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact = Contact(name, phone)
            contact_book.add_contact(contact)
        elif choice == 2:
            contact_book.display_contacts()
        elif choice == 3:
            try:
                contact_number = int(input("Enter contact number to delete: "))
                contact_book.delete_contact(contact_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

