# from decorators.decor_logic import str2int_before
# from decorators.decorator import complete_bar, count_time


# @count_time
def consistent_search(mas: list, find_el: int) -> int:
    """
    going throw the mas (n >> n + 1 >> n + 2) to find el
    """
    for i in range(len(mas)):
        if mas[i] == find_el:
            return i + 1
    return -1


# @count_time
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


# @count_time
def fibonacci_search(mas: list, find_el: int, total_index=0) -> int:
    mas = sorted(mas)
    fibonacci_index_1 = 1
    fibonacci_index_2 = 1

    while fibonacci_index_2 < len(mas) - 1 and mas[fibonacci_index_2] < find_el:
        # For example
        # 1 + 1 = 2; 1 + 2 = 3
        # 2 + 3 = 5; 3 + 5 = 8
        fibonacci_index_1 += fibonacci_index_2
        fibonacci_index_2 += fibonacci_index_1

    # Now find_el <= fib_i_2

    while fibonacci_index_1 > len(mas) - 1 or mas[fibonacci_index_1] > find_el:
        """
        fib n'th and fib (n + 1)'th
        to >>>
        fib (n - 1)'th and fib n'th
        """
        type_var = fibonacci_index_2
        fibonacci_index_2 = fibonacci_index_1
        fibonacci_index_1 = type_var - fibonacci_index_1

    # Now fib_i_1 <= find_el <= fib_i_2
    # Heres might be diff fib_i_2 than in prev while
    new_mas = []
    for i in range(fibonacci_index_1, fibonacci_index_2):
        new_mas.append(mas[i])

    if fibonacci_index_1 == fibonacci_index_2:
        if mas[0] == find_el:
            return total_index + fibonacci_index_1 + 1
        if mas[1] == find_el:
            return total_index + fibonacci_index_1 + 2
        else:
            return -1

    return fibonacci_search(new_mas, find_el, total_index + fibonacci_index_1)


# @count_time
def interpolation_search(mas: list, find_el: int) -> int:
    mas = sorted(mas)
    left = 0
    right = len(mas) - 1

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
    res = fibonacci_search([-89, -858, 653, -52, 910, 543, 606, -163, -327, -801, 956, -740, 496, -787, 277, -101, 788, 346, -582, -663, -224, -824, 790, 778, -604, 559, -269, 
-524, 126, -510, -765, -203, -320, -654, -911, -677, 915, -112, 924, 520, -617, -513, -391, 757, -657, 205, 900, 145, 468, -561, 747, -163, 560, -650, 759, 577, 60, 537, 650, -756, 273, -703, -230, -944, -471, -505, -731, 415, 923, -346, -359, -733, -515, -489, -974, 971, -53, -884, -473, 195, 795, -267, -723, 584, 310, -713, -800, 429, -162, 738, -11, -296, -665, -168, -177, -726, -572, -58, -129, 292, 99, -356, 828, 304, -349, -851, -405, 921, -25, 696, 784, 
153, -198, -853, -926, 807, 226, -640, -807, -245, 203, 446, 914, -190, 467, -945, 990, -820, 548, -396, -717, -857, 919, -678, 129, -367, 376, -307, 371, 
425, 124, -473, -835, 765, -692, 796, -531, -354, 410, -823, 203, 17, -564, 819, -994, -118, -525, -645, 130, 55, -262, -929, 505, 229, 683, -412, 322, -974, 656, -554, 954, -407, -847, 850, 1000, -292, 401, 623, 242, 900, -847, 942, -552, 853, -5, -210, -885, 194, 719, -53, -606, 61, -372, 885, 393, 779, 242, -242, -268, -171], 60, 0)
    print(res)