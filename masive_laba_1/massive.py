from random import randint


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
            return '00'
        number //= 10
    return '11'


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
        if result_mas[i] == result_mas[i + 1] and result_mas[i] == '11':
            count += 1
        else:
            res1 = max(res1, count)
            count = 1

    count = 1

    for i in range(mas_len - 1):
        if result_mas[i] == result_mas[i + 1] and result_mas[i] == '00':
            count += 1
        else:
            res0 = max(res0, count)
            count = 1

    return res1, res0


def task_b8():
    number_mas = []
    result_mas = []

    mas_len = 20
    num_len = 4

    for _ in range(mas_len):
        number = randint(10**(num_len - 1), 10**num_len)
        number_mas.append(number)

        result = chered_checker(number, num_len, 2)
        result_mas.append(result)

    """
    Random numbers
    Results, Yes(11) No(00)
    Total amount
    """

    print(number_mas)
    print(result_mas)
    amount_numbers = result_mas.count('11')
    print(amount_numbers)


def task_c8():

    number_mas = []
    result_mas = []

    mas_len = 20
    num_len = 4

    for _ in range(mas_len):
        number = randint(10**(num_len - 1), 10**num_len)
        number_mas.append(number)

        result = chered_checker(number, num_len, 10)
        result_mas.append(result)

    print(number_mas)
    print(result_mas)

    res1, res0 = consecutive_result(mas_len, result_mas)

    print(f' max 1 = {res1}, max 0 = {res0}')


if __name__ == '__main__':
    task_b8()
    task_c8()
