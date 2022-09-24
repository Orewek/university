from input_mas_io import create_mas
from adjust_mas_io import adjust_mas


def menu(action: int, mas: tuple) -> tuple:
    switcher = {
        1: create_mas,
        2: adjust_mas,
        #3: output_mas,
        #4: task,
        '5': 'exit'
    }
    mas = switcher[action](mas)
    return mas


#def output_mas(mas: tuple):
#    print(mas)
#
#
#def task():

def main(mas: tuple) -> tuple:
    print(f'1: input massive\n'
          f'2: adjust massive\n'
          f'3: output massive\n'
          f'4: task\n'
          f'5: exit\n')
    
    print('What u wanna do? Write one digit')
    action = input()

    while len(action) != 1 or action.isdigit() is False:
        print('U can write only one digit. After operation u can continue working with massive')
        action = input()

    action = int(action)
    mas = menu(action, mas)
    return mas
    

if __name__ == '__main__':
    mas = []
    mas = main(mas)

    print('One more?\n [y, yes, 1]')
    additional_check = input()
    approved = ['y', 'yes', '1']
    while additional_check.lower() in approved:
        main(mas)
    print(mas)
    

    #print('Wanna make one more action? Yes/No')


