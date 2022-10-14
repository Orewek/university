from decorators.decorator import mas_before_after, str_to_int, count_time


def mean_arif(mas: tuple) -> tuple:
    """
    Calculation arif sum of whole mas el
    Firstly count total sum and divide on amount of elements
    """
    el_sum = 0
    for i in range(len(mas)):
        el_sum += int(mas[i])

    arif_sum = el_sum / len(mas)
    print(f'Arifmetical sum = {arif_sum}')

    return mas


def min_el(mas: tuple) -> tuple:
    """
    Outputing the min el of mas
    """
    print(f'minimal element of massvie = {min(mas)}')
    return mas


def max_el(mas: tuple) -> tuple:
    """
    Outputing the max el of mas
    """
    print(f'maxmimum element of massvie = {max(mas)}')
    return mas


def chered_checker(number: int, num_len: int, divide: int) -> str:
    """
    TASK B8
        if n'th and (n-1)'th element give the same remainder % 2 -> return 0
        else -> return 1

        kinda yes/no

    TASK C8
        if n'th element == (n - 1)'th -> return 0
        else -> return 1
    """
    for i in range(num_len - 1):
        if number % divide == (number // 10) % divide:
            return '0'
        number //= 10
    return '1'


def consecutive_result(mas_len: int, result_mas: tuple) -> tuple:
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

    for i in range(mas_len - 1):
        if result_mas[i] == result_mas[i + 1] and str(result_mas[i]) == '1':
            count += 1
        else:
            res1 = max(res1, count)
            count = 1

    count = 1

    for i in range(mas_len - 1):
        if result_mas[i] == result_mas[i + 1] and str(result_mas[i]) == '0':
            count += 1
        else:
            res0 = max(res0, count)
            count = 1

    return res1, res0


@mas_before_after
@str_to_int
@count_time
def bubble_sort(mas: tuple) -> tuple:
    for _ in range(len(mas)):
        for i in range(len(mas) - 1):
            if int(mas[i]) > int(mas[i + 1]):
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas


if __name__ == '__main__':
    print('You cant run this file as main')
    mas = ['989', '213', '832', '932', '731', '84331', '232']
    mas = mas.sort()
    print(mas)
