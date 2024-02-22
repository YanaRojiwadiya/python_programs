"""Assignment 5: Inventory Management System
Design a Python program to manage an inventory system for a small store.
The inventory should consist of items with attributes like name, quantity, price, and category.
Implement functionality to add new items, update existing items, remove items, and display the inventory.
Allow users to search for items by name or category and display details of the matching items.
Include features for checking the availability of items, adding items to a shopping cart, and generating a bill.
Ensure the program handles errors gracefully, such as attempting to remove a non-existent item or adding a negative quantity.
Implement a simple text-based user interface with a menu system for navigating different functionalities."""

inventory = {}

def add_book(inventory):
    book_name = input("enter the name of the book: ")
    quantity = int(input("quantity of the book: "))
    category = input("enter the category of the book: ")
    price = int(input("price of the book: "))
    inventory[book_name] = {'quantity': quantity, 'category': category, 'price': price}
    print("book added successfully")

def display_inventory(inventory):
    dict_inventory = {}
    print("current Inventory:")
    for book_name, details in inventory.items():
        dict_inventory[book_name] = {'quantity': details['quantity'], 'category': details['category'], 'price': details['price']}
    print(dict_inventory)

def update_book_quantity(inventory):
    book_name = input("name of the book: ")
    if book_name in inventory:
        new_quantity = int(input("enter the new quantity: "))
        inventory[book_name]["quantity"] = new_quantity
        print("quantity updated")
    else:
        print("Book not found in inventory.")

def update_book_price(inventory):
    book_name = input("name of the book: ")
    if book_name in inventory:
        new_price = int(input("enter the new price: "))
        inventory[book_name]["price"] = new_price
        print("price updated")
    else:
        print("Book not found in inventory.")

def remove_book(inventory):
    name = input("enter a book name: ")
    if name in inventory:
        inventory.pop(name)
        print("book removed ")
    else:
        print("book is not in the inventory")

def search_item(inventory):
        search = input("enter the name of book or category: ")
        found_items = {}
        founded = {}
        for book_name, details in inventory.items():
            if search in book_name or search in details["category"]:
                found_items[book_name] = details
        if found_items:
            for book_name, details in found_items.items():
                founded[book_name] = {'quantity': details['quantity'], 'category': details['category'], 'price': details['price']}
                print(founded)
        else:
            print("item not found.")

def check_availability(inventory):
    name = input("enter the name of book: ")
    for book_name, details in inventory.items():
        if name in book_name:
            if details['quantity'] > 0:
                print("yes, this book is available")
            else:
                print("no, this book is not available")

shopping_cart = {}
def add_to_cart(inventory):
    display_inventory(inventory)
    name = input("enter the name of book you want to buy: ")
    for book_name, details in inventory.items():
        if name in book_name:
            if details['quantity'] > 0:
                shopping_cart[book_name] = {'quantity': details['quantity'], 'category': details['category'], 'price': details['price']}
                print("shopping cart: ", shopping_cart)
            else:
                print("sorry, this book is not available right now")

def generate_bill(inventory):
    customer = input("enter your name: ")
    print("---------- Book Store ----------")
    print("Name :",customer)
    total = 0
    for book_name, details in shopping_cart.items():
        print(f"Product Name: {book_name} , 'quantity': {details['quantity']}, 'category': {details['category']}, 'price': {details['price']}") 
        total += details['price']
        inventory[book_name]['quantity'] -= 1
    print("Total : ",total)
    print("---------- Thank You ----------")

while True:
    print("\nOptions:")
    print("1. Add a book to inventory")
    print("2. Display current inventory")
    print("3. Update book quantity")
    print("4. Update book price")
    print("5. Remove book")
    print("6. search item by name or category")
    print("7. check availability")
    print("8. add to cart")
    print("9. generate bill")
    print("10. Exit")

    choice = input("select option: ")

    if choice == '1':
        add_book(inventory)
    elif choice == '2':
        display_inventory(inventory)
    elif choice == '3':
        update_book_quantity(inventory)
    elif choice == '4':
        update_book_price(inventory)
    elif choice == '5':
        remove_book(inventory)
    elif choice == '6':
        search_item(inventory)
    elif choice == '7':
        check_availability(inventory)
    elif choice == '8':
        add_to_cart(inventory)
    elif choice == '9':
        generate_bill(inventory)
    elif choice == '10':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose from option 1 to 10")
