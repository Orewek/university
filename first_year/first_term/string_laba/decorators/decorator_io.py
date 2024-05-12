import time
from typing import Any, Callable, Iterable


def count_time(func: Callable[[Iterable[Any]], Any]):
    """
    start_time; end_time; after operation (end - start)
    """
    def wrapper(*args: Any):
        start_time: float = time.time()
        result = func(*args)
        end_time: float = time.time()

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
