class LinkNode:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class LinkListOperation:
    def __init__(self):
        self.initial = None

    def _insert(self, current, value):
        if current.next is not None:
            self._insert(current.next, value)
        else:
            current.next = LinkNode(value)
            current.next.prev = current

    def insert(self, value):
        length = len(value)
        if self.initial is None:
            self.initial = LinkNode(value[0])
        for x in range(1, length):
            self._insert(self.initial, value[x])

    def _display(self, current):
        print(current.value)
        if current.next is not None:
            self._display(current.next)

    def display(self):
        if self.initial is None:
            return None
        self._display(self.initial)

node = LinkListOperation()
node.insert([1, 5, 3, 4, 6, 9])
node.display()