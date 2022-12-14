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
    """
    Checking, might be that find_el contains same letters
    for example in "apple" heres 2 'p'
    """
    status = {el: [0 for _ in range(len(find_el))] for el in set(find_el)}
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
    status = set_status(find_el)
    key_set = set(status.keys())
    match = []
    # Havent found good name for var j
    j = 0
    for i in range(len(user_str)):
        j = status[user_str[i]][j] if user_str[i] in key_set else 0
        if j == len(find_el):
            match.append(i - len(find_el) + 1)
            j = 0
    return match
```

### Метод Бойера-Мура

``` Все пояснения в коде ```

```py
def letters_jump(user_str: str, find_el: str) -> list:
    """
    numeric each letter in find_el (in reversed find_el)
    vpo -> [[o, 0], [p, 1], [v, 2]]
    rest letters in ASCII will have [letter, len(find_el)]
    """
    # creating this [letter, len(find_el)]
    prefix = [[i, len(find_el)] for i in range(255)]
    # numeric this vpo
    find_el_index = [[ord(find_el[::-1][i]), i] for i in range(len(find_el))]

    # if letter was before, it must have same index as last one
    find_el_index = same_letters_find_el(find_el_index)
    # replacing this vpo stuff into prefix
    # so, for vpo [v, len(find_el)] ([v, 3]) => [v, 2]
    for i in range(len(find_el_index)):
        prefix[find_el_index[i][0]][1] = find_el_index[i][1]

    return prefix
```
```py
def same_letters_find_el(find_el_index: list) -> list:
    """
    [p, 1] -> separating [i][j] to 2 diff lists
    if we found p and its already in our list[i]
    we should take his el from list[j] (so here j == i)
    so our [p, 4] must change to [p, 1] in total
    """
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
    """
    by this prefix we will make jump
    lets say that [user_str = 'asdkjvpoijqvpoqego[qf', find_el = 'vpo']
    in prefix [a, 3], so we go from index 0 to index 3 in user_str
    same for [k, 3] to 6
    user_str[6] is p, which is [p, 1] in prefix, so go to 7
    in prefix [o, 0] so we check, does {
      user_str[user_str_index - len(find_el) + 1: user_str_index + 1] == find_el
    }
    after we decide does that equal, we make += len(find_el)
    and like that to the end
    """
    # making this prefix
    prefix = letters_jump(user_str, find_el)
    user_str_index = 0
    result: List[int] = []
    # by user_str_index we will make a jump
    while user_str_index <= len(user_str):
        if prefix[ord(user_str[user_str_index])][1] != 0:
            # Adding this for jump
            user_str_index += prefix[ord(user_str[user_str_index])][1]
        else:
            # Here our jump equal to 0
            if user_str[user_str_index - len(find_el) + 1: user_str_index + 1] == find_el:
                result.append(user_str_index - len(find_el) + 1)
            user_str_index += len(find_el)

    return result
```
