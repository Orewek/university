import itertools
from random import randint


def input_manually(user_str: str) -> str:
    add_letters: str = input()
    user_str += add_letters

    return user_str


def input_generate(user_str: str, amount_of_els: int) -> str:
    # itertools.chain(range(65, 91), range(97, 123))
    add_letters: str = ''
    for _ in range(amount_of_els):
        new_letter_code: int = randint(65, 122 + 1)

        while 92 <= new_letter_code <= 96:
            new_letter_code: int = randint(65, 122 + 1)

        add_letters += chr(new_letter_code)
    user_str += add_letters
    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
