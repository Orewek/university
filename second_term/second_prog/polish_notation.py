import os
from ctypes import WinDLL


def remove_last_line(lines_amount: int) -> None:
    i = 1
    with open("temp.txt", "r") as f:
        with open("stack.txt", "w") as s:
            for line in f:
                if i != lines_amount:
                    s.write(line)
                i += 1

    os.remove("temp.txt")


def main() -> None:
    parser = WinDLL(r".\dll\parser.dll")
    print("PARSER WAS SUCCESSFULLY LOADED")

    lines_amount = parser.parse()
    remove_last_line(lines_amount)


if __name__ == '__main__':
    main()
