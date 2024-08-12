MIN_CAPITAL = 50_000_000
from conftest import bank
import faker
class Bank:
    accounts = []




    def __init__(self, name: str, stakeholders: list[str], capital: int):
        if capital < MIN_CAPITAL:
            raise ValueError("Too low capital amount")
        self.name = f"VAT {name.upper()}"
        self.stakeholders = stakeholders
        self.capital = capital

    def add_stakeholders(self, stakeholder, capital):
        self.stakeholders.append(stakeholder)
        self.capital += capital


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address



class Account:
    def __init__(self,Bank: str,):
        self.bank = Bank
        self.balance = 0
        self.account_number = faker.iban()




