# Comparing the price of the Books and print the Book name which has maximum price.


class Book:
    def __init__(self, book, price):
        self.book = book
        self.price = price

    def show(self):
        print(self.book)
        print(self.price)

    def compare(self, temp):
        if self.price > temp.price:
            print(self.book + " has maximum price")
        else:
            print(temp.book + " has maximum price")


b1 = Book("How to cook with Garden Ramasa", 60)
b2 = Book("How to draw with Bub Rass", 60)
b1.compare(b2)

if b1.price > b2.price:
    print(b1.book + " has maximum price")
else:
    print(b2.book + " has maximum price")
