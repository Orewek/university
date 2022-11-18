import time

from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic_2 import quick_sort, selection_sort


def speed_checker(mas: list) -> list:
    mas_copy = mas
    start_time = time.time()
    quick_sort(mas_copy)
    result = time.time() - start_time
    print(f'\nQUICK SORT TIME {result}\n')

    mas_copy = mas
    selection_sort(mas_copy)

    mas_copy = mas
    bubble_sort(mas_copy)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
