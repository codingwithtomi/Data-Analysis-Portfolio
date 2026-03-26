class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author} ({self.pages} pages)")

    def is_long(self):
        return self.pages > 300


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("The Old Man and the Sea", "Ernest Hemingway", 127)

book1.describe()
book2.describe()
book3.describe()

long_books = []

if book1.is_long():
    long_books.append(book1.title)
if book2.is_long():
    long_books.append(book2.title)
if book3.is_long():
    long_books.append(book3.title)

print("Long books: ", ",".join(long_books))
