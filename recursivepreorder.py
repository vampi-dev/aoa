class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    """Visit node, left subtree, then right subtree."""
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(preorder(root))
