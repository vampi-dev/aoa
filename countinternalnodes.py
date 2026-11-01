class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_internal_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(count_internal_nodes(root))
