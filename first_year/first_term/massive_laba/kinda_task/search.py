from decorators.decor_logic import str2int_before
from decorators.decorator import count_time


@count_time
@str2int_before
def consistent_search(mas: list, find_el: int) -> int:
    """
    going throw the mas (n >> n + 1 >> n + 2) to find el
    """
    for i in range(len(mas)):
        if mas[i] == find_el:
            return i + 1
    return -1


@count_time
@str2int_before
def binary_search(mas: list, find_el: int) -> int:
    mas: list = sorted(mas)
    low: int = 0
    mid: int = 0
    high: int = len(mas) - 1

    while low < high:
        mid: int = (low + high) // 2
        if mas[mid] < find_el:
            low: int = mid

        if mas[mid] == find_el:
            return mid + 1

        if mas[mid] > find_el:
            high: int = mid

    return - 1


@str2int_before
def fibonacci_search(mas: list, find_el: int, total_index=0) -> int:
    mas: list = sorted(mas)
    fib_index_1: int = 1
    fib_index_2: int = 1

    fib_index_1, fib_index_2 = looking_for_limit(fib_index_1,
                                                 fib_index_2,
                                                 find_el, mas)
    # Now find_el <= fib_i_2
    fib_index_1, fib_index_2 = reduce_nth(fib_index_1,
                                          fib_index_2,
                                          find_el, mas)

    # Now fib_i_1 <= find_el <= fib_i_2
    # Heres might be diff fib_i_2 than in prev while
    # Cutting new mas
    new_mas = [mas[i] for i in range(fib_index_1, fib_index_2)]

    # Checking the corners

    return corners_check(fib_index_1,
                         fib_index_2,
                         total_index,
                         find_el, mas)
    return fibonacci_search(new_mas, find_el, total_index + fib_index_1)


def looking_for_limit(fib_index_1: int,
                      fib_index_2: int,
                      find_el: int, mas: list) -> tuple:
    while fib_index_2 <= len(mas) - 1 and mas[fib_index_2] <= find_el:
        # For example
        # 1 + 1 = 2; 1 + 2 = 3
        # 2 + 3 = 5; 3 + 5 = 8
        fib_index_1 += fib_index_2
        fib_index_2 += fib_index_1

        # Heres might be 4 els in mas, but 2 + 3 = 5
        # So fib_index_2 = 5, whichs > len(mas)
        if fib_index_2 > len(mas):
            fib_index_1: int = fib_index_2 - fib_index_1
            fib_index_2: int = len(mas)
            break

    return (fib_index_1, fib_index_2)


def reduce_nth(fib_index_1: int,
               fib_index_2: int,
               find_el: int, mas: list) -> tuple:
    while fib_index_1 > len(mas) - 1 or mas[fib_index_1] > find_el:
        """
        fib n'th and fib (n + 1)'th
        to >>>
        fib (n - 1)'th and fib n'th
        """
        type_var: int = fib_index_2
        fib_index_2: int = fib_index_1
        fib_index_1: int = type_var - fib_index_1

    return (fib_index_1, fib_index_2)


def corners_check(fib_index_1: int,
                  fib_index_2: int,
                  total_index: int,
                  find_el: int, mas: list) -> tuple:
    if fib_index_1 == fib_index_2 or fib_index_1 == 0:
        if mas[0] == find_el:
            return total_index + fib_index_1 + 1
        if mas[-1] == find_el:
            return total_index + fib_index_1 + 2

        return -1


@count_time
@str2int_before
def interpolation_search(mas: list, find_el: int) -> int:
    mas: list = sorted(mas)
    l: int = 0
    r: int = len(mas) - 1

    # If mas[0] == mas[-1] means that whole mas contains same el
    if mas[0] == mas[-1]:
        return 0

    while mas[l] <= find_el <= mas[r]:
        mid: int = l + int((find_el - mas[l]) / (mas[r] - mas[l]) * (r - l))

        if find_el < mas[mid]:
            r: int = mid - 1

        if find_el == mas[mid]:
            return mid + 1

        if find_el > mas[mid]:
            l: int = mid - 1

    return - 1


if __name__ == '__main__':
    print('You cant run this file as main')
