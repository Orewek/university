## Работа с массивом
#### Есть несколько типов в данном блоке
* Узнать длину, кол-во элементов
* Поменять некоторые элементы в массиве
* Полностью очистить массив

### Поменять массив
##### Сначала мы показываем пользователю занумерованные элементы массива
###### Нумеруем их с единицы, то есть `i + 1`
```py
def show_elements(mas: list) -> list:
    print(*[f'{count + 1}: {item}' for count, item in enumerate(mas)], sep='\n')
```
##### После позователь записывает построчно индексы элементов, которые надо поменять
```py
def change_elements(mas: list, change_mas: list) -> list:
    for i in range(len(mas)):
        if i in change_mas:
            print(f'{i + 1}: {mas[i]}. Type new element for this cell')

            replace_cell: str = check_int(input())
            mas[i]: int = replace_cell
    return mas
```
##### Очистить массив и узнать его длину
```py
def clear_mas(mas: list) -> list:
    mas.clear()
    return mas


def len_mas(mas: list) -> str:
    ans: str = f'{len(mas)} - length of massive'
    return ans
```