from typing import Callable


def add_two_number(n_1: int, n_2: int)-> int:
    result = n_1 + n_2
    n_1 = 5
    n_2 = 5
    return result


def decorator(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("homework_decorator.csv", mode="a", encoding="utf-8") as file:
            file.write(f"{func.__name__};{result}")

        return result
    wrapper.__name__ = func.__name__
    return wrapper