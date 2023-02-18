# Fungsi untuk membaca phone_book
def read_phone_book(book, file):
    with open(file, "r") as f:
        for line in f:
            name, number = line.strip().split(":")
            book[name] = number
        if book:
            print("Contacts:")
            for name, number in book.items():
                print(f"{name}: {number}")
            print()


def options():
    print("What would you like to do?")
    print("1. Add a new contact")
    print("2. Update an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Print phone book")
    print("6. Quit")


def add_contact(book):
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")
    book[name] = number
    print(f"{name} has been added to the phone book.\n")


def update_contact(book):
    name = input("Enter the name of the contact: ")
    if name in book:
        number = input("Enter the new phone number of the contact: ")
        book[name] = number
        print(f"{name}'s phone number has been updated.\n")
    else:
        print(f"{name} is not in the phone book.\n")


def delete_contact(book):
    name = input("Enter the name of the contact: ")
    if name in book:
        del book[name]
        print(f"{name} has been deleted from the phone book.\n")
    else:
        print(f"{name} is not in the phone book.\n")


def search_contact(book):
    name = input("Enter the name of the contact: ")
    if name in book:
        print(f"{name}: {book[name]}\n")
    else:
        print(f"{name} is not in the phone book.\n")


def quit(book, file):
    #write the phone book data to the file
    with open(file, "w") as f:
        for name, number in book.items():
            f.write(f"{name}:{number}\n")

    print("Goodbye!")
    exit(0)
