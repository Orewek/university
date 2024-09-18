# -*- coding: utf-8 -*-
"""Find out time spent on sort."""

import time as tm

from kinda_task.search import (binary_search,
                               consistent_search,
                               fibonacci_search,
                               interpolation_search)
from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic_2 import quick_sort, selection_sort


def speed_checker_sort(mas: list) -> list:
    """Test sort.

    Args:
    ----
        mas: massive with numbers

    Return:
    ------
        mas: massive with numbers
    """
    mas_copy: list = mas
    start_time: float = tm.time()
    sorted(mas_copy)
    result: float = tm.time() - start_time
    print(f'PYTHON SORTED TIME {result}\n')

    mas_copy: list = mas
    start_time: float = tm.time()
    quick_sort(mas_copy)
    result = tm.time() - start_time
    print(f'\nQUICK SORT TIME {result}\n')

    mas_copy: list = mas
    selection_sort(mas_copy)

    mas_copy: list = mas
    bubble_sort(mas_copy)

    return mas


def speed_checker_search(mas: list) -> list:
    """Test search.

    Args:
    ----
        mas: massive with numbers

    Return:
    ------
        mas: massive with numbers
    """
    number: int = int(input())
    binary_search(mas, number)
    interpolation_search(mas, number)
    consistent_search(mas, number)

    start_time: float = tm.time()
    fibonacci_search(mas, number)
    end_time: float = tm.time()

    start_time: float = tm.time()
    mas.index(number)
    end_time: float = tm.time()
    print(f'PYTHON SEARCH TIME {end_time - start_time}')

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
