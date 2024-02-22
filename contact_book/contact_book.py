"""Assignment 3: Contact Book
Develop a Python program to manage a contact book.
Allow users to add new contacts, search for contacts by name, and delete contacts.
Use a dictionary to store contacts where the keys are contact names and the values are dictionaries containing contact information like phone number, email, etc.
Implement error handling for cases where a contact is not found during search or deletion."""

contact = {}
def add_contact(contact):
    name = input("enter name: ")
    number = int(input("enter number: "))
    email = input("Enter email: ")
    n = str(number)
    if len(n) == 10:
        contact[name]={'phone': n, 'email': email}
        print("contact added")
    else:
        print("please enter valid phone number")

def display_contact(contact):
    dict_contact = {}
    for name, info in contact.items():
        dict_contact[name] = {'Phone': info['phone'], 'email': info['email']}
    print(dict_contact)

def remove_contact(contact):
    name = input("enter name: ")
    if name in contact:
        contact.pop(name)
        print("contact removed ")
    else:
        print("name is not in the contacts")    

def search_contact(contact):
    name = input("enter name: ")
    if name in contact:
        info = contact[name]
        print(f"{name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("name is not in the contacts")

def main():

    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. Display contact")
        print("3. Remove contact")
        print("4. Search contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contact)
        elif choice == '2':
            display_contact(contact)    
        elif choice == '3':
            remove_contact(contact)
        elif choice == '4':
            search_contact(contact)
        elif choice == '5':
            print("exit")
            break
        else:
            print("choose number between 1 to 5")

if __name__ == "__main__":
    main()
