class Book:

    def __init__(self, title: str):
        self.title = title

    def __del__(self):
        print(f"Book object destroyed: '{self.title}'")


class Library:

    def __init__(self, books: list[Book] = None):
        # Accepts pre-existing Book objects
        self.books = books if books else []

    def __del__(self):
        print("Library object destroyed.")


# Usage
book1 = Book("The Hobbit")
book2 = Book("1984")

my_library = Library([book1, book2])
print(f"Library populated with: {[b.title for b in my_library.books]}")

# Destroying Library container leaves Book objects active in memory
del my_library
print(f"Still active in memory -> book1: {book1.title}")
print(f"Still active in memory -> book2: {book2.title}")