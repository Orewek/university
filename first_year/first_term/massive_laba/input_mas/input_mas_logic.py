from random import randint

from decorators.decor_logic import str2int_after


@str2int_after
def add_elements(mas: list) -> list:
    """
    input: massive with n elements
    adding each elements into it
    if user pressed Enter -> break
    """
    el_mas: str = input()
    while el_mas != '':
        if el_mas.isdigit() is True:
            mas.append(el_mas)
        el_mas: str = input()

    return mas


def generate_el(mas: list, amount_elements: int) -> list:
    """
    input: massive with n elements
    generating (-1000; 1000) number
    appending this number to mas
    """
    mas = [randint(-1000, 1000) for _ in range(amount_elements)]

    return mas


@str2int_after
def generate_border(mas: list,
                    amount_els: int,
                    l_border: int,
                    r_border: int) -> list:

    mas = [randint(l_border, r_border) for _ in range(amount_els)]

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
