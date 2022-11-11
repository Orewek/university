def show_elements(mas: list) -> list:
    """
    enumerate each element in mas
    """
    for count, ma in enumerate(mas):
        print(f'{count + 1}: {ma}')

    return mas


def change_elements(mas: list, change_mas: list) -> list:
    """
    changing/replacing elements
    """
    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')

            replace_cell = input()
            while replace_cell.isdigit() is False:
                print('You can change element only on another number/digit')
                replace_cell = input()
            mas[i] = replace_cell
    return mas


def clear_mas(mas: list) -> list:
    """
    clearing massive (reinitialization)
    """
    mas = []
    return mas


def len_mas(mas: list) -> str:
    """
    Just calculating and returning the len of mas
    """
    ans = f'{len(mas)} - length of massive'
    return ans


if __name__ == '__main__':
    print('You cant run this file as main')
