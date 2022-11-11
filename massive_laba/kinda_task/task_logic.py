from decorators.decor_logic import int2str_before, str2int_before
from decorators.decorator import complete_bar, count_time


@str2int_before
def mean_arif(mas: list) -> list:
    """
    Calculation arif sum of whole mas el
    Firstly count total sum and divide on amount of elements
    """
    el_sum = 0
    for i in range(len(mas)):
        el_sum += mas[i]

    arif_sum = el_sum / len(mas)
    print(f'Arifmetical sum = {arif_sum}')

    return mas


@str2int_before
def min_el(mas: list) -> list:
    """
    Outputing the min el of mas
    """
    print(f'minimal element of massvie = {min(mas)}')
    return mas


@str2int_before
def max_el(mas: list) -> list:
    """
    Outputing the max el of mas
    """
    print(f'maxmimum element of massvie = {max(mas)}')
    return mas


def chered_checker(number: int, divide: int) -> str:
    """
    TASK B8
        if n'th and (n-1)'th element give the same remainder % 2 -> return 0
        else -> return 1

        kinda yes/no

    TASK C8
        if n'th element == (n - 1)'th -> return 0
        else -> return 1
    """
    while (number // 10) > 0:
        if number % divide == (number // 10) % divide:
            return '0'
        number //= 10
    return '1'


@int2str_before
def consecutive_result(result_mas: list) -> list:
    """
    consecutive 1 in the row = res1
    consecutive 0 in the row = res0

    while we finding out that n == n + 1 -> count += 1
    else: if count > the longest row (res1 / res0) -> res = count
    reseting count -> count = 1
    """
    count = 1

    res1 = 0
    res0 = 0

    for i in range(len(result_mas) - 1):
        if result_mas[i] == result_mas[i + 1] and str(result_mas[i]) == '1':
            count += 1
        else:
            res1 = max(res1, count)
            count = 1

    count = 1

    for i in range(len(result_mas) - 1):
        if result_mas[i] == result_mas[i + 1] and str(result_mas[i]) == '0':
            count += 1
        else:
            res0 = max(res0, count)
            count = 1

    return res1, res0


@count_time
@str2int_before
@complete_bar
def bubble_sort(mas: list) -> list:
    for _ in range(len(mas)):
        for i in range(len(mas) - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
