## Ввод массива 

### Есть два способа
* Вручную
* Сгенерировать рандомно

##### Пользователь вводит поэлементно
```py
@str2int_after
def add_elements(mas: list) -> list:
    el_mas: str = input()
    while el_mas != '':
        if el_mas.isdigit() is True:
            mas.append(el_mas)
        el_mas: str = input()

    return mas
```

##### Работает генератор
```py
def generate_el(mas: list, amount_elements: int) -> list:
    for _ in range(amount_elements):
        mas = [randint(-1000, 1000) for _ in range(amount_elements)]

    return mas
```