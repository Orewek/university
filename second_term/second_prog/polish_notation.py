import ctypes
import os


from calculate_postfix import eval_postfix

from make_postfix import infix_to_postfix


def change_file_name(file_name: str) -> None:
    """ changing name from temp.txt to infix/postfix.txt """
    with open(r'.\txts\temp.txt', 'r') as tm:
        with open(rf'.\txts\{file_name}.txt', 'w') as fp:
            lines = tm.readlines()

            for line in lines:
                fp.write(line)

    os.remove(r'.\txts\temp.txt')


def calculace_expression() -> float:
    """ calucaling math expression """
    with open(r".\txts\postfix.txt", "r") as f:
        lines = f.readlines()
        result = eval_postfix(lines)

    return result


def main() -> None:
    # loading parser
    parser = ctypes.WinDLL(r".\dll\parser.dll")
    print("PARSER_INFIX WAS SUCCESSFULLY LOADED")

    # our math expression
    our_string = str(input())
    our_string_utf = our_string.encode('utf-8')

    # parsing math expression to infix
    parser.parse.arguments = [ctypes.c_char_p]
    parser.parse(our_string_utf)
    change_file_name("infix")

    # creating string with postfix
    postfix = infix_to_postfix()

    postfix_utf = postfix.encode('utf-8')
    parser.parse.arguments = [ctypes.c_char_p]

    # making additiona .txt file with potfix
    parser.parse(postfix_utf)
    change_file_name("postfix")

    result = calculace_expression()
    print(f"result: {result}")


if __name__ == '__main__':
    main()
