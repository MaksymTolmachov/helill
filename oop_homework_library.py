from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        return f"{self.title} was wrote by {self.author_or_director} in {self.year}."


class Book(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, number_of_pages: int):
        self.number_of_pages = number_of_pages
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"{self.title} was wrote by {self.author_or_director} in {self.year}."


class Magazine(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, issue_number: int):
        self.issue_number = issue_number
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"{self.title} was wrote by {self.author_or_director} in {self.year}."


class Dvd(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, duration: int):
        self.duration = duration
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"{self.title} was wrote by {self.author_or_director} in {self.year} and last for {self.duration}."















