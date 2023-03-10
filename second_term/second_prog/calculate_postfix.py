from make_postfix import infix_to_postfix


def eval_postfix(text):
    stack = list()
    for symbol in text:
        print(f'input symbol: "{symbol}"')

        if symbol == " ":
            continue 
        if symbol in '0123456789':
            print(f'symbol: {symbol}')
            stack.append(int(symbol))

        elif len(stack) != 0:
            plus = None
            print("here in stack calc")
            if symbol == "+":
                plus = stack.pop() + stack.pop()
            elif symbol == "-":
                plus = stack.pop() - stack.pop()
            elif symbol == "*":
                plus = stack.pop() * stack.pop()
            elif symbol == "/":
                plus = stack.pop() / stack.pop()

            if plus is not None:
                stack.append(plus)
                print("append in stack", plus)
            else:
                raise Exception(f'unknown value "{symbol}"')
    return stack.pop()


if __name__ == '__main__':
    text = infix_to_postfix()
    print(f'text: {text}')
    result = eval_postfix(text)
    print(result)
