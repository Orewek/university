"""
SAME DECORATORS AS IN decorator.py
THESE WERE MADE KINDA LOGIC, W/O ANY PRINTS
HERES ONLY DECORATORS THAT HAS ANY SENSE W/O PRINTS
"""


def str2int_before(func):
    """
    Making whole el in mas str -> int
    """
    def wrapper(*args):
        for i in range(len(args[0])):
            if type(args[0][i]) is str:
                args[0][i] = int(args[0][i])

        result = func(args[0], *args[1:])

        return result
    return wrapper


def str2int_after(func):
    """
    Making the same, but after the function
    """
    def wrapper(*args):
        result = func(args[0], *args[1:])
        for i in range(len(args[0])):
            if type(args[0][i]) is str:
                args[0][i] = int(args[0][i])

        return result
    return wrapper


def int2str_before(func):
    """
    Making whole el in mas: int -> str
    """
    def wrapper(*args):
        for i in range(len(args[0])):
            if type(args[0][i]) is int:
                args[0][i] = str(args[0][i])

        result = func(args[0], *args[1:])

        return result
    return wrapper


def negative_positive_logic(func):
    """
    changing negative el to positive
    """
    def wrapper(*args):
        for el in range(len(args[0])):
            if el < 0:
                el = abs(el)

        result = func(args[0], *args[1:])

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
