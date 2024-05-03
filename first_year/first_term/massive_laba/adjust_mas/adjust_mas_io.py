from Unit_tests.some_checks import check_action, check_int

from adjust_mas.adjust_mas_logic import change_elements, show_elements
from adjust_mas.adjust_mas_logic import clear_mas, len_mas


def mas_elements(mas: list) -> list:
    """
    read show_elemetns .__doc__
    read change_elements .__doc__
    """
    show_elements(mas)

    print("""
          Now You can write digits next to elements that we need to change
          Write them separated, after each digit press Enter
          It will be able to write more digits. When You done: press Enter
          """)

    # change_number = number of element, that we need to change
    # adding each number of these elements into change_mas
    # so, if we wanna change 2nd and 3rd element: [2, 3]
    change_mas: list = []
    change_number: str = input()

    while change_number != '':

        # checking for letters
        change_number: int = check_int(change_number)

        # Number of element cant be > than number of elemtns
        # ['a' 'b' 'c'] - 3, so user cant write smth > 3
        while int(change_number) > len(mas):
            change_number: str = input('Elements with this number doesnt exist')

        change_mas.append(int(change_number))
        change_number: str = input()

    # System count elements from 0 to n - 1
    # Ppl do that from 1 to n
    change_mas = list(map(lambda item: item - 1, change_mas))

    change_elements(mas, change_mas)

    return mas


def adjust_massive(mas: list) -> list:
    adjust_table: str = """
            1: massive length
            2: change elements
            3: clear massive
            """

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    # checking for letters and multi-digits
    action = check_action(input(adjust_table), action_table, adjust_table)

    switcher: dict = {
        1: len_mas,
        2: mas_elements,
        3: clear_mas,
    }
    # when we writing len of mas (1 action), we dont change anything
    if int(action) != 1:
        mas: list = switcher[int(action)](mas)
    else:
        mas_len: str = switcher[int(action)](mas)
        print(mas_len)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
