from input_string.input_io import input_string_io

from output_string.output_logic import output_user_str

from search_string.search_io import input_find_ed

from task.tasks import task_b9

from Unit_tests.some_checks import check_action


def main_menu(user_str: str, action: int) -> str:
    switcher = {
        1: input_string_io,
        2: output_user_str,
        3: input_find_ed,

        4: task_b9,
    }
    user_str = switcher[action](user_str)

    return user_str


def main(user_str: str) -> str:
    table = """
            1: input string
            2: output string
            3: search string

            4: task b9
            """

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    print(table)

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    action: int = check_action(input(), action_table, table)

    user_str = main_menu(user_str, action)

    return user_str


if __name__ == '__main__':
    user_str = ''
    while True:
        user_str = main(user_str)
