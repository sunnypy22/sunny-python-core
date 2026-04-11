
# __str__, __repr__, and __len__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
   
    # Called by print() and str()
    def __str__(self):
        return f"'{self.title}' by {self.author}"
   
    # Official representation (used in debugging and repr())
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
   
    # Called by len()
    def __len__(self):
        return self.pages
# Usage
book = Book("Python Programming", "Sunny", 450)
print(book)                    # Uses __str__
print(str(book))
print(repr(book))              # Uses __repr__
print(f"Number of pages: {len(book)}")   # Uses __len__
