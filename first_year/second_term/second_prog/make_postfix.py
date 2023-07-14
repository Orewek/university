def infix_to_postfix() -> str:
    """ making a string with postfix expression """
    expression = read_expression()
    print(f'expression: {expression}')

    stack = []
    output = ''

    for char in expression:
        if char not in '+-*/()^':
            output += char

        elif char == '(':
            stack.append('(')

        elif char == ')':
            output = read_parenthesized_expression(stack, output)

        else:
            output = logical_postfix(stack, output, char)

    output = get_rest_stack(stack, output)

    return output


def read_expression() -> str:
    """ reading math expression from the file """
    expression = ''

    with open(r".\txts\infix.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            expression += f' {line.strip()}'

    return expression.strip()


def read_parenthesized_expression(stack: list, output: str) -> str:
    """ readling expression into () """
    while stack and stack[-1] != '(':
        output += stack.pop()
    stack.pop()

    return output


def get_rest_stack(stack: list, output: str) -> str:
    """ reading rest of the stack """
    while stack:
        output += stack.pop()

    return output


def logical_postfix(stack: list, output: str, char: str) -> str:
    """ reading stack with prio of operands """
    prio = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    while stack and stack[-1] != '(' and prio[char] <= prio[stack[-1]]:
        output += stack.pop()

    stack.append(char)

    return output


def main() -> None:
    print('postfix notation: ', infix_to_postfix())


if __name__ == '__main__':
    main()
