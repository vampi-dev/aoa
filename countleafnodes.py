class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(count_leaf_nodes(root))
