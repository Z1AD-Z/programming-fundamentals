class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

def main():
    s = Stack()
    s.push(10)
    s.push(20)
    print("peek:", s.peek())
    print("pop:", s.pop())
    print("pop:", s.pop())
    print("empty:", s.is_empty())

if __name__ == "__main__":
    main()
