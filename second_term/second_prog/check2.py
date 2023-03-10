def infix_to_postfix() -> str:
    operators = '+-*/()^'
    prio = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    expression = read_expression()
    print(f'expression: {expression}')
    stack = []
    output = ''
    for char in expression:
        if char not in operators:
            output += char

        elif char == '(':
            stack.append('(')

        elif char == ')':
            output = read_parenthesized_expression(stack, output)

        else:
            output = logical_postfix(stack, output, char, prio)

    output = get_rest_stack(stack, output)

    return output


def read_expression() -> str:
    expression = ''

    with open("stack.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            expression += f' {line.strip()}'

    return expression.strip()


def read_parenthesized_expression(stack: list, output: str) -> str:
    while stack and stack[-1] != '(':
        output += stack.pop()
    stack.pop()

    return output


def get_rest_stack(stack: list, output: str) -> str:
    while stack:
        output += stack.pop()

    return output


def logical_postfix(stack: list, output: str, char: str, prio: list) -> str:
    while stack and stack[-1] != '(' and prio[char] <= prio[stack[-1]]:
        output += stack.pop()

    stack.append(char)

    return output


def main() -> None:
    print('postfix notation: ', infix_to_postfix())


if __name__ == '__main__':
    main()
