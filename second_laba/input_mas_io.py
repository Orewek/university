from input_mas_logic import add_elements


def create_mas(mas: tuple) -> tuple:
    print('\nWrite each element separated\nIf u wanna to exit, press Enter')
    mas = add_elements(mas)    

    print(f'Massive wa sucsessfully createad. Mas - {mas}')
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')