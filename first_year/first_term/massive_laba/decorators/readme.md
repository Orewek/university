## Декораторы

### Есть несколько типов:
* `mas_before_after` - показывает состояние масива до и после функции
* `str_to_int` - для целочисленных операций
* `count_time` - фиксируем время до операции, и после. end - start = время работы функции
* `negative_positive` - Берем все числа по модулю

#### Также существуют `name_logic` декораторы
#### Они выполняют какую-либо функции, не выводя что-либо на экан
##### К примеру `negative_positive`

`mas_before_after`
```py
def mas_before_after(func):
    def wrapper(*args):
        print(f'\nMassive before operation {args[0]}')
        result = func(args[0], *args[1:])
        print(f'\nMassive after operation {args[0]}\n')

        return result
    return wrapper
```

`str_to_int`
```py
def str_to_int(func: Callable[[Iterable[Any]], Any]):
    def wrapper(*args: Any):
        str_count: int = 0
        str_el: list = []

        for i in range(len(args[0])):
            if type(args[0][i]) is str:
                args[0][i]: int = int(args[0][i])
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
```

`count_time`
```py
def count_time(func: Callable[[Iterable[Any]], Any]):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()

        time_result = end_time - start_time
        print(f'\n==TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME=\n'
              f'This function had been working for {time_result} seconds\n'
              f'===TIME===TIME===TIME===TIME===TIME===TIME===TIME===TIME==')

        return result
    return wrapper
```
`negative_positive`
```py
def negative_positive(func: Callable[[Iterable[Any]], Any]):
    def wrapper(*args: Any):
        neg_count: int = 0
        for el in range(len(args[0])):
            if el < 0:
                el: int = abs(el)
                neg_count += 1

        if neg_count > 0:
            print(f'{neg_count} elements were changed: negative -> positive')

        result = func(*args)

        return result
    return wrapper
```