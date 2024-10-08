# Лаба #1
## Задание А8
### Найти min / max элемент. Средне-арифмитическое

##### Средне-арифмитическое. Складываем все эллементы и делим на кол-во
```py
@str2int_before
def mean_arif(mas: list) -> list:
    el_sum = reduce(lambda x, y: x + y, mas)

    arif_sum: float = el_sum / len(mas)
    print(f'Arifmetical sum = {arif_sum}')

    return mas
```

##### Минимальный / максимальный
```py
def min_el(mas: list) -> list:
    print(f'minimal element of massvie = {min(mas)}')
    return mas


def max_el(mas: list) -> list:
    print(f'maxmimum element of massvie = {max(mas)}')
    return mas
```


## Задание B8
### Найти количество таких элементов, в которых чередуются четные и нечетные цифры

#### Общий вид программы
* Создать массив
* Два соседних числа дают одинаковый остаток при делении на 2
    * `1` если нет
    * `0` если да

##### Посмотрим на остатки двух соседних цифр, после чего выведим `1: подоходит` `0: не подходит`
```py
def chered_checker(number: int, divide: int) -> str:
    while (number // 10) > 0:
        if number % divide == (number // 10) % divide:
            return '0'
        number //= 10
    return '1'
```

#### Пример работы

##### Создали массив
`[2102, 1945, 1427, 3793, 8738, 3268, 5113, 9188, 4240, 9424, 8530, 1756, 4484, 1658, 2828, 5159, 8842, 6320, 5850, 9975]`

`['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0']`

```py
amount_numbers = result_mas.count('1')
print(amount_numbers)
```
Вывели их итоговое количество


# Задание C8
### Число состоит из попарно различных цифр

#### Общий вид программы
* Создать массив
* Два соседних числа дают одинаковы
    * `1` если нет
    * `0` если да

```py
def chered_checker(number: int, divide: int) -> str:
    while (number // 10) > 0:
        if number % divide == (number // 10) % divide:
            return '0'
        number //= 10
    return '1'
```

##### Посмотрим, равны ли две соседние цифры, после чего выведим `11: подоходит` `00: не подходит`
```py
def chered_checker(number: int, divide: int) -> str:
    while (number // 10) > 0:
        if number % divide == (number // 10) % divide:
            return '0'
        number //= 10
    return '1'
```

##### Находим максимальную последовательность `11` и `00` в массиве с результатами
```py
@int2str_before
def consecutive_result(result_mas: list) -> tuple:
    res1: str = '1'
    res0: str = '0'

    string = ''.join(result_mas)
    while res1 in string:
        res1 += '1'

    while res0 in string:
        res0 += '0'

    res1 = res1[:-1]
    res0 = res0[:-1]

    return len(res1), len(res0)
```
* Смотрим, равны ли два подряд идущих элемента
    * Изначально `count = 1`, потому что если мы найдем такую пару, это же уже строчка из 2 элементов
* Проверяем `n + 1` и `n + 2` элемент, если и они равны `count += 1`
    * Если это верно => `n` == `n + 2` и строка продолжается
* Как только мы выясняем что два подряд идущих эелемента не равны, заканчиваем сравнение.
    * Сравниваем `count` с максимально длинной строчкой, известной на данный момент. Если `count` больше => записываем
    * Сбрасываем `count` до 1, проходимся алгоритмом до конца массива
* После того, как мы сделали данный алгоритм для `1`, делаем тоже самое для `0`
* По итогу получили `res0` и `res1`, которые содержает нужные нам значения. Возвращаем их из функции

#### Пример работы
##### Создали массив 
`[6701, 7455, 2672, 5847, 9047, 7983, 6033, 5150, 2015, 7967, 2172, 5375, 5115, 9922, 7886, 7860, 9848, 9433, 1490, 8683]`
##### Попарно проверили числа
`['1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1']`
##### Вернули максимальные длины
`max 1 = 5, max 0 = 3`

# Лаба #2
## Сортирвка выбором / Selection sort
```
Находим максимальный элемент среди всех элементов
Меняем его с последним элементов, он становится перманентным
Находим след. макс. эл., меняет с последним не перманентным (предпосл.)
Делаем так до тех пор пока массив не станет весь из перманентных
```

