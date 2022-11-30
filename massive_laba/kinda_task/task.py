from Unit_tests.some_checks import check_int
from Unit_tests.test_sort_speed import speed_checker_search, speed_checker_sort

from decorators.decor_logic import str2int_before

from kinda_task.search import binary_search, interpolation_search
from kinda_task.search import consistent_search, fibonacci_search
from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic import chered_checker, consecutive_result
from kinda_task.task_logic import max_el, mean_arif, min_el
from kinda_task.task_logic_2 import chered_odd, selection_sort
from kinda_task.task_logic_2 import quick_sort, sum_max2_min1


def task_menu(action: int, mas: list) -> list:
    switcher = {
        1: mean_arif,
        2: min_el,
        3: max_el,
        4: task_b8,
        5: task_c8,
        6: bubble_sort,

        7: selection_sort,
        8: sum_max2_min1,
        9: chered_odd,
        10: quick_sort,

        11: binary_search,
        12: interpolation_search,
        13: consistent_search,
        14: fibonacci_search,

        15: speed_checker_sort,
        16: speed_checker_search,
    }
    if 11 <= action <= 14:
        mas = search_collection(mas, action)
    else:
        mas = switcher[action](mas)
    return mas


def task_io(mas: list) -> list:
    """
    User can find min/max so + or * of el, median etc.
    Rn it has the name "task", cant change it
    """

    print('Well, you can find some info about your massive\n'
          'Heres the table what can you do:')

    task_table = """
                1: mean arifmetical
                2: minimal element
                3: maxmimun element
                4: even / odd pairs
                5: same digit pairs
                6: bubble sort

                7: selection sort
                8: max_even + min_odd
                9: odd pairs (second way)
                10: quick sort

                11: binary search
                12: interpolation search
                13: consistent search
                14: fibonacci search

                15: Check sort speed
                16: Check search el in massive speed
                """
    print(task_table)

    print('What u wanna do? Write one digit')
    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) > 2 or action.isdigit() is False:
        if action != '-table':
            print(task_table)
        else:
            print(task_table)
        action = input()

    mas = task_menu(int(action), mas)
    return mas


@str2int_before
def task_b8(mas: list) -> list:
    result_mas = []

    for i in range(len(mas)):
        result = chered_checker(mas[i], 2)
        result_mas.append(result)

    """
    Random numbers
    Results, Yes(11) No(00)
    Total amount
    """

    print(mas)
    print(result_mas)
    amount_numbers = result_mas.count('1')
    print(f'Amount of non-chered elements: {amount_numbers}')

    return mas


@str2int_before
def task_c8(mas: list) -> list:
    result_mas = []

    for i in range(len(mas)):
        result = chered_checker(mas[i], 10)
        result_mas.append(result)

    print(mas)
    print(result_mas)

    res1, res0 = consecutive_result(result_mas)

    print(f' max 1 = {res1}, max 0 = {res0}')

    return mas


def search_collection(mas: list, search: int) -> list:
    print('Write which element you want to find in massive')
    element = input()
    check_int(element)

    switcher = {
        11: binary_search,
        12: interpolation_search,
        13: consistent_search,
        14: fibonacci_search,
    }

    result = switcher[search](mas, int(element))
    print(result)

    return mas

if __name__ == '__main__':
    print('You cant run this file as main')
