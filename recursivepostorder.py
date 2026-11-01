class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(root):
    """Visit left subtree, right subtree, then node."""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(postorder(root))
