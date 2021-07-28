# 52133283
class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def overflow(self):
        return self.size >= self.max_n

    def push_back(self, item):
        if self.overflow():
            raise OverfullError
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, item):
        if self.overflow():
            raise OverfullError
        if self.head == 0 and self.tail == 0:
            self.queue[self.head] = item
            self.tail = (self.tail + 1) % self.max_n
        elif self.head == 0 and self.tail == 1:
            self.head = self.max_n - 1
            self.queue[self.head] = item
        else:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = item
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise EmptyError
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise EmptyError
        if self.tail == 0:
            self.tail = self.max_n - 1
            item = self.queue[self.tail]
            self.queue[self.tail] = None
        else:
            self.tail = (self.tail - 1) % self.max_n
            item = self.queue[self.tail]
            self.queue[self.tail] = None
        self.size -= 1
        return item


class EmptyError(Exception):
    """Raised when deque is empty"""
    pass


class OverfullError(Exception):
    """Raised when deque is overfull"""
    pass


if __name__ == '__main__':
    number_commands = int(input())
    deque = Deque(int(input()))
    commands = [input() for _ in range(number_commands)]
    result = []
    for command in commands:
        function, *params = command.split()
        try:
            result = (getattr(deque, function)(*params))
            if result:
                print(result)
        except OverfullError:
            print('error')
        except EmptyError:
            print('error')
