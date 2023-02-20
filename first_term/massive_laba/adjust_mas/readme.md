## Работа с массивом
#### Есть несколько типов в данном блоке
* Узнать длину, кол-во элементов
* Поменять некоторые элементы в массиве
* Полностью очистить массив

### Поменять массив
##### Сначала мы показываем пользователю занумерованные элементы массива
###### Нумеруем их с единицы, то есть `i + 1`
```py
def show_elements(mas: tuple):
    for count, ma in enumerate(mas):
        print(f'{count + 1}: {ma}')
```
##### После позователь записывает построчно индексы элементов, которые надо поменять
```py
def change_elements(mas: tuple, change_mas: tuple) -> tuple:
    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')

            replace_cell = input()
            mas[i] = replace_cell
    return mas
```
##### Очистить массив и узнать его длину
```py
def clear_mas(mas: tuple) -> tuple:
    mas = []
    return mas


def len_mas(mas: tuple) -> str:
    ans = f'{len(mas)} - length of massive'
    return ans
```