from decorators.decor_logic import str2int_before
from decorators.decorator import count_time


@str2int_before
def sum_max2_min1(mas: list) -> list:
    """
    max_even - max el % 2 in mas
    min_odd - min el !% 2n in mas
    find_num - min_odd + max_even
    check if this find_num in mas
    """
    min_odd: int = 10**10
    max_even: int = - 1

    for el in mas:
        if el % 2 == 0 and el > max_even:
            max_even: int = el
        if el % 2 != 0 and el < min_odd:
            min_odd: int = el

    if ((min_odd + max_even) in mas) is True:
        print(f'maximum even + minimum odd in massive!\n'
              f'{max_even} + {min_odd} = {max_even + min_odd}')
    else:
        print('maximum even + minimum odd not in massive!')

    return mas


def swap_el(index_max: int, perma_el: int, mas: list) -> list:
    """
    swapping max el in mas and last el in mas
    """
    index_last: int = len(mas) - perma_el - 1
    mas[index_last], mas[index_max] = mas[index_max], mas[index_last]

    return mas


@count_time
# @str2int_before
# @complete_bar
def selection_sort(mas: list) -> list:
    """
    perma_el - how many el's r permanent
    -(last 2, last 3 cuz the already max)

    max_el: finding max el for O(n)

    index_el - index of the max el in mas

    swap_el(max_el, last_el)
    perma_el += 1
    """
    perma_el: int = 0
    for _ in range(len(mas)):
        max_el: int = mas[0]
        for i in range(len(mas) - perma_el):
            if mas[i] > max_el:
                max_el: int = mas[i]
                index_el: int = i

        mas: int = swap_el(index_el, perma_el, mas)
        perma_el += 1

    return mas


@str2int_before
def chered_odd(mas: list) -> list:
    """
    pair - x'th and (x + 1)'th
    x'th % 2 != (x + 1)'th % 2 => count += 1
    so, even_odd or odd_even += 1
    """
    count_odd_pairs: int = 0
    for i in range(len(mas) - 1):
        if mas[i] % 2 != mas[i + 1] % 2:
            count_odd_pairs += 1

    print(f'Found {count_odd_pairs} even_odd pairs')

    return mas


@str2int_before
def quick_sort(mas: list) -> list:
    """
    Quick_sort
    pivot - first el in mas
    sorting rest els to less; equal; greater
    """
    less: list = []
    equal: list = []
    greater: list = []

    if len(mas) > 1:
        pivot: int = mas[0]
        for el in mas:
            if el < pivot:
                less.append(el)
            if el == pivot:
                equal.append(el)
            if el > pivot:
                greater.append(el)

        return quick_sort(less) + equal + quick_sort(greater)

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
