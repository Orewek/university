# -*- coding: utf-8 -*-


def check_int(int_variable: int | str) -> int:
    while int_variable.isdigit() is False:
        int_variable: str = input('You can write only digits')

    return int_variable


def check_action(action: int | str, action_table: str, table: str) -> int:
    while len(action) != 1 or action.isdigit() is False:
        print(action_table if action != '-table' else table)
        action: str = input()

    return int(action)


if __name__ == '__main__':
    print('You cant run this file as main')
