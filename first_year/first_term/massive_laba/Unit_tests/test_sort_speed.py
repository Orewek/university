import time

from kinda_task.search import binary_search, interpolation_search
from kinda_task.search import consistent_search, fibonacci_search
from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic_2 import quick_sort, selection_sort


def speed_checker_sort(mas: list) -> list:
    mas_copy: list = mas
    start_time = time.time()
    sorted(mas_copy)
    result = time.time() - start_time
    print(f'PYTHON SORTED TIME {result}\n')

    mas_copy: list = mas
    start_time = time.time()
    quick_sort(mas_copy)
    result = time.time() - start_time
    print(f'\nQUICK SORT TIME {result}\n')

    mas_copy = mas
    selection_sort(mas_copy)

    mas_copy = mas
    bubble_sort(mas_copy)

    return mas


def speed_checker_search(mas: list) -> list:
    number: int = int(input())
    binary_search(mas, number)
    interpolation_search(mas, number)
    consistent_search(mas, number)

    start_time = time.time()
    fibonacci_search(mas, number)
    end_time = time.time()

    start_time = time.time()
    mas.index(number)
    end_time = time.time()
    print(f'PYTHON SEARCH TIME {end_time - start_time}')

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
