## Ввод массива 

### Есть два способа
* Вручную
* Сгенерировать рандомно

##### Пользователь вводит поэлементно
```py
def add_elements(mas: tuple) -> tuple:
    el_mas = input()
    while el_mas != '':
        if el_mas.isdigit() is True:
            mas.append(el_mas)
        el_mas = input()

    return mas
```

##### Работает генератор
```py
def generate_el(mas: tuple, amount_elements: int) -> tuple:
    for _ in range(amount_elements):
        number = randint(-1000, 1000)
        mas.append(number)

    return mas
```