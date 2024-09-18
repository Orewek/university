# -*- coding: utf-8 -*-
"""Main file that starts up the program."""


from Unit_tests.some_checks import check_action

from adjust_mas.adjust_mas_io import adjust_massive

from input_mas.input_mas_io import create_mas_io

from kinda_task.task import task_io

from output.output_mas import show_mas


def menu(action: int, mas: list) -> list:
    """Menu with other menus.

    Args:
    ----
        action: User input
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    switcher: dict = {
        1: create_mas_io,
        2: adjust_massive,
        3: show_mas,
        4: task_io,
    }
    if action != 5:
        mas: list = switcher[action](mas)

    return mas


def main(mas: list) -> list:
    """Menu or user input.

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    table: str = """
            1: input massive
            2: adjust massive
            3: output massive
            4: tasks
            5: exit
            """
    action_table: str = """
                   U can write only one digit, 1 to 5
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    print(table)

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    action: int = check_action(input('What u wanna do? Write one digit'),
                               action_table, table)

    mas: list = menu(action, mas)
    if action == 5:
        mas.append('exit')

    return mas


if __name__ == '__main__':
    mas: list = main(mas=[])

    # If user wanna continue, he can write 1/yes/y
    approved: list = ['y', 'yes', '1']

    additional_check: str = input(f'One more?\n {approved}')

    while additional_check.lower() in approved and 'exit' not in mas:
        mas: list = main(mas)

    mas: list = mas[:-1]
    print(mas)
