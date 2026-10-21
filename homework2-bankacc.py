
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                print("ეს წიგნი უკვე დამატებულია!")
                return

        self.books.append(book)
        print("წიგნი წარმატებით დაემატა!")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("წიგნი წაიშალა!")
                return

        print("წიგნი ვერ მოიძებნა!")

    def list_books(self):
        if len(self.books) == 0:
            print("ბიბლიოთეკა ცარიელია!")
        else:
            for book in self.books:
                print(book.title, "-", book.author, "-", book.year)


library = Library()

book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1712)
book2 = Book("განდეგილი", "ილია ჭავჭავაძე", 1883)
book3 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1712)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print()

library.list_books()

print()

library.remove_book("განდეგილი")

print()

library.list_books()
