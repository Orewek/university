import os
from collections import Counter
from heapq import heapify, heappop, heappush
from io import StringIO
from string import hexdigits


def input_file_path(file_path: str) -> str:
    """ input a path to .csv and check on validation """
    file_path: None = None
    print('Choose file')

    while file_path is None:
        file_path: str = str(input())

        try:
            with open(file_path, 'r'):
                pass
        except:
            print('Cannot open a file on this destination')
            file_path: None = None

    return file_path


def show_file_content(file_path: str) -> str:
    with open(file_path, 'r') as f:
        print(f.read())

    return file_path


def count_letters_occurence(file_path: str) -> str:
    string: str = ''
    with open(file_path, 'r') as f:
        string += f.read()

    freq: dict = {}
    for letter in set(string):
        freq[letter]: int = string.count(letter)

    sorted_freq: dict = {key: value for key, value in sorted(freq.items(), key=lambda item: item[1])}
    print(sorted_freq)
    return file_path


def show_code_table_const(file_path: str) -> str:
    string: str = ''
    with open(file_path, 'r') as f:
        string += f.read()

    for letter in set(string):
        print(letter, bin(ord(letter))[2:])

    return file_path


def compress_constant(file_path: str) -> str:
    string: str = ''
    with open(file_path, 'r') as f:
        string += f.read()

    bin_string: bin = str.encode(string)

    with open('constant_len.bin', 'wb') as new_f:
        new_f.write(bin_string)

    return file_path


def compare_sizes(file_path: str) -> str:
    default_size = os.stat('code.txt').st_size
    const_size = os.stat('constant_len.bin').st_size
    huffman_size = os.stat('huffman_len.bin').st_size

    print(f"""
           default: {default_size}
           constant: {const_size}
           huffman: {huffman_size}
           """)
    return file_path


class Node:
    """
    showing list of elements in freq first, unicode code in secondly
    """

    def __init__(self, letter=None, freq=0, children=None):
        self.letter = letter
        self.freq = freq
        self.children = children or []

    def tuple(self):
        return (self.freq, ord(self.letter) if self.letter else -1)

    def __lt__(self, other):
        return self.tuple() < other.tuple()

    def __eq__(self, other):
        return self.tuple() == other.tuple()


def encoding_table(node, code=''):
    """
    making a tree
    """

    if node.letter is None:
        mapping: dict = {}
        for child, digit in zip(node.children, hexdigits):
            mapping.update(encoding_table(child, code + digit))
        return mapping
    else:
        return {node.letter: code}


def huffman_encode_code(text: str) -> str:
    """ param text to encode return: (tree, binary str) """
    text: str = ''
    with open(file_path, 'r') as f:
        text += f.read()

    nodes: list = [Node(letter, freq) for letter, freq in Counter(text).items()]
    heapify(nodes)

    # Строит n-арное дерево
    while len(nodes) > 1:
        list_children: list = [heappop(nodes) for _ in range(2)]
        freq: int = sum([node.freq for node in list_children])

        node = Node(None, freq)
        node.children = list_children

        heappush(nodes, node)

    root = nodes[0]
    codes = encoding_table(root)
    print(codes)
    return file_path


def huffman_encode_compress(text: str) -> str:
    """ param text to encode return: (tree, binary str) """
    text: str = ''
    with open(file_path, 'r') as f:
        text += f.read()

    nodes: list = [Node(letter, freq) for letter, freq in Counter(text).items()]
    heapify(nodes)

    # Строит n-арное дерево
    while len(nodes) > 1:
        list_children = [heappop(nodes) for _ in range(2)]
        freq: int = sum([node.freq for node in list_children])

        node = Node(None, freq)
        node.children = list_children

        heappush(nodes, node)

    root = nodes[0]
    codes = encoding_table(root)
    res: str = ''.join([codes[letter] for letter in text])
    print(res)

    with open('huffman_len.bin', 'wb') as f:
        sio = StringIO(res)
        while 1:
            # Grab the next 8 bits
            b: str = sio.read(8)
            # Bail if we hit EOF
            if not b:
                break
            # If we got fewer than 8 bits, pad with zeroes on the right
            if len(b) < 8:
                b: str = f'{b}{'0' * (8 - len(b))}'
            # Convert to int
            i: int = int(b, 2)
            # Write
            f.write(i.to_bytes(1, byteorder='big'))

    return file_path


def main_menu(file_path: str, action: int) -> str:
    switcher: dict = {
        1: input_file_path,
        2: show_file_content,
        3: count_letters_occurence,
        4: show_code_table_const,
        5: huffman_encode_code,
        6: compress_constant,
        7: huffman_encode_compress,
        8: compare_sizes,
    }
    file_path = switcher[action](file_path)

    return file_path


def main(file_path: str) -> str:
    table: str = """
            1: read a file
            2: show file content
            3: show letters occurrence frequency
            4: show code table for const
            5: show code table for huffman
            6: compress file by constant length
            7: compress file by Huffman code
            8: compare sizes
            """

    action_table: str = """
                   U can write only one digit.
                   After operation u can continue working with massive
                   write -table to see the options
                   """
    action: str = input(table)

    while action.isdigit is False or (not (1 <= int(action) <= 8)):
        if action != '-table':
            print(action_table)
        else:
            print(table)

        action: str = input()

    file_path = main_menu(file_path, int(action))
    return file_path


if __name__ == '__main__':
    file_path = None
    while True:
        file_path = main(file_path)
