class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minimum_value(root):
    if root is None:
        raise ValueError("The tree is empty")
    values = [root.value]
    if root.left is not None:
        values.append(minimum_value(root.left))
    if root.right is not None:
        values.append(minimum_value(root.right))
    return min(values)


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    print(minimum_value(root))
