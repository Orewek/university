from decorators.decor_logic import str2int_before
from decorators.decorator import count_time


@str2int_before
def find_sum_max2_min1(mas: tuple) -> tuple:
    """
    max_even - max el % 2 in mas
    min_odd - min el !% 2n in mas
    find_num - min_odd + max_even
    check if this find_num in mas
    """
    min_odd = 10**10
    max_even = - 1

    for el in mas:
        if el % 2 == 0 and el > max_even:
            max_even = el
        if el % 2 != 0 and el < min_odd:
            min_odd = el

    if ((min_odd + max_even) in mas) is True:
        print(f'maximum even + minimum odd in massive!\n'
              f'{max_even} + {min_odd} = {max_even + min_odd}')
    else:
        print('maximum even + minimum odd not in massive!')
    return mas


def swap_el(index_max: int, perma_el: int, mas: tuple) -> tuple:
    """
    swapping max el in mas and last el in mas
    """
    index_last = len(mas) - perma_el - 1
    mas[index_last], mas[index_max] = mas[index_max], mas[index_last]

    return mas


@str2int_before
def selection_sort(mas: tuple) -> tuple:
    """
    perma_el - how many el's r permanent
    -(last 2, last 3 cuz the already max)

    max_el: finding max el for O(n)

    index_el - index of the max el in mas

    swap_el(max_el, last_el)
    perma_el += 1
    """
    perma_el = 0
    for _ in range(len(mas)):
        max_el = mas[0]
        for i in range(len(mas) - perma_el):
            if mas[i] > max_el:
                max_el = mas[i]
                index_el = i

        mas = swap_el(index_el, perma_el, mas)
        perma_el += 1

    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
