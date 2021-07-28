# 52098657
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("error")
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return None
        else:
            return max(self.items)


def stack_max(number_commands, commands):
    stack = Stack()
    number = 0
    for number in range(number_commands):
        if 'push' in commands[number]:
            stack.push(int(commands[number][1]))
        elif 'pop' in commands[number]:
            stack.pop()
        elif 'get_max' in commands[number]:
            print(stack.get_max())


if __name__ == '__main__':
    number_commands = int(input())
    commands = []
    for i in range(number_commands):
        row = input().split()
        commands.append(row)
    stack_max(number_commands, commands)
