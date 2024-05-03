from Unit_tests.some_checks import check_int


def show_elements(mas: list) -> list:
    """
    enumerate each element in mas
    """
    print(*[f'{count + 1}: {item}' for count, item in enumerate(mas)], sep='\n')

    return mas


def change_elements(mas: list, change_mas: list) -> list:
    """
    changing/replacing elements
    """
    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')

            replace_cell: str = check_int(input())
            mas[i]: int = replace_cell
    return mas


def clear_mas(mas: list) -> list:
    """
    clearing massive (reinitialization)
    """
    mas.clear()
    return mas


def len_mas(mas: list) -> str:
    """
    Just calculating and returning the len of mas
    """
    ans: str = f'{len(mas)} - length of massive'
    return ans


if __name__ == '__main__':
    print('You cant run this file as main')
