# -*- coding: utf-8 -*-
"""
SAME DECORATORS AS IN decorator.py .
THESE WERE MADE KINDA LOGIC, W/O ANY PRINTS
HERES ONLY DECORATORS THAT HAS ANY SENSE W/O PRINTS
"""


def str2int_before(func: callable[[Iterable[any]], any]) -> any:
    """Make whole el in mas str -> int."""
    def wrapper(*args: any) -> any:
        [int(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


def str2int_after(func: callable[[Iterable[any]], any]) -> any:
    """Make the same, but after the function."""
    def wrapper(*args: any) -> any:
        result = func(args[0], *args[1:])
        [int(number) for number in args[0]]

        return result
    return wrapper


def int2str_before(func: callable[[Iterable[any]], any]) -> any:
    """Make whole el in mas: int -> str."""
    def wrapper(*args: any) -> any:
        [str(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


def negative_positive_logic(func: callable[[Iterable[any]], any]) -> any:
    """Change negative el to positive."""
    def wrapper(*args: any) -> any:
        [abs(number) for number in args[0]]
        result = func(args[0], *args[1:])

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
