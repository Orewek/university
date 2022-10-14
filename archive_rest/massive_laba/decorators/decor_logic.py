"""
SAME DECORATORS AS IN decorator.py
THESE WERE MADE KINDA LOGIC, W/O ANY PRINTS
HERES ONLY DECORATORS THAT HAS ANY SENSE W/O PRINTS
"""


def str_to_int_logic(func):
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


def negative_positive_logic(func):
    """
    changing negative el to positive
    """
    def wrapper(*args):
        for x in range(len(args[0])):
            if x < 0:
                x = abs(x)

        result = func(args[0], *args[1:])

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
