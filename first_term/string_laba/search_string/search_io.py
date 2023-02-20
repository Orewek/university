from search_string.search_logic import boiera_mura_search, kmp_logic

from check_speed import time_speed
def search_menu(user_str: str, find_el: str, action: int) -> str:
    switcher = {
        1: kmp_logic,
        2: boiera_mura_search,
        3: time_speed,
    }
    user_str = switcher[action](user_str, find_el)

    return user_str


def input_find_ed(user_str: str) -> str:
    print('Which which line u wanna find in your str')
    find_el = str(input())

    search_table = """
            1: Knuth-Morris-Pratt
            2: Boierra-Mura
            3: compare time speed
            """

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """

    print(search_table)

    action = input()

    # checking for letters and multi-digits
    # -talbe: user can void a talbe with options
    while len(action) != 1 or action.isdigit() is False:
        if action != '-table':
            print(action_table)
        else:
            print(search_table)
        action = input()

    index_res = search_menu(user_str, find_el, int(action))
    if index_res != []:
        print(f'{find_el} was found! indexes: {index_res}')
    else:
        print(f'{find_el} was not found')

    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
