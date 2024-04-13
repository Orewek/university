# Задаем массив

```
Пользователь вводит строчку с клавиатуры
```
```py
def input_manually(user_str: str) -> str:
    add_letters: str = input()
    user_str += add_letters

    return user_str
```

```
Строка генерируется автоматически

На вход кол-во эллементов, которые должны быть в строчке
Берется число через рандом, преобразуется в эллемент через ord()
```
```py
def input_generate(user_str: str, amount_of_els: int) -> str:
    # itertools.chain(range(65, 91), range(97, 123))
    add_letters: str = ''
    for _ in range(amount_of_els):
        new_letter_code: int = randint(65, 122 + 1)

        while 92 <= new_letter_code <= 96:
            new_letter_code: int = randint(65, 122 + 1)

        add_letters += chr(new_letter_code)
    user_str += add_letters
    return user_str
```