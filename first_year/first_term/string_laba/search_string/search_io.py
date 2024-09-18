# -*- coding: utf-8 -*-


from Unit_tests.some_checks import check_action

from check_speed import time_speed

from search_string.search_logic import boiera_mura_search, kmp_logic


def search_menu(user_str: str, find_el: str, action: int) -> str:
    switcher: dict = {
        1: kmp_logic,
        2: boiera_mura_search,
        3: time_speed,
    }
    user_str: str = switcher[action](user_str, find_el)

    return user_str


def input_find_ed(user_str: str) -> str:
    find_el: str = input('Which which line u wanna find in your str')

    search_table: str = """
            1: Knuth-Morris-Pratt
            2: Boierra-Mura
            3: compare time speed
            """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with option
    action: int = check_action(input(search_table), action_table, search_table)

    index_res: list = search_menu(user_str, find_el, action)
    print(f'{find_el} was found! indexes: {index_res}' if index_res != [] else f'{find_el} was not found')

    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
