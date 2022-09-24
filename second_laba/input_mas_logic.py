def add_elements(mas: tuple) -> tuple:
    """
    input: empty massive (at least it should be)
    adding each elements into it
    if user pressed Enter -> break
    """
    el_mas = input()
    while el_mas != '':
        mas.append(el_mas)
        el_mas = input()

    return mas