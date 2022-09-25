def show_elements(mas: tuple):
    """
    enumerate each element in mas
    """

    for count, ma in enumerate(mas):
        print(f'{count + 1}: {ma}')


def change_elements(mas: tuple, change_mas: tuple) -> tuple:
    """
    changing/replacing elements
    """

    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')
            replace_cell = input()
            mas[i] = replace_cell
    print(f'change VIHOD - {mas}')
    return mas


def clear_mas(mas: tuple) -> tuple:
    """
    clearing massive (reinitialization)
    """
    mas = []
    return mas


def len_mas(mas: tuple) -> str:
    """
    Just calculating and returning the len of mas
    """
    ans = f'{len(mas)} - length of massive'
    return ans


if __name__ == '__main__':
    print('You cant run this file as main')
