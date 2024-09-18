# -*- coding: utf-8 -*-
"""Some variable checks."""

def check_int(variable: int | str) -> int:
    """Check does variable contains only digits, reinput till true.

    Args:
    ----
        variable: Our variable

    Return: Our variable
    ------
    """
    while variable.isdigit() is False:
        variable: str = input('You can write only digits')

    return variable


def check_action(action: int | str, action_table: str, table: str) -> int:
    """Check check_action.

    Args:
    ----
        action: User input
        action_table: table with error
        table: table with func
    
    Return: action with type int
    ------
    """
    while len(action) != 1 or action.isdigit() is False:
        print(action_table if action != '-table' else table)
        action: str = input()

    return int(action)


if __name__ == '__main__':
    print('You cant run this file as main')
