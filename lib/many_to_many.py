# lib/many_to_many.py

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []  # Initialize _contracts here
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)  # Append the contract to the _contracts list
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        print(len(cls.all))
        return [contract for contract in Contract.all if contract.date == date]
