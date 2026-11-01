class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(inorder_iterative(root))
