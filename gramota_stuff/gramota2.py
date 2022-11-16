from typing import Any


def find_exp_stepen(number: str) -> int:
    exp_stepen = len(number.replace('-', '').split('.')[0]) - 1
    return exp_stepen


def main(number: str) -> Any:
    return find_exp_stepen(number)


if __name__ == '__main__':
    print('Input number')
    number = input()

    res = main(number)
    print(res)
