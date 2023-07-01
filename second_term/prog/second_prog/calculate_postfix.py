from make_postfix import infix_to_postfix


def eval_postfix(text: list) -> float:
    """ calculating math expression """
    stack = list()
    for symbol in text:
        symbol = symbol.strip()

        if symbol == " ":
            continue

        if symbol in '0123456789':
            stack.append(int(symbol))

        elif len(stack) != 0:
            plus = elementary_calc(symbol, stack)

            stack.append(plus)

    return stack.pop()


if __name__ == '__main__':
    print("You cant run this file as main")


def elementary_calc(operand: str, stack: list) -> int:
    """ making an elementary math calculations """
    if operand == "+":
        plus = stack.pop() + stack.pop()
    elif operand == "-":
        num1 = stack.pop()
        num2 = stack.pop()
        plus = num2 - num1
    elif operand == "*":
        plus = stack.pop() * stack.pop()
    elif operand == "/":
        num1 = stack.pop()
        num2 = stack.pop()
        plus = num2 / num1

    return plus
