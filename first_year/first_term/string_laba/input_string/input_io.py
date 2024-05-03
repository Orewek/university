from Unit_tests.some_checks import check_action, check_int

from input_string.input_logic import input_generate, input_manually


def input_menu(user_str: str, action: int) -> str:
    switcher: dict = {
        1: input_manually,
        2: input_generate_io,
    }
    user_str: str = switcher[action](user_str)

    return user_str


def input_string_io(user_str: str) -> str:
    input_table: str = """
                  1: input string manually
                  2: generate random string
                  """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    action: int = check_action(input(input_table), action_table, input_table)

    user_str: str = input_menu(user_str, action)

    return user_str


def input_generate_io(user_str: str) -> str:
    amount_of_els: str = input('Write how many letter you wanna add')
    check_int(amount_of_els)

    user_str: str = input_generate(user_str, int(amount_of_els))
    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
