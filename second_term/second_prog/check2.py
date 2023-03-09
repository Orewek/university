def infix_to_postfix() -> str:
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    prio = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    expression = ''
    with open("stack.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            expression += f' {line.strip()}'

    expression = expression.strip()

    print(f'expression: {expression}')
    stack = []
    output = ''
    for char in expression:
        if char not in operators:
            output += char

        elif char == '(':
            stack.append('(')

        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prio[char] <= prio[stack[-1]]:
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()

    return output


def main() -> None:
    print('postfix notation: ', infix_to_postfix())


if __name__ == '__main__':
    main()
