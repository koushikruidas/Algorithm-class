class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    # global root
    def __init__(self, value):
        self.root = Node(value)


def insert(tree, value):
    current = tree
    if current.value > value:
        if current.left is not None:
            insert(current.left, value)
        else:
            current.left = Node(value)
    else:
        if current.right is not None:
            insert(current.right, value)
        else:
            current.right = Node(value)


def print_inorder_tree(tree):
    current = tree
    if current.left is not None:
        print_inorder_tree(current.left)

    print(current.value)

    if current.right is not None:
        print_inorder_tree(current.right)


def print_preorder(tree):
    current = tree
    print(current.value)
    if current.left is not None:
        print_preorder(current.left)

    if current.right is not None:
        print_preorder(current.right)


myBst = BST(4)
# print(myBst.print())

# myBst.insert()
arr = [5, 3, 6, 9, 7, 2, 1]
for x in range(len(arr)):
    insert(myBst.root, arr[x])

print_inorder_tree(myBst.root)
print("---------")
print_preorder(myBst.root)
a = arr
