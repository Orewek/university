# -*- coding: utf-8 -*-

"""Input massive menu."""
from Unit_tests.some_checks import check_action, check_int

from decorators.decorator import count_time

from input_mas.input_mas_logic import add_elements, generate_border, generate_el


def input_menu(action: int, mas: list) -> list:
    """Menu for input.

    Args:
    ----
        action: which line from the dict we should take 
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    switcher: dict[int, callable] = {
        1: create_mas_manually,
        2: create_mas_generated,
        3: generate_border_io,
    }
    mas: list = switcher[action](mas)
    return mas


def create_mas_io(mas: list) -> list:
    """Create massive menu.

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    print('You can input mas manually, by writing each element\n'
          'Or generate n elements randomly (-1000; 1000)')

    input_table: str = """
                1: manually
                2: generate
                3: generate with borders
                """
    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    action = check_action(input(input_table), action_table, input_table)

    mas: list = input_menu(int(action), mas)
    return mas


def create_mas_manually(mas: list) -> list:
    """Create massive by typing each element manually.
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    print("""
          Write each element separated
          Remember,You can write only digits.
          Non-digits elements will be deleted
          If u wanna to exit, press Enter
          """)
    mas: list = add_elements(mas)

    print(f'Massive was sucsessfully createad. Mas - {mas}')
    return mas


@count_time
def create_mas_generated(mas: list) -> list:
    """Create massive by generating elements.
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    amount_elements: int = check_int(input('How many elements do u want?'))

    mas: list = generate_el(mas, int(amount_elements))

    return mas


@count_time
def generate_border_io(mas: list) -> list:
    """
    Input l and r border.
    whole els in mas mas will be [lborder, rborder]

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    amount_els: int = check_int(input('How many elements do u want?'))
    l_border: int = check_int(input('Write left border'))
    r_border: int = check_int(input('Write right border'))

    l_border, r_border = min(r_border, l_border), max(r_border, l_border)
    mas: list = generate_border(mas,
                                int(amount_els),
                                int(l_border),
                                int(r_border))

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
