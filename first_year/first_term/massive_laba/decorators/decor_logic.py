from typing import Any, Callable, Iterable

"""
SAME DECORATORS AS IN decorator.py
THESE WERE MADE KINDA LOGIC, W/O ANY PRINTS
HERES ONLY DECORATORS THAT HAS ANY SENSE W/O PRINTS
"""


def str2int_before(func: Callable[[Iterable[Any]], Any]):
    """
    Making whole el in mas str -> int
    """
    def wrapper(*args: Any):
        [int(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


def str2int_after(func: Callable[[Iterable[Any]], Any]):
    """
    Making the same, but after the function
    """
    def wrapper(*args: Any):
        result = func(args[0], *args[1:])
        [int(number) for number in args[0]]

        return result
    return wrapper


def int2str_before(func: Callable[[Iterable[Any]], Any]):
    """
    Making whole el in mas: int -> str
    """
    def wrapper(*args: Any):
        [str(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


def negative_positive_logic(func: Callable[[Iterable[Any]], Any]):
    """
    changing negative el to positive
    """
    def wrapper(*args: Any):
        [abs(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
