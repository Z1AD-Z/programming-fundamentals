class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        self.head = Node(value, self.head)

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result

def main():
    ll = LinkedList()
    ll.insert_front(3)
    ll.insert_front(2)
    ll.insert_front(1)
    print("linked list:", ll.to_list())

if __name__ == "__main__":
    main()
