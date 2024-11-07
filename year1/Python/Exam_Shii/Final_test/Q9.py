#  Class Implementation: Library System
# Define a class `LibraryBook` that represents a book in a library. Each book has the following
# properties:
# - `title`: Title of the book
# - `author`: Author of the book
# - `available`: Boolean indicating if the book is available
# Include the following methods:
# - `borrow()`: Marks the book as not available
# - `return_book()`: Marks the book as available
# Then, define a subclass `ReferenceBook` that extends `LibraryBook`. A reference book can never
# be borrowed. Modify the `borrow()` method to print 'This book cannot be borrowed.

class LibaryBook:
    def __init__(self, title, author, available:bool =True):
        self.title = title
        self.author = author
        self.ava = available
        
    def borrow(self):
        if self.ava == False:
            print("This book alr borrowed")
        else :
            self.ava = False
        
    def return_book(self):
        if self.ava == True:
            print("This book still here lil bro")
        else:
            self.ava = True
        
class RefBook(LibaryBook):
    def __init__(self, title, author):
        super().__init__(title, author, available=True)
        
    def borrow(self):
        print("This book cannot be borrowed")
        
book = LibaryBook('Halal Madrid', 'Carlo')
ref = RefBook('Real', 'Vini')

ref.borrow()

        