```py
@count_time
def selection_sort(mas: list) -> list:
    perma_el: int = 0
    for _ in range(len(mas)):
        max_el: int = mas[0]
        for i in range(len(mas) - perma_el):
            if mas[i] > max_el:
                max_el: int = mas[i]
                index_el: int = i

        mas: int = swap_el(index_el, perma_el, mas)
        perma_el += 1

    return mas
```
##### Swap_el меняет местами элементы

```py
def swap_el(index_max: int, perma_el: int, mas: list) -> list:
    index_last: int = len(mas) - perma_el - 1
    mas[index_last], mas[index_max] = mas[index_max], mas[index_last]

    return mas
```

## Быстрая сортировка / Quick sort

```
Берем первые эллемент массива
Сортируем остальные по принципу (меньше, равны, больше)
Отедельно проделываем процедуру с каждой из "куч"
В результате получается отсортированный массива
```
```py
@str2int_before
def quick_sort(mas: list) -> list:
    less: list = []
    equal: list = []
    greater: list = []

    if len(mas) > 1:
        pivot: int = mas[0]
        for el in mas:
            if el < pivot:
                less.append(el)
            if el == pivot:
                equal.append(el)
            if el > pivot:
                greater.append(el)

        return quick_sort(less) + equal + quick_sort(greater)

    return mas
```

## Задача B8

##### Определить, имеется ли в массиве элемент, равный сумме:
##### Найбольший четный + наименьший нечетный

```py
def sum_max2_min1(mas: list) -> list:
    min_odd: int = 10**10
    max_even: int = - 1

    min_odd, max_even = find_max_even_min_odd(mas, min_odd, max_even)
    if ((min_odd + max_even) in mas) is True:
        print(f"""
               maximum even + minimum odd in massive!
               {max_even} + {min_odd} = {max_even + min_odd}
               """)
    else:
        print('maximum even + minimum odd not in massive!')

    return mas
```

## Задача С8

##### Найти чет-нечет / нечет-чет пары

```py
@str2int_before
def chered_odd(mas: list) -> list:
    count_odd_pairs: int = 0
    for i in range(len(mas) - 1):
        if mas[i] % 2 != mas[i + 1] % 2:
            count_odd_pairs += 1

    print(f'Found {count_odd_pairs} even_odd pairs')

    return mas
```

# Лаба #3

## Последовательный поиск
##### Просто перебираем эллементы в массиве
```py
@count_time
@str2int_before
def consistent_search(mas: list, find_el: int) -> int:
    return mas.index(find_el) + 1 if find_el in mas else -1
```

## Бинарный поиск

```
Берем эллемент посередине, допустим число которое мы ищем меньше
Тогда мы делим массив пополам, и берем левую часть
В этой часть находим опять эллемент в середине, и повторяем процедуру

В конце остается один эллемент, если и он не совпадает, в след шаге массив будет пустым, а low = high, значит вернет -1
```
```py
@count_time
@str2int_before
def binary_search(mas: list, find_el: int) -> int:
    mas: list = sorted(mas)
    low: int = 0
    mid: int = 0
    high: int = len(mas) - 1

    while low < high:
        mid: int = (low + high) // 2
        if mas[mid] < find_el:
            low: int = mid

        if mas[mid] == find_el:
            return mid + 1

        if mas[mid] > find_el:
            high: int = mid

    return - 1
```

## Поиск фибоначчи

```
В отсортированном массиве ищем между какими числами (индексами) фибоначчи находится наше число

Когда мы нашли этот отрезок, опять нумеруем эллементы (их индексы) через числа фибонначи

В конце такого цикла у нас останется два или одно число, проверяем их на совпадение с нашим искомым эллементом
```

