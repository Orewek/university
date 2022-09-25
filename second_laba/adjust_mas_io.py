from adjust_mas_logic import clear_mas, len_mas
from adjust_mas_logic import show_elements, change_elements


def mas_elements(mas: tuple) -> tuple:
    """
    read show_elemetns .__doc__
    read change_elements .__doc__
    """
    show_elements(mas)

    print('\nNow You can write digits next to elements that we need to change\n'
          'Write them separated, after each digit press Enter\n'
          'It will be able to write more digits. When You done: press Enter\n')

    change_mas = []
    change_number = input()

    while change_number != '':

        while change_number.isdigit() is False:
            print('You can write only digits. Try again')
            change_number = input()
        change_number = int(change_number)

        while int(change_number) > len(mas):
            print('Elements with this number doesnt exist. Try again')
            change_number = input()

        change_mas.append(change_number)
        change_number = input()

    for i in range(len(change_mas)):
        change_mas[i] -= 1

    change_elements(mas, change_mas)

    return mas


def adjust_mas(mas: tuple):
    print(f'VXOD MASSIVE - {mas}')
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
    if action != 1:
        print(f'2 VHOD MASSIVE -{mas}')
        mas = switcher[action](mas)
    else:
        mas_len = switcher[action](mas)
        print(mas_len)

    print(f'VIHOD MASSIVE - {mas}')
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
    mas = ['asfasgqwegqg', 'qwqweqwe', '312321']
    mas = adjust_mas(mas)
    print(mas)
