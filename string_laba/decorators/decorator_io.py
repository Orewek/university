import time
from typing import Any, Callable, Iterable

from progress.bar import Bar


def count_time(func: Callable[[Iterable[Any]], Any]):
    """
    start_time; end_time; after operation (end - start)
    """
    def wrapper(*args: Any):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()

        time_result = end_time - start_time
        print(f'\n==TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME=\n'
              f'Function had been working for {round(time_result, 3)} seconds\n'
              f'===TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME==')

        return result
    return wrapper


if __name__ == '__main__':
    print('You cant run this file as main')
