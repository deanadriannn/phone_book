from module import *
# variabel penampung file txt
phone_book_file = "phone_book.txt"

# Fictionary kosong
phone_book = {}

while True:
    options()
    choice = input("Enter your choice (1-6): ")

    # tambah kontak
    if choice == "1":
        add_contact(phone_book)

    # update kontak yang sudah ada
    elif choice == "2":
        update_contact(phone_book)

    # menghapus kontak
    elif choice == "3":
        delete_contact(phone_book)

    # mencari kontak
    elif choice == "4":
        search_contact(phone_book)

    # print kontak
    elif choice == "5":
        read_phone_book(phone_book, phone_book_file)

    # quit program
    elif choice == "6":
        quit(phone_book, phone_book_file)

    # invalid choice
    else:
        print("Invalid choice. Please try again.\n")
