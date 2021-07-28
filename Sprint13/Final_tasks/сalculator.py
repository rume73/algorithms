# 52132660
import operator


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()


def division(first, second):
    if second != 0:
        return first // second


def operator_choose(symbol, first, second):
    return {'+': operator.add(first, second),
            '-': operator.sub(first, second),
            '*': operator.mul(first, second),
            '/': division(first, second),
            }.get(symbol)


def calculator(expression):
    expression = list(expression)
    for commands in expression:
        if (commands != '+' and commands != '-' and commands != '/'
                and commands != '*'):
            stack.push(int(commands))
        else:
            second_operand = int(stack.pop())
            first_operand = int(stack.peek())
            symbol = commands
            stack.items[-1] = operator_choose(symbol,
                                              first_operand,
                                              second_operand)
    return stack.peek()


if __name__ == '__main__':
    stack = Stack()
    print(calculator(input().split()))
