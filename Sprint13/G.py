# 52112542
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class StackMaxEffective(Stack):
    def __init__(self):
        super().__init__()
        self.max_item = Stack()

    def push(self, item):
        self.items.append(item)
        if self.max_item.isEmpty():
            self.max_item.push(item)
        elif self.max_item.peek() <= item:
            self.max_item.push(item)

    def pop(self):
        if self.isEmpty():
            return print("error")
        removed_item = self.items.pop()
        if removed_item == self.max_item.peek():
            self.max_item.pop()
        return removed_item

    def get_max(self):
        if self.isEmpty():
            return None
        return self.max_item.peek()


def stack_max_effective(number_commands, commands):
    for number in range(number_commands):
        if 'push' in commands[number]:
            stack.push(int(commands[number][1]))
        elif 'pop' in commands[number]:
            stack.pop()
        elif 'get_max' in commands[number]:
            print(stack.get_max())


if __name__ == '__main__':
    stack = StackMaxEffective()
    number_commands = int(input())
    commands = []
    for i in range(number_commands):
        row = input().split()
        commands.append(row)
    stack_max_effective(number_commands, commands)
