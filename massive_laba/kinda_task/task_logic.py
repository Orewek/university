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


if __name__ == '__main__':
    print('You cant run this file as main')
