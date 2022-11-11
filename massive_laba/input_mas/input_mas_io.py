from input_mas.input_mas_logic import add_elements, generate_border, generate_el


def input_menu(action: int, mas: tuple) -> tuple:
    switcher = {
        1: create_mas_manually,
        2: create_mas_generated,
        3: generate_border,
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


def create_mas_generated(mas: tuple) -> tuple:
    print('How many elements do u want?')
    amount_elements = input()

    while amount_elements.isdigit() is False:
        print('You can write only digits')
        amount_elements = input()

    mas = generate_el(mas, int(amount_elements))

    print(f'Your massive was sucsessfully generated\n mas: {mas}')
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
