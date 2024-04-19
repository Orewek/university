from typing import List

from input_string.input_logic import input_generate

from typing import reduce


def task_b9(user_str: str) -> str:
    words: List[str] = [input_generate(user_str, 20) for _ in range(10)]
    print(words)

    one_digit_words: list[str] = []
    for i in range(len(words)):
        if sum(letter.isdigit() for letter in words[i]) == 1:
            one_digit_words.append(remove_arifmetical(words[i]))
    print(f'Words with 1 digit w/o arifmetical letters: {one_digit_words}\n')

    same_letter_count: int = 0
    for i in range(len(words)):
        if words[i] is True:
            same_letter_count += 1

    print(f'{same_letter_count} words with same letter had found!\n')

    return user_str


def remove_arifmetical(word: str) -> str:
    """ removing arifmetical letters """
    arif_mas: list = ['-', '*', '+', '/']
    new_word: str = ''.join([letter for letter in word if letter not in arif_mas])

    return new_word


def same_letters(word: str) -> bool:
    letters_mas: list = []
    for i in range(len(word)):
        if word[i] not in letters_mas:
            letters_mas.append(word[i])
        else:
            return True

    return False


if __name__ == '__main__':
    print('You cant run this file as main')
