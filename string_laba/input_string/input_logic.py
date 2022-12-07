import itertools
from random import randint


def input_manually(user_str: str) -> str:
    add_letters = str(input())
    user_str += add_letters

    return user_str


def input_generate(user_str: str, amount_of_els: int) -> str:
    # itertools.chain(range(65, 91), range(97, 123))
    add_letters = ''
    for _ in range(amount_of_els):
        new_letter_code = randint(65, 122 + 1)

        while 92 <= new_letter_code <= 96:
            new_letter_code = randint(65, 122 + 1)

        add_letters += chr(new_letter_code)
    print('1', add_letters)
    user_str += add_letters
    print('2', user_str)
    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
