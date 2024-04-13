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
    mas = sorted(mas)
    low = 0
    mid = 0
    high = len(mas) - 1

    while low < high:
        mid = (low + high) // 2
        if mas[mid] < find_el:
            low = mid

        if mas[mid] == find_el:
            return mid + 1

        if mas[mid] > find_el:
            high = mid

    return - 1


@str2int_before
def fibonacci_search(mas: list, find_el: int, total_index=0) -> int:
    mas = sorted(mas)
    fib_index_1 = 1
    fib_index_2 = 1

    while fib_index_2 <= len(mas) - 1 and mas[fib_index_2] <= find_el:
        # For example
        # 1 + 1 = 2; 1 + 2 = 3
        # 2 + 3 = 5; 3 + 5 = 8
        fib_index_1 += fib_index_2
        fib_index_2 += fib_index_1

        # Heres might be 4 els in mas, but 2 + 3 = 5
        # So fib_index_2 = 5, whichs > len(mas)
        if fib_index_2 > len(mas):
            fib_index_1 = fib_index_2 - fib_index_1
            fib_index_2 = len(mas)
            break

    # Now find_el <= fib_i_2

    while fib_index_1 > len(mas) - 1 or mas[fib_index_1] > find_el:
        """
        fib n'th and fib (n + 1)'th
        to >>>
        fib (n - 1)'th and fib n'th
        """
        type_var = fib_index_2
        fib_index_2 = fib_index_1
        fib_index_1 = type_var - fib_index_1

    # Now fib_i_1 <= find_el <= fib_i_2
    # Heres might be diff fib_i_2 than in prev while
    new_mas = []
    # Cutting new mas
    for i in range(fib_index_1, fib_index_2):
        new_mas.append(mas[i])

    # Checking the corners
    if fib_index_1 == fib_index_2 or fib_index_1 == 0:
        if mas[0] == find_el:
            return total_index + fib_index_1 + 1
        if mas[-1] == find_el:
            return total_index + fib_index_1 + 2
        else:
            return -1

    return fibonacci_search(new_mas, find_el, total_index + fib_index_1)


@count_time
@str2int_before
def interpolation_search(mas: list, find_el: int) -> int:
    mas = sorted(mas)
    left = 0
    right = len(mas) - 1

    # If mas[0] == mas[-1] means that whole mas contains same el
    if mas[0] == mas[-1]:
        return 0

    while mas[left] <= find_el <= mas[right]:
        mid = left + int((find_el - mas[left]) / (mas[right] - mas[left]) * (right - left))

        if find_el < mas[mid]:
            right = mid - 1

        if find_el == mas[mid]:
            return mid + 1

        if find_el > mas[mid]:
            left = mid - 1

    return - 1


if __name__ == '__main__':
    print('You cant run this file as main')
