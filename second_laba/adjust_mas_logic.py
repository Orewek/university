def change_elements(mas: tuple) -> tuple:
    """
    showing whole massive
    After that user can choose digits, which elements we should change
    changing it
    """
    print(f'Your massive:\n{mas}')
    for count, el in enumerate(len(mas)):
        print(f'{count}: {el}')


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
    ans = f'{len(mas)}- length of massive'
    return ans
    