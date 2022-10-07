from kinda_task.task_logic import mean_arif, min_el, max_el


def task_menu(action: int, mas: tuple) -> tuple:
    switcher = {
        1: mean_arif,
        2: min_el,
        3: max_el
    }
    mas = switcher[action](mas)
    return mas


def task_io(mas: tuple) -> tuple:
    """
    User can find min/max so + or * of el, median etc.
    Rn it has the name "task", cant change it
    """

    print('Well, you can find some info about your massive\n'
          'Heres the table what can you do:')

    task_table = """
                 1: mean arifmetical
                 2: minimal element
                 3: maxmimun element
                 """
    print(task_table)

    
    print('What u wanna do? Write one digit')
    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(task_table)
        else:
            print(task_table)
        action = input()

    action = int(action)
    mas = task_menu(action, mas)
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')