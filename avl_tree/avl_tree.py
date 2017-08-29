class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        self.root = Node(value[0])
        n = len(value)
        for x in range(1, n):
            self.insert(value[x])

    def _insert(self, tree, value):
        current = tree
        if current.value > value:
            if current.left is not None:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        if current.value <= value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def _print(self, tree):
        current = tree
        if current.left is not None:
            self._print(current.left)
        print(current.value)

        if current.right is not None:
            self._print(current.right)

    def insert(self, value):
        self._insert(self.root, value)

    def print(self):
        self._print(self.root)

myBST1 = BST([2,5,3,4,2,1,14,7,1])
myBST1.print()

print("kou")