```py
@str2int_before
def fibonacci_search(mas: list, find_el: int, total_index=0) -> int:
    mas: list = sorted(mas)
    fib_index_1: int = 1
    fib_index_2: int = 1

    while fib_index_2 <= len(mas) - 1 and mas[fib_index_2] <= find_el:
        # For example
        # 1 + 1 = 2; 1 + 2 = 3
        # 2 + 3 = 5; 3 + 5 = 8
        fib_index_1 += fib_index_2
        fib_index_2 += fib_index_1

        # Heres might be 4 els in mas, but 2 + 3 = 5
        # So fib_index_2 = 5, whichs > len(mas)
        if fib_index_2 > len(mas):
            fib_index_1: int = fib_index_2 - fib_index_1
            fib_index_2: int = len(mas)
            break

    # Now find_el <= fib_i_2

    while fib_index_1 > len(mas) - 1 or mas[fib_index_1] > find_el:
        """
        fib n'th and fib (n + 1)'th
        to >>>
        fib (n - 1)'th and fib n'th
        """
        type_var: int = fib_index_2
        fib_index_2: int = fib_index_1
        fib_index_1: int = type_var - fib_index_1

    # Now fib_i_1 <= find_el <= fib_i_2
    # Heres might be diff fib_i_2 than in prev while
    new_mas: list = []
    # Cutting new mas
    for i in range(fib_index_1, fib_index_2):
        new_mas.append(mas[i])

    # Checking the corners
    if fib_index_1 == fib_index_2 or fib_index_1 == 0:
        if mas[0] == find_el:
            return total_index + fib_index_1 + 1
        if mas[-1] == find_el:
            return total_index + fib_index_1 + 2
            
        return -1

    return fibonacci_search(new_mas, find_el, total_index + fib_index_1)
```

## Интерполяционный поиск

```py
@count_time
@str2int_before
def interpolation_search(mas: list, find_el: int) -> int:
    mas: list = sorted(mas)
    l: int = 0
    r: int = len(mas) - 1

    # If mas[0] == mas[-1] means that whole mas contains same el
    if mas[0] == mas[-1]:
        return 0

    while mas[l] <= find_el <= mas[r]:
        mid: int = l + int((find_el - mas[l]) / (mas[r] - mas[l]) * (r - l))

        if find_el < mas[mid]:
            r: int = mid - 1

        if find_el == mas[mid]:
            return mid + 1

        if find_el > mas[mid]:
            l: int = mid - 1

    return - 1
```

## Задание B8
```
Найти минимальное симметричное число, и перевернуть все числа с длиной равной три
```
```py
@negative_positive_logic
@str2int_before
def laba_3_b8(mas: list) -> list:
    max_num: int = 10 ** 10
    max_num = min([number for number in mas if symmetrical_number(number) is True and max_num > number > 100])

    print('0 symmetrical numbers have found' if max_num == 10 ** 10 else f'{max_num} is the lowest symmetrical number')

    for i in range(len(mas)):
        if len(str(mas[i])) == 3:
            mas[i]: int = reverse_number(mas[i])

    return mas
```
##### Нахождеие симметричного числа
```py
def symmetrical_number(number: int) -> bool:
    digits_of_num: list = [int(i) for i in str(abs(number))]

    for i in range(len(digits_of_num) // 2):
        if digits_of_num[i] != digits_of_num[len(digits_of_num) - 1 - i]:
            return False
```
##### Переворт числа
```py
def reverse_number(number: int) -> int:
    digits_of_num: list = [int(i) for i in str(abs(number))]
    reversed_number: int = sum([digits_of_num[i] * (10 ** i) for i in range(len(digits_of_num))])

    return reversed_number
```

## Задание C5
```
Удалить из массива все простые числа без цифры пять
Отсортировать все нечетные числа, при этом не трогая четные
```
```py
@negative_positive_logic
@str2int_before
def laba_3_c5(mas: list) -> list:
    # Removing prime numbers which doesnt contain digit 5
    mas: list = [i for i in mas if not(check_contain_5(mas[i]) is False and prime_number(mas[i]) is True)]

    odd_els: list = [number for number in mas if number % 2 != 0]

    odd_els: list = sorted(odd_els)
    print(odd_els)
    for i in range(len(mas)):
        if mas[i] % 2 == 1:
            mas[i]: int = odd_els[0]
            odd_els.pop(0)

    return mas
```