from adjust_mas_logic import change_elements, clear_mas, len_mas

def adjust_mas(mas: tuple):

    print(f'1: massive length\n'
          f'2: change elements\n'
          f'3: clear massive')
    action = input()


    while len(action) != 1 or action.isdigit() is False:
        print('U can write only one digit. After operation u can continue working with massive')
        action = input()
    action = int(action)

    
    switcher = {
        1: len_mas,
        2: change_elements,
        3: clear_mas
    }
    if action != 1:
        mas = switcher[action](mas)
    else:
        mas_len = switcher[action](mas)
        print(mas_len)

    return mas

if __name__ == '__main__':
    print('You cant run this file as main')