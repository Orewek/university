from Unit_tests.some_checks import check_int

from decorators.decorator import count_time

from input_mas.input_mas_logic import add_elements, generate_border, generate_el


def input_menu(action: int, mas: tuple) -> tuple:
    switcher = {
        1: create_mas_manually,
        2: create_mas_generated,
        3: generate_border_io,
    }
    mas = switcher[action](mas)
    return mas


def create_mas_io(mas: tuple) -> tuple:
    print('You can input mas manually, by writing each element\n'
          'Or generate n elements randomly (-1000; 1000)')

    input_table = """
                1: manually
                2: generate
                3: generate with borders
                """
    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    print(input_table)

    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(input_table)
        action = input()

    mas = input_menu(int(action), mas)
    return mas


def create_mas_manually(mas: tuple) -> tuple:
    print('\nWrite each element separated\n'
          'Remember,You can write only digits. '
          'Non-digits elements will be deleted\n'
          'If u wanna to exit, press Enter')
    mas = add_elements(mas)

    print(f'Massive was sucsessfully createad. Mas - {mas}')
    return mas


@count_time
def create_mas_generated(mas: tuple) -> tuple:
    print('How many elements do u want?')
    amount_elements = input()
    amount_elements = check_int(amount_elements)

    mas = generate_el(mas, int(amount_elements))

    # print(f'Your massive was sucsessfully generated\n mas: {mas}')
    return mas


@count_time
def generate_border_io(mas: list) -> list:
    """
    Input l and r border
    whole els in mas mas will be [lborder, rborder]
    """
    print('How many elements do u want?')
    amount_els = input()
    amount_els = check_int(amount_els)

    print('Write left border')
    l_border = input()
    l_border = check_int(l_border)

    print('Write right border')
    r_border = input()
    r_border = check_int(r_border)

    if r_border < l_border:
        l_border, r_border = r_border, l_border
    mas = generate_border(mas, int(amount_els), int(l_border), int(r_border))

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
