import ctypes
import os


from calculate_postfix import eval_postfix

from make_postfix import infix_to_postfix


def change_file_name(lines_amount: int, file_name: str) -> None:
    with open(r'.\txts\temp.txt', 'r') as tm:
        with open(rf'.\txts\{file_name}.txt', 'w') as fp:
            lines = tm.readlines()

            for line in lines:
                fp.write(line)

    os.remove(r'.\txts\temp.txt')


def main() -> None:
    parser = ctypes.WinDLL(r".\dll\parser.dll")
    print("PARSER_INFIX WAS SUCCESSFULLY LOADED")

    our_string = str(input())
    our_string_utf = our_string.encode('utf-8')

    parser.parse.arguments = [ctypes.c_char_p]
    lines_amount = parser.parse(our_string_utf)
    change_file_name(lines_amount, "infix")

    postfix = infix_to_postfix()

    postfix_utf = postfix.encode('utf-8')
    parser.parse.arguments = [ctypes.c_char_p]

    new_lines_amount = parser.parse(postfix_utf)
    change_file_name(new_lines_amount, "postfix")

    with open(r".\txts\postfix.txt", "r") as f:
        lines = f.readlines()
        eval_postfix(lines)


if __name__ == '__main__':
    main()
