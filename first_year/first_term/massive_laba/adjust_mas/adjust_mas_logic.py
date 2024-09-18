# -*- coding: utf-8 -*-
"""Show elements/change elements/Show len of massive."""


from Unit_tests.some_checks import check_int


def show_elements(mas: list[int]) -> list:
    """Enumerate each element in mas.

    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    print(*[f'{count + 1}: {item}' for count, item in enumerate(mas)], sep='\n')

    return mas


def change_elements(mas: list[int], change_mas: list) -> list:
    """Change/replace elements.
    
    
    Args:
    ----
        mas: massive with numbers
        change_mas: indexes of elements in massive that we need to change
    
    Return:
    ------
        mas: massive with numbers
    """
    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')

            replace_cell: str = check_int(input())
            mas[i]: int = replace_cell

    return mas


def clear_mas(mas: list[int]) -> list:
    """Clear massive (reinitialization).
    
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    mas.clear()
    return mas


def len_mas(mas: list) -> str:
    """Just calculating and returning the len of mas.
    
    Args:
    ----
        mas: massive with numbers
    
    Return:
    ------
        mas: massive with numbers
    """
    ans: str = f'{len(mas)} - length of massive'
    return ans


if __name__ == '__main__':
    print('You cant run this file as main')
