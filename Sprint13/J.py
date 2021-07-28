# 52114961
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


class LinkedListQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        return self.head.value

    def get(self):
        if self.size == 0:
            return 'error'
        result = self.head.value
        self.head = self.head.next
        self.size -= 1
        return result

    def put(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self.head


def list_queue(number_commands, commands):
    queue = LinkedListQueue()
    for number in range(number_commands):
        if 'put' in commands[number]:
            queue.put(int(commands[number][1]))
        elif 'get' in commands[number]:
            print(queue.get())
        elif 'size' in commands[number]:
            print(queue.size)


if __name__ == '__main__':
    number_commands = int(input())
    commands = []
    for i in range(number_commands):
        row = input().split()
        commands.append(row)
    list_queue(number_commands, commands)
