from adjust_mas.adjust_mas_io import adjust_massive

from input_mas.input_mas_io import create_mas_io

from kinda_task.task import task_io

from output.output_mas import show_mas


def menu(action: int, mas: list) -> list:
    switcher: dict = {
        1: create_mas_io,
        2: adjust_massive,
        3: show_mas,
        4: task_io,
    }
    if action != 5:
        mas: list = switcher[action](mas)
    return mas


def main(mas: list) -> list:
    table: str = """
            1: input massive
            2: adjust massive
            3: output massive
            4: tasks
            5: exit
            """
    action_table: str = """
                   U can write only one digit, 1 to 5
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    print(table)

    print('What u wanna do? Write one digit')

    action: str = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(table)
        action: str = input()

    mas: list = menu(int(action), mas)
    if int(action) == 5:
        mas.append('exit')
    return mas


if __name__ == '__main__':
    mas: list = main(mas=[])

    # If user wanna continue, he can write 1/yes/y
    approved: list = ['y', 'yes', '1']

    print(f'One more?\n {approved}')
    additional_check: str = input()

    while additional_check.lower() in approved and 'exit' not in mas:
        mas: list = main(mas)
    mas: list = mas[:-1]
    print(mas)
