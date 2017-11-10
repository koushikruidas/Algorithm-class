class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return str(self.value)


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
                current.left.parent = current
        if current.value <= value:
            if current.right is None:
                current.right = Node(value)
                current.right.parent = current
            else:
                self._insert(current.right, value)
        BST.update_height(current)

    def _print(self, tree):
        current = tree
        if current.left is not None:
            self._print(current.left)
        print(current.value)

        if current.right is not None:
            self._print(current.right)

    def _find(self, current, value):
        if current.value > value:
            if current.left is not None:
                if current.left.value == value:
                    return current.left
                else:
                    self._find(current.left, value)
            else:
                return None
        elif current.value < value:
            if current.right is not None:
                if current.right.value == value:
                    return current.right
                else:
                    self._find(current.right, value)
            else:
                return None
        elif current.value == value:
            return current

    def delete(self, value):
        deleting_node = self.find(value)
        current_node = deleting_node
        if current_node is not None:
            if current_node.right is not None:
                current_node = current_node.right
                while current_node.left is not None:
                    current_node = current_node.left
                deleting_node.value = current_node.value
                current_node = None
            else:
                current_node is None

    def insert(self, value):
        self._insert(self.root, value)

    def print(self):
        self._print(self.root)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(self.root, value)

    @staticmethod
    def update_height(current):
        if current.left is None:
            current.height = 1 + current.right.height
        elif current.right is None:
            current.height = 1 + current.left.height
        else:
            current.height = 1 + max(current.left.height, current.right.height)



myBST1 = BST([2,5,3,4,2,1,14,7,1])
# myBST1.print()
print(myBST1.find(2))
print("kou")