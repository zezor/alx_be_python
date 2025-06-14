


from library_management import add_book, search_book_by_title, list_all_books, delete_book_by_id

def main():
    print("Library Management System")
    print("1. Add Book")
    print("2. Search Book by Title")
    print("3. List All Books")
    print("4. Delete Book by ID")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            add_book(title, author, isbn)

        elif choice == "2":
            title = input("Enter title to search: ")
            search_book_by_title(title)

        elif choice == "3":
            list_all_books()

        elif choice == "4":
            book_id = input("Enter Book ID to delete: ")
            if book_id.isdigit():
                delete_book_by_id(int(book_id))
            else:
                print("Invalid ID")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
