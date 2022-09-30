from input_mas.input_mas_logic import add_elements


def create_mas(mas: tuple) -> tuple:
    print('\nWrite each element separated\n'
          'Remember,You can write only digits. Non-digits elements will be deleted\n'
          'If u wanna to exit, press Enter')
    mas = add_elements(mas)

    print(f'Massive was sucsessfully createad. Mas - {mas}')
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
