import time
from progress.bar import Bar


def mas_before_after(func):
    """
    Massive before operation
    Operation is happening
    Massive after operation

    Need to find some bugs or just to watch the diff
    """
    def wrapper(*args):
        print(f'\nMassive before operation {args[0]}')
        result = func(*args)
        print(f'\nMassive after operation {args[0]}\n')

        return result
    return wrapper


def str_to_int(func):
    """
    Making whole el in mas str -> int
    """
    def wrapper(*args):
        str_count = 0
        str_el = []

        for i in range(len(args[0])):
            if type(args[0][i]) is str:
                args[0][i] = int(args[0][i])
                str_count += 1
                str_el.append(args[0][i])

        if str_count > 0:
            print(f'\n===STRING_TO_INT===STRING_TO_INT===STRING_TO_INT\n'
                  f'{str_count} elements were changed: str -> int\n'
                  f'This elements were str {str_el}\n'
                  f'===STRING_TO_INT===STRING_TO_INT===STRING_TO_INT')

        result = func(*args)

        return result
    return wrapper


def count_time(func):
    """
    start_time; end_time; after operation (end - start)
    """
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()

        time_result = end_time - start_time
        print(f'\n==TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME=\n'
              f'Function had been working for {round(time_result, 3)} seconds\n'
              f'===TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME==')

        return result
    return wrapper


def negative_positive(func):
    """
    changing negative el to positive
    """
    def wrapper(*args):
        neg_count = 0
        for x in range(len(args[0])):
            if x < 0:
                x = abs(x)
                neg_count += 1

        if neg_count > 0:
            print(f'{neg_count} elements were changed: negative -> positive')

        result = func(*args)

        return result
    return wrapper


def complete_bar(func):
    """
    Progress bar
    """
    def wrapper(*args):
        bar = Bar('Processing', max=len(args[0]))
        for i in range(len(args[0])):
            result = func(*args)
            bar.next()
        bar.finish()

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')
