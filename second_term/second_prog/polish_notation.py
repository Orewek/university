import os
import ctypes
from make_postfix import infix_to_postfix


def remove_last_line(lines_amount: int, file_name: str, delete: int) -> None:
    with open(r".\txts\temp.txt", "r") as f:
        with open(rf".\txts\{file_name}.txt", "w") as s:
            for line in f:
                s.write(line)
    os.rename(r)
    os.remove(r"txts\temp.txt")


def main() -> None:
    parser_infix = ctypes.WinDLL(r".\dll\parser_infix.dll")
    print("PARSER_INFIX WAS SUCCESSFULLY LOADED")

    our_string = str(input())
    our_string_utf = our_string.encode('utf-8')

    parser_infix.parse.arguments = [ctypes.c_char_p]
    lines_amount = parser_infix.parse(our_string_utf)
    remove_last_line(lines_amount, "infix", 0)

    postfix = infix_to_postfix()
    print(postfix)

    postfix_utf = postfix.encode('utf-8')
    parser_infix.parse.arguments = [ctypes.c_char_p]

    new_lines_amount = parser_infix.parse(postfix_utf)
    remove_last_line(new_lines_amount, "postfix", 1)
    print(f'\n {new_lines_amount}')


if __name__ == '__main__':
    main()
