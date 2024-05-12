import time

from search_string.search_logic import boiera_mura_search, kmp_logic


def time_speed(user_str: str, find_el: str) -> str:
    start_time: float = time.time()
    kmp_logic(user_str, find_el)
    end_time: float = time.time()
    print(end_time - start_time)

    start_time: float = time.time()
    boiera_mura_search(user_str, find_el)
    end_time: float = time.time()
    print(end_time - start_time)

    return user_str


if __name__ == '__main__':
    print('You cant run this file as main')
