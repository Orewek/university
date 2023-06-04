import os

def input_file_path(file_path: str) -> str:
    """ input a path to .csv and check on validation """
    file_path = None
    print('Choose file')

    while file_path is None:
        file_path = str(input())

        try:
            with open(file_path, 'r'):
                pass
        except:
            print('Cannot open a file on this destination')
            file_path = None

    return file_path


def show_file_content(file_path: str) -> str:
    with open(file_path, 'r') as f:
        print(f.read())
    
    return file_path


def count_letters_occurence(file_path: str) -> str:
    string = ''
    with open(file_path, 'r') as f:
        string += f.read()

    freq = {}
    for letter in set(string):
        freq[letter] = string.count(letter)

    sorted_freq = {key: value for key, value in sorted(freq.items(), key=lambda item: item[1])}
    print(sorted_freq)
    return file_path


def show_code_table_const(file_path: str) -> str:
    string = ''
    with open(file_path, 'r') as f:
        string += f.read()

    for letter in set(string):
        print(letter, bin(ord(letter))[2:])

    return file_path


def show_code_huffman(file_path: str) -> str:
    return file_path


def compress_constant(file_path: str) -> str:
    string = ''
    with open(file_path, 'r') as f:
        string += f.read()

    bin_string = str.encode(string)

    with open(f'constant_len.bin', 'wb') as new_f:
        new_f.write(bin_string)

    return file_path


def compress_huffman(file_path: str) -> str:
    return file_path


def compare_sizes(file_path: str) -> str:
    default_size = os.stat('code.txt').st_size
    const_size = os.stat('constant_len.bin').st_size
    huffman_size = os.stat('huffman_len.bin').st_size

    print(f'default: {default_size}\n'
          f'constant: {const_size}\n'
          f'huffman: {huffman_size}')
    return file_path


def main_menu(file_path: str, action: int) -> str:
    switcher = {
        1: input_file_path,
        2: show_file_content,
        3: count_letters_occurence,
        4: show_code_table_const,
        5: show_code_huffman,
        6: compress_constant,
        7: compress_huffman,
        8: compare_sizes,
    }
    file_path = switcher[action](file_path)

    return file_path


def main(file_path: str) -> str:
    table = """
            1: read a file
            2: show file content
            3: show letters occurrence frequency
            4: show code table for const
            5: show code table for huffman
            6: compress file by constant length
            7: compress file by Huffman code
            8: compare sizes
            """

    action_table = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    print(table)
    action = input()

    while action.isdigit is False or (not (1 <= int(action) <= 8)):
        if action != '-table':
            print(action_table)
        else:
            print(table)

        action = input()

    file_path = main_menu(file_path, int(action))
    return file_path


if __name__ == '__main__':
    file_path = None
    while True:
        file_path = main(file_path)
