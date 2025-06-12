class Book:
    """Represents a book with a title and author, and tracks if it is checked out."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that can add, check out, return, and list books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Lists all books that are available (not checked out)."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

