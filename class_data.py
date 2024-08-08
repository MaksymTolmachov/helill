MIN_CAPITAL = 50_000_000


class Bank:
    def __init__(self, name: str, stakeholders: list[str], capital: int):
        if capital < MIN_CAPITAL:
            raise ValueError("Too low capital amount")
        self.name = name
        self.stakeholders = stakeholders
        self.capital = capital



