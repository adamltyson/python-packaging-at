from typing import Union


def add_numbers(a: int | float, b: Union[int, float]) -> Union[int, float]:
    return a + b


def subtract_numbers(a, b):
    return a - b
