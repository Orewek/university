def mas_before_after(func):
    """
    Massive before operation
    Operation is happening
    Massive after operation

    Need to find some bugs or just to watch the diff
    """
    def wrapper(*args):
        print(f'\nMassive before operation {args[0]}')
        result = func(args[0], *args[1:])
        print(f'Massive after operation {args[0]}\n')

        return result
    return wrapper


if __name__ == '__main__':
    print('U cant run this file as main')