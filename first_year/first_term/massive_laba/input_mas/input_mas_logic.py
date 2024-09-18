# -*- coding: utf-8 -*-
"""Functions whichs put numbers into massive."""
from random import randint

from decorators.decor_logic import str2int_after


@str2int_after
def add_elements(mas: list) -> list:
    """
    Input: massive with n elements.
    adding each elements into it
    if user pressed Enter -> break
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    el_mas: str = input()
    while el_mas != '':
        if el_mas.isdigit() is True:
            mas.append(el_mas)

        el_mas: str = input()

    return mas


def generate_el(mas: list, amount_elements: int) -> list:
    """
    Input: massive with n elements.
    generating (-1000; 1000) number
    appending this number to mas
    
    Args:
    ----
        mas: massive with numbers
        amount_elements: how many elements going to be in massive
    
    Return:
    ------
        mas: massive with numbers
    """
    mas = [randint(-1000, 1000) for _ in range(amount_elements)]

    return mas


@str2int_after
def generate_border(
        mas: list,
        amount_els: int,
        l_border: int,
        r_border: int) -> list:
    """Generate massive automatically with borders.
    
    Args:
    ----
        mas: massive with numbers
        amount_els: how many elements going to be in massive
        l_border: left border
        r_border: right border
    
    Return:
    ------
        mas: massive with numbers
    """
    mas = [randint(l_border, r_border) for _ in range(amount_els)]

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
