class Book:
    # Constructor method used to create a new Book object
    def __init__(self, title, author, ISBN, avalibility_status ):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.avalibility_status = True
    
    # Method used when a user borrows a book
    def borrow_book(self):
        if self.avalibility_status == True:
            self.avalibility_status = False
            print(f"{self.title} has been borrowed.")
        else: 
            print(f"{self.title} is not available.")
  
    # Method used when a borrowed book is returned
    def return_book(self): 
        self.avalibility_status = True
        print(f"{self.title} has been returned.")

    def __str__(self):
        # Return a readable string containing the book details
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Available: {self.availability_status}"


class Library:
    # Constructor method used to create a new Library object
    def __init__(self):
        self.books = []
 
    # Method used to add a new book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    # Method used to search for a book using its ISBN
    def find_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None

    # Method used to borrow a book from the library
    def borrow_book(self, ISBN):
        book = self.find_book(ISBN)
        
        if book is not None:
            book.borrow_book()
        else:
            print("Book not found.")
  
    # Method used to return a book to the library
    def return_book(self, ISBN):
        book = self.find_book(ISBN)
        if book is not None:
            book.return_book()
        else:
            print("Book not found.")

    # Method used to display all books currently stored in the library
    def display_books(self):
        for book in self.books:
            print(book)
