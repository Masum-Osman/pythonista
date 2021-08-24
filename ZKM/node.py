class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DoubleLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.size = 0
