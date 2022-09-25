from adjust_mas.adjust_mas_logic import clear_mas, len_mas
from adjust_mas.adjust_mas_logic import show_elements, change_elements


def mas_elements(mas: tuple) -> tuple:
    """
    read show_elemetns .__doc__
    read change_elements .__doc__
    """
    show_elements(mas)

    print('\nNow You can write digits next to elements that we need to change\n'
          'Write them separated, after each digit press Enter\n'
          'It will be able to write more digits. When You done: press Enter\n')

    # change_number = number of element, that we need to change
    # adding each number of these elements into change_mas
    # so, if we wanna change 2nd and 3rd element: [2, 3]
    change_mas = []
    change_number = input()

    while change_number != '':

        # checking for letters
        while change_number.isdigit() is False:
            print('You can write only digits. Try again')
            change_number = input()
        change_number = int(change_number)

        # Number of element cant be > than number of elemtns
        # ['a' 'b' 'c'] - 3, so user cant write smth > 3
        while int(change_number) > len(mas):
            print('Elements with this number doesnt exist. Try again')
            change_number = input()

        change_mas.append(change_number)
        change_number = input()

    # System count elements from 0 to n - 1
    # Ppl do that from 1 to n
    for i in range(len(change_mas)):
        change_mas[i] -= 1

    change_elements(mas, change_mas)

    return mas


def adjust_massive(mas: tuple) -> tuple:
    adjust_table = """
            1: massive length
            2: change elements
            3: clear massive
            """
    print(adjust_table)
    action = input()

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    # checking for letters and multi-digits
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(adjust_table)
        action = input()
    action = int(action)

    switcher = {
        1: len_mas,
        2: mas_elements,
        3: clear_mas
    }
    # when we writing len of mas (1 action), we dont change anything
    if action != 1:
        mas = switcher[action](mas)
    else:
        mas_len = switcher[action](mas)
        print(mas_len)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
