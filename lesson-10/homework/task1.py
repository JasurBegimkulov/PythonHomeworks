class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member has reached the borrowing limit.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print("This book was not borrowed by the member.")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"Book '{title}' by {author} added to the library.")

    def add_member(self, name):
        self.members[name] = Member(name)
        print(f"Member '{name}' added to the library.")

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")
        if member_name not in self.members:
            print("Member not found.")
            return
        self.members[member_name].borrow_book(self.books[book_title])

    def return_book(self, member_name, book_title):
        if member_name not in self.members or book_title not in self.books:
            print("Invalid member or book.")
            return
        self.members[member_name].return_book(self.books[book_title])

if __name__ == "__main__":
    library = Library()
    
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    
    library.add_member("Alice")
    library.add_member("Bob")
    
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
    except Exception as e:
        print(e)
    
    library.return_book("Alice", "1984")
    
    try:
        library.borrow_book("Bob", "1984")
    except Exception as e:
        print(e)
