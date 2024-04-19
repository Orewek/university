from Unit_tests.some_checks import check_int
from Unit_tests.test_sort_speed import speed_checker_search, speed_checker_sort

from decorators.decor_logic import negative_positive_logic, str2int_before

from kinda_task.search import binary_search, interpolation_search
from kinda_task.search import consistent_search, fibonacci_search
from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic import chered_checker, consecutive_result
from kinda_task.task_logic import max_el, mean_arif, min_el
from kinda_task.task_logic_2 import chered_odd, selection_sort
from kinda_task.task_logic_2 import quick_sort, sum_max2_min1
from kinda_task.task_logic_3 import check_contain_5, prime_number
from kinda_task.task_logic_3 import reverse_number, symmetrical_number


def task_menu(action: int, mas: list) -> list:
    switcher: dict = {
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

        17: laba_3_b8,
        18: laba_3_c5,
    }
    if 11 <= action <= 14:
        mas: list = search_collection(mas, action)
    else:
        mas: list = switcher[action](mas)
    return mas


def task_io(mas: list) -> list:
    """
    User can find min/max so + or * of el, median etc.
    Rn it has the name "task", cant change it
    """

    print('Well, you can find some info about your massive\n'
          'Heres the table what can you do:')

    task_table: str = """
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

                17: min symmetrical / reverse 100-999
                18: sorting odds / removing prime w/o digit 5
                """
    print(task_table)

    action: str = input('What u wanna do? Write one digit')

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) > 2 or action.isdigit() is False:
        if action != '-table':
            print(task_table)
        else:
            print(task_table)
        action = input()

    mas: list = task_menu(int(action), mas)
    return mas


@str2int_before
def task_b8(mas: list) -> list:
    result_mas: list = [chered_checker(mas[i], 2) for i in range(len(mas))]

    """
    Random numbers
    Results, Yes(11) No(00)
    Total amount
    """

    print(mas)
    print(result_mas)
    amount_numbers: int = result_mas.count('1')
    print(f'Amount of non-chered elements: {amount_numbers}')

    return mas


@str2int_before
def task_c8(mas: list) -> list:
    result_mas: list = [chered_checker(mas[i], 10) for i in range(len(mas))]

    print(mas)
    print(result_mas)

    res1, res0 = consecutive_result(result_mas)

    print(f' max 1 = {res1}, max 0 = {res0}')

    return mas


def search_collection(mas: list, search: int) -> list:
    element: str = input('Write which element you want to find in massive')
    check_int(element)

    switcher: dict = {
        11: binary_search,
        12: interpolation_search,
        13: consistent_search,
        14: fibonacci_search,
    }

    result = switcher[search](mas, int(element))
    print(result)

    return mas


@negative_positive_logic
@str2int_before
def laba_3_b8(mas: list) -> list:
    max_num: int = 10 ** 10
    max_num = min([number for number in mas if symmetrical_number(number) is True and max_num > number > 100])

    if max_num == 10 ** 10:
        print('0 symmetrical numbers have found')
    else:
        print(f'{max_num} is the lowest symmetrical number')

    for i in range(len(mas)):
        if len(str(mas[i])) == 3:
            mas[i]: int = reverse_number(mas[i])

    return mas


@negative_positive_logic
@str2int_before
def laba_3_c5(mas: list) -> list:
    # Removing prime numbers which doesnt contain digit 5
    mas: list = [number for number in mas if not(check_contain_5(mas[i]) is False and prime_number(mas[i]) is True)]

    odd_els: list = [number for number in mas if number % 2 != 0]

    odd_els: list = sorted(odd_els)
    print(odd_els)
    for i in range(len(mas)):
        if mas[i] % 2 == 1:
            mas[i]: int = odd_els[0]
            odd_els.pop(0)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
