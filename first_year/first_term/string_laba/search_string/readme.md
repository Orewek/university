# Поиск подстроки в строке

### Последовательный поиск
```
Идем по строке, делаем срез на длину подстроки, смотри == ли
если не нашли выводим -1
```
```py
def consistent_search(user_str: str, find_str: str) -> int:
    for i in range(len(user_str) - len(find_str)):
        if user_str[i:i + len(find_str)] == find_str:
            return i + 1

    return - 1
```


### Поиск через метод Кнута-Морриса-Пратта
```
У нас есть подстрока, которую мы ищем - это наш префикс
Проходимся вдоль подстроки, и там ищем подстроку подстроки, а также одинаковые эл.
Возращаем лист эллементов, с вложенным листом для каждого эл.
```
```py
def set_status(find_el: str) -> dict:
    status: dict = {el: [0 for _ in range(len(find_el))] for el in set(find_el)}
    for i in range(len(find_el)):
        for j in range(i + 1):
            if find_el[i - j:i] == find_el[0:j]:
                status[find_el[j]][i] = j + 1
    return status
```
```
Делаем наш префикс
берем уникальные буквы из этого префикса
В соотвестивии с эллементами из префикса нумеруем эл. из строки
Так, где номер под эллементов == len(подстрока), там и есть наша подстрока (ее конец)
Возвращаем лист со всеми такими найдеными len(подстрока)
```
```py
def kmp_logic(user_str: str, find_el: str) -> list:
    status: dict = set_status(find_el)
    key_set = set(status.keys())
    match: list = []
    # Havent found good name for var j
    j: int = 0
    for i in range(len(user_str)):
        j: int = status[user_str[i]][j] if user_str[i] in key_set else 0
        if j == len(find_el):
            match.append(i - len(find_el) + 1)
            j: int = 0
    return match
```

### Метод Бойера-Мура

``` Все пояснения в коде ```

```py
def letters_jump(user_str: str, find_el: str) -> list:
    # creating this [letter, len(find_el)]
    prefix: list = [[i, len(find_el)] for i in range(255)]
    # numeric this vpo
    find_el_index: list = [[ord(find_el[::-1][i]), i] for i in range(len(find_el))]

    # if letter was before, it must have same index as last one
    find_el_index: list = same_letters_find_el(find_el_index)
    # replacing this vpo stuff into prefix
    # so, for vpo [v, len(find_el)] ([v, 3]) => [v, 2]
    for i in range(len(find_el_index)):
        prefix[find_el_index[i][0]][1] = find_el_index[i][1]

    return prefix
```
```py
def same_letters_find_el(find_el_index: list) -> list:
    total_letter: List[list] = []
    letters_ascii_letter: List[int] = []
    letters_word_jump: List[int] = []
    for i in range(len(find_el_index)):
        if find_el_index[i][0] not in letters_ascii_letter:
            letters_ascii_letter.append(find_el_index[i][0])
            letters_word_jump.append(find_el_index[i][1])
            total_letter.append([find_el_index[i][0], find_el_index[i][1]])
        else:
            for j in range(len(find_el_index)):
                if letters_ascii_letter[j] == find_el_index[i][0]:
                    total_letter.append([find_el_index[i][0], letters_word_jump[j]])
                    break

    return total_letter
```
```py
def boiera_mura_search(user_str: str, find_el: str) -> list:
    # making this prefix
    prefix: list = letters_jump(user_str, find_el)
    user_index: int = 0
    result: List[int] = []
    # by user_index we will make a jump
    while user_index < len(user_str):
        if prefix[ord(user_str[user_index])][1] != 0:
            # Adding this for jump
            user_index += prefix[ord(user_str[user_index])][1]
        else:
            # Here our jump equal to 0
            if user_str[user_index - len(find_el) + 1: user_index + 1] == find_el:
                result.append(user_index - len(find_el) + 1)
            user_index += len(find_el)

    return result
```
```py
def task_b9(user_str: str) -> str:
    words: List[str] = [input_generate(user_str, 20) for _ in range(10)]
    print(words)

    one_digit_words: list[str] = []
    for i in range(len(words)):
        if sum(letter.isdigit() for letter in words[i]) == 1:
            one_digit_words.append(remove_arifmetical(words[i]))
    print(f'Words with 1 digit w/o arifmetical letters: {one_digit_words}\n')

    same_letter_count: int = words.count(True)

    print(f'{same_letter_count} words with same letter had found!\n')

    return user_str

```
```py
def remove_arifmetical(word: str) -> str:
    arif_mas: list = ['-', '*', '+', '/']
    new_word: str = ''.join([letter for letter in word if letter not in arif_mas])

    return new_word

```
```py
def same_letters(word: str) -> bool:
    letters_mas: list = []
    for i in range(len(word)):
        if word[i] not in letters_mas:
            letters_mas.append(word[i])
        else:
            return True

    return False
```