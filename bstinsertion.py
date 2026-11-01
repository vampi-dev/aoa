class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


if __name__ == "__main__":
    root = None
    for value in [5, 3, 7, 2, 4]:
        root = insert(root, value)
    print(inorder(root))
