# Лаба #1
## Задание А8
### Найти минимальный / максимальный элемент. Средне-арифмитическое

##### Средне-арифмитическое. Складываем все эллементы и делим на кол-во
```py
def mean_arif(mas: list) -> list:
    el_sum = 0
    for i in range(len(mas)):
        el_sum += int(mas[i])

    arif_sum = el_sum / len(mas)
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
def chered_checker(number: int, num_len: int) -> str:
    for i in range(num_len - 1):
        if number % 2 == (number // 10) % 2:
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
def chered_checker(number: int, num_len: int) -> str:
    for i in range(num_len - 1):
        if number % 10 == (number // 10) % 10:
            return '0'
        number //= 10
    return '1'
```

##### Посмотрим, равны ли две соседние цифры, после чего выведим `11: подоходит` `00: не подходит`
```py
def chered_checker(number: int, num_len: int) -> str:
    for i in range(num_len - 1):
        if number % 10 == (number // 10) % 10:
            return '0'
        number //= 10
    return '1'
```

##### Находим максимальную последовательность `11` и `00` в массиве с результатами
```py
def consecutive_result(mas_len: int, result_mas: list) -> list:
    count = 1

    res1 = 0
    res0 = 0

    for i in range(mas_len - 1):
        if result_mas[i] == result_mas[i + 1] and result_mas[i] == '1':
            count += 1
        else:
            res1 = max(res1, count)
            count = 1

    count = 1

    for i in range(mas_len - 1):
        if result_mas[i] == result_mas[i + 1] and result_mas[i] == '0':
            count += 1
        else:
            res0 = max(res0, count)
            count = 1

    return res1, res0
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
def selection_sort(mas: list) -> list:
    perma_el = 0
    for _ in range(len(mas)):
        max_el = mas[0]
        for i in range(len(mas) - perma_el):
            if mas[i] > max_el:
                max_el = mas[i]
                index_el = i

        mas = swap_el(index_el, perma_el, mas)
        perma_el += 1

    return mas
```
##### Swap_el меняет местами элементы

```py
def swap_el(index_max: int, perma_el: int, mas: list) -> list:
    index_last = len(mas) - perma_el - 1
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
def quick_sort(mas: list) -> list:
    less = []
    equal = []
    greater = []

    if len(mas) > 1:
        pivot = mas[0]
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
    min_odd = 10**10
    max_even = - 1

    for el in mas:
        if el % 2 == 0 and el > max_even:
            max_even = el
        if el % 2 != 0 and el < min_odd:
            min_odd = el

    if ((min_odd + max_even) in mas) is True:
        print(f'maximum even + minimum odd in massive!\n'
              f'{max_even} + {min_odd} = {max_even + min_odd}')
    else:
        print('maximum even + minimum odd not in massive!')
    return mas
```

## Задача С8

##### Найти чет-нечет / нечет-чет пары

```py
def chered_odd(mas: list) -> list:
    """
    pair - x'th and (x + 1)'th
    x'th % 2 != (x + 1)'th % 2 => count += 1
    so, even_odd or odd_even += 1
    """
    count_odd_pairs = 0
    for i in range(len(mas) - 1):
        if mas[i] % 2 != mas[i + 1] % 2:
            count_odd_pairs += 1

    print(f'Found {count_odd_pairs} even_odd pairs')

    return mas
```