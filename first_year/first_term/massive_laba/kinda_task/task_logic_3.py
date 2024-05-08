def symmetrical_number(number: int) -> bool:
    digits_of_num: list = [int(i) for i in str(abs(number))]

    for i in range(len(digits_of_num) // 2):
        if digits_of_num[i] != digits_of_num[len(digits_of_num) - 1 - i]:
            return False

    # if u wanna see whole symmetrical numbers in mas
    # print(digits_of_num)
    return True


def reverse_number(number: int) -> int:
    digits_of_num: list = [int(i) for i in str(abs(number))]
    reversed_number: int = sum([digits_of_num[i] * (10 ** i) for i in range(len(digits_of_num))])

    return reversed_number


def prime_number(number: int) -> bool:
    return not(any([int(x) for x in range(2, (number // 2) + 1) if number % x == 0]))


def check_contain_5(number: int) -> bool:
    return any([int(x) for x in str(abs(number)) if int(x) % 5 == 0])


if __name__ == '__main__':
    print('You cant run this file as main')
