class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

ml = DLList()
ml.add(100)
ml.add(200)
ml.add(500)
ml.add(600)
print(ml.size)
print(ml)