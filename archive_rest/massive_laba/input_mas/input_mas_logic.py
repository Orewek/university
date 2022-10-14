from random import randint


def add_elements(mas: tuple) -> tuple:
    """
    input: massive with n elements
    adding each elements into it
    if user pressed Enter -> break
    """
    el_mas = input()
    while el_mas != '':
        if el_mas.isdigit() is True:
            mas.append(el_mas)
        el_mas = input()

    return mas


def generate_el(mas: tuple, amount_elements: int) -> tuple:
    """
    input: massive with n elements
    generating (-1000; 1000) number
    appending this number to mas
    """
    for _ in range(amount_elements):
        number = randint(-1000, 1000)
        mas.append(number)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
