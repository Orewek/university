import os
import ctypes
from make_postfix import infix_to_postfix


def remove_last_line(lines_amount: int) -> None:
    i = 1
    with open(r".\txts\temp.txt", "r") as f:
        with open(r".\txts\infix.txt", "w") as s:
            for line in f:
                if i != lines_amount:
                    s.write(line)
                i += 1

    os.remove(r"txts\temp.txt")


def main() -> None:
    parser_infix = ctypes.WinDLL(r".\dll\parser_infix.dll")
    print("PARSER_INFIX WAS SUCCESSFULLY LOADED")
    
    parser_postfix = ctypes.WinDLL(r".\dll\parser_postfix.dll")
    print("PARSER_POSTFIX WAS SUCCESSFULLY LOADED")

    our_string = str(input())
    our_string_utf = our_string.encode('utf-8')
    parser_infix.parse.arguments = [ctypes.c_char_p]
    lines_amount = parser_infix.parse(our_string_utf)
    remove_last_line(lines_amount)

    postfix = infix_to_postfix()
    print(postfix)
    postfix_utf = postfix.encode('utf-8')
    parser_postfix.parse.arguments = [ctypes.c_char_p]

    new_lines_amount = parser_postfix.parse(postfix_utf)
    print(f'\n {new_lines_amount}')





if __name__ == '__main__':
    main()
