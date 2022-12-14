from adjust_mas.adjust_mas_io import adjust_massive

from input_mas.input_mas_io import create_mas_io

from kinda_task.task import task_io

from output.output_mas import show_mas


def menu(action: int, mas: list) -> list:
    switcher = {
        1: create_mas_io,
        2: adjust_massive,
        3: show_mas,
        4: task_io,
    }
    if action != 5:
        mas = switcher[action](mas)
    return mas


def main(mas: list) -> list:
    table = """
            1: input massive
            2: adjust massive
            3: output massive
            4: tasks
            5: exit
            """
    action_table = """
                   U can write only one digit, 1 to 5
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    print(table)

    print('What u wanna do? Write one digit')

    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action = input()

    mas = menu(int(action), mas)
    if int(action) == 5:
        mas.append('exit')
    return mas


if __name__ == '__main__':
    mas = main(mas=[])

    # If user wanna continue, he can write 1/yes/y
    approved = ['y', 'yes', '1']

    print(f'One more?\n {approved}')
    additional_check = input()

    while additional_check.lower() in approved and 'exit' not in mas:
        mas = main(mas)
    mas = mas[:-1]
    print(mas)
