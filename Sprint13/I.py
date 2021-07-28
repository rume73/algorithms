# 52113696
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def limited_queue(number_commands, max_size, commands):
    queue = Queue(max_size)
    for number in range(number_commands):
        if 'push' in commands[number]:
            queue.push(int(commands[number][1]))
        elif 'pop' in commands[number]:
            print(queue.pop())
        elif 'peek' in commands[number]:
            print(queue.peek())
        elif 'size' in commands[number]:
            print(queue.size)


if __name__ == '__main__':
    number_commands = int(input())
    max_size = int(input())
    commands = []
    for i in range(number_commands):
        row = input().split()
        commands.append(row)
    limited_queue(number_commands, max_size, commands)
