from decorators.decor_logic import str2int_before

from kinda_task.task_logic import bubble_sort
from kinda_task.task_logic import chered_checker, consecutive_result
from kinda_task.task_logic import max_el, mean_arif, min_el
from kinda_task.task_logic_2 import chered_odd, selection_sort, sum_max2_min1


def task_menu(action: int, mas: tuple) -> tuple:
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
    }
    mas = switcher[action](mas)
    return mas


def task_io(mas: tuple) -> tuple:
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
                 """
    print(task_table)

    print('What u wanna do? Write one digit')
    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(task_table)
        else:
            print(task_table)
        action = input()

    mas = task_menu(int(action), mas)
    return mas


@str2int_before
def task_b8(mas: tuple) -> tuple:
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
def task_c8(mas: tuple) -> tuple:
    result_mas = []

    for i in range(len(mas)):
        result = chered_checker(mas[i], 10)
        result_mas.append(result)

    print(mas)
    print(result_mas)

    res1, res0 = consecutive_result(result_mas)

    print(f' max 1 = {res1}, max 0 = {res0}')

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')