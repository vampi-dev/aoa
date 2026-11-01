class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    found = search(root, 7)
    print(found.value if found else "Not found")
