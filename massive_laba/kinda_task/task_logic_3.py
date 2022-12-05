from decorators.decor_logic import negative_positive_logic, str2int_before
from decorators.decorator import complete_bar, count_time


def symmetrical_number(number: int) -> bool:
    digits_of_num = []
    while number != 0:
        digits_of_num.append(number % 10)
        number //= 10

    for i in range(len(digits_of_num) // 2):
        if digits_of_num[i] != digits_of_num[len(digits_of_num) - 1 - i]:
            return False

    # if u wanna see whole symmetrical numbers in mas
    # print(digits_of_num)
    return True


def reverse_number(number: int) -> int:
    digits_of_num = []
    while number != 0:
        digits_of_num.append(number % 10)
        number //= 10

    reversed_number = 0
    for i in range(len(digits_of_num)):
        reversed_number += digits_of_num[i] * (10 ** i)

    return reversed_number


def prime_number(number: int) -> bool:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False

    # Showing prime numbers in mas
    # print(number, 'prime')
    return True


def check_contain_5(number: int) -> bool:
    while number != 0:
        if number % 10 == 5:
            return True
        number //= 10

    return False


if __name__ == '__main__':
    print('You cant run this file as main')
