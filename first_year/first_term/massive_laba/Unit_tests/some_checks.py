from typing import Any


def check_int(int_variable: Any) -> int:
    while int_variable.isdigit() is False:
        print('You can write only digits')
        int_variable: str = input()

    return int_variable


if __name__ == '__main__':
    print('You cant run this file as main')
