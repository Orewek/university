from typing import Any


def check_int(int_variable: Any) -> int:
    while int_variable.isdigit() is False:
        int_variable: str = input('You can write only digits')

    return int_variable


def check_action(action: Any, action_table: str, table: str) -> int:
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action: str = input()

    return int(action)


if __name__ == '__main__':
    print('You cant run this file as main')
