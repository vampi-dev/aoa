
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a value
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Search a value
def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


# Inorder traversal: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder traversal: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder traversal: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Find minimum value
def find_min(root):
    while root.left:
        root = root.left
    return root.data


# Delete a value
def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        root.data = find_min(root.right)
        root.right = delete(root.right, root.data)

    return root


# Main program
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)

key = 40
if search(root, key):
    print("\nValue found:", key)
else:
    print("\nValue not found")

root = delete(root, 30)

print("After deletion:")
inorder(root)
