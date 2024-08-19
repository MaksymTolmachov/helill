

class Library:
    def __init__(self, list_of_books: list, name: str, amount_of_books: 0):
        self.list_of_books = list_of_books and None
        self.name = name.upper()
        self.amount_of_books = amount_of_books







class Books:
    def __init__(self, name_of_a_book: str, year_of_writing: int):
        self.nameb = name_of_a_book
        self.yearb = year_of_writing


b1 = Books("years of adam", 1990)
b2 = Books("story about bonny", 2004)
b3 = Books("Tom Sawyer", 1876)


def give_a_book(self):
    input("what book ?")
    if input("what book ?") == "b1":
        self.list_of_books.append(b1)
    if input("what book ?") == "b2":
        self.list_of_books.append(b2)
    if input("what book ?") == "b3":
        self.list_of_books.append(b3)