from __future__ import annotations


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author


class Library:
    def __init__(self):
        self.__books = {}

    def add_book(self, book: Book):
        self.__books[book.get_title()] = book.get_author()

    def list_books(self):
        print(f"{self.__books}")


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.list_books()
