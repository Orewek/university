from Unit_tests.some_checks import check_int

from input_string.input_logic import input_generate, input_manually


def input_menu(user_str: str, action: int) -> str:
    switcher = {
        1: input_manually,
        2: input_generate_io,
    }
    user_str = switcher[action](user_str)

    return user_str


def input_string_io(user_str: str) -> str:
    input_table = """
                  1: input string manually
                  2: generate random string
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

    user_str = input_menu(user_str, int(action))

    return user_str


def input_generate_io(user_str: str) -> str:
    print('Write how many letter you wanna add')
    amount_of_els = input()
    check_int(amount_of_els)

    user_str = input_generate(user_str, int(amount_of_els))
    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
