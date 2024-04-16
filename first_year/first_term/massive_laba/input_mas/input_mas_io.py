from Unit_tests.some_checks import check_int, check_action

from decorators.decorator import count_time

from input_mas.input_mas_logic import add_elements, generate_border, generate_el


def input_menu(action: int, mas: tuple) -> tuple:
    switcher: dict = {
        1: create_mas_manually,
        2: create_mas_generated,
        3: generate_border_io,
    }
    mas: list = switcher[action](mas)
    return mas


def create_mas_io(mas: tuple) -> tuple:
    print('You can input mas manually, by writing each element\n'
          'Or generate n elements randomly (-1000; 1000)')

    input_table: str = """
                1: manually
                2: generate
                3: generate with borders
                """
    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    print(input_table)

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    action = check_action(input(), action_table, input_table)

    mas: list = input_menu(int(action), mas)
    return mas


def create_mas_manually(mas: tuple) -> tuple:
    print('\nWrite each element separated\n'
          'Remember,You can write only digits. '
          'Non-digits elements will be deleted\n'
          'If u wanna to exit, press Enter')
    mas: list = add_elements(mas)

    print(f'Massive was sucsessfully createad. Mas - {mas}')
    return mas


@count_time
def create_mas_generated(mas: tuple) -> tuple:
    amount_elements: int = check_int(input('How many elements do u want?'))

    mas: list = generate_el(mas, int(amount_elements))

    # print(f'Your massive was sucsessfully generated\n mas: {mas}')
    return mas


@count_time
def generate_border_io(mas: list) -> list:
    """
    Input l and r border
    whole els in mas mas will be [lborder, rborder]
    """
    amount_els: int = check_int(input('How many elements do u want?'))
    l_border: int = check_int(input('Write left border'))
    r_border: int = check_int(input('Write right border'))

    if r_border < l_border:
        l_border, r_border = r_border, l_border
    mas: list = generate_border(mas, amount_els, l_border, r_border)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
