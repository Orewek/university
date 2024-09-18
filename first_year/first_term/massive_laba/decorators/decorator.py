# -*- coding: utf-8 -*-
"""All decorators."""
import time as tm


def mas_before_after(func: callable[[Iterable[any]], any]) -> any:
    """
    Massive before operation.
    Operation is happening
    Massive after operation

    Need to find some bugs or just to watch the diff
    """
    def wrapper(*args: any) -> any:
        print(f'\nMassive before operation {args[0]}')
        result = func(*args)
        print(f'\nMassive after operation {args[0]}\n')

        return result
    return wrapper


def str_to_int(func: callable[[Iterable[any]], any]) -> any:
    """Make whole el in mas str -> int."""
    def wrapper(*args: any) -> any:
        str_count: int = 0
        str_el: list = []

        for i in range(len(args[0])):
            if type(args[0][i]) is str:
                args[0][i]: int = int(args[0][i])
                str_count += 1
                str_el.append(args[0][i])

        if str_count > 0:
            print(f"""
                   ===STRING_TO_INT===STRING_TO_INT===STRING_TO_INT
                   {str_count} elements were changed: str -> int
                   This elements were str {str_el}
                   ===STRING_TO_INT===STRING_TO_INT===STRING_TO_INT
                   """)

        result = func(*args)

        return result
    return wrapper


def count_time(func: callable[[Iterable[any]], any]) -> any:
    """Start_time; end_time; after operation (end - start)."""
    def wrapper(*args: any) -> any:
        start_time: float = tm.time()
        result = func(*args)
        end_time: float = tm.time()

        time_result: float = end_time - start_time
        print(f"""
               ==TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME=
               Function had been working for {round(time_result, 3)} seconds
               ===TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME==
               """)

        return result
    return wrapper


def negative_positive(func: callable[[Iterable[any]], any]) -> any:
    """Change negative el to positive."""
    def wrapper(*args: any) -> any:
        neg_count: int = 0
        for el in range(len(args[0])):
            if el < 0:
                el: int = abs(el)
                neg_count += 1

        if neg_count > 0:
            print(f'{neg_count} elements were changed: negative -> positive')

        result = func(*args)

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
