def consistent_search(user_str: str, find_str: str) -> int:
    for i in range(len(user_str) - len(find_str)):
        if user_str[i:i + len(find_str)] == find_str:
            return i + 1

    return - 1


"""
def KnuthMorrisPratt(text, pattern):
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos
"""


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


if __name__ == '__main__':
    print('You cant run this file as main')
