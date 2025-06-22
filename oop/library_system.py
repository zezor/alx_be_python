# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return self.get_details()


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __str__(self):
        return self.get_details()


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __str__(self):
        return self.get_details()


# Composition - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        for book in self.books:
            print(book)  # Uses __str__ method
