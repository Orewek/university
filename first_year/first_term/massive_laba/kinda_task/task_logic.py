# -*- coding: utf-8 -*-
"""Func for tasks."""
from functools import reduce


from decorators.decor_logic import int2str_before, str2int_before
from decorators.decorator import count_time



@str2int_before
def mean_arif(mas: list) -> list:
    """
    Calculate arif sum of whole mas el.
    Firstly count total sum and divide on amount of elements
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    el_sum = reduce(lambda x, y: x + y, mas)

    arif_sum: float = el_sum / len(mas)
    print(f'Arifmetical sum = {arif_sum}')

    return mas


@str2int_before
def min_el(mas: list) -> list:
    """Output the min el of mas.

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    print(f'minimal element of massvie = {min(mas)}')
    return mas


@str2int_before
def max_el(mas: list) -> list:
    """Output the max el of mas.
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with number
    """
    print(f'maxmimum element of massvie = {max(mas)}')
    return mas


def chered_checker(number: int, divide: int) -> str:
    """
    TASK B8.
        if n'th and (n-1)'th element give the same remainder % 2 -> return 0
        else -> return 1

        kinda yes/no

    TASK C8
        if n'th element == (n - 1)'th -> return 0
        else -> return 1
    
    Args:
    ----
        number: number
        divide: divider
    
    Return:
    ------
        mas: massive with number
    """
    while (number // 10) > 0:
        if number % divide == (number // 10) % divide:
            return '0'

        number //= 10

    return '1'


@int2str_before
def consecutive_result(result_mas: list) -> tuple:
    """Count 1 in a row and 0 in a row.

    Args:
    ----
        result_mas: mas with 1 and 0
    
    Return: max len of row with only 1 and 0
    ------
    """
    res1: str = '1'
    res0: str = '0'

    string = ''.join(result_mas)
    while res1 in string:
        res1 += '1'

    while res0 in string:
        res0 += '0'

    res1 = res1[:-1]
    res0 = res0[:-1]

    return len(res1), len(res0)


@count_time
# @str2int_before
def bubble_sort(mas: list) -> list:
    """Bubble sort.

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with number
    """
    for _ in range(len(mas)):
        for i in range(len(mas) - 1):
            mas[i], mas[i + 1] = min(mas[i + 1], mas[i]), max(mas[i + 1], mas[i])

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
