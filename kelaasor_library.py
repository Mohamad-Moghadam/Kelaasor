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

    def add_book(book: Book):
        books = {}
        books[book.get_title()] = book.get_author()


Library.add_book(Book("1984", "George Orwell"))
Library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
