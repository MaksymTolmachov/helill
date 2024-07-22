from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint
from typing import Self
from enum import Enum, unique, auto


@unique
class General(Enum):
    HEALTH = 100


@dataclass(frozen=True)
class Params:
    DWARFS_POWER = 45
    DWARFS_ACCURACY = 29
    ELVES_POWER = 24
    ELVES_ACCURACY = 54


class Character(ABC):

    def __init__(self, name: str, power, accuracy: int):
        self.name = name
        self.health = General.HEALTH.value
        self.power = power
        self.accuracy = accuracy

    @property
    def is_alive(self):
        return self.health > 0

    # def attack(self, other: Self):
    def attack(self, other: "Character") -> bool:
        if not self.is_alive:
            return False

        our_try = randint(1, 101)
        if our_try <= self.accuracy:
            print(f"{other.name} was hit by {self.name}")
            other.health -= self.power
            if not other.is_alive:
                print(f"I was already killed (I'm {other.name})")
                return True
            else:
                return False


    def __str__(self):
        return f"My name is {self.name}"


class Dwarfs(Character):
    def __init__(self, name: str, power, accuracy: int):
        power = Params.DWARFS_POWER
        accuracy = Params.DWARFS_ACCURACY
        super().__init__(name, power, accuracy)

    def __str__(self):
        return f"My name is {self.name} I'm a Dwarf"


class Elves(Character):
    def __init__(self, name: str, power, accuracy: int):
        power = Params.ELVES_POWER
        accuracy = Params.ELVES_ACCURACY
        super().__init__(name, power, accuracy)

    def __str__(self):
        return f"My name is {self.name} I'm an Elv "


d = Dwarfs("Dwarf")
d2 = Dwarfs("Dwarf2")
el = Elves("Elv")
el2 = Elves("Elv2")

print(type(d))
print(isinstance(d, Dwarfs))
print(isinstance(d, Character))
