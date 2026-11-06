class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.is_available else 'Checked Out'}"

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False
book1 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
book2 = Book("1984", "George Orwell", "978-0-452-28423-4")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
book1.borrow()
book2.borrow()
book3.return_book()
print(book1)
print(book2)
print(book3)
