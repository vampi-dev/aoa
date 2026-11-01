class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    """Visit left subtree, node, then right subtree."""
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(inorder(root))
