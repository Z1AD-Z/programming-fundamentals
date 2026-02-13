from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self):
        return len(self._data) == 0

def main():
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print("dequeue:", q.dequeue())
    print("dequeue:", q.dequeue())
    print("empty:", q.is_empty())

if __name__ == "__main__":
    main()
