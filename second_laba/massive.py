from input_mas_io import create_mas
from adjust_mas_io import adjust_mas


def menu(action: int, mas: tuple) -> tuple:
    switcher = {
        1: create_mas,
        2: adjust_mas,
        #3: output_mas,
        #4: task,
        5: 'exit'
    }
    mas = switcher[action](mas)
    return mas


#def output_mas(mas: tuple):
#    print(mas)
#
#
#def task():

def main(mas: tuple) -> tuple:
    table = """
            1: input massive
            2: adjust massive
            3: output massive
            4: task
            5: exit
            """
    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    print(table)

    print('What u wanna do? Write one digit')
    action = input()

    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action = input()

    action = int(action)
    mas = menu(action, mas)
    return mas


if __name__ == '__main__':
    mas = []
    mas = main(mas)

    approved = ['y', 'yes', '1']
    print(f'One more?\n {approved}')
    additional_check = input()

    while additional_check.lower() in approved:
        mas = main(mas)
    print(mas)

    # print('Wanna make one more action? Yes/No')