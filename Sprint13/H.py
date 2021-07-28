# 52113132
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return (self.items[-1])


def is_correct_bracket_seq(brackets):
    stack = Stack()
    for i in brackets:
        if i in '([{':
            stack.push(i)
        else:
            try:
                first = stack.peek()
            except BaseException:
                return False
            if i == ')' and first == '(':
                stack.pop()
            elif i == ']' and first == '[':
                stack.pop()
            elif i == '}' and first == '{':
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
