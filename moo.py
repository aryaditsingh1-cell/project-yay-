# ── BOOK CLASS ───────────────────────────────────────────────── called Book
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"
# ── LIBRARY ────────────────────────────────────────────────────
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print("=" * 42)
print("         📚 LIBRARY SYSTEM")
print("=" * 42)
print(book1)
print(book2)
print(book3)
book1.borrow()
book1.borrow()  # Attempt to borrow the same book again
book2.borrow()
book1.return_book()
book1.return_book()
book3.return_book()  # Attempt to return the same book again