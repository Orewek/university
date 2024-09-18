# -*- coding: utf-8 -*-
"""Count how long func was working."""


import time as tm

def count_time(func: callable[[iterable[any]], any]) -> any:
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


if __name__ == '__main__':
    print('You cant run this file as main')
